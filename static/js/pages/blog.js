import { bindPaginationEvents } from "../handlers/index.js";
import {showBlogPage} from "../main.js"


export async function initBlogPage() {
  await showBlogPage();
  bindPaginationEvents();
}
