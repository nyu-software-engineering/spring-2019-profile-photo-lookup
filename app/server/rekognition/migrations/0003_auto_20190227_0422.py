# Generated by Django 2.1.7 on 2019-02-27 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekognition', '0002_auto_20190227_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerekognition',
            name='picture',
            field=models.ImageField(upload_to='./rekognition/asset'),
        ),
    ]