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
      console.log("if !res " + response.ok)
      // const errorText = JSON.stringify(data.errors || data);
      // document.querySelector('.form-errors').innerText = errorText;
      // throw new Error('Помилка збереження поста');
    }

  } catch (error) {
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
