# Generated by Django 2.2.6 on 2019-10-30 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20191029_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_requesting', to=settings.AUTH_USER_MODEL)),
                ('target_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_requested', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
