from django.db import models

from accounts.models import Account


class Post(models.Model):
    text = models.TextField(verbose_name="Текст", max_length=500)
    title = models.CharField(verbose_name="Заголовок", max_length=50)

    author = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="Автор")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    text = models.TextField(verbose_name="Текст", max_length=200)

    author = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="Автор")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", related_name="comments", related_query_name="comment")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
