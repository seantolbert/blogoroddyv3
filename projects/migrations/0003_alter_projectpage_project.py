# Generated by Django 4.0.3 on 2022-09-06 19:33

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_projectpage_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='project',
            field=wagtail.core.fields.StreamField([('project_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.RichTextBlock())]))], blank=True, null=True),
        ),
    ]