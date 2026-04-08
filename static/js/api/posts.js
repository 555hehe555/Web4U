import { log, warn, error, info, TheAlert } from "../utils";

export async function getAllPosts(page = 1) {
  try {
    warn("api/posts.js", 5, "getAllPosts called", page);
    const response = await fetch(`/api/posts/?page=${page}`);
    const data = await response.json();
    log("api/posts.js", 8, "getAllPosts response:", data);
    return data;
  } catch (err) {
    error("api/posts.js", 11, "Error getting all posts:", err);
    return [];
  }
}

export async function getPostByID(id) {
  try {
    const response = await fetch(`/api/posts/${id}`);
    const data = await response.json();
    log("api/posts.js", 20, "getPostByID response:", data);
    return data;
  } catch (err) {
    error("api/posts.js", 23, "Error getting post by id:", err);
    return [];
  }
}

export async function postCreatePost(csrfToken, title, description, img) {
  warn("api/posts.js", 29, "postCreatePost called");
  info("api/posts.js", 31, `csrfToken ${csrfToken}`);
  info("api/posts.js", 32, `title ${title}`);
  info("api/posts.js", 33, `description ${description}`);
  info("api/posts.js", 34, `img ${img}`);

  try {
    const formData = new FormData();

    formData.append("title", title);
    formData.append("description", description);
    formData.append("img", img); // img = input.files[0]

    const response = await fetch("/api/posts/", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
        // НЕ ставимо Content-Type вручну
      },
      body: formData
    });

    const data = await response.json();

    if (!response.ok) {
      warn("api/posts.js", 54, "API returned non-ok response:", data);
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

    log("api/posts.js", 60, "Успішна відповідь від API:", data);
    // Можна тут показати повідомлення або оновити DOM
  } catch (err) {
    error("api/posts.js", 63, "Помилка при створенні поста:", err);
    TheAlert("api/posts.js", 64, "Сталася помилка при збереженні. Спробуйте ще раз.", err);
  }
}

export async function getUserPostsById(id) {
  try {
    const response = await fetch(`/api/users/${id}/posts/`);
    const data = await response.json();
    log("api/posts.js", 72, "getUserPostsById response:", data);
    return data;
  } catch (err) {
    error("api/posts.js", 75, "Error getting user posts by id:", err);
    return [];
  }
}

export async function PatchPost(csrfToken, postID, dataToUpdate) {
  warn("api/posts.js", 81, "PatchPost called");
  info("api/posts.js", 82, `csrfToken ${csrfToken}`);
  info("api/posts.js", 83, `postID ${postID}`);
  info("api/posts.js", 84, "dataToUpdate" , JSON.stringify(dataToUpdate));

  try {
    const res = await fetch(`/api/posts/${postID}/`, {
      method: "PATCH",
      headers: {
        "X-CSRFToken": csrfToken
      },
      body: dataToUpdate
    });

    const data = await res.json();
    if (!res.ok) {
      warn("api/posts.js", 97, "API returned non-ok response:", data);
    }

    log("api/posts.js", 100, "PatchPost response:", data);
    return data;
  } catch (err) {
    error("api/posts.js", 103, "Помилка при оновленні поста:", err);
    TheAlert("api/posts.js", 104, "Сталася помилка при оновленні. Спробуйте ще раз.", err);
    return null;
  }
}

export async function DeletePost(csrfToken, postID) {
  warn("api/posts.js", 110, "DeletePost called");
  info("api/posts.js", 111, `csrfToken ${csrfToken}`);
  info("api/posts.js", 112, `postID ${postID}`);

  try {
    const response = await fetch(`/api/posts/${postID}/`, {
      method: "DELETE",
      headers: {
        "X-CSRFToken": csrfToken,
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const data = await response.json();
      warn("api/posts.js", 125, "API returned non-ok response:", data);
    }

    log("api/posts.js", 128, "Успішна відповідь від API:", response);
  } catch (err) {
    error("api/posts.js", 130, "Помилка при видаленні поста:", err);
    TheAlert("api/posts.js", 131, "Сталася помилка при видаленні. Спробуйте ще раз.", err);
  }
}
