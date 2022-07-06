# Generated by Django 4.0.5 on 2022-07-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0005_swiftprojectslike_rprojectslike_pythonprojectslike_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='androidprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.androidprojectsparent'),
        ),
        migrations.AlterField(
            model_name='cplusprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.cplusprojectsparent'),
        ),
        migrations.AlterField(
            model_name='cprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.cprojectsparent'),
        ),
        migrations.AlterField(
            model_name='csharpprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.csharpprojectsparent'),
        ),
        migrations.AlterField(
            model_name='dotnetprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.dotnetprojectsparent'),
        ),
        migrations.AlterField(
            model_name='javaprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.javaprojectsparent'),
        ),
        migrations.AlterField(
            model_name='javascriptprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.javascriptprojectsparent'),
        ),
        migrations.AlterField(
            model_name='kotlinprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.kotlinprojectsparent'),
        ),
        migrations.AlterField(
            model_name='phpprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.phpprojectsparent'),
        ),
        migrations.AlterField(
            model_name='pythonprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.pythonprojectsparent'),
        ),
        migrations.AlterField(
            model_name='rprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.rprojectsparent'),
        ),
        migrations.AlterField(
            model_name='swiftprojects',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.swiftprojectsparent'),
        ),
    ]
