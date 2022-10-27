# Generated by Django 4.1.2 on 2022-10-27 08:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_released', models.DateField(default=datetime.datetime.today)),
                ('likes', models.PositiveIntegerField()),
                ('artist_id', models.IntegerField()),
                ('Artist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='musicapp.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('song_id', models.IntegerField()),
                ('Song', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='musicapp.song')),
            ],
        ),
    ]