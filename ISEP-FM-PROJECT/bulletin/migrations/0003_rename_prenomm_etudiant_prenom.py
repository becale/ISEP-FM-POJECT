# Generated by Django 4.1.5 on 2023-01-08 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0002_alter_etudiant_date_naissance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='etudiant',
            old_name='prenomm',
            new_name='prenom',
        ),
    ]
