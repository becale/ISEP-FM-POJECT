# Generated by Django 4.1.5 on 2023-02-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0011_alter_etudiant_specialite_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniteenseignement',
            name='groupe',
            field=models.CharField(choices=[('Fondanmental', 'Fondamentale'), ('Transversal', 'Transversale'), ('Professionel', 'Professionnele'), ('Specialite', 'Specialite')], max_length=200),
        ),
    ]
