# Generated by Django 4.0.5 on 2022-07-04 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0013_alter_blogs_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutCommonParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='blogcomments',
            name='ip_address',
            field=models.GenericIPAddressField(default='45.243.82.169'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
