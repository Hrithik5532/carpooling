# Generated by Django 3.2.6 on 2022-10-08 17:30

from django.db import migrations, models
import django.db.models.deletion
import usercreationApp.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usercreate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=10)),
                ('add', models.TextField()),
                ('state', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('zipcode', models.CharField(max_length=7)),
                ('password', models.CharField(max_length=10)),
                ('cpssword', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='docverifyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panimg', models.ImageField(upload_to=usercreationApp.models.docverifyModel.upload_to)),
                ('aadharimg', models.ImageField(upload_to=usercreationApp.models.docverifyModel.upload_to)),
                ('drivinglicimg', models.ImageField(blank=True, null=True, upload_to='drivinglicimg/')),
                ('panno', models.CharField(max_length=10)),
                ('aadharno', models.CharField(max_length=12)),
                ('drivinglicno', models.CharField(blank=True, max_length=10, null=True)),
                ('did', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usercreationApp.usercreate')),
            ],
        ),
    ]