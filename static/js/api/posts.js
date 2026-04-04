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
