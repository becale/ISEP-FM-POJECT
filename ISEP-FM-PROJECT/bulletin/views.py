from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from itertools import islice

from django.views.generic import View
from .utils import render_to_pdf 

import statistics as stat


# Create your views here.

def home(request):
    
    template = loader.get_template('bulletin/home.html')
    return HttpResponse(template.render({}, request))

def bulletin(request):
    template = loader.get_template('bulletin/bulletin.html')
    return HttpResponse(template.render({}, request))

def bulletinCollectif(request):
    template = loader.get_template('bulletin/releveCommun/bulletinCollectif.html')
    return HttpResponse(template.render({}, request))

def notes(request):
    #les données des etudiants, notes et matières doivent être chargées dans cette pages et receptionnées


    template = loader.get_template('bulletin/notes.html')
    return HttpResponse(template.render({}, request))


############### API REQUETTES GET###########################################################
def EtudiantApi(request):
    mydata = list(Etudiant.objects.all().values())

    return JsonResponse(mydata, safe=False)

def EtudiantNiveau1Staps(request):
    etudiantStaps1 = list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values())
    
    return JsonResponse(etudiantStaps1, safe= False)

def EtudiantNiveau1MDS(request):
    etudiantMDS1 = list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values())

    return JsonResponse(etudiantMDS1, safe= False)

def EtudiantNiveau2Staps(request):
    etudiantStaps2 = list(Etudiant.objects.filter(filiere="STAPS", niveau=2).values())

    return JsonResponse(etudiantStaps2, safe= False)

def EtudiantNiveau3(request):
    etudiantMAS = list(Etudiant.objects.filter(filiere="MAS", niveau=3).values())

    return JsonResponse(etudiantMAS, safe= False)

def EtudiantNiveau3MSO(request):
    etudiantMSO = list(Etudiant.objects.filter(Specialite="MSO", niveau=3).values())

    return JsonResponse(etudiantMSO, safe= False)

def EtudiantNiveau3EVE(request):
    etudiantEVE = list(Etudiant.objects.filter(Specialite="EVENEMENTIEL", niveau=3).values())

    return JsonResponse(etudiantEVE, safe= False)

def UEAPI(request):
    mydata = list(UniteEnseignement.objects.all().values())

    return JsonResponse(mydata, safe=False)


############### API REQUETTES POST ###########################################################
def AddNoteEtudiant(request):
    if request.method == 'POST':
        data = request.POST

    key,values = extract(data)
    
    #Ajout de la fonction de couplage
    saveData(key,values)
    print(key, values)
    text = "<html><body> %s </body></html>" % data
    return JsonResponse(request.POST, safe=False)


def test(request):
    return render(request, 'bulletin/BulletinTemplate/bulletin1.html')



