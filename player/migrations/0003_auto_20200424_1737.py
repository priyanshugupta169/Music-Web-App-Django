# Generated by Django 3.0.3 on 2020-04-24 12:07

import datetime
from django.db import migrations, models
import player.models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_songs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=70)),
                ('image', models.ImageField(blank=True, upload_to=player.models.song_path)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AlterField(
            model_name='songs',
            name='song_file',
            field=models.FileField(upload_to=player.models.song_path),
        ),
    ]
