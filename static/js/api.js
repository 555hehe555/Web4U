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
