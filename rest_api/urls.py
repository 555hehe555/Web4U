from django.urls import path, include
from django.shortcuts import redirect

from rest_framework.routers import DefaultRouter

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views.post import *
from .views.comment import *
from .views.like import *
from .views.user import *

router = DefaultRouter()
router.register(r'', ManagerViewSet, basename='manager')

urlpatterns = [
    path('posts/', PostModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:pk>/', PostModelViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'partial_update'
    })),
    path('posts/<int:post_pk>/comments/', CommentModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/', CommentModelViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'partial_update'
    })),
    path('posts/<int:post_pk>/likes/', LikePostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:post_pk>/likes/<int:pk>/', LikePostViewSet.as_view({
        'delete': 'destroy'
    })),
    path('users/', CustomUserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('users/<int:pk>/', CustomUserViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'partial_update'
    })),
    path('users/<int:user_pk>/posts/', CustomUserViewSet.as_view({'get': 'post_list'}), name='post_list'),
    path('accounts/login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
    path('accounts/logout/', AuthViewSet.as_view({'post': 'logout'}), name='logout'),

    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', lambda request: redirect("swagger-ui")),
    path(route='v1/docs/', view=SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
