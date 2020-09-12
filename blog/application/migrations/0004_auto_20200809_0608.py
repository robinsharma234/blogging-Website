# Generated by Django 2.2.12 on 2020-08-09 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_blog_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(),
        ),
    ]