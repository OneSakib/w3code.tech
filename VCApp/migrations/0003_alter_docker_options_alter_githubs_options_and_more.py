# Generated by Django 4.0.5 on 2022-06-27 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VCApp', '0002_gitscomments_githubscomments_dockercomments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docker',
            options={'verbose_name_plural': 'Docker'},
        ),
        migrations.AlterModelOptions(
            name='githubs',
            options={'verbose_name_plural': 'Githubs'},
        ),
        migrations.AlterModelOptions(
            name='gits',
            options={'verbose_name_plural': 'Gits'},
        ),
    ]