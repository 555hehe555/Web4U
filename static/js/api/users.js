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
