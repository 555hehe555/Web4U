from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='main'),
    path('<int:pk>', views.PostDetail.as_view()),
    path('profile/', views.profile_view, name='profile'),
    path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
    path('accounts/logout/profile/', views.logout_user, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('create-post/<int:pk>/', views.CreatePostView.as_view(), name='create_post'),
    path('post-info/<int:pk>', views.PostDetail.as_view())
]
