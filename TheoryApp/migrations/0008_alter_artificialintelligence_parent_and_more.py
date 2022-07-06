# Generated by Django 4.0.5 on 2022-07-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TheoryApp', '0007_webapilike_softwareengineeringlike_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artificialintelligence',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.artificialintelligenceparent'),
        ),
        migrations.AlterField(
            model_name='automata',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.automataparent'),
        ),
        migrations.AlterField(
            model_name='compilerdesign',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.compilerdesignparent'),
        ),
        migrations.AlterField(
            model_name='computergraphics',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.computergraphicsparent'),
        ),
        migrations.AlterField(
            model_name='computernetwork',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.computernetworkparent'),
        ),
        migrations.AlterField(
            model_name='computerorganization',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.computerorganizationparent'),
        ),
        migrations.AlterField(
            model_name='cybersecurity',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.cybersecurityparent'),
        ),
        migrations.AlterField(
            model_name='daa',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.daaparent'),
        ),
        migrations.AlterField(
            model_name='datamining',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.dataminingparent'),
        ),
        migrations.AlterField(
            model_name='datastructure',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.datastructureparent'),
        ),
        migrations.AlterField(
            model_name='dbms',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.dbmsparent'),
        ),
        migrations.AlterField(
            model_name='ddbms',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.ddbmsparent'),
        ),
        migrations.AlterField(
            model_name='discretemathematics',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.discretemathematicsparent'),
        ),
        migrations.AlterField(
            model_name='operatingsystem',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.operatingsystemparent'),
        ),
        migrations.AlterField(
            model_name='softwareengineering',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.softwareengineeringparent'),
        ),
        migrations.AlterField(
            model_name='webapi',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TheoryApp.webapiparent'),
        ),
    ]
