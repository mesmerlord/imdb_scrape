# Generated by Django 3.2.12 on 2022-03-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220308_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name of Movie'),
        ),
    ]