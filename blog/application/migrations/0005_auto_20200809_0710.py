# Generated by Django 2.2.12 on 2020-08-09 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20200809_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='uname',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]