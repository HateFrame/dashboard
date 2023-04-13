from django.db import models
from apps.channel.models import Channel, Post


class Log(models.Model):
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        verbose_name='Канал',
        related_name='logs'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='logs',
        blank=True,
        null=True,
        default=None
    )
    subscribers_count = models.PositiveIntegerField(
        verbose_name='Количество подписчиков',
        default=0,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата добавления лога'
    )

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        if self.post:
            return f'{self.channel} - {self.post.name} - {self.created_at}'
        return f'{self.channel} - {self.created_at}'
