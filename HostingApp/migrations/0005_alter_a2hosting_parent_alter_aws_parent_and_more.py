# Generated by Django 4.0.5 on 2022-07-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HostingApp', '0004_pythonanywherelike_msazurelike_inmotionhostinglike_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a2hosting',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.a2hostingparent'),
        ),
        migrations.AlterField(
            model_name='aws',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.awsparent'),
        ),
        migrations.AlterField(
            model_name='bluehost',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.bluehostparent'),
        ),
        migrations.AlterField(
            model_name='digitalocean',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.digitaloceanparent'),
        ),
        migrations.AlterField(
            model_name='githubhost',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.githubhostparent'),
        ),
        migrations.AlterField(
            model_name='godaddy',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.godaddyparent'),
        ),
        migrations.AlterField(
            model_name='greengeeks',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.greengeeksparent'),
        ),
        migrations.AlterField(
            model_name='herokuapp',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.herokuappparent'),
        ),
        migrations.AlterField(
            model_name='hostgator',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.hostgatorparent'),
        ),
        migrations.AlterField(
            model_name='hostinger',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.hostingerparent'),
        ),
        migrations.AlterField(
            model_name='inmotionhosting',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.inmotionhostingparent'),
        ),
        migrations.AlterField(
            model_name='msazure',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.msazureparent'),
        ),
        migrations.AlterField(
            model_name='pythonanywhere',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostingApp.pythonanywhereparent'),
        ),
    ]