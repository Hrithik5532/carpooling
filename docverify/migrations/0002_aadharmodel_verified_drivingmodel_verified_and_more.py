# Generated by Django 4.1.7 on 2023-03-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docverify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aadharmodel',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='drivingmodel',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='panmodel',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]