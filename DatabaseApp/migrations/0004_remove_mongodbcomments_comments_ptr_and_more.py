# Generated by Django 4.0.5 on 2022-07-02 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DatabaseApp', '0003_alter_mariadb_options_alter_mongodb_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mongodbcomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='mongodbcomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='mysqldbcomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='mysqldbcomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='oracledbcomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='oracledbcomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postgresqldbcomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='postgresqldbcomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='sqlitedbcomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='sqlitedbcomments',
            name='post',
        ),
        migrations.DeleteModel(
            name='MariaDBComments',
        ),
        migrations.DeleteModel(
            name='MongoDBComments',
        ),
        migrations.DeleteModel(
            name='MysqlDBComments',
        ),
        migrations.DeleteModel(
            name='OracleDBComments',
        ),
        migrations.DeleteModel(
            name='PostgreSQLDBComments',
        ),
        migrations.DeleteModel(
            name='SqliteDBComments',
        ),
    ]
