# Generated by Django 2.1 on 2018-08-17 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20180817_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
