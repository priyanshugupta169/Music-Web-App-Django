# Generated by Django 3.0.3 on 2020-04-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_auto_20200426_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='id',
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist',
            field=models.CharField(max_length=70, primary_key=True, serialize=False),
        ),
    ]