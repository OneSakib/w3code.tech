# Generated by Django 4.0.5 on 2022-06-26 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_alter_tutlist_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutlist',
            name='link',
            field=models.URLField(default='https://127.0.0.1:8000/'),
        ),
    ]
