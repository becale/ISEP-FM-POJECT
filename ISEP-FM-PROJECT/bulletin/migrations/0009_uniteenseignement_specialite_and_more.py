# Generated by Django 4.1.5 on 2023-02-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0008_semestre_date_cc_semestre_date_sn_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniteenseignement',
            name='Specialite',
            field=models.CharField(choices=[('EPS', 'Eps'), ('Management du Sport', 'Mds'), ('EVENEMENTIEL', 'Eve'), ('MSO', 'Mso')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='uniteenseignement',
            name='filiere',
            field=models.CharField(choices=[('GESTION', 'Gestion'), ('STAPS', 'Staps'), ('MAS', 'Mas')], max_length=200, null=True),
        ),
    ]
