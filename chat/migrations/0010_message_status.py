# Generated by Django 2.2.6 on 2019-10-27 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20191027_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.IntegerField(choices=[(1, 'Sent'), (2, 'Seen')], default=2),
        ),
    ]
