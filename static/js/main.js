import {getAllPosts, getPostByID} from "./api.js"

//TODO: need refactoring


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
          <li class="post">
              <a class="post-title post-item" href="post-info/${id}"><h3>${title}</h3></a>
              <img class="post-image post-item" src="${imageSrc}" width="200px" height="200px" style="border-radius: 20px;">
              <p class="post-description post-item">${description}</p>
              <p class="post-author post-item">${author}</p>
          </li>
        </div>
      `;
    })
    .join("");
}

//TODO: change corner templates markup, their have wrong semantics
function renderPostInfo(post){
    const { id, title, img, description, author, date } = post
    const imageSrc = img ? img : "/media/image/standart/dfault.png";
    return `
        <div class="container-item-detail">
            <div class="post-detail">
                <a class="post-title post-detail-title post-item" href="/daun"><h3>${title}</h3></a>
                <p class="post-description post-detail-description post-item">${description}</p>
                <p class="post-author post-detail-author post-item">${author}</p>
                <p class="post-date post-detail-date post-item">${date}</p>
            </div>
            <div class="img-container">
                <img class="post-image post-detail-image post-item" src="${imageSrc}" width="400" style="border-radius: 20px;">
            </div>
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

//TODO: add new func in this listener
document.addEventListener("DOMContentLoaded", async function () {
    const postInfoContainer = document.querySelector(".container-item-detail");
    const path = window.location.pathname;
    const parts = path.split("/").filter(Boolean); // розіб'є /post/42 => ['post', '42']

    const pageType = parts[0]; // 'post' або 'category' або 'user'
    const id = parts[1];

    if (pageType === "post-info" && id) {
        try {
            const post = await getPostByID(id);
            console.log(post)
            console.log(postInfoContainer)
            postInfoContainer.innerHTML = renderPostInfo(post);
        } catch (error) {
            console.error("Не вдалося завантажити пост:", error);
        }
    }
});

//TODO: use func only into first page
showBlogPage();