################################# REQUETES POUR BULLETIN SEMESTRE 1 3 5 #############################################################
def bulls1epsmds(request, filiere):
    if (filiere =='GESTION'):

        infoEtudiantMDS =list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

        coefS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("coefficient", "intitule_UE"))
        coefS1MDS1 = epurationCoef(coefS1MDS1)

        creditS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("nombre_credit"))
        creditS1MDS1 = epurationCre(creditS1MDS1)
        
        MDS111 =list(Evaluation.objects.filter(uniteEnseignement_id=40).values('note_Examen'))
        sort111 = epurationTriCroissant(MDS111)

        MDS111b =list(Evaluation.objects.filter(uniteEnseignement_id=41).values('note_Examen'))
        sort111b = epurationTriCroissant(MDS111b)

        MDS112 =list(Evaluation.objects.filter(uniteEnseignement_id=42).values('note_Examen'))
        sort112 = epurationTriCroissant(MDS112)

        MDS112b =list(Evaluation.objects.filter(uniteEnseignement_id=43).values('note_Examen'))
        sort112b = epurationTriCroissant(MDS112b)

        MDS113 =list(Evaluation.objects.filter(uniteEnseignement_id=44).values('note_Examen'))
        sort113 = epurationTriCroissant(MDS113)

        MDS114 =list(Evaluation.objects.filter(uniteEnseignement_id=45).values('note_Examen'))
        sort114 = epurationTriCroissant(MDS114)

        MDS115 =list(Evaluation.objects.filter(uniteEnseignement_id=46).values('note_Examen'))
        sort115 = epurationTriCroissant(MDS115)

        MDS116 =list(Evaluation.objects.filter(uniteEnseignement_id=47).values('note_Examen'))
        sort116 = epurationTriCroissant(MDS116)

        MDS117 =list(Evaluation.objects.filter(uniteEnseignement_id=48).values('note_Examen'))
        sort117 = epurationTriCroissant(MDS117)

        MDS117b =list(Evaluation.objects.filter(uniteEnseignement_id=49).values('note_Examen'))
        sort117b = epurationTriCroissant(MDS117b)

        listeMatrice = []
        mds1Moyenne = []

        for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

            matrice = [
                infoEtudiantMDS[j],

                [ MDS111[j], coefS1MDS1[0], MDS111[j]*coefS1MDS1[0], round( ((MDS111[j]*coefS1MDS1[0]) + (MDS111b[j]*coefS1MDS1[1]) + ( MDS112[j]*coefS1MDS1[2]) + (MDS112b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2), sort111.index(MDS111[j])+1,(MDS111[j]>=10), creditS1MDS1[0] ],

                [ MDS111b[j], coefS1MDS1[1], MDS111b[j]*coefS1MDS1[1], "MOYENNE", sort111b.index(MDS111b[j])+1,(MDS111b[j]>=10), creditS1MDS1[1]],

                [ MDS112[j], coefS1MDS1[2], MDS112[j]*coefS1MDS1[2], "MOYENNE", sort112.index(MDS112[j])+1,(MDS112[j]>=10), creditS1MDS1[2]],

                [ MDS112b[j], coefS1MDS1[3], MDS112b[j]*coefS1MDS1[3], "MOYENNE", sort112b.index(MDS112b[j])+1,(MDS112b[j]>=10), creditS1MDS1[3]],


                [ MDS113[j], coefS1MDS1[4], MDS113[j]*coefS1MDS1[4], 

                round( ((MDS113[j]*coefS1MDS1[4]) + (MDS114[j]*coefS1MDS1[5]) + MDS115[j]*coefS1MDS1[6] + MDS116[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2), 
                
                sort113.index(MDS113[j])+1,
                (MDS113[j]>=10), 
                creditS1MDS1[4]],

                [ MDS114[j], coefS1MDS1[5], MDS114[j]*coefS1MDS1[5], "MOYENNE", sort114.index(MDS114[j])+1,(MDS114[j]>=10), creditS1MDS1[5]],

                [ MDS115[j], coefS1MDS1[6], MDS115[j]*coefS1MDS1[6], "MOYENNE", sort115.index(MDS115[j])+1,(MDS115[j]>=10), creditS1MDS1[6]],

                [ MDS116[j], coefS1MDS1[7], MDS116[j]*coefS1MDS1[7], "MOYENNE", sort116.index(MDS116[j])+1,(MDS116[j]>=10), creditS1MDS1[7]],


                [ MDS117[j], coefS1MDS1[8], MDS117[j]*coefS1MDS1[8], 
                
                round(( MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2), 
                sort117.index(MDS117[j])+1,
                (MDS117[j]>=10), 
                creditS1MDS1[8]],

                [ MDS117b[j], coefS1MDS1[9], MDS117b[j]*coefS1MDS1[9], "MOYENNE", sort117b.index(MDS117b[j])+1,(MDS117b[j]>=10), creditS1MDS1[9]],

                [
                    ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),

                   round (MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] , 2),

                   round (( MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                ]

            ]

            listeMatrice.append(matrice)
            mds1Moyenne.append(matrice[11][2])
            mds1Moyenne.sort(reverse=True)

            moy = stat.mean(mds1Moyenne)
            moy = round(moy, 2)
            session = 'Janvier 2023'

            #filiere, listeMatrice, staps1Moyenne, moy, session

        semestre1MDS = [filiere,  listeMatrice, mds1Moyenne,  moy, session] #infoEtudiantMDS, coefS1MDS1, creditS1MDS1, MDS111, MDS111b, MDS112, MDS112b, MDS113, MDS114, MDS115, MDS116, MDS117, MDS117b,
        
    elif (filiere == 'STAPS1'):
        
        infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

        coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("coefficient"))
        coefS1STAPS1 = epurationCoef(coefS1STAPS1)

        creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("nombre_credit"))
        creditS1STAPS1 = epurationCre(creditS1STAPS1)

        EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=50).values('note_Examen'))
        sort111 = epurationTriCroissant(EPS111)

        EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=51).values('note_Examen'))
        sort112 = epurationTriCroissant(EPS112)

        EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=52).values('note_Examen'))
        sort113 = epurationTriCroissant(EPS113)

        EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=53).values('note_Examen'))
        sort114 = epurationTriCroissant(EPS114)

        EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=54).values('note_Examen'))
        sort115a = epurationTriCroissant(EPS115a)

        EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=55).values('note_Examen'))
        sort115b = epurationTriCroissant(EPS115b) 

        EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=56).values('note_Examen'))
        sort115j = epurationTriCroissant(EPS115j)

        EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=57).values('note_Examen'))
        sort115l = epurationTriCroissant(EPS115l)

        EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=58).values('note_Examen'))
        sort116 = epurationTriCroissant(EPS116)

        EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=59).values('note_Examen')) 
        sort117 = epurationTriCroissant(EPS117)

        EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=60).values('note_Examen'))
        sort118 = epurationTriCroissant(EPS118)

        EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=61).values('note_Examen'))
        sort119 = epurationTriCroissant(EPS119)

        student = {}
        temp = {}
        staps1 = []
        staps1Moyenne = []
        listeMatrice = [ ]

        for j in range( len(infoEtudiantSTAPS1) ):

            #for j in range( len(coefS1STAPS1) ):
            matrice = [
                    infoEtudiantSTAPS1[j],

                    [ EPS111[j], coefS1STAPS1[0], EPS111[j]*coefS1STAPS1[0], round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2), sort111.index(EPS111[j])+1,(EPS111[j]>=10), creditS1STAPS1[0]],

                    [ EPS112[j], coefS1STAPS1[1], EPS112[j]*coefS1STAPS1[1], "MOYENNE", sort112.index(EPS112[j])+1,(EPS112[j]>=10), creditS1STAPS1[1]],

                    [ EPS113[j], 

                        coefS1STAPS1[2], 

                        EPS113[j]*coefS1STAPS1[2], 

                        round( ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5]) + (EPS115j[j]*coefS1STAPS1[6]) + (EPS115l[j]*coefS1STAPS1[7]) + (EPS116[j]*coefS1STAPS1[8]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]) ,2), 
                        
                        sort113.index(EPS113[j])+1,
                        
                        (EPS113[j] >=10),
                        
                        creditS1STAPS1[2]
                    ],

                    [ EPS114[j],  coefS1STAPS1[3], EPS114[j]*coefS1STAPS1[3], "MOYENNE", sort114.index(EPS114[j])+1, (EPS114[j] >=10), creditS1STAPS1[3] ],

                    [ EPS115a[j], coefS1STAPS1[4], EPS115a[j]*coefS1STAPS1[4], "MOYENNE", sort115a.index(EPS115a[j])+1, (EPS115a[j] >=10), creditS1STAPS1[4] ], #crédits

                    [ EPS115b[j], coefS1STAPS1[5], EPS115b[j]*coefS1STAPS1[5], "MOYENNE", sort115b.index(EPS115b[j])+1, (EPS115b[j] >=10), creditS1STAPS1[5] ],

                    [ EPS115j[j], coefS1STAPS1[6], EPS115j[j]*coefS1STAPS1[6], "MOYENNE", sort115j.index(EPS115j[j])+1, (EPS115j[j] >=10), creditS1STAPS1[6] ],

                    [ EPS115l[j], coefS1STAPS1[7], EPS115l[j]*coefS1STAPS1[7], "MOYENNE", sort115l.index(EPS115l[j])+1, (EPS115l[j] >=10), creditS1STAPS1[7] ],

                    [ EPS116[j],  coefS1STAPS1[8], EPS116[j]*coefS1STAPS1[8], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[8] ],

                    [ EPS117[j], coefS1STAPS1[9], 

                        EPS117[j]*coefS1STAPS1[9], 

                        round( ((EPS117[j]*coefS1STAPS1[9]) + (EPS118[j]*coefS1STAPS1[10]) + (EPS119[j]*coefS1STAPS1[11])) / ( coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]) ,2), 

                        sort117.index(EPS117[j])+1, 

                        (EPS117[j] >=10), 
                        
                        creditS1STAPS1[9] 
                    ],

                    [ EPS118[j], coefS1STAPS1[10], EPS118[j]*coefS1STAPS1[10], "MOYENNE", sort118.index(EPS118[j])+1, (EPS118[j] >=10), creditS1STAPS1[10] ],

                    [ EPS119[j], coefS1STAPS1[11], EPS119[j]*coefS1STAPS1[11], "MOYENNE", sort119.index(EPS119[j])+1, (EPS119[j] >=10), creditS1STAPS1[11] ],

                    [ 
                        ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ),

                        round( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115j[j]*coefS1STAPS1[6]+EPS115l[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11], 2),

                        round(( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115j[j]*coefS1STAPS1[6]+EPS115l[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2 ),

                        4,
                        5
                    ]
            ]
            staps1Moyenne.append(matrice[13][2])



            listeMatrice.append(matrice)
            
        #infoEtudiantSTAPS1, coefS1STAPS1, creditS1STAPS1, EPS111, EPS112, EPS113, EPS114, EPS115a ,EPS115b, EPS115j, EPS115l, EPS116, EPS117, EPS118, EPS119, 

        staps1Moyenne.sort(reverse=True)
        moy = stat.mean(staps1Moyenne)
        moy = round(moy, 2)
        session = 'Janvier 2023'
            
        semestre1MDS = [filiere, listeMatrice, staps1Moyenne, moy, session ]


    return render(request,'bulletin/BulletinTemplate/bullS1eps.html', {'semestre1MDS': semestre1MDS}) 





