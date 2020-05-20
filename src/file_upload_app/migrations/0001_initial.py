# Generated by Django 3.0.5 on 2020-05-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SingleFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploader', models.CharField(max_length=20)),
                ('file_name', models.FileField(upload_to='documents')),
            ],
        ),
    ]