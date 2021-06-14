# Generated by Django 3.2.3 on 2021-05-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('release_date', models.CharField(blank=True, max_length=100, null=True)),
                ('poster_path', models.CharField(blank=True, max_length=200, null=True)),
                ('vote_average', models.FloatField()),
                ('popularity', models.IntegerField()),
                ('genres', models.CharField(max_length=100)),
            ],
        ),
    ]
