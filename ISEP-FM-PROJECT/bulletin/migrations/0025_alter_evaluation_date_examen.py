# Generated by Django 4.1.5 on 2024-02-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0024_rename_annee_acadmeqique_semestre_annee_academique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='date_Examen',
            field=models.DateField(blank=True, default='00-00-00', null=True),
        ),
    ]