# Generated by Django 4.2 on 2023-05-17 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='detailsUrl',
        ),
    ]
