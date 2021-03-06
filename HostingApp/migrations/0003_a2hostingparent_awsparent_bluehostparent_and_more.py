# Generated by Django 4.0.5 on 2022-07-04 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0014_tutcommonparent_blogcomments_ip_address_blogs_author'),
        ('HostingApp', '0002_alter_a2hosting_options_alter_aws_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='A2HostingParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': ' A2Hosting Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='AWSParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'AWS Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='BlueHostParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'BlueHost Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='DigitalOceanParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'DigitalOcean Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='GithubHostParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'GithubHost Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='GoDaddyParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'GoDaddy Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='GreenGeeksParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'GreenGeeks Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='HerokuAppParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'HerokuApp Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='HostGatorParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'HostGator Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='HostingerParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'Hostinger Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='InMotionHostingParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'InMotionHosting Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='MSAzureParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'MSAzure Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.CreateModel(
            name='PythonAnywhereParent',
            fields=[
                ('tutcommonparent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.tutcommonparent')),
            ],
            options={
                'verbose_name_plural': 'PythonAnywhere Parent',
            },
            bases=('MainApp.tutcommonparent',),
        ),
        migrations.AddField(
            model_name='a2hosting',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='aws',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bluehost',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='digitalocean',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='githubhost',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='godaddy',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='greengeeks',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='herokuapp',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hostgator',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hostinger',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inmotionhosting',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='msazure',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pythonanywhere',
            name='author',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='a2hosting',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.a2hostingparent'),
        ),
        migrations.AddField(
            model_name='aws',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.awsparent'),
        ),
        migrations.AddField(
            model_name='bluehost',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.bluehostparent'),
        ),
        migrations.AddField(
            model_name='digitalocean',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.digitaloceanparent'),
        ),
        migrations.AddField(
            model_name='githubhost',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.githubhostparent'),
        ),
        migrations.AddField(
            model_name='godaddy',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.godaddyparent'),
        ),
        migrations.AddField(
            model_name='greengeeks',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.greengeeksparent'),
        ),
        migrations.AddField(
            model_name='herokuapp',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.herokuappparent'),
        ),
        migrations.AddField(
            model_name='hostgator',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.hostgatorparent'),
        ),
        migrations.AddField(
            model_name='hostinger',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.hostingerparent'),
        ),
        migrations.AddField(
            model_name='inmotionhosting',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.inmotionhostingparent'),
        ),
        migrations.AddField(
            model_name='msazure',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.msazureparent'),
        ),
        migrations.AddField(
            model_name='pythonanywhere',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HostingApp.pythonanywhereparent'),
        ),
    ]
