# Generated by Django 2.2.6 on 2019-11-12 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0002_discussions_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussions',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
