export function getCountLikes(likes) {
  return likes[postId] || 0;
}

export function itsLiked(likes) {
  return likes.user_liked;
}

export function likeImg(likes) {
  if (likes.user_liked) {
    return "/media/image/standard/like.png";
  } else {
    return "/media/image/standard/no_like.png";
  }
}

