# Generated by Django 4.0.5 on 2022-07-04 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0014_tutcommonparent_blogcomments_ip_address_blogs_author'),
        ('Projects', '0003_alter_androidprojects_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'AndroidProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='CPlusProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'CPlusProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='CProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'CProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='CSharpProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'CSharpProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='DotNetProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'DotNetProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='JavaProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'JavaProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='JavaScriptProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'JavaScriptProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='KotlinProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'KotlinProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='PHPProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'PHPProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='PythonProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'PythonProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='RProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'RProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='SwiftProjectsParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'SwiftProjects Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.AddField(
            model_name='androidprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cplusprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='csharpprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dotnetprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='javaprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='javascriptprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='kotlinprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='phpprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pythonprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='swiftprojects',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='androidprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.androidprojectsparent'),
        ),
        migrations.AddField(
            model_name='cplusprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.cplusprojectsparent'),
        ),
        migrations.AddField(
            model_name='cprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.cprojectsparent'),
        ),
        migrations.AddField(
            model_name='csharpprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.csharpprojectsparent'),
        ),
        migrations.AddField(
            model_name='dotnetprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.dotnetprojectsparent'),
        ),
        migrations.AddField(
            model_name='javaprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.javaprojectsparent'),
        ),
        migrations.AddField(
            model_name='javascriptprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.javascriptprojectsparent'),
        ),
        migrations.AddField(
            model_name='kotlinprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.kotlinprojectsparent'),
        ),
        migrations.AddField(
            model_name='phpprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.phpprojectsparent'),
        ),
        migrations.AddField(
            model_name='pythonprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.pythonprojectsparent'),
        ),
        migrations.AddField(
            model_name='rprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.rprojectsparent'),
        ),
        migrations.AddField(
            model_name='swiftprojects',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Projects.swiftprojectsparent'),
        ),
    ]
