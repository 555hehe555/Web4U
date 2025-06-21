from django.urls import path
from django.shortcuts import redirect
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views


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
        'get': 'retrieve',
        'delete': 'destroy'
    })),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path("", lambda request: redirect("swagger-ui")),
    path(route='v1/docs/', view=SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


