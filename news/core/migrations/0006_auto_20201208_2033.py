# Generated by Django 3.1.3 on 2020-12-08 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.author'),
        ),
        migrations.AddField(
            model_name='post',
            name='cover_img',
            field=models.ImageField(null=True, upload_to='', verbose_name='Cover image'),
        ),
    ]
