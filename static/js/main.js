import {
  getAllPosts,
  getPostByID,
  getCommentsByPostID,
  postCreateComment,
  postCreatePost,
  getCurrentUser,
  getLikesByPostID,
  postCreateLike,
  deleteLike,
  postCreateUser,
  postLoginUser,
  postLogoutUser,
  getUserPostsById,
  PatchUser,
  PatchPost,
  DeletePost
} from "./api.js"
import getCookie from "./get_csrf_token.js";


//TODO: need refactoring and dividing to extra modules

function deleteMarkup(el) {
  el.innerHTML = "";
}

let currentPage = 1;
let totalPages = null;

let isEditing = false;

let paginationContainer = document.querySelector(".pagination-container");

let first = document.getElementById('first');
let prev = document.getElementById('prev');
let next = document.getElementById('next');
let last = document.getElementById('last');
let current = document.getElementById('current');

function getPage(){
  const path = window.location.pathname;
  const parts = path.split("/").filter(Boolean); // розіб'є /post/42 => ['post', '42']
  console.log(parts)

  const pageType = parts[0]; // 'post' або 'category' або 'user'
  const id = parts[1];

  return { pageType, id }
}

function formatDate(dateString) {
  const d = new Date(dateString);

  return d.toLocaleString("uk-UA", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit"
  });
}

function renderBlogPosts(posts) {
  const withoutPlaceholders = true

  if ("results" in posts) {
    console.log(posts);
    totalPages = Math.ceil(posts.count / 10);
    if (posts.count === 0) {
      paginationContainer.style.display = "none";
      return "<img src='/media/image/standard/no_posts_placeholder.png' width='500px' style='display: block; margin: 0 auto; border-radius: 20px'>";
    }
    else if (totalPages === 1) {
      paginationContainer.style.display = "none";
    } else {
      paginationContainer.style.display = "flex";
    }

    return posts.results
      .map(({ id, title, img, description, author, date }) => {
        const hasImage = !!img;
        const imageSrc = hasImage ? img : "/media/image/standard/img_placeholder.png";
        const showImage = withoutPlaceholders ? hasImage : true;

        const shortDate = date.split("T")[0];
      //   Це пости на головній сторінці
          return `
            <div class="container-item">

              <div class="post">
                <div class="post-img-contener">
                    ${showImage ? `<img class="post-image post-item" src="${imageSrc}">` : ""}
                </div>
                <div class="post-info-contener">
                <a class="post-title post-item" href="/post-info/${id}"><h3>${title}</h3></a>
                  <p class="post-description post-item">${description}</p>
                  <p class="post-date post-item">${shortDate}</p>
                  <p class="post-author post-item">${author}</p>
                </div>
              </div>
            </div>
          `;
        }).join("");
  } else if (!("results" in posts) && posts.length) {
    // Це пости на сторінці профілю
    return posts
      .map(({ id, title, img, description, author, date }) => {
        const hasImage = !!img;
        const imageSrc = hasImage ? img : "/media/image/standard/img_placeholder.png";
        const showImage = withoutPlaceholders ? hasImage : true;

        const shortDate = date.split("T")[0];
        return `
          <div class="container-item">
            <div class="post">
                <div class="post-img-contener">
                    ${showImage ? `<img class="post-image post-item" src="${imageSrc}">` : ""}
                </div>
                <div class="post-info-contener">
                  <a class="post-title post-item" href="/post-info/${id}"><h3>${title}</h3></a>
                  <p class="post-description post-item">${description}</p>
                  <p class="post-date post-item">${shortDate}</p>
                  <p class="post-author post-item">${author}</p>
                </div>
              </div>
          </div>
        `;
      }).join("");
  } else {return "<img src='/media/image/standard/no_posts_placeholder.png' width='500px' style='display: block; margin: 0 auto; border-radius: 20px'>";}
}

function renderCommentsPost(comments) {
  console.log(comments.results);
  const commentsItem = comments.results
    .map(({ id, user, text_comments, post }) => {
      return `
      <div>
          <p class="comment-finished-user-text-comments">${user}: ${text_comments}</p>
      </div>
      `;
    })

  commentsItem.unshift(`
              <div class="comment-form">
              <textarea type="text" class="comment-input" placeholder="Write a comment..."></textarea>
              <button class="comment-submit-btn">Submit</button>
          </div>
          `)

    return commentsItem.join("");
}

