# Generated by Django 3.1.4 on 2020-12-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201223_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Имя группы'),
        ),
    ]
