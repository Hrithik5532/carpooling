# Generated by Django 3.2.6 on 2022-10-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercreationApp', '0002_alter_usercreate_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreate',
            name='phonenumber',
            field=models.CharField(max_length=12),
        ),
    ]
