# Generated by Django 4.0.5 on 2022-07-07 07:05

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0020_alter_comments_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
