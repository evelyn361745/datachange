# Generated by Django 3.0.4 on 2020-03-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoDatabase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dbname', models.CharField(max_length=25, unique=True)),
                ('description', models.CharField(max_length=25, null=True)),
                ('host', models.CharField(max_length=25)),
                ('port', models.CharField(max_length=25)),
                ('user', models.CharField(max_length=25)),
                ('passwd', models.CharField(max_length=25)),
                ('type', models.CharField(max_length=25)),
                ('create_time', models.CharField(max_length=25)),
                ('update_time', models.CharField(max_length=25)),
                ('jdbcurl', models.CharField(max_length=50)),
                ('jdbcdriver', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'info_database',
            },
        ),
        migrations.CreateModel(
            name='Infouser',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('token', models.CharField(max_length=25)),
                ('introduction', models.CharField(max_length=255, null=True)),
                ('avatar', models.CharField(max_length=255, null=True)),
                ('roles', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('create_time', models.CharField(max_length=25)),
                ('update_time', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'info_user',
            },
        ),
    ]
