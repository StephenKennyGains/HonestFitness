# Generated by Django 3.2 on 2022-02-09 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_userreview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserReview',
        ),
    ]
