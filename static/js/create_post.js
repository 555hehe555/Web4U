createPostForm = document.querySelector(".post_form")

createPostForm.addEventListener('submit', function(e) {
  e.preventDefault();

  const formData = new FormData(this);
  const title = formData.get('title');
  const description = formData.get('description');
  const author = "admin"

  console.log(`title ${title}`)
  console.log(`description ${description}`)
  console.log(`autor ${author}`)

  const csrfToken = getCookie('csrftoken');
  createPost(csrfToken, title, description, author)
});
