# Generated by Django 2.2a1 on 2019-02-03 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190203_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='is_favourite',
            new_name='is_favourites',
        ),
    ]