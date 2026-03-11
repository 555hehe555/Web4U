from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.forms import UserModel

from .models import Likes


class PostView(View):
    def get(self, request):
        return render(request, "blog/blog.html")


class PostDetail(View):
    def get(self, request, pk):
        return render(request, "blog/blog_detail.html")


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(".")[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            print("try")
            a = Likes.objects.get(ip=ip_client, post_id=pk)
            print(a)
            return redirect(f"/{pk}")
        except:
            print("except")
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = int(pk)
            new_like.save()
            return redirect(f"/{pk}")


@login_required(login_url="/login/")
def profile_view(request):
    return render(request, 'profile/profile.html')


def logout_user(request):
    return redirect("/profile")


class RegisterView(View):
    def get(self, request):
        print("get in blog register")
        return render(request, "registration/registration.html")


class LoginView(View):
    def get(self, request):
        print("get in blog login")
        return render(request, "registration/login.html")


class CreatePostView(View):
    def get(self, request, pk):
        post = UserModel.objects.get(pk=pk)
        print(post)
        return render(request, "profile/create-post.html", {"post": post})
    