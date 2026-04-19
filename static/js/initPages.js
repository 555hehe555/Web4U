import { getPage } from "./utils/index.js";
import { initBlogPage } from "./pages/index.js";
import { showPostInfo } from "./main.js";
import { createPost } from "./main.js";
import { createUser, loginUser } from "./main.js";
import { profileUser, logoutUser } from "./main.js";


export async function initPages() {
  const { pageType, id } = getPage();

  if (pageType === undefined) {
    await initBlogPage();
    return;
  }

  if (pageType === "post-info" && id) {
    await showPostInfo(id);
    return;
  }

  if (pageType === "create-post") {
    await createPost();
    return;
  }

  if (pageType === "register") {
    await createUser();
    return;
  }

  if (pageType === "login") {
    await loginUser();
    return;
  }

  if (pageType === "profile") {
    await profileUser();
    await logoutUser();
    return;
  }

  console.error("Unknown page type or missing ID")
}
