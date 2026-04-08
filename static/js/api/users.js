import { log, warn, error, info, TheAlert } from "../utils";

export async function getCurrentUser() {
  try {
    const response = await fetch("/api/me/");
    const data = await response.json();
    log("api/users.js", 7, "getCurrentUser response:", data);
    return data;
  } catch (err) {
    error("api/users.js", 9, "Error getting current user:", err);
    return null;
  }
}

export async function getUserByID(id) {
  try {
    const response = await fetch(`/api/users/${id}/`);
    const data = await response.json();
    log("api/users.js", 19, "getUserByID response:", data);
    return data;
  } catch (err) {
    error("api/users.js", 22, "Error getting user by id:", err);
    return [];
  }
}

export async function postCreateUser(csrfToken, username, password, email) {
  warn("api/users.js", 28, "postCreateUser called");
  info("api/users.js", 29, `csrfToken ${csrfToken}`);
  info("api/users.js", 30, `username ${username}`);
  info("api/users.js", 31, `password ${password}`);
  info("api/users.js", 32, `email ${email}`);

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
      warn("api/users.js", 51, "API returned non-ok response:", data);
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

    log("api/users.js", 57, "Успішна відповідь від API:", data);
    // Можна тут показати повідомлення або оновити DOM
  } catch (err) {
    error("api/users.js", 60, "Помилка при створенні користувача:", err);
    TheAlert("api/users.js", 61, "Сталася помилка при збереженні. Спробуйте ще раз.", err);
  }
}

export async function PatchUser(csrfToken, userID, dataToUpdate) {
  warn("api/users.js", 66, "PatchUser called");
  info("api/users.js", 67, `csrfToken ${csrfToken}`);
  info("api/users.js", 68, `userID ${userID}`);
  info("api/users.js", 69, `dataToUpdate ${JSON.stringify(dataToUpdate)}`);

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
      warn("api/users.js", 83, "API returned non-ok response:", data);
    }

    log("api/users.js", 86, "Успішна відповідь від API:", data);
  } catch (err) {
    error("api/users.js", 88, "Помилка при оновленні користувача:", err);
    TheAlert("api/users.js", 89, "Сталася помилка при оновленні. Спробуйте ще раз.", err);
  }
}
