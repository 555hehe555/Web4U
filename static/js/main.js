import {getAllPosts, getPostByID, getCommentsByPostID, createPost} from "./api.js"
import getCookie from "./get_csrf_token.js";


//TODO: need refactoring and dividing to extra modules


function deleteMarkup(el) {
  el.innerHTML = "";
}

function renderBlogPosts(posts) {
  console.log(posts);
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
    return `
        <div class="container-item-detail">
            <div class="post-detail">
                <h3 class="post-title post-detail-title post-item">${title}</h3>
                <p class="post-description post-detail-description post-item">${description}</p>
                <p class="post-author post-detail-author post-item">${author}</p>
                <p class="post-date post-detail-date post-item">${date}</p>
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
  const data = await getAllPosts();
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


function testCreatePost(){
  const csrfToken = getCookie('csrftoken');

  createPost(csrfToken, "api_test", "api_testapi_testapi_testapi_testapi_testapi_testapi_", "a", "2025-07-22")
}


document.addEventListener("DOMContentLoaded", async function () {
    const path = window.location.pathname;
    const parts = path.split("/").filter(Boolean); // розіб'є /post/42 => ['post', '42']
    console.log(parts)

    const pageType = parts[0]; // 'post' або 'category' або 'user'
    const id = parts[1];

    if (parts.length === 0){
      showBlogPage();
    } else if (pageType === "post-info" && id) {
      showPostInfo(id)
    } else if (pageType === "create-post") {
        console.log("we are in create-post page")
    }
});
