# Generated by Django 4.0.5 on 2022-07-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JavaScriptApp', '0007_alter_angularjs_parent_alter_expressjs_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='angularjs',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='expressjs',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='jquery',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='nodejs',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='reactjs',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='typescripts',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vuejs',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
