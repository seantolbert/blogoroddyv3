# Generated by Django 4.0.3 on 2022-09-19 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_background'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='background',
            new_name='background_img',
        ),
    ]
