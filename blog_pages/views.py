from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.base import View


class PostView(View):
    def get(self, request):
        return render(request, "blog/blog.html")


class PostDetail(View):
    def get(self, request, pk):
        return render(request, "blog/blog_detail.html")

@login_required(login_url="/login/")
def profile_view(request):
    return render(request, 'profile/profile.html')

class RegisterView(View):
    def get(self, request):
        return render(request, "registration/registration.html")


class LoginView(View):
    def get(self, request):
        return render(request, "registration/login.html")

@login_required
def create_post_view(request):
    return render(request, "profile/create-post.html")
    