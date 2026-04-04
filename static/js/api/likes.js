export async function postCreateLike(csrfToken, postID) {
  console.warn("createLike function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`postID ${postID}`);
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
      console.log("if !res" + response.ok)
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

    console.log("Успішна відповідь від API:", data);
    // Можна тут показати повідомлення або оновити DOM
  } catch (error) {
    console.error("Помилка при створенні лайка:", error);
    alert("Сталася помилка при збереженні. Спробуйте ще раз.");
  }
}

export async function deleteLike(csrfToken, postID) {
  console.warn("deleteLike function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`postID ${postID}`);

  try {
    const response = await fetch(`/api/posts/${postID}/likes/`, {
      method: 'DELETE',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}`);
    }

    console.log("Успішна відповідь від API:", response);
    // Можна тут показати повідомлення або оновити DOM
  } catch (error) {
    console.error("Помилка при видаленні лайка:", error);
    alert("Сталася помилка при збереженні. Спробуйте ще раз.");
  }
}

export async function getLikesByPostID(id) {
  try {
    const response = await fetch(`/api/posts/${id}/likes/`);
    const data = await response.json();
    console.log("like");
    console.log(data);
    return data;
  } catch (error) {
    console.error("Error:", error);
    return [];
  }
}