####################################################################################### STAPS2 ###############################################################################
def bulls3eps2(request, filiere):
    
    filiere = filiere

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=2).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=3,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = epurationCoef(coefS1STAPS1)

    creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=3,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS1 = epurationCre(creditS1STAPS1)

    EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=62).values('note_Examen'))
    sort111 = epurationTriCroissant(EPS111)

    EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=63).values('note_Examen'))
    sort112 = epurationTriCroissant(EPS112)

    EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=64).values('note_Examen'))
    sort113 = epurationTriCroissant(EPS113)

    EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=65).values('note_Examen'))
    sort114 = epurationTriCroissant(EPS114)

    EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=66).values('note_Examen'))
    sort115a = epurationTriCroissant(EPS115a)

    EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=67).values('note_Examen'))
    sort115b = epurationTriCroissant(EPS115b) 

    EPS115f = list(Evaluation.objects.filter(uniteEnseignement_id=68).values('note_Examen'))
    sort115f = epurationTriCroissant(EPS115f)

    EPS115g = list(Evaluation.objects.filter(uniteEnseignement_id=69).values('note_Examen'))
    sort115g = epurationTriCroissant(EPS115g)

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=70).values('note_Examen'))
    sort115j = epurationTriCroissant(EPS115j)

    EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=71).values('note_Examen')) 
    sort115l = epurationTriCroissant(EPS115l)

    EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=72).values('note_Examen'))
    sort116 = epurationTriCroissant(EPS116)

    EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=73).values('note_Examen'))
    sort117 = epurationTriCroissant(EPS117)

    EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=74).values('note_Examen'))
    sort118 = epurationTriCroissant(EPS118)

    EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=75).values('note_Examen'))
    sort119 = epurationTriCroissant(EPS119)

    staps1Moyenne = []
    listeMatrice = []

    for j in range( len(infoEtudiantSTAPS1) ):

            matrice = [
                    infoEtudiantSTAPS1[j],

                    [ EPS111[j], coefS1STAPS1[0], EPS111[j]*coefS1STAPS1[0], round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1])) / (coefS1STAPS1[0]+coefS1STAPS1[1]), 2 ), sort111.index(EPS111[j])+1,(EPS111[j]>=10), creditS1STAPS1[0]],

                    [ EPS112[j], coefS1STAPS1[1], EPS112[j]*coefS1STAPS1[1], "MOYENNE", sort112.index(EPS112[j])+1,(EPS112[j]>=10), creditS1STAPS1[1]],

                    [ EPS113[j], coefS1STAPS1[2], EPS113[j]*coefS1STAPS1[2], round(  ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5]) + (EPS115f[j]*coefS1STAPS1[6]) + (EPS115g[j]*coefS1STAPS1[7]) + (EPS115j[j]*coefS1STAPS1[8]) + (EPS115l[j]*coefS1STAPS1[9]) + (EPS116[j]*coefS1STAPS1[10]) ) / (coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]), 2 ), 
                    
                      sort113.index(EPS113[j])+1, 

                      (EPS113[j] >=10), 

                      creditS1STAPS1[2] 
                    ],

                    [ EPS114[j],  coefS1STAPS1[3], EPS114[j]*coefS1STAPS1[3], "MOYENNE", sort114.index(EPS114[j])+1, (EPS114[j] >=10), creditS1STAPS1[3] ],

                    [ EPS115a[j], coefS1STAPS1[4], EPS115a[j]*coefS1STAPS1[4], "MOYENNE", sort115a.index(EPS115a[j])+1, (EPS115a[j] >=10), creditS1STAPS1[4] ], #crédits

                    [ EPS115b[j], coefS1STAPS1[5], EPS115b[j]*coefS1STAPS1[5], "MOYENNE", sort115b.index(EPS115b[j])+1, (EPS115b[j] >=10), creditS1STAPS1[5] ],

                    [ EPS115f[j], coefS1STAPS1[6], EPS115f[j]*coefS1STAPS1[6], "MOYENNE", sort115f.index(EPS115f[j])+1, (EPS115f[j] >=10), creditS1STAPS1[6] ],

                    [ EPS115g[j], coefS1STAPS1[7], EPS115g[j]*coefS1STAPS1[7], "MOYENNE", sort115g.index(EPS115g[j])+1, (EPS115g[j] >=10), creditS1STAPS1[7] ],

                    [ EPS115j[j], coefS1STAPS1[8], EPS115j[j]*coefS1STAPS1[8], "MOYENNE", sort115j.index(EPS115j[j])+1, (EPS115j[j] >=10), creditS1STAPS1[8] ],

                    [ EPS115l[j], coefS1STAPS1[9], EPS115l[j]*coefS1STAPS1[9], "MOYENNE", sort115l.index(EPS115l[j])+1, (EPS115l[j] >=10), creditS1STAPS1[9] ],

                    [ EPS116[j],  coefS1STAPS1[10], EPS116[j]*coefS1STAPS1[10], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[10] ],

                    [ EPS117[j],  coefS1STAPS1[11], EPS117[j]*coefS1STAPS1[11], 

                        round( ( (EPS117[j]*coefS1STAPS1[11]) + (EPS118[j]*coefS1STAPS1[12]) + (EPS119[j]*coefS1STAPS1[13]) ) / ( coefS1STAPS1[11]+coefS1STAPS1[12]+coefS1STAPS1[13]), 2 ),  

                        sort117.index(EPS117[j])+1, 

                        (EPS117[j] >=10), 

                        creditS1STAPS1[11] 
                        
                    ],

                    [ EPS118[j],  coefS1STAPS1[12], EPS118[j]*coefS1STAPS1[12], "MOYENNE", sort118.index(EPS118[j])+1, (EPS118[j] >=10), creditS1STAPS1[12] ],

                    [ EPS119[j],  coefS1STAPS1[13], EPS119[j]*coefS1STAPS1[13], "MOYENNE", sort119.index(EPS119[j])+1, (EPS119[j] >=10), creditS1STAPS1[13] ],

                    [ 
                        ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]+coefS1STAPS1[13]), 
                    
                    round( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115f[j]*coefS1STAPS1[6]+EPS115g[j]*coefS1STAPS1[7]+EPS115j[j]*coefS1STAPS1[8]+EPS115l[j]*coefS1STAPS1[9]+EPS116[j]*coefS1STAPS1[10]+EPS117[j]*coefS1STAPS1[11]+EPS118[j]*coefS1STAPS1[12]+EPS119[j]*coefS1STAPS1[13] ,2), 

                    round(( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115f[j]*coefS1STAPS1[6]+EPS115g[j]*coefS1STAPS1[7]+EPS115j[j]*coefS1STAPS1[8]+EPS115l[j]*coefS1STAPS1[9]+EPS116[j]*coefS1STAPS1[10]+EPS117[j]*coefS1STAPS1[11]+EPS118[j]*coefS1STAPS1[12]+EPS119[j]*coefS1STAPS1[13] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]+coefS1STAPS1[13] ), 2), #moyenne
                        
                        4,

                        5
                    ]
            ]
            
            listeMatrice.append(matrice)

            staps1Moyenne.append(matrice[15][2])
            staps1Moyenne.sort(reverse=True)

            moy = stat.mean(staps1Moyenne)
            moy = round(moy, 2)
            session = 'Janvier 2023'

    semestre1MDS = [filiere , listeMatrice, staps1Moyenne, moy, session]

    return render(request,'bulletin/BulletinTemplate/bullS1eps.html', {'semestre1MDS': semestre1MDS} ) 