async function renderPostInfo(post, comments, likes) {
  const { id, title, img, description, author, date } = post;

  const countLikes = likes.count || 0;
  const commentsMarkup = renderCommentsPost(comments);

  const imageSrc = img
    ? img
    : "/media/image/standard/img_placeholder.png";

  const likeImgSrc = likes.user_liked
    ? "/media/image/standard/like.png"
    : "/media/image/standard/no_like.png";

  const shortDate = date.split("T")[0];


  const currentUser = await getCurrentUser();

  let showEditButtons = false;
  if (currentUser.username === post.author) {
    showEditButtons = true;
    console.log("User is the author of the post. Edit buttons will be shown.");
  }
  console.log("Current Current user:", currentUser);
  console.log("currentUser json:", JSON.stringify(currentUser));
  console.log("Current user:", currentUser.username);
  console.log("Post author:", post.author);
  console.log("Show edit buttons:", showEditButtons);
  console.log("Like image source:", likeImgSrc);
  console.log(currentUser.username === post.author);
  console.log(`${currentUser.username} === ${post.author}`);

  return `
        <div class="container-item-detail" data-post-id="${id}">
            <div class="container-item">
                <div class="post post-detail" style="display: flex;
                                         justify-content: space-between;
                                         flex-direction: row-reverse;">

                    <div class="post-img-contener">
                        <input 
                            class="button-img mt-2"
                            type="file"
                            name="img"
                            accept="image/*"
                            id="id_img"
                            style="display: none;"
                            disabled>

                        <label for="id_img" style="display: flex;
                                                   flex-direction: column;
                                                   align-items: flex-start;">
                            <img id="prev_img" src="${img}" style="display: ${img ? "block" : "none"}">
                        </label>
                        
                        <button id="editCurrentPost"   style="display: ${showEditButtons ? "block" : "none"};">
                            Редагувати
                        </button>
                        <button id="deleteCurrentPost" style="display: ${showEditButtons ? "block" : "none"};">
                            Видалити цей пост
                        </button>
                    </div>

                    <div class="post-info-contener" style="width: auto;">
                        <a href="javascript:history.back()" class="back-button"><img src="/media/image/standard/arrow_left.svg"></svg></a>
                        
                        <h3 id="post-title" class="post-title post-detail-title post-item">
                            ${title}
                        </h3>

                        <input
                            type="text"
                            name="title"
                            class="form-control input-style vTextField mt-2"
                            maxlength="70"
                            required
                            id="post-title-edit"
                            value=${title}
                            style="display: none">

                        <p id="post-description" class="post-description post-detail-description post-item">
                            ${description}
                        </p>

                        <textarea
                            name="description"
                            cols="40"
                            rows="10"
                            class="form-control textarea-style vLargeTextField mt-2"
                            required
                            id="post-description-edit"
                            spellcheck="false"
                            style="display: none">${description}</textarea>

                        <p class="post-author post-detail-author post-item">
                            ${author}
                        </p>

                        <p class="post-date post-detail-date post-item">
                            ${shortDate}
                        </p>
                    </div>

                </div>
            </div>

            <div class="like">
                <a class="like-btn">
                    <img src="${likeImgSrc}" width="20" height="20">
                </a>
                <span class="like-count">
                    ${countLikes}
                </span>
            </div>

            <div class="comment-finished">
                <h2 class="comment-finished-title">
                    <br>Comment<br>
                </h2>
                ${commentsMarkup}
            </div>

        </div>
    `;
}

