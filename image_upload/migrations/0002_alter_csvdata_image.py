# Generated by Django 4.0.1 on 2022-06-28 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvdata',
            name='image',
            field=models.ImageField(default='upload.jpg', null=True, upload_to=''),
        ),
    ]
