# Generated by Django 3.2 on 2022-02-11 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]