#################################################################################################################################### NIVEAU 3###############################
def bulls5msoeve(request, filiere):

    MDS111 =list(Evaluation.objects.filter(uniteEnseignement_id=12).values('note_Examen'))
    MDS111b =list(Evaluation.objects.filter(uniteEnseignement_id=13).values('note_Examen'))
    MDS112 =list(Evaluation.objects.filter(uniteEnseignement_id=14).values('note_Examen'))
    MDS113 =list(Evaluation.objects.filter(uniteEnseignement_id=15).values('note_Examen'))
    MDS114 =list(Evaluation.objects.filter(uniteEnseignement_id=16).values('note_Examen'))
    MDS115 =list(Evaluation.objects.filter(uniteEnseignement_id=17).values('note_Examen'))
    MDS116 =list(Evaluation.objects.filter(uniteEnseignement_id=18).values('note_Examen'))
    MDS117 =list(Evaluation.objects.filter(uniteEnseignement_id=19).values('note_Examen'))

    semestre1MDS = [filiere,MDS111, MDS111b, MDS112, MDS113, MDS114, MDS115, MDS116, MDS117]

    return render(request,'bulletin/BulletinTemplate/bullS1eps.html', {'semestre1MDS': semestre1MDS} )




################################# REQUETES POUR BULLETIN SEMESTRE 2 4 6 #########################################################################################################
def bulls2epsmds(request, filiere):
    pass
