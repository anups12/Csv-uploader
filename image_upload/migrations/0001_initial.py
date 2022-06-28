# Generated by Django 4.0.1 on 2022-06-28 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Csvdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('detected', models.CharField(max_length=100, null=True)),
                ('dateadd', models.DateField()),
                ('image', models.ImageField(default='upload.jpg', null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='UploadCsv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fileupload', models.FileField(upload_to='data')),
            ],
        ),
    ]