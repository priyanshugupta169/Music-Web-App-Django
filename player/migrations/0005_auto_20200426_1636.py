# Generated by Django 3.0.3 on 2020-04-26 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_auto_20200425_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songs',
            old_name='song_file',
            new_name='song_path',
        ),
    ]