document.addEventListener("DOMContentLoaded", function() {
 const container = document.querySelector(".post");
 if (!container) return; // якщо контейнера нема, нічого не робимо

 container.addEventListener("click", async function(e) {
   const postElem = e.target.closest(".container-item-detail");
   if (!postElem) return;

   const postId = postElem.dataset.postId;

   const editButton = e.target.closest("#editCurrentPost");
   const deleteButton = e.target.closest("#deleteCurrentPost");


   const titleElem = postElem.querySelector("#post-title");
   const descriptionElem = postElem.querySelector("#post-description");

   const titleInput = postElem.querySelector("#post-title-edit");
   const descriptionInput = postElem.querySelector("#post-description-edit");

   const prevImg = postElem.querySelector("#prev_img");
   const imgInput = postElem.querySelector("#id_img");


  if (editButton && !isEditing) {
    console.log("Edit button clicked");
    isEditing = true

    editButton.textContent = "Зберегти";

      titleElem.style.display = "none";
      descriptionElem.style.display = "none";

      titleInput.style.display = "block";
      descriptionInput.style.display = "block";

      imgInput.disabled = false;

      imgInput.addEventListener("change", function() {
        const file = this.files[0];
        if (file) {
          prevImg.src = URL.createObjectURL(file);
        } else {
          prevImg.src = "none";
        }
      });
  } else if (editButton && isEditing) {
    console.log("Save button clicked");
    isEditing = false

      titleElem.style.display = "block";
      descriptionElem.style.display = "block";

      titleInput.style.display = "none";
      descriptionInput.style.display = "none";

      imgInput.disabled = true;

      const updatedTitle = titleInput.value.trim();
      const updatedDescription = descriptionInput.value.trim();
      const updatedImageFile = imgInput.files[0];

      prevImg.src = updatedImageFile ? URL.createObjectURL(updatedImageFile) : prevImg.src;

      const formData = new FormData();

      if (updatedTitle)       {formData.append("title", updatedTitle);}
      if (updatedDescription) {formData.append("description", updatedDescription);}
      if (updatedImageFile)   {formData.append("img", updatedImageFile);}

      const csrfToken = getCookie('csrftoken');

      await PatchPost(csrfToken, postId, formData)

      titleElem.textContent = updatedTitle;
      descriptionElem.textContent = updatedDescription;
      editButton.textContent = "Редагувати";
      window.location.href = `/post-info/${postId}`;
    }
  else if (deleteButton) {
    console.log("Delete button clicked");
      if (confirm("Ви впевнені, що хочете видалити цей пост?")) {
        try {
          const csrfToken = getCookie('csrftoken');
          await DeletePost(csrfToken, postId);
          alert("Пост успішно видалено");
          window.location.href = "/"; // повертаємося на головну після видалення
        } catch (error) {
          console.error("Не вдалося видалити пост:", error);
          alert("Сталася помилка при видаленні поста. Спробуйте ще раз.");
        }
      }
   }
 })
});

async function showBlogPage() {
  const postContainer = document.querySelector(".own-container");
  deleteMarkup(postContainer);
  const data = await getAllPosts(currentPage);
  postContainer.insertAdjacentHTML("beforeend", renderBlogPosts(data));

  console.log(document.querySelectorAll(".post-title"));
}

