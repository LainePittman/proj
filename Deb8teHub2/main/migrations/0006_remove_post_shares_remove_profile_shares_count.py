# Generated by Django 4.2.6 on 2023-10-30 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_post_id_alter_post_likes_alter_post_postid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='shares',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='shares_count',
        ),
    ]
