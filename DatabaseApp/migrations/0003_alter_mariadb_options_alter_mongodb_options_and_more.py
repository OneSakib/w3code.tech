# Generated by Django 4.0.5 on 2022-06-27 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseApp', '0002_sqlitedbcomments_postgresqldbcomments_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mariadb',
            options={'verbose_name_plural': 'MariaDB'},
        ),
        migrations.AlterModelOptions(
            name='mongodb',
            options={'verbose_name_plural': 'MongoDB'},
        ),
        migrations.AlterModelOptions(
            name='mysqldb',
            options={'verbose_name_plural': 'MysqlDB'},
        ),
        migrations.AlterModelOptions(
            name='oracledb',
            options={'verbose_name_plural': 'OracleDB'},
        ),
        migrations.AlterModelOptions(
            name='postgresqldb',
            options={'verbose_name_plural': 'PostgreSQLDB'},
        ),
        migrations.AlterModelOptions(
            name='sqlitedb',
            options={'verbose_name_plural': 'SqliteDB'},
        ),
    ]