async function showPostInfo(id) {
  try {
    const postInfoContainer = document.querySelector(".container-detail");
    const post = await getPostByID(id);
    const comments = await getCommentsByPostID(id);
    const likes = await getLikesByPostID(id);
    console.log(comments)
    postInfoContainer.innerHTML = await renderPostInfo(post, comments, likes);
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
        const image = formData.get('img')

        const csrfToken = getCookie('csrftoken')
        await postCreatePost(csrfToken, title, description, image)
        alert("Пост успішно створено")
        window.location.href = "/profile/";
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
        await deleteLike(csrfToken, postId);
      } else {
        await postCreateLike(csrfToken, postId);
      }

      // оновлюємо UI
      const updatedLikes = await getLikesByPostID(postId);
      const img = likeBtn.querySelector("img");
      const userLiked = updatedLikes.results.some(like => like.author === currentUser.username);
      img.src = userLiked ? "/media/image/standard/like.png" : "/media/image/standard/no_like.png";

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


async function createUser(){
  console.log("createUser function called");
  const registerForm = document.querySelector(".login-form")

  registerForm.addEventListener('submit', async function(e) {
    e.preventDefault()
    console.log("createUser event listener called");

      try {
        const formData = new FormData(this)
        const username = formData.get('username')
        const password = formData.get('password1')
        const password2 = formData.get('password2')
        const email = formData.get('email')

        if (password !== password2) {
          alert("Паролі не співпадають")
          return
        }

        const csrfToken = getCookie('csrftoken')
        console.warn(csrfToken, username, password, email)
        await postCreateUser(csrfToken, username, password, email)
        alert("Користувача успішно створено")
        await postLoginUser(csrfToken, username, password)
        window.location.href = "/profile/";
        

      } catch (error) {
        console.error("Не вдалося створити користувача:", error);
      }
    });
}

async function loginUser(){
  console.log("loginUser function called");
  const loginForm = document.querySelector(".login-form")

  loginForm.addEventListener('submit', async function(e) {
    e.preventDefault()
    console.log("loginUser event listener called");

      try {
        const formData = new FormData(this)
        const username = formData.get('username')
        const password = formData.get('password')

        const csrfToken = getCookie('csrftoken')
        console.warn(csrfToken, username, password)
        await postLoginUser(csrfToken, username, password)
        alert("Вхід успішний")
        window.location.href = "/profile/";

      } catch (error) {
        console.error("Не вдалося увійти:", error);
      }
    });
}

async function logoutUser(){
  const logoutBtn = document.querySelector(".logout-btn")
  if (!logoutBtn) return;

  logoutBtn.addEventListener('click', async function(e) {
    e.preventDefault()
    console.log("logoutUser event listener called");

      try {
        const csrfToken = getCookie('csrftoken')
        console.warn(csrfToken)
        await postLogoutUser(csrfToken)
        alert("Вихід успішний")
        window.location.href = "/";

      } catch (error) {
        console.error("Не вдалося вийти:", error);
      }
    });
}

async function profileUser() {
  const profileContainer = document.querySelector(".main-profile");
  if (!profileContainer) return;

  const infoUserContainer = document.querySelector(".profile-info");
  if (!infoUserContainer) return;

  const currentUser = await getCurrentUser();

  document.querySelector(".username").innerText = currentUser.username;

  const infoUser = [
    ["Ваш id", currentUser.id, false, "user-id"],
    ["Ваш нік", currentUser.username, true, "user-username"],
    ["Ваш пароль", '********', true, "user-password"],
    ["Ваша пошта", currentUser.email, false, "user-email"],
    ["Ваша дата реєстрації", formatDate(currentUser.date_joined), false, "user-date-joined"],
    ["Ваше імʼя", currentUser.first_name, true, "user-first-name"],
    ["Ваше прізвище", currentUser.last_name, true, "user-last-name"],
    ["Роль", currentUser.is_staff ? "адміністратор" : "користувач", false, "user-is-staff" ],
  ];

  renderUserData(infoUser, infoUserContainer);

  document
    .querySelector("#edit-profile-btn")
    .addEventListener("click", await editProfileUser);

  const userPostsContainer = document.querySelector(".user-posts-container");
  const data = await getUserPostsById(currentUser.id);
  userPostsContainer.innerHTML = renderBlogPosts(data);
}

function renderUserData(infoUser, container) {
  container.innerHTML = infoUser.map(item => {
    const [label, value, editable, id] = item;

    return `
      <div class="row user-data-row" data-editable="${editable}">
        <div class="col-sm-3">
          <h6 class="mb-0">${label}</h6>
        </div>
        <div class="col-sm-9 text-secondary">
          <p class="user-data-p">${value}</p>
          <input 
            type="text"
            id="${id}"
            class="user-data-input"
            placeholder="${item[0] === "Ваш пароль" ? "Введідь новий пароль" : value}"
            ${editable ? "" : "disabled"}
            style="display: none;"
          />
        </div>
      </div>
      <hr>
    `;
  }).join("");

  container.innerHTML += `
    <div class="row">
      <div class="col-sm-12">
        <button id="edit-profile-btn" class="btn btn-info secondary-btn">
          Редагувати
        </button>
      </div>
    </div>
  `;
}

async function editProfileUser(e) {
  e.preventDefault();

  const rows = document.querySelectorAll(".user-data-row");
  const editBtn = document.querySelector("#edit-profile-btn");

  const dataToUpdate = {};

  rows.forEach(row => {
    const editable = row.dataset.editable === "true";
    const p = row.querySelector(".user-data-p");
    const input = row.querySelector(".user-data-input");

    if (!editable) return;

    if (isEditing) {
      // вихід з редагування
      p.style.display = "block";
      input.style.display = "none";

      if (input.value.trim() !== "") {
        dataToUpdate[input.id.replace("user-", "")] = input.value;
        p.textContent = input.value;
      }
    } else {
      // вхід в редагування
      p.style.display = "none";
      input.style.display = "block";
    }
  });

  console.log(dataToUpdate);

  if (isEditing && Object.keys(dataToUpdate).length) {
    const user = await getCurrentUser()
    const userId = user.id;
    const csrfToken = getCookie('csrftoken')

    await PatchUser(csrfToken, userId, dataToUpdate).catch(err => {
      console.error("Не вдалося оновити користувача:", err);
    });
  }

  editBtn.innerText = isEditing ? "Редагувати" : "Зберегти";
  isEditing = !isEditing;
}

document.addEventListener("DOMContentLoaded", async () => {
  const { pageType, id } = getPage();

  if (pageType === undefined) {
    await showBlogPage();

    for (let i of [first, prev, next, last]) {
      i.addEventListener('click', async function (e) {
        e.preventDefault();
        if (i.id === 'first') {
          currentPage = 1;
        } else if (i.id === 'prev') {
          currentPage = currentPage > 1 ? currentPage - 1 : 1;
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
    await showPostInfo(id);
  } else if (pageType === "create-post") {
    await createPost();
  } else if (pageType === "register") {
    await createUser();
  } else if (pageType === "login") {
    await loginUser();
  } else if (pageType === "profile") {
    await profileUser();
    await logoutUser();
  } else {
    console.error("Unknown page type or missing ID");
  }
});
