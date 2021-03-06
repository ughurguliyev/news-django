# Generated by Django 3.1.3 on 2020-12-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201203_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Username')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
