from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='main'),
    path('<int:pk>', views.PostDetail.as_view()),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('create-post/', views.create_post_view, name='create_post'),
    path('post-info/<int:pk>', views.PostDetail.as_view(), name='post_info')
]
