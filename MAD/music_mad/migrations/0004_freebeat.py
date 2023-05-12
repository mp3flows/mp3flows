# Generated by Django 4.2 on 2023-04-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_mad', '0003_ads_music_musicimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeBeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beatname', models.CharField(max_length=200)),
                ('beatfile', models.FileField(upload_to='music')),
                ('beatimg', models.ImageField(upload_to='image')),
            ],
        ),
    ]
