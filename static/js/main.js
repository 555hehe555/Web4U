import {getAllPosts, getPostByID, getCommentsByPostID, postCreateComment, postCreatePost, getCurrentUser,
  getLikesByPostID, postCreateLike, deleteLike} from "./api.js"
import getCookie from "./get_csrf_token.js";


//TODO: need refactoring and dividing to extra modules


function deleteMarkup(el) {
  el.innerHTML = "";
}

let currentPage = 1;
let totalPages = null;

const current = document.getElementById('current')
const first = document.getElementById('first')
const prev = document.getElementById('prev')
const next = document.getElementById('next')
const last = document.getElementById('last')


function getPage(){
  const path = window.location.pathname;
  const parts = path.split("/").filter(Boolean); // розіб'є /post/42 => ['post', '42']
  console.log(parts)

  const pageType = parts[0]; // 'post' або 'category' або 'user'
  const id = parts[1];

  return { pageType, id }
}


function renderBlogPosts(posts) {
  console.log(posts);
  totalPages = Math.ceil(posts.count / 10);
  return posts.results
    .map(({ id, title, img, description, author, date }) => {
      const imageSrc = img ? img : "/media/image/standart/img_placeholder.png";
      return `
        <div class="container-item">
          <div class="post">
              <a class="post-title post-item" href="post-info/${id}"><h3>${title}</h3></a>
              <img class="post-image post-item" src="${imageSrc}" width="200px" height="200px" style="border-radius: 20px;">
              <p class="post-description post-item">${description}</p>
              <p class="post-author post-item">${author}</p>
          </div>
        </div>
      `;
    })
    .join("");
}

function renderCommentsPost(comments) {
  console.log(comments.results);
  return comments.results
    .map(({ id, user, text_comments, post }) => {
      return `
      <div>
          <p class="comment-finished-user-text-comments">${user}: ${text_comments}</p>
      </div>
      `;
    })
    .join("");
}


function renderPostInfo(post, comments, likes) {
  const { id, title, img, description, author, date } = post;
  const countLikes = likes.count || 0;
  const commentsMarkup = renderCommentsPost(comments);
  const imageSrc = img ? img : "/media/image/standart/img_placeholder.png";
  const likeImgSrc = likes.user_liked
    ? "/media/image/standart/like.png"
    : "/media/image/standart/no_like.png";
  const shortDate = date.split("T")[0];

  return `
        <div class="container-item-detail" data-post-id="${id}">
            <div class="post-detail">
                <h3 class="post-title post-detail-title post-item">${title}</h3>
                <p class="post-description post-detail-description post-item">${description}</p>
                <p class="post-author post-detail-author post-item">${author}</p>
                <p class="post-date post-detail-date post-item">${shortDate}</p>
            </div>
            <div class="img-container">
                <img class="post-image post-detail-image post-item" src="${imageSrc}" width="400" style="border-radius: 20px;">
            </div>
            
            <div class="like">
              <a href="#" class="like-btn">
                <img src="${likeImgSrc}" width="20" height="20">
              </a>
              <span class="like-count">${countLikes}</span>
            </div>
            
            <div class="comment-form">
                <textarea type="text" class="comment-input" placeholder="Write a comment..."></textarea>
                <button class="comment-submit-btn">Submit</button>
            </div>
        </div>

        <div class="comment-finished">
          <h2 class="comment-finished-title"><br>Comment<br></h2> 
          ${commentsMarkup}
        </div>
    `;
}



async function showBlogPage() {
  const postContainer = document.querySelector(".own-container");
  deleteMarkup(postContainer);
  const data = await getAllPosts(currentPage);
  postContainer.insertAdjacentHTML("beforeend", renderBlogPosts(data));

  console.log(document.querySelectorAll(".post-title"));
}


async function showPostInfo(id) {
  try {
    const postInfoContainer = document.querySelector(".container-item-detail");
    const post = await getPostByID(id);
    const comments = await getCommentsByPostID(id);
    const likes = await getLikesByPostID(id);
    console.log(comments)
    console.error(likes)
    postInfoContainer.innerHTML = renderPostInfo(post, comments, likes);
  } catch (error) {
    console.error("Не вдалося завантажити пост:", error);
  }
}

