function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            console.log(`cookieValue ${cookieValue}`)
              break;
          }
      }
  }
  return cookieValue;
}

async function createPost(csrfToken, title, description, author) {
  console.warn("createPost function called");
  console.log(`csrfToken ${csrfToken}`);
  console.log(`title ${title}`);
  console.log(`description ${description}`);
  console.log(`author ${author}`);


  try {
    const response = await fetch(`/api/posts/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        title: title,
        description: description,
        author: author,
        date: "2000-01-10"
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




let createPostForm = document.querySelector(".post_form")
createPostForm.addEventListener('submit', async function(e) {
  e.preventDefault();

  const formData = new FormData(this);
  const title = formData.get('title');
  const description = formData.get('description');
  const author = "admin";

  const csrfToken = getCookie('csrftoken'); // або `await getCookie(...)` якщо вона async
  await createPost(csrfToken, title, description, author);
});

