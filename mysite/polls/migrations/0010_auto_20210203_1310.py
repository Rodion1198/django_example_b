# Generated by Django 3.1.4 on 2021-02-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20210130_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteauthor',
            name='date_of_birth',
            field=models.CharField(max_length=100, verbose_name='author'),
        ),
    ]