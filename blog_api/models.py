from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from uuid import uuid4


def user_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"image/avatars/user_{instance.id}/{uuid4()}.{ext}"


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to=user_avatar_path, null=True, blank=True)
    email = models.EmailField("email", blank=True, max_length=254)


class Post(models.Model):
    title = models.CharField('заголовок поста', max_length=70)
    description = models.TextField("текст поста", max_length=500)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="автор",
        on_delete=models.CASCADE,
        related_name="posts"
    )
    img = models.ImageField("зображеня", upload_to="image/temp/%Y", blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}, {self.author.username}'

    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    text_comments = models.TextField('текст коментаря', max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='користувач',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(Post, verbose_name='публікація', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.user.username}, {self.post}'

    class Meta:
        verbose_name = 'коментар'
        verbose_name_plural = 'коментарі'


class Like(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='користувач', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='публікація', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки'
        unique_together = ('user', 'post')
