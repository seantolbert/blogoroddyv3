# Generated by Django 4.0.3 on 2022-09-07 15:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_projectpage_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='project',
            field=wagtail.core.fields.StreamField([('project', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock())]))], blank=True, null=True),
        ),
    ]