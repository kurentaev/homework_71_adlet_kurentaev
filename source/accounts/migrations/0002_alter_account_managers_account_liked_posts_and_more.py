# Generated by Django 4.1.1 on 2022-10-26 14:30

import accounts.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "__first__"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="account",
            managers=[
                ("objects", accounts.managers.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name="account",
            name="liked_posts",
            field=models.ManyToManyField(related_name="user_likes", to="posts.post"),
        ),
        migrations.AddField(
            model_name="account",
            name="subscriptions",
            field=models.ManyToManyField(
                related_name="subscribers", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]