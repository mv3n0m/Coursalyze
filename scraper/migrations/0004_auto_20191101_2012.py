# Generated by Django 2.2.6 on 2019-11-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_auto_20191027_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='search_text',
            field=models.TextField(null=True),
        ),
    ]