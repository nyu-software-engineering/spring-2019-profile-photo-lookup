# Generated by Django 2.1.7 on 2019-03-06 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rekognition', '0003_auto_20190227_0422'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ImageRekognition',
            new_name='ImageUpload',
        ),
    ]
