export async function getCommentsByPostID(id) {
  try {
    const response = await fetch(`/api/posts/${id}/comments/`);
    const data = await response.json();
    console.log("comment" + data);
    return data;
  } catch (error) {
    console.error("Error:", error);
    return [];
  }
}

export async function postCreateComment(csrfToken, postID, text) {
  console.warn("createComment function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`postID ${postID}`);
  console.log(`text ${text}`);

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
      console.log("if !res " + response.ok)
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

    console.log("Успішна відповідь від API:", data);
    // Можна тут показати повідомлення або оновити DOM
  } catch (error) {
    console.error("Помилка при створенні коментаря:", error);
    alert("Сталася помилка при збереженні. Спробуйте ще раз.");
  }
}
