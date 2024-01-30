from django.db import models


# Create your models here. 



class Etudiant(models.Model):
    matricule = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=200)
    nationalite = models.CharField(max_length=200)

    moyS1 = models.FloatField(null=True, blank=True)
    crS1 = models.IntegerField(null=True, blank=True)
    
    moyS2 = models.FloatField(null=True, blank=True)
    crS2 = models.IntegerField(null=True, blank=True)

    moyS3 = models.FloatField(null=True, blank=True)
    crS3 = models.IntegerField(null=True,blank=True)

    moyS4 = models.FloatField(null=True,blank=True)
    crS4 = models.IntegerField(null=True, blank=True)

    moyS5 = models.FloatField(null=True, blank=True)
    crS5 = models.IntegerField(null=True, blank=True)

    moyS6 = models.FloatField(null=True, blank=True)
    crS6 = models.IntegerField(null=True, blank=True)


    
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
            MSO="MSO"

            def __str__(self):
                return str(self)
    """class Specialite(models.TextChoices):
            EPS ="EPS"
            MDS="Management du Sport"
            EVE="EVENEMENTIEL"
            MSO="Metier du sport et de l'evenement sportif"

            def __str__(self):
                return str(self)"""
        
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

    class Redoublant(models.TextChoices):
        oui = '1'
        non = '0'

        def __str__(self):
            return str(self)
    redoublant = models.CharField(choices=Redoublant.choices)

    def __str__(self):
        return str(self.nom)

class Semestre(models.Model):

    num_semestre = models.IntegerField()
    date_debut = models.DateField(null=True)
    date_fin = models.DateField(null=True)
    date_CC = models.DateField(null=True)
    date_SN = models.DateField(null=True)

    def __str__(self):
        return str('Semestre '+str(self.num_semestre))


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
    filiere = models.CharField
    coefficient = models.IntegerField()

    class Filiere(models.TextChoices):
        GESTION="GESTION"
        STAPS="STAPS"
        MAS="MAS"
        
        def __str__(self):
            return str(self)
    filiere = models.CharField(max_length=200,choices=Filiere.choices, null=True)

    class Specialite(models.TextChoices):
            MDS="Management du Sport"
            EVE="EVENEMENTIEL"
            MSO="MSO"
            TRC="Tronc-Commun"
            EPS="EPS"

            def __str__(self):
                return str(self)
    Specialite = models.CharField(max_length=200, choices=Specialite.choices, null=True)
    
    class Groupe(models.TextChoices):
        FONDAMENTALE = "Fondanmental"
        TRANSVERSALE = "Transversal"
        PROFESSIONNELE = "Professionel"
        SPECIALITE = "Specialite"

        def __str__(self):
            return str(self)
    groupe = models.CharField(max_length=200, choices=Groupe.choices)

    def __str__(self):
        return str(self.code_UE+' '+self.intitule_UE)

class Evaluation(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    uniteEnseignement = models.ForeignKey(UniteEnseignement, on_delete=models.CASCADE)
    
    """class NatureEvaluation(models.TextChoices):
        CC = "Contrôle_Continue"
        SN = "Session_Normale"
        RT = "Rattrapage"

        def __str__(self):
            return str(self.cc+self.SN)"""
    natureEvaluation = models.CharField(max_length=50)#, choices=NatureEvaluation.choices)

    note_cc = models.FloatField(null=False)
    note_sn = models.FloatField(null=False)
    note_Examen = models.FloatField(null=False)
    date_Examen = models.DateField(null=True, default='1800-01-01', blank=True)
    
    note_rattrapage = models.FloatField(null=True)
    date_Rattrapage = models.DateField(null=True)

    #Ajout du champ date pour les évaluation

    def __str__(self):
        return str(self.natureEvaluation +'_'+self.uniteEnseignement.code_UE+'_'+self.etudiant.nom)

class Calendrier(models.Model):
    annee_academique = models.CharField(max_length=50)

    debut_SN1 = models.DateField(null=True, default="", blank=True)
    fin_SN1 = models.DateField(null=True, default="", blank=True)

    debut_SN2 = models.DateField(null=True, default="", blank=True)
    fin_SN2 = models.DateField(null=True, default="", blank=True)

    def __str__(self):
        return str('Annee Acamdeique '+self.annee_academique )

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

