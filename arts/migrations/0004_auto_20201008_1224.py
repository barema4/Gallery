# Generated by Django 2.2.7 on 2020-10-08 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0003_picture_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
