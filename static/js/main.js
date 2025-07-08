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

async function getPostByID(id) {
  try {
    const response = await fetch(`/api/posts/${id}`);
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
  console.log(posts);
  return posts.results
    .map(({ id, title, img, description, author, date }) => {
      const imageSrc = img ? img : "/media/image/standart/dfault.png"; // заміни на свій плейсхолдер
      return `
        <div class="container-item">
          <li class="post">
              <a class="post-title post-item" href="${id}"><h3>${title}</h3></a>
              <img class="post-image post-item" src="${imageSrc}" width="200px" height="200px" style="border-radius: 20px;">
              <p class="post-description post-item">${description}</p>
              <p class="post-author post-item">${author}</p>
          </li>
        </div>
      `;
    })
    .join("");
}

document.addEventListener('DOMContentLoaded', function () {
  const postLinks = document.querySelectorAll(".post-title")
  postLinks.forEach(link => {
      link.addEventListener('click', function (event) {
          event.preventDefault();
          alert(link.href)
      });
  });
});


async function showBlogPage() {
  deleteMarkup();
  const data = await getAllPosts(); // ⬅️ Тепер чекаємо результат
  postContainer.insertAdjacentHTML("beforeend", renderBlogPosts(data));

  console.log(document.querySelectorAll(".post-title"));
}

showBlogPage();
