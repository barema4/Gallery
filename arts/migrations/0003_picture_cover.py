# Generated by Django 2.2.7 on 2020-10-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
