# Generated by Django 4.1.5 on 2023-08-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0017_evaluation_date_rattrapage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='crS1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='crS2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='crS3',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='crS4',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='crS5',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='crS6',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='moyS1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='moyS2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='moyS3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='moyS4',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='moyS5',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='moyS6',
            field=models.FloatField(null=True),
        ),
    ]
