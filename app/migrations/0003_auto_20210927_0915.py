# Generated by Django 3.2.5 on 2021-09-27 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210927_0914'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lectures',
            new_name='Lecture',
        ),
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
        migrations.RenameModel(
            old_name='Teachers',
            new_name='Teacher',
        ),
    ]
