# Generated by Django 5.1.7 on 2025-03-26 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('number_of_speaker', models.IntegerField(blank=True, null=True)),
                ('event_type', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('until_date', models.DateField(blank=True, null=True)),
                ('time', models.CharField(max_length=20)),
                ('banner', models.ImageField(upload_to='banner')),
                ('venue', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker', models.CharField(max_length=30)),
                ('webinar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webinar.webinar')),
            ],
        ),
        migrations.CreateModel(
            name='WebinarAttendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('webinar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webinar.webinar')),
            ],
        ),
    ]
