# Generated by Django 3.1.4 on 2021-02-08 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20210203_1310'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quot',
        ),
        migrations.DeleteModel(
            name='QuoteAuthor',
        ),
    ]