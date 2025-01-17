# Generated by Django 2.2.6 on 2019-10-14 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('plant_name', models.CharField(blank=True, max_length=200, null=True)),
                ('plant_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('temp', models.CharField(blank=True, max_length=128, null=True)),
                ('humid', models.CharField(blank=True, max_length=128, null=True)),
                ('light', models.CharField(blank=True, max_length=128, null=True)),
                ('flow_water', models.CharField(blank=True, max_length=128, null=True)),
                ('ph_water', models.CharField(blank=True, max_length=128, null=True)),
                ('tds_water', models.CharField(blank=True, max_length=128, null=True)),
                ('started_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('etc', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
