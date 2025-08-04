import {getAllPosts, getPostByID, getCommentsByPostID, postCreatePost, getCurrentUser} from "./api.js"
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


function renderBlogPosts(posts) {
  console.log(posts);
  totalPages = Math.ceil(posts.count / 10);
  return posts.results
    .map(({ id, title, img, description, author, date }) => {
      const imageSrc = img ? img : "/media/image/standart/dfault.png";
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
  console.log(comments);
  return comments.results
    .map(({ id, name, text_comments, post }) => {
      return `
      <div>
          <p class="comment-finished-user-text-comments">${text_comments}: ${name}</p>
      </div>
      `;
    })
    .join("");
}

function renderPostInfo(post, comments){
    const { id, title, img, description, author, date } = post
    const commentsMarkup = renderCommentsPost(comments)
    console.log(commentsMarkup)
    const imageSrc = img ? img : "/media/image/standart/dfault.png";
    const shortDate = date.split("T")[0];
    return `
        <div class="container-item-detail">
            <div class="post-detail">
                <h3 class="post-title post-detail-title post-item">${title}</h3>
                <p class="post-description post-detail-description post-item">${description}</p>
                <p class="post-author post-detail-author post-item">${author}</p>
                <p class="post-date post-detail-date post-item">${shortDate}</p>
            </div>
            <div class="img-container">
                <img class="post-image post-detail-image post-item" src="${imageSrc}" width="400" style="border-radius: 20px;">
            </div>
        </div>
        <div class="comment-finished">
          <h2 class="comment-finished-title"><br>Comment<br></h2> 
          ${commentsMarkup}
        </div>
    `
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
    console.log(comments)
    postInfoContainer.innerHTML = renderPostInfo(post, comments);
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


document.addEventListener("DOMContentLoaded", async function () {
    const path = window.location.pathname;
    const parts = path.split("/").filter(Boolean); // розіб'є /post/42 => ['post', '42']
    console.log(parts)

    const pageType = parts[0]; // 'post' або 'category' або 'user'
    const id = parts[1];

    if (parts.length === 0){
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
