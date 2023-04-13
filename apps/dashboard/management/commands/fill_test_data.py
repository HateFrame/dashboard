import random

from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta

from apps.dashboard.models import Log
from apps.channel.models import Channel, Post

CHANNEL_NAME = 'Test'
POST_NAME = 'PostGeneratedName'

class Command(BaseCommand):
    help = 'filling test_data'

    def handle(self, *args, **options):
        for i in range(1,14):
            posts = []
            channel_name = f'{CHANNEL_NAME}-{str(i)}'
            channel = Channel.objects.create(name=channel_name)
            for k in range(50):
                posts.append(Post(
                    channel=channel,
                    name=f'{POST_NAME}-{str(k)} in {channel_name}',
                    content=f'TEST CONTENT. HELLO! in channel pk = {i} and post number = {k}'
                ))
            Post.objects.bulk_create(posts)

        created_at = now()
        channels = Channel.objects.all()
        logs = []
        for i in range(10):
            created_at = created_at - timedelta(days=1)
            if i == 4:
                continue
            for channel in channels:
                logs.append(Log(
                    channel=channel,
                    subscribers_count=random.randint(10, 400),
                    created_at=created_at
                ))
            Log.objects.bulk_create(logs)
            logs = []
