from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField("email", blank=True, max_length=30)


class Post(models.Model):
    title = models.CharField('заголовок поста', max_length=70)
    description = models.TextField("текст поста")
    author = models.CharField("імя автора", max_length=60)
    # img = models.ImageField("зображеня", upload_to="image/%Y", blank=True)
    date = models.DateField("дата публікації")

    def __str__(self):
        return f'{self.title},{self.author}'

    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    name = models.CharField(max_length=25)
    text_comments = models.TextField('текст коментаря', max_length=240)
    post = models.ForeignKey(Post, verbose_name='публікації', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name},{self.post}'

    class Meta:
        verbose_name = 'коментар'
        verbose_name_plural = 'коментарi'


class Like(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='користувач', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='публікація', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'

    class Meta:
        verbose_name = 'лайк'
        verbose_name_plural = 'лайки'
        unique_together = ('user', 'post')
