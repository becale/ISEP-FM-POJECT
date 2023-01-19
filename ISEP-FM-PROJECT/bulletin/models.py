from django.db import models


# Create your models here. 



class Etudiant(models.Model):
    matricule = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=200)
    nationalite = models.CharField(max_length=200)
    
    class Sexe(models.TextChoices):
        FEMININ = "FEMININ"
        MASCULIN = "MASCULIN"

        def __str__(self):
            return str(self)
    sexe = models.CharField(max_length=200, choices=Sexe.choices)

    
    #mail = models.EmailField()
    #tel = models.CharField(max_length="15")

    class Filiere(models.TextChoices):
        GESTION="GESTION"
        STAPS="STAPS"
        MAS="MAS"
        
        def __str__(self):
            return str(self)

    class Specialite(models.TextChoices):
            EPS ="EPS"
            MDS="Management du Sport"
            EVE="EVENEMENTIEL"
            MSO="Metier du sport et de l'evenement sportif"

            def __str__(self):
                return str(self)
    class Specialite(models.TextChoices):
            EPS ="EPS"
            MDS="Management du Sport"
            EVE="EVENEMENTIEL"
            MSO="Metier du sport et de l'evenement sportif"

            def __str__(self):
                return str(self)
        
    class Niveau(models.TextChoices):
            NIVEAU1 = "1"
            NIVEAU2 = "2"
            NIVEAU3 = "3"

            def __str__(self):
                return str(self)
    Specialite = models.CharField(max_length=200, choices=Specialite.choices)
    filiere = models.CharField(max_length=200,choices=Filiere.choices)
    Specialite = models.CharField(max_length=200, choices=Specialite.choices)
    niveau = models.CharField(max_length=200,choices=Niveau.choices)

    def __str__(self):
        return str(self.nom)

class Semestre(models.Model):

    num_semestre = models.IntegerField()
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)

    def __str__(self):
        return str(self.num_semestre)


class UniteEnseignement(models.Model):

    etudiant = models.ManyToManyField(
        Etudiant, 
        through='Evaluation',
        #through_fields=('etudiant','uniteEnseignement'),
        )
    semestre = models.ForeignKey(Semestre,
     on_delete=models.SET_NULL,
     null=True,
     blank=True
     )
    code_UE = models.CharField(max_length=20)
    intitule_UE = models.CharField(max_length=500)

    volume_Horaire = models.IntegerField()
    nombre_credit = models.IntegerField()
    coefficient = models.IntegerField()

    class Groupe(models.TextChoices):
        FONDAMENTALE = "Fondanmental"
        TRANSVERSALE = "Transversal"
        PROFESSIONNELE = "Professionel"

        def __str__(self):
            return str(self)
    groupe = models.CharField(max_length=200, choices=Groupe.choices)

    def __str__(self):
        return str(self.intitule_UE)

class Evaluation(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    uniteEnseignement = models.ForeignKey(UniteEnseignement, on_delete=models.CASCADE)
    
    class NatureEvaluation(models.TextChoices):
        CC = "Contrôle_Continue"
        SN = "Session_Normale"

        def __str__(self):
            return str(self)
    natureEvaluation = models.CharField(max_length=50, choices=NatureEvaluation.choices)

    note = models.FloatField(null=False)
    #dateEvaluation = models.DateField()

    def __str__(self):
        return str(self)


"""class Filiere(models.Model):
    intitule_fil = models.CharField(200='200')

    def __str__(self):
        return str(self)

class Specialite(models.Model):
    filiere = models.ForeignKey(filiere,
     on_delete=models.SET_NULL,
     null=True,
     blank=True
     )
     
    intitule_spe = models.CharFied(max_length=200)

    def __str__(self):
        return str(self) """

"""class Stage(models.Model):
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    note_stage = models.FloatField(min_value(0.0), max_value(20.0))

    def __str__(self):
        return str(self)"""
