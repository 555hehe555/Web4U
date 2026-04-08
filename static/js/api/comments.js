import { log, warn, error, info, TheAlert } from "../utils";

export async function getCommentsByPostID(id) {
  try {
    const response = await fetch(`/api/posts/${id}/comments/`);
    const data = await response.json();
    log("api/comments.js", 7, "getCommentsByPostID response:", data);
    return data;
  } catch (err) {
    error("api/comments.js", 10, "Error getting comments by post id:", err);
    return [];
  }
}

export async function postCreateComment(csrfToken, postID, text) {
  warn("api/comments.js", 16, "postCreateComment called");
  info("api/comments.js", 17, `csrfToken ${csrfToken}`);
  info("api/comments.js", 18, `postID ${postID}`);
  info("api/comments.js", 19, `text ${text}`);

  try {
    const response = await fetch(`/api/posts/${postID}/comments/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "text_comments": text,
        "post": postID
      })
    });

    const data = await response.json();

    if (!response.ok) {
      warn("api/comments.js", 37, "API returned non-ok response:", data);
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

    log("api/comments.js", 43, "Успішна відповідь від API:", data);
    // Можна тут показати повідомлення або оновити DOM
  } catch (err) {
    error("api/comments.js", 46, "Помилка при створенні коментаря:", err);
    TheAlert("api/comments.js", 47, "Сталася помилка при збереженні. Спробуйте ще раз.", err);
  }
}
