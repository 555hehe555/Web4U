import { log, warn, error, info, TheAlert} from "../utils";

export async function postLoginUser(csrfToken, username, password) {

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
      warn("api/auth.js", 21, "Помилка при логіні користувача:", data);
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

  } catch (error) {
    TheAlert("api/auth.js", 28, "Помилка при логіні користувача:", error);
  }
}

export async function postLogoutUser(csrfToken) {
  info("api/auth.js", 33, "Виклик функції postLogoutUser");

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
      error("api/auth.js", 47, "Помилка при логауті користувача:", data);
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

    log("api/auth.js", 53, "Успішна відповідь від API:", data);
    TheAlert("api/auth.js", 54, "Успішна відповідь від API:", data)
    // Можна тут показати повідомлення або оновити DOM
  } catch (error) {
    error("api/auth.js", 57, "Помилка при логауті користувача:", error);
    TheAlert("api/auth.js", 58, "Помилка при логауті користувача:", error);
  }
}
