# Generated by Django 4.1.5 on 2023-01-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0005_evaluation_dateevaluation_evaluation_note_examen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='Specialite',
            field=models.CharField(choices=[('EPS', 'Eps'), ('Management du Sport', 'Mds'), ('EVENEMENTIEL', 'Eve'), ('MSO', 'Mso')], max_length=200),
        ),
    ]
