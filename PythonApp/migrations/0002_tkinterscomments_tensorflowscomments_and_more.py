# Generated by Django 4.0.5 on 2022-06-20 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_comments'),
        ('PythonApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TkintersComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TkintersComments', to='PythonApp.tkinters')),
            ],
            options={
                'verbose_name_plural': 'TkintersComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='TensorflowsComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TensorflowsComments', to='PythonApp.tensorflows')),
            ],
            options={
                'verbose_name_plural': 'TensorflowsComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='SeleniumsComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SeleniumsComments', to='PythonApp.seleniums')),
            ],
            options={
                'verbose_name_plural': 'SeleniumsComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='ScipysComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ScipysComments', to='PythonApp.scipys')),
            ],
            options={
                'verbose_name_plural': 'ScipysComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='PytorchsComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PytorchsComments', to='PythonApp.pytorchs')),
            ],
            options={
                'verbose_name_plural': 'PytorchsComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='PygamesComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PygamesComments', to='PythonApp.pygames')),
            ],
            options={
                'verbose_name_plural': 'PygamesComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='PillowsComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PillowsComments', to='PythonApp.pillows')),
            ],
            options={
                'verbose_name_plural': 'PillowsComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='PandassComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PandassComments', to='PythonApp.pandass')),
            ],
            options={
                'verbose_name_plural': 'PandassComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='OpenCVsComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='OpenCVsComments', to='PythonApp.opencvs')),
            ],
            options={
                'verbose_name_plural': 'OpenCVsComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='NumpysComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NumpysComments', to='PythonApp.numpys')),
            ],
            options={
                'verbose_name_plural': 'NumpysComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='MatplotlibsComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MatplotlibsComments', to='PythonApp.matplotlibs')),
            ],
            options={
                'verbose_name_plural': 'MatplotlibsComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='MachineLearningComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MachineLearningComments', to='PythonApp.machinelearning')),
            ],
            options={
                'verbose_name_plural': 'MachineLearningComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='KivysComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='KivysComments', to='PythonApp.kivys')),
            ],
            options={
                'verbose_name_plural': 'KivysComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='JupytersComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='JupytersComments', to='PythonApp.jupyters')),
            ],
            options={
                'verbose_name_plural': 'JupytersComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='FlaskComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FlaskComments', to='PythonApp.flask')),
            ],
            options={
                'verbose_name_plural': 'FlaskComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='DjangoComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DjangoComments', to='PythonApp.django')),
            ],
            options={
                'verbose_name_plural': 'DjangoComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='DeepLearningComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DeepLearningComments', to='PythonApp.deeplearning')),
            ],
            options={
                'verbose_name_plural': 'DeepLearningComments',
            },
            bases=('MainApp.comments',),
        ),
        migrations.CreateModel(
            name='DataScienceComments',
            fields=[
                ('comments_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MainApp.comments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DataScienceComments', to='PythonApp.datascience')),
            ],
            options={
                'verbose_name_plural': 'DataScienceComments',
            },
            bases=('MainApp.comments',),
        ),
    ]
