# Generated by Django 4.0.5 on 2022-07-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VCApp', '0007_alter_docker_parent_alter_githubs_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docker',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='githubs',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='gits',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
