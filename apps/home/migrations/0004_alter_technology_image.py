# Generated by Django 3.2.13 on 2022-08-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220808_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
