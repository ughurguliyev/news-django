# Generated by Django 3.1.3 on 2020-12-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20201210_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='trending_now',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
