import {blogState} from "../utils/index.js";
import {paginationElements} from "../utils/index.js";


export function bindPaginationEvents() {
  for (const button of [paginationElements.first, paginationElements.prev, paginationElements.next, paginationElements.last]) {
    button.addEventListener("click", onPaginationClick);
  }
}

async function onPaginationClick(event) {
  event.preventDefault();

  const buttonId = event.currentTarget.id;

  if (buttonId === "first") {
    blogState.currentPage = 1;
  } else if (buttonId === "prev") {
    blogState.currentPage = blogState.currentPage > 1 ? blogState.currentPage - 1 : 1;
  } else if (buttonId === "next") {
    blogState.currentPage = blogState.currentPage !== blogState.totalPages ? blogState.currentPage + 1 : blogState.totalPages;
  } else if (buttonId === "last") {
    blogState.currentPage = blogState.totalPages;
  }

  current.textContent = blogState.currentPage;
  await showBlogPage();
}
