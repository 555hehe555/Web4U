const postContainer = document.querySelector(".own-container");

async function getAllPosts() {
  try {
    const response = await fetch("/api/posts/");
    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error("Error:", error);
    return []; // Повертаємо порожній масив, щоб уникнути краху
  }
}

function deleteMarkup() {
  postContainer.innerHTML = "";
}

function renderBlogPosts(posts) {

  console.log(posts)
  return posts.results
    .map(
      ({ id, title, description, author, date }) =>
        ` 
          <div class="container-item">
            <li class="post">
                <a class="post-title post-item" href="${id}"><h3>${title}</h3></a>
                <p class="post-description post-item">${description}</p>
                <p class="post-author post-item">${author}</p>
            </li>
          </div>
        `
    )
    .join("");
}

async function showBlogPage() {
  deleteMarkup();
  const data = await getAllPosts(); // ⬅️ Тепер чекаємо результат
  postContainer.insertAdjacentHTML("beforeend", renderBlogPosts(data));
}

showBlogPage();
