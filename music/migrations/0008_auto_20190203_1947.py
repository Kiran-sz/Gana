# Generated by Django 2.2a1 on 2019-02-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20190203_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_favourites',
        ),
        migrations.AddField(
            model_name='song',
            name='is_favourte',
            field=models.BooleanField(default=False),
        ),
    ]