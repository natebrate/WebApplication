# Generated by Django 3.1.6 on 2021-02-11 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApplication', '0004_auto_20210211_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='trainerID',
            field=models.IntegerField(null=True),
        ),
    ]