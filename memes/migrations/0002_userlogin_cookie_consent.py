# Generated by Django 2.2.6 on 2020-12-29 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlogin',
            name='cookie_consent',
            field=models.CharField(default=None, max_length=10),
        ),
    ]