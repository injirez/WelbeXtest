# Generated by Django 3.2.7 on 2021-09-27 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='number',
            new_name='quantity',
        ),
    ]