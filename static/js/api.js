///Add another endpoints there
export async function getAllPosts(page = 1) {
  try {
    console.warn("getAllPosts function called", page);
    const response = await fetch(`/api/posts/?page=${page}`);
    const data = await response.json();
    console.log("All post", data);
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
    console.log("post by id", data);
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

export async function postCreatePost(csrfToken, title, description, img) {
  console.warn("createPost function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`title ${title}`);
  console.log(`description ${description}`);
  console.log(`img ${img}`);


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

// НЕ ПЕРЕВІРЕНИЙ КОД
export async function getUserByID(id) {
  try {
    const response = await fetch(`/api/users/${id}/`);
    const data = await response.json();
    console.log("user by id" + data);
    return data;
  } catch (error) {
    console.error("Error:", error);
    return [];
  }
}

export async function postCreateUser(csrfToken, username, password, email) {
  console.warn("createUser function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`username ${username}`);
  console.log(`password ${password}`);
  console.log(`email ${email}`);

  try {
    const response = await fetch(`/api/users/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username,
        password: password,
        email: email
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
    console.error("Помилка при створенні користувача:", error);
    alert("Сталася помилка при збереженні. Спробуйте ще раз.");
  }
}


export async function postLoginUser(csrfToken, username, password) {
  console.warn("loginUser function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`username ${username}`);
  console.log(`password ${password}`);

  try {
    const response = await fetch(`/api/accounts/login/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username,
        password: password
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
    alert("Успішна відповідь від API:", data)
    // Можна тут показати повідомлення або оновити DOM
  } catch (error) {
    console.error("Помилка при логіні користувача:", error);
    alert("Сталася помилка при збереженні. Спробуйте ще раз.");
  }
}

export async function postLogoutUser(csrfToken) {
  console.warn("logoutUser function called");
  console.log(`csrfToken ${csrfToken}`);

  try {
    const response = await fetch(`/api/accounts/logout/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
    });

    const data = await response.json();

    if (!response.ok) {
      console.log("if !res " + response.ok)
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

    console.log("Успішна відповідь від API:", data);
    alert("Успішна відповідь від API:", data)
    // Можна тут показати повідомлення або оновити DOM
  } catch (error) {
    console.error("Помилка при логіні користувача:", error);
    alert("Сталася помилка при збереженні. Спробуйте ще раз.");
  }
}


export async function getUserPostsById(id) {
  try {
    const response = await fetch(`/api/users/${id}/posts/`);
    const data = await response.json();
    console.log("user posts by id", data);
    return data;
  } catch (error) {
    console.error("Error:", error);
    return [];
  }
}


export async function PatchUser(csrfToken, userID, dataToUpdate) {
  console.warn("PatchUser function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`userID ${userID}`);
  console.log(`dataToUpdate ${JSON.stringify(dataToUpdate)}`);

  try {
    const response = await fetch(`/api/users/${userID}/`, {
      method: 'PATCH',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dataToUpdate)
    });

    const data = await response.json();
    if (!response.ok) {
      console.log("if !res " + response.ok)
    }

    console.log("Успішна відповідь від API:", data);
  } catch (error) {
    console.error("Помилка при оновленні користувача:", error);
    alert("Сталася помилка при оновленні. Спробуйте ще раз.");
  }
}

export async function PatchPost(csrfToken, postID, dataToUpdate) {
  console.warn("PatchPost function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`postID ${postID}`);
  console.log("dataToUpdate", JSON.stringify(dataToUpdate))

  try {
    const response = await fetch(`/api/posts/${postID}/`, {
      method: "PATCH",
      headers: {
        "X-CSRFToken": csrfToken
      },
      body: dataToUpdate
    });
  } catch (error) {
    console.error("Помилка при оновленні поста:", error);
    alert("Сталася помилка при оновленні. Спробуйте ще раз.");
  }
}

export async function DeletePost(csrfToken, postID) {
  console.warn("DeletePost function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`postID ${postID}`);

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
      console.log("if !res" + response.ok)
    }

    console.log("Успішна відповідь від API:", response);
  } catch (error) {
    console.error("Помилка при видаленні поста:", error);
    alert("Сталася помилка при видаленні. Спробуйте ще раз.");
  }
}