# Generated by Django 4.0.5 on 2022-07-06 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0018_blogslike'),
        ('Exercise', '0007_swiftexerciselike_rexerciselike_pythonexerciselike_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'CExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='CPlusExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'CPlusExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='CSharpExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'CSharpExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='DotNetExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'DotNetExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='JavaExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'JavaExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='JavaScriptExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'JavaScriptExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='KotlinExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'KotlinExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='PHPExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'PHPExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='PythonExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'PythonExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='RExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'RExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='SwiftExerciseParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'SwiftExercise Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.AddField(
            model_name='cexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.cexerciseparent'),
        ),
        migrations.AddField(
            model_name='cplusexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.cplusexerciseparent'),
        ),
        migrations.AddField(
            model_name='csharpexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.csharpexerciseparent'),
        ),
        migrations.AddField(
            model_name='dotnetexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.dotnetexerciseparent'),
        ),
        migrations.AddField(
            model_name='javaexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.javaexerciseparent'),
        ),
        migrations.AddField(
            model_name='javascriptexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.javascriptexerciseparent'),
        ),
        migrations.AddField(
            model_name='kotlinexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.kotlinexerciseparent'),
        ),
        migrations.AddField(
            model_name='phpexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.phpexerciseparent'),
        ),
        migrations.AddField(
            model_name='pythonexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.pythonexerciseparent'),
        ),
        migrations.AddField(
            model_name='rexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.rexerciseparent'),
        ),
        migrations.AddField(
            model_name='swiftexercise',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Exercise.swiftexerciseparent'),
        ),
    ]
