# Generated by Django 2.1.15 on 2022-12-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20221207_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mfname', models.CharField(max_length=15)),
                ('mlname', models.CharField(max_length=15)),
                ('mcontact', models.CharField(max_length=13)),
                ('memail', models.CharField(max_length=25)),
                ('mmessage', models.CharField(max_length=500)),
            ],
        ),
    ]