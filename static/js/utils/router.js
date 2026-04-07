 export function getPage(){
  const path = window.location.pathname;
  const parts = path.split("/").filter(Boolean); // розіб'є /post/42 => ['post', '42']
  console.log(parts)

  const pageType = parts[0]; // 'post' або 'category' або 'user'
  const id = parts[1];

  return { pageType, id }
}
