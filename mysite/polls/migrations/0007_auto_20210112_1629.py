# Generated by Django 3.1.4 on 2021-01-12 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_person'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonAddress',
            new_name='HumanAddress',
        ),
    ]