# Generated by Django 4.1.5 on 2023-01-08 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='date_naissance',
            field=models.DateField(),
        ),
    ]
