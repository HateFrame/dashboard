from django.db import models


class Channel(models.Model):
    name = models.CharField(
        verbose_name='Название канала',
        max_length=511,
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        verbose_name='Канал',
        related_name='posts'
    )
    name = models.CharField(
        verbose_name='Название поста',
        max_length=511
    )
    content = models.TextField(
        verbose_name='Тело поста'
    )

    def __str__(self):
        return self.name
