# Generated by Django 2.2.6 on 2019-11-18 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_post_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
