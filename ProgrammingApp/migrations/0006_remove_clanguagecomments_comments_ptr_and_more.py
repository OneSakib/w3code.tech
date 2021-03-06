# Generated by Django 4.0.5 on 2022-07-02 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProgrammingApp', '0005_alter_androidlanguage_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='clanguagecomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='cpluslanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='cpluslanguagecomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='csharplanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='csharplanguagecomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='dotnetlanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='dotnetlanguagecomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='javalanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='javalanguagecomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='javascriptlanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='javascriptlanguagecomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='kotlinlanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='kotlinlanguagecomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='phplanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='phplanguagecomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='pythonlanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='pythonlanguagecomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='rlanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='rlanguagecomments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='swiftlanguagecomments',
            name='comments_ptr',
        ),
        migrations.RemoveField(
            model_name='swiftlanguagecomments',
            name='post',
        ),
        migrations.DeleteModel(
            name='AndroidLanguageComments',
        ),
        migrations.DeleteModel(
            name='CLanguageComments',
        ),
        migrations.DeleteModel(
            name='CplusLanguageComments',
        ),
        migrations.DeleteModel(
            name='CsharpLanguageComments',
        ),
        migrations.DeleteModel(
            name='DotNetLanguageComments',
        ),
        migrations.DeleteModel(
            name='JavaLanguageComments',
        ),
        migrations.DeleteModel(
            name='JavaScriptLanguageComments',
        ),
        migrations.DeleteModel(
            name='KotlinLanguageComments',
        ),
        migrations.DeleteModel(
            name='PHPLanguageComments',
        ),
        migrations.DeleteModel(
            name='PythonLanguageComments',
        ),
        migrations.DeleteModel(
            name='RLanguageComments',
        ),
        migrations.DeleteModel(
            name='SwiftLanguageComments',
        ),
    ]
