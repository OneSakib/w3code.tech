# Generated by Django 4.0.5 on 2022-07-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0033_authormodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tutlist',
            name='link',
            field=models.URLField(default='http://localhost:8000/'),
        ),
    ]
