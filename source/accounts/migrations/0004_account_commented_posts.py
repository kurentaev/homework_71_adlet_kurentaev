# Generated by Django 4.1.2 on 2022-10-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('accounts', '0003_alter_account_liked_posts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='commented_posts',
            field=models.ManyToManyField(related_name='user_comments', to='posts.post', verbose_name='Прокомментированные публикации'),
        ),
    ]