################################# RESULTATS COMMUNS #############################################################################################################################

def resultatCommunepsmds(request):


    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = epurationCoef(coefS1STAPS1)

    creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS1 = epurationCre(creditS1STAPS1)

    EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=50).values('note_Examen'))
    sort111 = epurationTriCroissant(EPS111)

    EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=51).values('note_Examen'))
    sort112 = epurationTriCroissant(EPS112)

    EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=52).values('note_Examen'))
    sort113 = epurationTriCroissant(EPS113)

    EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=53).values('note_Examen'))
    sort114 = epurationTriCroissant(EPS114)

    EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=54).values('note_Examen'))
    sort115a = epurationTriCroissant(EPS115a)

    EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=55).values('note_Examen'))
    sort115b = epurationTriCroissant(EPS115b) 

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=56).values('note_Examen'))
    sort115j = epurationTriCroissant(EPS115j)

    EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=57).values('note_Examen'))
    sort115l = epurationTriCroissant(EPS115l)

    EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=58).values('note_Examen'))
    sort116 = epurationTriCroissant(EPS116)

    EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=59).values('note_Examen')) 
    sort117 = epurationTriCroissant(EPS117)

    EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=60).values('note_Examen'))
    sort118 = epurationTriCroissant(EPS118)

    EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=61).values('note_Examen'))
    sort119 = epurationTriCroissant(EPS119)

    student = {}
    temp = {}
    staps1 = []
    staps1Moyenne = []
    listeMatrice = [ ]

    for j in range( len(infoEtudiantSTAPS1) ):

        #for j in range( len(coefS1STAPS1) ):
        matrice = [
                        infoEtudiantSTAPS1[j],

                        [ EPS111[j], coefS1STAPS1[0], EPS111[j]*coefS1STAPS1[0], round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2), sort111.index(EPS111[j])+1,(EPS111[j]>=10), creditS1STAPS1[0]],

                        [ EPS112[j], coefS1STAPS1[1], EPS112[j]*coefS1STAPS1[1], "MOYENNE", sort112.index(EPS112[j])+1,(EPS112[j]>=10), creditS1STAPS1[1]],

                        [ EPS113[j], 

                            coefS1STAPS1[2], 

                            EPS113[j]*coefS1STAPS1[2], 

                            round( ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5]) + (EPS115j[j]*coefS1STAPS1[6]) + (EPS115l[j]*coefS1STAPS1[7]) + (EPS116[j]*coefS1STAPS1[8]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]) ,2), 
                            
                            sort113.index(EPS113[j])+1,
                            
                            (EPS113[j] >=10),
                            
                            creditS1STAPS1[2]
                        ],

                        [ EPS114[j],  coefS1STAPS1[3], EPS114[j]*coefS1STAPS1[3], "MOYENNE", sort114.index(EPS114[j])+1, (EPS114[j] >=10), creditS1STAPS1[3] ],

                        [ EPS115a[j], coefS1STAPS1[4], EPS115a[j]*coefS1STAPS1[4], "MOYENNE", sort115a.index(EPS115a[j])+1, (EPS115a[j] >=10), creditS1STAPS1[4] ], #crédits

                        [ EPS115b[j], coefS1STAPS1[5], EPS115b[j]*coefS1STAPS1[5], "MOYENNE", sort115b.index(EPS115b[j])+1, (EPS115b[j] >=10), creditS1STAPS1[5] ],

                        [ EPS115j[j], coefS1STAPS1[6], EPS115j[j]*coefS1STAPS1[6], "MOYENNE", sort115j.index(EPS115j[j])+1, (EPS115j[j] >=10), creditS1STAPS1[6] ],

                        [ EPS115l[j], coefS1STAPS1[7], EPS115l[j]*coefS1STAPS1[7], "MOYENNE", sort115l.index(EPS115l[j])+1, (EPS115l[j] >=10), creditS1STAPS1[7] ],

                        [ EPS116[j],  coefS1STAPS1[8], EPS116[j]*coefS1STAPS1[8], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[8] ],

                        [ EPS117[j], coefS1STAPS1[9], 

                            EPS117[j]*coefS1STAPS1[9], 

                            round( ((EPS117[j]*coefS1STAPS1[9]) + (EPS118[j]*coefS1STAPS1[10]) + (EPS119[j]*coefS1STAPS1[11])) / ( coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]) ,2), 

                            sort117.index(EPS117[j])+1, 

                            (EPS117[j] >=10), 
                            
                            creditS1STAPS1[9] 
                        ],

                        [ EPS118[j], coefS1STAPS1[10], EPS118[j]*coefS1STAPS1[10], "MOYENNE", sort118.index(EPS118[j])+1, (EPS118[j] >=10), creditS1STAPS1[10] ],

                        [ EPS119[j], coefS1STAPS1[11], EPS119[j]*coefS1STAPS1[11], "MOYENNE", sort119.index(EPS119[j])+1, (EPS119[j] >=10), creditS1STAPS1[11] ],

                        [ 
                            ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ),

                            round( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115j[j]*coefS1STAPS1[6]+EPS115l[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11], 2),

                            round(( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115j[j]*coefS1STAPS1[6]+EPS115l[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2 ),

                            4,
                            5
                        ]
        ]
                
        staps1Moyenne.append(matrice[13][2])

        listeMatrice.append(matrice)

        staps1Moyenne.sort(reverse=True)
        moy = stat.mean(staps1Moyenne)
        moy = round(moy, 2)
        session = 'Janvier 2023'

        filiere = 'STAPS'
                
        semestre1MDS = [filiere, listeMatrice, staps1Moyenne, moy, session ] #

    return render(request, 'bulletin/releveCommun/releveCommun.html', {'semestre1MDS': semestre1MDS})
