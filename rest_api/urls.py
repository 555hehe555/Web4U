from django.urls import path, include
from django.shortcuts import redirect
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'', views.ManagerViewSet, basename='manager')

urlpatterns = [
    path('posts/', views.PostModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:pk>/', views.PostModelViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'partial_update'
    })),
    path('posts/<int:post_pk>/comments/', views.CommentModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/', views.CommentModelViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'partial_update'
    })),
    path('posts/<int:post_pk>/likes/', views.LikePostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:post_pk>/likes/<int:pk>/', views.LikePostViewSet.as_view({
        # 'get': 'retrieve',
        'delete': 'destroy'
    })),
    path('users/', views.CustomUserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('users/<int:pk>/', views.CustomUserViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put': 'update',
        'patch': 'partial_update'
    })),
    path('users/<int:user_pk>/posts/', views.CustomUserViewSet.as_view({'get': 'post_list'}), name='post_list'),
    path('accounts/login/', views.AuthViewSet.as_view({'post': 'login'}), name='login'),
    path('accounts/logout/', views.AuthViewSet.as_view({'post': 'logout'}), name='logout'),

    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', lambda request: redirect("swagger-ui")),
    path(route='v1/docs/', view=SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


