# Generated by Django 3.2.9 on 2021-11-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Фото'),
        ),
    ]
