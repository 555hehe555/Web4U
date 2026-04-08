import { log, warn, error, info, TheAlert } from "../utils";

export async function postCreateLike(csrfToken, postID) {
  warn("api/likes.js", 4, "postCreateLike called");
  info("api/likes.js", 5, `csrfToken ${csrfToken}`);
  info("api/likes.js", 6, `postID ${postID}`);
  try {
    const response = await fetch(`/api/posts/${postID}/likes/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        post_id: postID
      })
    });

    const data = await response.json();

    if (!response.ok) {
      warn("api/likes.js", 22, "API returned non-ok response:", data);
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

    log("api/likes.js", 28, "Успішна відповідь від API:", data);
    // Можна тут показати повідомлення або оновити DOM
  } catch (err) {
    error("api/likes.js", 31, "Помилка при створенні лайка:", err);
    TheAlert("api/likes.js", 32, "Сталася помилка при збереженні. Спробуйте ще раз.", err);
  }
}

export async function deleteLike(csrfToken, postID) {
  warn("api/likes.js", 37, "deleteLike called");
  info("api/likes.js", 38, `csrfToken ${csrfToken}`);
  info("api/likes.js", 39, `postID ${postID}`);

  try {
    const response = await fetch(`/api/posts/${postID}/likes/`, {
      method: 'DELETE',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const err = new Error(`HTTP error ${response.status}`);
      warn("api/likes.js", 52, "API returned non-ok response while deleting like:", err);
      TheAlert("api/likes.js", 53, "Не вдалося видалити лайк.", err);
      return null;
    }

    log("api/likes.js", 57, "Успішна відповідь від API:", response);
    // Можна тут показати повідомлення або оновити DOM
    return response;
  } catch (err) {
    error("api/likes.js", 61, "Помилка при видаленні лайка:", err);
    TheAlert("api/likes.js", 62, "Сталася помилка при збереженні. Спробуйте ще раз.", err);
    return null;
  }
}

export async function getLikesByPostID(id) {
  try {
    const response = await fetch(`/api/posts/${id}/likes/`);
    const data = await response.json();
    log("api/likes.js", 71, "getLikesByPostID response:", data);
    return data;
  } catch (err) {
    error("api/likes.js", 74, "Error getting likes by post id:", err);
    return [];
  }
}
