# Generated by Django 4.0.3 on 2022-04-19 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('blog', '0003_blogpagetags_blogpage_tags_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPageTags',
            new_name='BlogPageTag',
        ),
    ]