async function createPost(){
  const createPostForm = document.querySelector(".post_form")
  createPostForm.addEventListener('submit', async function(e) {
    e.preventDefault()

      try {
        const formData = new FormData(this)
        const title = formData.get('title')
        const description = formData.get('description')

        const csrfToken = getCookie('csrftoken')
        await postCreatePost(csrfToken, title, description)
        alert("Пост успішно створено")
      } catch (error) {
        console.error("Не вдалося створити пост:", error);
      }
    });
}

document.addEventListener("DOMContentLoaded", function() {
  const container = document.querySelector(".container-detail");
  if (!container) return; // якщо контейнера нема, нічого не робимо

  container.addEventListener("click", async function(e) {
    const likeBtn = e.target.closest(".like-btn");
    if (!likeBtn) return;

    const postElem = likeBtn.closest(".container-item-detail");
    if (!postElem) return;

    const postId = postElem.dataset.postId;
    if (!postId) return;

    console.log("Like button clicked for post", postId); // <- перевірка

    try {
      const likes = await getLikesByPostID(postId);
      const currentUser = await getCurrentUser();
      const userLike = likes.results.find(like => like.author === currentUser.username);
      const csrfToken = getCookie("csrftoken");

      if (currentUser?.detail) {
        alert("Щоб поставити лайк, будь ласка, увійдіть або зареєструйтесь.");
        return;
      }

      if (userLike) {
        await deleteLike(csrfToken, postId, userLike.id);
      } else {
        await postCreateLike(csrfToken, postId);
      }

      // оновлюємо UI
      const updatedLikes = await getLikesByPostID(postId);
      const img = likeBtn.querySelector("img");
      const userLiked = updatedLikes.results.some(like => like.author === currentUser.username);
      img.src = userLiked ? "/media/image/standart/like.png" : "/media/image/standart/no_like.png";

      const countElem = postElem.querySelector(".like-count");
      if (countElem) countElem.textContent = updatedLikes.count || 0;
    } catch (err) {
      console.error("Не вдалося оновити лайк:", err);
    }
  });
});


document.addEventListener("DOMContentLoaded", function() {
  console.warn("111")
  const container = document.querySelector(".container-detail");
  if (!container) return; // якщо контейнера нема, нічого не робимо
  console.warn("222")

  container.addEventListener("click", async function(e) {
    console.warn("333")
    const commentSubmitBtn = e.target.closest(".comment-submit-btn");
    if (!commentSubmitBtn) return;

    const commentInput = document.querySelector(".comment-input");
    console.log(commentInput, commentSubmitBtn); // <- перевірка
    console.warn("444")

    const postElem = commentSubmitBtn.closest(".container-item-detail");
    if (!postElem) return;
    console.warn("555")

    const postId = postElem.dataset.postId;
    if (!postId) return;
    console.log("666")

    console.log("Comment button clicked for post", postId); // <- перевірка

    console.log("Submit comment clicked"); // <- перевірка
    e.preventDefault();
    const commentText = commentInput.value;
    console.error(commentText);
    if (!commentText) {
      alert("Коментар не може бути порожнім.");
      return;
    }

    try {
        const csrfToken = getCookie("csrftoken");
        console.warn(csrfToken, postId, commentText);
        await postCreateComment(csrfToken, postId, commentText);
        commentInput.value = ""; // очищаємо поле вводу

        // Оновлюємо список коментарів
        const comments = await getCommentsByPostID(postId);
        const commentsContainer = document.querySelector(".comment-finished");
        if (commentsContainer) {
          commentsContainer.innerHTML = `
            <h2 class="comment-finished-title"><br>Comment<br></h2>
            ${renderCommentsPost(comments)}
          `;
        }
      } catch (err) {
        console.error("Не вдалося додати коментар:", err);
        alert("Сталася помилка при додаванні коментаря. Спробуйте ще раз.");
      }
  });
});



document.addEventListener("DOMContentLoaded", async function () {
    const { pageType, id } = getPage();

    if (pageType === undefined) {
      await showBlogPage();

      for (let i of [first, prev, next, last]) {
        i.addEventListener('click', async function (e) {
          e.preventDefault();
          if (i.id === 'first') {
            currentPage = 1;
          } else if (i.id === 'prev') {
            currentPage--
          } else if (i.id === 'next') {
            currentPage = currentPage != totalPages ? currentPage + 1 : totalPages;
          } else if (i.id === 'last') {
            currentPage = totalPages;
          }
          current.textContent = currentPage;
          await showBlogPage();
        });
      }
    } else if (pageType === "post-info" && id) {
      await showPostInfo(id)
    } else if (pageType === "create-post") {
      await createPost()
    }
});
