# Generated by Django 4.0.5 on 2022-06-24 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='gruppe',
        ),
        migrations.DeleteModel(
            name='Gruppe',
        ),
    ]
