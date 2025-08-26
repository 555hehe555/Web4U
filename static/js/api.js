///Add another endpoints there
export async function getAllPosts(page = 1) {
  try {
    console.warn("getAllPosts function called", page);
    const response = await fetch(`/api/posts/?page=${page}`);
    const data = await response.json();
    console.log("All post" + data);
    return data;
  } catch (error) {
    console.error("Error:", error);
    return [];
  }
}

export async function getPostByID(id) {
  try {
    const response = await fetch(`/api/posts/${id}`);
    const data = await response.json();
    console.log("post by id" + data);
    return data;
  } catch (error) {
    console.error("Error:", error);
    return [];
  }
}

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

export async function postCreatePost(csrfToken, title, description) {
  console.warn("createPost function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`title ${title}`);
  console.log(`description ${description}`);


  try {
    const response = await fetch(`/api/posts/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: title,
        description: description
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
    console.error("Помилка при створенні поста:", error);
    alert("Сталася помилка при збереженні. Спробуйте ще раз.");
  }
}

export async function getCurrentUser() {
  try {
    const response = await fetch("/api/me/");
    const data = await response.json();
    console.log("get me", data);
    return data;
  } catch (error) {
    console.error("Error:", error);
    return null;
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


export async function deleteLike(csrfToken, postID, likeID) {
  console.warn("deleteLike function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`postID ${postID}`);
  console.log(`likeID ${likeID}`);
  try {
    const response = await fetch(`/api/posts/${postID}/likes/${likeID}/`, {
      method: 'DELETE',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const data = await response.json();
      console.log("if !res" + response.ok)
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

    console.log("Успішна відповідь від API:", response);
    // Можна тут показати повідомлення або оновити DOM
  } catch (error) {
    console.error("Помилка при видаленні лайка:", error);
    alert("Сталася помилка при збереженні. Спробуйте ще раз.");
  }
}


