"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>', views.PostDetail.as_view()),
    path('profile/', views.profile_view, name='profile'),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
    path('accounts/logout/profile/', views.logout_user, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('create-post/', views.CreatePostView.as_view(), name='create_post'),
    path('create-post-user/', views.CreateUserPostView.as_view(), name='create_post_user')
]
