# Generated by Django 4.1.7 on 2023-03-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainride', '0003_alter_createrideloc_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='createrideloc',
            name='available_seats',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
