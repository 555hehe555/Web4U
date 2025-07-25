///Add another endpoints there
export async function getAllPosts() {
  try {
    const response = await fetch("/api/posts/");
    const data = await response.json();
    console.log(data);
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
    console.log(data);
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
    console.log(data);
    return data;
  } catch (error) {
    console.error("Error:", error);
    return [];
  }
}

export async function createPost(csrfToken, title, description, author) {
  const response = fetch(`/api/posts/`, 
  {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrfToken,
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      "title": title,
      "description": description,
      "author": author,
    })
  })
  .then(response => {
    if (!response.ok) {
        return response.json().then(errorData => {
            form.querySelector('.form-errors').innerText = JSON.stringify(errorData.errors);
            throw new Error('Network response was not ok');
        });
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
      console.error('Error:', error);
      alert('An error occurred while updating the data.');
  });
}
