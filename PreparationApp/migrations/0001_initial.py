# Generated by Django 4.0.5 on 2022-06-20 11:24

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aptitude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Aptitude',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='CompanyQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'CompanyQuestion',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='InterviewQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'InterviewQuestion',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Reasoning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Reasoning',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='VerbalAbility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', tinymce.models.HTMLField()),
                ('viewcounter', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'VerbalAbility',
                'ordering': ['-timestamp'],
            },
        ),
    ]
