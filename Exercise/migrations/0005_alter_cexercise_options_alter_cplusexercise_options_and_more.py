# Generated by Django 4.0.5 on 2022-06-27 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise', '0004_alter_questionanswercommon_answer_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cexercise',
            options={'verbose_name_plural': 'CExercise'},
        ),
        migrations.AlterModelOptions(
            name='cplusexercise',
            options={'verbose_name_plural': 'CPlusExercise'},
        ),
        migrations.AlterModelOptions(
            name='csharpexercise',
            options={'verbose_name_plural': 'CSharpExercise'},
        ),
        migrations.AlterModelOptions(
            name='dotnetexercise',
            options={'verbose_name_plural': 'DotNetExercise'},
        ),
        migrations.AlterModelOptions(
            name='javaexercise',
            options={'verbose_name_plural': 'JavaExercise'},
        ),
        migrations.AlterModelOptions(
            name='javascriptexercise',
            options={'verbose_name_plural': 'JavaScriptExercise'},
        ),
        migrations.AlterModelOptions(
            name='kotlinexercise',
            options={'verbose_name_plural': 'KotlinExercise'},
        ),
        migrations.AlterModelOptions(
            name='phpexercise',
            options={'verbose_name_plural': 'PHPExercise'},
        ),
        migrations.AlterModelOptions(
            name='pythonexercise',
            options={'verbose_name_plural': 'PythonExercise'},
        ),
        migrations.AlterModelOptions(
            name='rexercise',
            options={'verbose_name_plural': 'RExercise'},
        ),
        migrations.AlterModelOptions(
            name='swiftexercise',
            options={'verbose_name_plural': 'SwiftExercise'},
        ),
    ]
