from django.db import models


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


