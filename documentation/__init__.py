from .comments import (
    comments_list_doc,
    comments_create_doc,
    comments_update_doc,
    comments_patch_doc,
    comments_delete_doc,
    comments_retrieve_doc
)
from .likes import (
    like_list_doc,
    like_post_doc,
    like_delete_doc,
)
from .login_user import (
    login_user_list_doc,
    logout_user_list_doc,
)
from .posts import (
    post_list_doc,
    post_create_doc,
    post_update_doc,
    post_patch_doc,
    post_delete_doc,
    user_post_list_doc,
)
from .custom_user import (
    user_list_doc,
    user_retrieve_doc,
    user_create_doc,
    user_update_doc,
    user_patch_doc,
    user_delete_doc,
    get_me_doc,
)
