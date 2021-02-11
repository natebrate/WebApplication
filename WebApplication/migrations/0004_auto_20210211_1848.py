# Generated by Django 3.1.6 on 2021-02-11 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApplication', '0003_staff_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('trainerID', models.IntegerField(max_length=200, null=True)),
                ('species', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=200, null=True)),
                ('weight', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('feedingType', models.CharField(max_length=200, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Staff', 'Staff')], max_length=200, null=True),
        ),
    ]
