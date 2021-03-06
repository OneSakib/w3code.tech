# Generated by Django 4.0.5 on 2022-06-20 11:24

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AndroidLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'AndroidLanguage',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='CLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'CLanguage',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='CplusLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'CplusLanguage',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='CsharpLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'CsharpLanguage',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='JavaLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'JavaLanguage',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='KotlinLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'KotlinLanguage',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='PHPLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'PHPLanguage',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='PythonLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'PythonLanguage',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='RLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'RLanguage',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='SwiftLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'SwiftLanguage',
                'ordering': ['-timestamp'],
            },
        ),
    ]