##########################################################################################################################################################################################################################################################################

def resultatCommunmds(request):
    

    infoEtudiantMDS =list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("coefficient", "intitule_UE"))
    coefS1MDS1 = epurationCoef(coefS1MDS1)

    creditS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("nombre_credit"))
    creditS1MDS1 = epurationCre(creditS1MDS1)
        
    MDS111 =list(Evaluation.objects.filter(uniteEnseignement_id=40).values('note_Examen'))
    sort111 = epurationTriCroissant(MDS111)

    MDS111b =list(Evaluation.objects.filter(uniteEnseignement_id=41).values('note_Examen'))
    sort111b = epurationTriCroissant(MDS111b)

    MDS112 =list(Evaluation.objects.filter(uniteEnseignement_id=42).values('note_Examen'))
    sort112 = epurationTriCroissant(MDS112)

    MDS112b =list(Evaluation.objects.filter(uniteEnseignement_id=43).values('note_Examen'))
    sort112b = epurationTriCroissant(MDS112b)

    MDS113 =list(Evaluation.objects.filter(uniteEnseignement_id=44).values('note_Examen'))
    sort113 = epurationTriCroissant(MDS113)

    MDS114 =list(Evaluation.objects.filter(uniteEnseignement_id=45).values('note_Examen'))
    sort114 = epurationTriCroissant(MDS114)

    MDS115 =list(Evaluation.objects.filter(uniteEnseignement_id=46).values('note_Examen'))
    sort115 = epurationTriCroissant(MDS115)

    MDS116 =list(Evaluation.objects.filter(uniteEnseignement_id=47).values('note_Examen'))
    sort116 = epurationTriCroissant(MDS116)

    MDS117 =list(Evaluation.objects.filter(uniteEnseignement_id=48).values('note_Examen'))
    sort117 = epurationTriCroissant(MDS117)

    MDS117b =list(Evaluation.objects.filter(uniteEnseignement_id=49).values('note_Examen'))
    sort117b = epurationTriCroissant(MDS117b)

    listeMatrice = []
    mds1Moyenne = []

    for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

        matrice = [
                infoEtudiantMDS[j],

                [ MDS111[j], coefS1MDS1[0], MDS111[j]*coefS1MDS1[0], round( ((MDS111[j]*coefS1MDS1[0]) + (MDS111b[j]*coefS1MDS1[1]) + ( MDS112[j]*coefS1MDS1[2]) + (MDS112b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2), sort111.index(MDS111[j])+1,(MDS111[j]>=10), creditS1MDS1[0] ],

                [ MDS111b[j], coefS1MDS1[1], MDS111b[j]*coefS1MDS1[1], "MOYENNE", sort111b.index(MDS111b[j])+1,(MDS111b[j]>=10), creditS1MDS1[1]],

                [ MDS112[j], coefS1MDS1[2], MDS112[j]*coefS1MDS1[2], "MOYENNE", sort112.index(MDS112[j])+1,(MDS112[j]>=10), creditS1MDS1[2]],

                [ MDS112b[j], coefS1MDS1[3], MDS112b[j]*coefS1MDS1[3], "MOYENNE", sort112b.index(MDS112b[j])+1,(MDS112b[j]>=10), creditS1MDS1[3]],


                [ MDS113[j], coefS1MDS1[4], MDS113[j]*coefS1MDS1[4], 

                round( ((MDS113[j]*coefS1MDS1[4]) + (MDS114[j]*coefS1MDS1[5]) + MDS115[j]*coefS1MDS1[6] + MDS116[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2), 
                
                sort113.index(MDS113[j])+1,
                (MDS113[j]>=10), 
                creditS1MDS1[4]],

                [ MDS114[j], coefS1MDS1[5], MDS114[j]*coefS1MDS1[5], "MOYENNE", sort114.index(MDS114[j])+1,(MDS114[j]>=10), creditS1MDS1[5]],

                [ MDS115[j], coefS1MDS1[6], MDS115[j]*coefS1MDS1[6], "MOYENNE", sort115.index(MDS115[j])+1,(MDS115[j]>=10), creditS1MDS1[6]],

                [ MDS116[j], coefS1MDS1[7], MDS116[j]*coefS1MDS1[7], "MOYENNE", sort116.index(MDS116[j])+1,(MDS116[j]>=10), creditS1MDS1[7]],


                [ MDS117[j], coefS1MDS1[8], MDS117[j]*coefS1MDS1[8], 
                
                round(( MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2), 
                sort117.index(MDS117[j])+1,
                (MDS117[j]>=10), 
                creditS1MDS1[8]],

                [ MDS117b[j], coefS1MDS1[9], MDS117b[j]*coefS1MDS1[9], "MOYENNE", sort117b.index(MDS117b[j])+1,(MDS117b[j]>=10), creditS1MDS1[9]],

                [
                    ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),

                   round (MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] , 2),

                   round (( MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                ]

        ]

        listeMatrice.append(matrice)
        mds1Moyenne.append(matrice[11][2])
        mds1Moyenne.sort(reverse=True)

        moy = stat.mean(mds1Moyenne)
        moy = round(moy, 2)
        session = 'Janvier 2023'

        filiere="GESTION"


        semestre1MDS = [filiere, listeMatrice, mds1Moyenne, moy, session] #filiere, listeMatrice, staps1Moyenne, moy, session

    return render(request, 'bulletin/releveCommun/releveCommunmds.html', {'semestre1MDS': semestre1MDS})

##########################################################################################################################################################################################################################################################################
def BulletinUnique(request):
    if request.method == 'GET':
        matri = request.GET['matricule']
        nom = request.GET['nom']
        
        context = {
            0: matri,
            1: nom,
        }

        return JsonResponse(context, safe=True)

def BulletinSpecialite(request):
    if request.method == 'GET':
        context = request.GET#["data[0]"]
    return JsonResponse(context, safe=True)


def saveData(key, values):
    if (len(key) == len(values)):
        print(key,values)

        for i in range(len(key)):
            
            setKey = key[i]
            """if(setKey[0]=="CC"):
                natureEvaluation_ = 'Contrôle_Continue'
                #note_cc = 
            elif(setKey[0]=="SN"):"""
            natureEvaluation_ = 'EXAMEN'
            matricule = setKey[1]
            codeUe = setKey[2]
            note = values[i]
            note_cc = note[0]
            note_sn = note[1]
            note_examen = 0.7*note_sn + 0.3*note_cc
            note_examen = float("{:.2f}".format(note_examen)) #Determiner la précision de 2 chiffres après la virgule


            etudiant_Query = Etudiant.objects.filter(matricule=matricule)#.values('nom')
            etudiant = etudiant_Query[0]

            ue_Query = UniteEnseignement.objects.filter(code_UE=codeUe)#.values('id')
            ue = ue_Query[0]
            
            evaluation = Evaluation(natureEvaluation=natureEvaluation_, note_cc=note_cc, note_sn=note_sn, etudiant=etudiant, note_Examen=note_examen,uniteEnseignement=ue)
            evaluation.save()

def extract(a):
    key1 = list(a.keys())
    value = list(a.values())
    key= []
    values = []
    shape = []
    #Epuration des Key
    for i in range(1,len(key1)):
        k = key1[i]
        key1[i] = k.split()
    #reduction à un type d'évaluation
    for i in range(1,len(key1)):
        if(i%2==0):
            key.append(key1[i])
    #Couplage des valeurs par liste de deux
    values = broke(value)
    shape = pattern(value)
    print(shape)
    values = formatt(values, shape)
    return (key, values)

def pattern(a):
    r = []
    for i in range(len(a)//2):
        r.append(2)
    return r   
def broke(a):
    values = []
    for i in range(1,len(a)):#décalage afin d'éviter la clé token du formulaire
        e = a[i]
        v = float((e))
        values.append(v)
    return values
def formatt(a, pattern):
    inputt = iter(a)
    output = [list(islice(inputt, elem))
        for elem in pattern]
    return output

##############GENERATION DE BULLETINS#####################################################################

#class GeneratePdf(View):
#    def get(self, request, *args, **kwargs):
#        pdf = render_to_pdf('bulletin/BulletinTemplate/bullS1eps.html')
#        return HttpResponse(pdf, content_type='application/pdf')

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('report.html')
#         if pdf:
#             response=HttpResponse(pdf,content_type='application/pdf')
#             filename = "PDF_%s.pdf" %("Report")
#             content = "inline; filename= %s" %(filename)
#             response['Content-Disposition']=content
#             return response
#         return HttpResponse("Page Not Found")


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
        "name": "Mama", #you can feach the data from database
        "id": "18",
        "amount": "333",
        }
        pdf = render_to_pdf('bulletin/BulletinTemplate/bullS1eps.html',data)
        if pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            filename = "Report_for_%s.pdf" %(data['id'])
            content = "inline; filename= %s" %(filename)
            response['Content-Disposition']=content
            return response
        return HttpResponse("Page Not Found")

########################################################## FONCTIONS UTILIES ########################################################
def extractNote(a):
    notes=[]
    for i in range(len(a)):
        data = a[i]
        value = data["note_Examen"]
        notes.append(value)
    return notes


######################################################################################################################################
def epurationTriCroissant(b):
    for i in range(len(b)):
        tmp = b[i]["note_Examen"]
        b[i] = tmp

    b = sorted(b, reverse=True)
    return b

def epurationCre(b):
    for i in range(len(b)):
        tmp = b[i]["nombre_credit"]
        b[i] = tmp

    #b.sort()
    return b

def epurationCoef(b):
    for i in range(len(b)):
        tmp = b[i]["coefficient"]
        b[i] = tmp

    #b.sort()
    return b