document.getElementById('post_form').addEventListener('submit', function(e) {
  console.log('aaaaaaaaaaaaa')
  e.preventDefault(); // щоб не перезавантажувалась сторінка

  const formData = new FormData(this);
  const title = formData.get('title');
  const description = formData.get('description');
  const author = "admin"

  console.log(`title ${title}`)
  console.log(`description ${description}`)
  console.log(`autor ${author}`)
});