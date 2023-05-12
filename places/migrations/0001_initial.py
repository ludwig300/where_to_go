# Generated by Django 4.2 on 2023-05-05 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('placeId', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('lng', models.FloatField(verbose_name='Долгота')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('detailsUrl', models.URLField(blank=True, verbose_name='URL подробностей')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='images', verbose_name='Изображение')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place')),
            ],
        ),
    ]