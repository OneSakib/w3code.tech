# Generated by Django 4.0.5 on 2022-06-27 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PreparationApp', '0002_verbalabilitycomments_reasoningcomments_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aptitude',
            options={'verbose_name_plural': 'Aptitude'},
        ),
        migrations.AlterModelOptions(
            name='companyquestion',
            options={'verbose_name_plural': 'CompanyQuestion'},
        ),
        migrations.AlterModelOptions(
            name='interviewquestion',
            options={'verbose_name_plural': 'InterviewQuestion'},
        ),
        migrations.AlterModelOptions(
            name='reasoning',
            options={'verbose_name_plural': 'Reasoning'},
        ),
        migrations.AlterModelOptions(
            name='verbalability',
            options={'verbose_name_plural': 'VerbalAbility'},
        ),
    ]