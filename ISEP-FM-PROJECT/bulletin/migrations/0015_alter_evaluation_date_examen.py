# Generated by Django 4.1.5 on 2023-02-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0014_remove_evaluation_date_rattrapage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='date_Examen',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]