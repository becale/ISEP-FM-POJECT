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
    
    saveData(key,values)
    
    return JsonResponse(data, safe=False)

def test(request):
    return render(request, 'bulletin/BulletinTemplate/bulletin1.html')

def AddNoteEtudiantRattrapage(request):
    if request.method == "POST":
        data = request.POST

    

    key,values = extractR(data)
    
    print(len(key))
    print(len(values))

    saveDataR(key,values)

    return JsonResponse(data, safe=False)





################################# REQUETES POUR BULLETIN SEMESTRE 1 3 5 | SEMESTRE 2 4 6 #############################################################
#EPS1 ET MDS1 SEMESTRE 1
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

#EPS1 ET MDS1 SEMESTRE2
def bulls2epsmds(request, filiere):
    if (filiere =='GESTION'):

        infoEtudiantMDS =list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

        coefS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="GESTION").values("coefficient", "intitule_UE"))
        coefS1MDS1 = epurationCoef(coefS1MDS1)

        creditS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="GESTION").values("nombre_credit"))
        creditS1MDS1 = epurationCre(creditS1MDS1)

        MDS121 =list(Evaluation.objects.filter(uniteEnseignement_id=88).values('note_Examen'))
        sort111 = epurationTriCroissant(MDS121)

        MDS121b =list(Evaluation.objects.filter(uniteEnseignement_id=89).values('note_Examen'))
        sort111b = epurationTriCroissant(MDS121b)

        MDS122 =list(Evaluation.objects.filter(uniteEnseignement_id=90).values('note_Examen'))
        sort112 = epurationTriCroissant(MDS122)

        MDS122b =list(Evaluation.objects.filter(uniteEnseignement_id=91).values('note_Examen'))
        sort112b = epurationTriCroissant(MDS122b)

        MDS123 =list(Evaluation.objects.filter(uniteEnseignement_id=92).values('note_Examen'))
        sort113 = epurationTriCroissant(MDS123)

        MDS124 =list(Evaluation.objects.filter(uniteEnseignement_id=93).values('note_Examen'))
        sort114 = epurationTriCroissant(MDS124)

        MDS125 =list(Evaluation.objects.filter(uniteEnseignement_id=95).values('note_Examen'))
        sort115 = epurationTriCroissant(MDS125)

        MDS126 =list(Evaluation.objects.filter(uniteEnseignement_id=96).values('note_Examen'))
        sort116 = epurationTriCroissant(MDS126)

        MDS127 =list(Evaluation.objects.filter(uniteEnseignement_id=97).values('note_Examen'))
        sort117 = epurationTriCroissant(MDS127)

        MDS127b =list(Evaluation.objects.filter(uniteEnseignement_id=98).values('note_Examen'))
        sort117b = epurationTriCroissant(MDS127b)


        for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

            matrice = [
                infoEtudiantMDS[j],

                [ MDS121[j], coefS1MDS1[0], MDS121[j]*coefS1MDS1[0], round( ((MDS121[j]*coefS1MDS1[0]) + (MDS121b[j]*coefS1MDS1[1]) + ( MDS122[j]*coefS1MDS1[2]) + (MDS122b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2), sort111.index(MDS121[j])+1,(MDS121[j]>=10), creditS1MDS1[0] ],

                [ MDS121b[j], coefS1MDS1[1], MDS121b[j]*coefS1MDS1[1], "MOYENNE", sort111b.index(MDS121b[j])+1,(MDS121b[j]>=10), creditS1MDS1[1]],

                [ MDS122[j], coefS1MDS1[2], MDS122[j]*coefS1MDS1[2], "MOYENNE", sort112.index(MDS122[j])+1,(MDS122[j]>=10), creditS1MDS1[2]],

                [ MDS122b[j], coefS1MDS1[3], MDS122b[j]*coefS1MDS1[3], "MOYENNE", sort112b.index(MDS122b[j])+1,(MDS122b[j]>=10), creditS1MDS1[3]],


                [ MDS123[j], coefS1MDS1[4], MDS123[j]*coefS1MDS1[4], 

                round( ((MDS123[j]*coefS1MDS1[4]) + (MDS124[j]*coefS1MDS1[5]) + MDS125[j]*coefS1MDS1[6] + MDS126[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2), 
                
                sort113.index(MDS123[j])+1,
                (MDS123[j]>=10), 
                creditS1MDS1[4]],

                [ MDS124[j], coefS1MDS1[5], MDS124[j]*coefS1MDS1[5], "MOYENNE", sort114.index(MDS124[j])+1,(MDS124[j]>=10), creditS1MDS1[5]],

                [ MDS125[j], coefS1MDS1[6], MDS125[j]*coefS1MDS1[6], "MOYENNE", sort115.index(MDS125[j])+1,(MDS125[j]>=10), creditS1MDS1[6]],

                [ MDS126[j], coefS1MDS1[7], MDS126[j]*coefS1MDS1[7], "MOYENNE", sort116.index(MDS126[j])+1,(MDS126[j]>=10), creditS1MDS1[7]],


                [ MDS127[j], coefS1MDS1[8], MDS127[j]*coefS1MDS1[8], 
                
                round(( MDS127[j]*coefS1MDS1[8]+MDS127b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2), 
                sort117.index(MDS127[j])+1,
                (MDS127[j]>=10), 
                creditS1MDS1[8]],

                [ MDS127b[j], coefS1MDS1[9], MDS127b[j]*coefS1MDS1[9], "MOYENNE", sort117b.index(MDS127b[j])+1,(MDS127b[j]>=10), creditS1MDS1[9]],

                [
                    ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),

                   round (MDS121[j]*coefS1MDS1[0]+MDS121b[j]*coefS1MDS1[1]+MDS122[j]*coefS1MDS1[2]+MDS122b[j]*coefS1MDS1[3]+MDS123[j]*coefS1MDS1[4]+MDS124[j]*coefS1MDS1[5]+MDS125[j]*coefS1MDS1[6]+MDS126[j]*coefS1MDS1[7]+ MDS127[j]*coefS1MDS1[8]+MDS127b[j]*coefS1MDS1[9] , 2),

                   round (( MDS121[j]*coefS1MDS1[0]+MDS121b[j]*coefS1MDS1[1]+MDS122[j]*coefS1MDS1[2]+MDS122b[j]*coefS1MDS1[3]+MDS123[j]*coefS1MDS1[4]+MDS124[j]*coefS1MDS1[5]+MDS125[j]*coefS1MDS1[6]+MDS126[j]*coefS1MDS1[7]+ MDS127[j]*coefS1MDS1[8]+MDS127b[j]*coefS1MDS1[9] )/( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                ]

            ]

            listeMatrice.append(matrice)
            mds1Moyenne.append(matrice[11][2])
            mds1Moyenne.sort(reverse=True)

            moy = stat.mean(mds1Moyenne)
            moy = round(moy, 2)
            session = 'Janvier 2023'

            #filiere, listeMatrice, staps1Moyenne, moy, session

        semestre1MDS = [filiere,  listeMatrice, mds1Moyenne,  moy, session] #infoEtudiantMDS, coefS1MDS1, creditS1MDS1, MDS111, MDS111b, MDS112, MDS112b, MDS113, MDS114, MDS115, MDS116, MDS117, MDS127b,

    elif (filiere == 'STAPS1'):

        infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

        coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="STAPS").values("coefficient"))
        coefS1STAPS1 = epurationCoef(coefS1STAPS1)

        creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("nombre_credit"))
        creditS1STAPS1 = epurationCre(creditS1STAPS1)

        EPS121 = list(Evaluation.objects.filter(uniteEnseignement_id=99).values('note_Examen'))
        sort111 = epurationTriCroissant(EPS121)

        EPS122 = list(Evaluation.objects.filter(uniteEnseignement_id=100).values('note_Examen'))
        sort112 = epurationTriCroissant(EPS122)

        EPS123 = list(Evaluation.objects.filter(uniteEnseignement_id=101).values('note_Examen'))
        sort113 = epurationTriCroissant(EPS123)

        EPS124 = list(Evaluation.objects.filter(uniteEnseignement_id=102).values('note_Examen'))
        sort114 = epurationTriCroissant(EPS124)

        EPS125a = list(Evaluation.objects.filter(uniteEnseignement_id=103).values('note_Examen'))
        sort115a = epurationTriCroissant(EPS125a)

        EPS125b = list(Evaluation.objects.filter(uniteEnseignement_id=104).values('note_Examen'))
        sort115b = epurationTriCroissant(EPS125b) 

        EPS125j = list(Evaluation.objects.filter(uniteEnseignement_id=105).values('note_Examen'))
        sort115j = epurationTriCroissant(EPS125j)

        EPS125l = list(Evaluation.objects.filter(uniteEnseignement_id=106).values('note_Examen'))
        sort115l = epurationTriCroissant(EPS125l)

        EPS126 = list(Evaluation.objects.filter(uniteEnseignement_id=108).values('note_Examen'))
        sort116 = epurationTriCroissant(EPS126)

        EPS127 = list(Evaluation.objects.filter(uniteEnseignement_id=109).values('note_Examen')) 
        sort117 = epurationTriCroissant(EPS127)

        EPS128 = list(Evaluation.objects.filter(uniteEnseignement_id=110).values('note_Examen'))
        sort118 = epurationTriCroissant(EPS128)

        EPS129 = list(Evaluation.objects.filter(uniteEnseignement_id=111).values('note_Examen'))
        sort119 = epurationTriCroissant(EPS129)

        student = {}
        temp = {}
        staps1 = []
        staps1Moyenne = []
        listeMatrice = [ ]

        for j in range( len(infoEtudiantSTAPS1) ):

            #for j in range( len(coefS1STAPS1) ):
            matrice = [
                    infoEtudiantSTAPS1[j],

                    [ EPS121[j], coefS1STAPS1[0], EPS121[j]*coefS1STAPS1[0], round( ((EPS121[j]*coefS1STAPS1[0]) + (EPS122[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2), sort111.index(EPS121[j])+1,(EPS121[j]>=10), creditS1STAPS1[0]],

                    [ EPS122[j], coefS1STAPS1[1], EPS122[j]*coefS1STAPS1[1], "MOYENNE", sort112.index(EPS122[j])+1,(EPS122[j]>=10), creditS1STAPS1[1]],

                    [ EPS123[j], 

                        coefS1STAPS1[2], 

                        EPS123[j]*coefS1STAPS1[2], 

                        round( ( (EPS123[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5]) + (EPS115j[j]*coefS1STAPS1[6]) + (EPS115l[j]*coefS1STAPS1[7]) + (EPS116[j]*coefS1STAPS1[8]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]) ,2), 
                        
                        sort113.index(EPS123[j])+1,
                        
                        (EPS123[j] >=10),
                        
                        creditS1STAPS1[2]
                    ],

                    [ EPS124[j],  coefS1STAPS1[3], EPS124[j]*coefS1STAPS1[3], "MOYENNE", sort114.index(EPS124[j])+1, (EPS124[j] >=10), creditS1STAPS1[3] ],

                    [ EPS125a[j], coefS1STAPS1[4], EPS125a[j]*coefS1STAPS1[4], "MOYENNE", sort125a.index(EPS125a[j])+1, (EPS125a[j] >=10), creditS1STAPS1[4] ], #crédits

                    [ EPS125b[j], coefS1STAPS1[5], EPS125b[j]*coefS1STAPS1[5], "MOYENNE", sort125b.index(EPS125b[j])+1, (EPS125b[j] >=10), creditS1STAPS1[5] ],

                    [ EPS125j[j], coefS1STAPS1[6], EPS125j[j]*coefS1STAPS1[6], "MOYENNE", sort125j.index(EPS125j[j])+1, (EPS125j[j] >=10), creditS1STAPS1[6] ],

                    [ EPS125l[j], coefS1STAPS1[7], EPS125l[j]*coefS1STAPS1[7], "MOYENNE", sort125l.index(EPS125l[j])+1, (EPS125l[j] >=10), creditS1STAPS1[7] ],

                    [ EPS126[j],  coefS1STAPS1[8], EPS126[j]*coefS1STAPS1[8], "MOYENNE", sort116.index(EPS126[j])+1, (EPS126[j] >=10), creditS1STAPS1[8] ],

                    [ EPS127[j], coefS1STAPS1[9], 

                        EPS127[j]*coefS1STAPS1[9], 

                        round( ((EPS127[j]*coefS1STAPS1[9]) + (EPS118[j]*coefS1STAPS1[10]) + (EPS119[j]*coefS1STAPS1[11])) / ( coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]) ,2), 

                        sort117.index(EPS127[j])+1, 

                        (EPS127[j] >=10), 
                        
                        creditS1STAPS1[9] 
                    ],

                    [ EPS128[j], coefS1STAPS1[10], EPS128[j]*coefS1STAPS1[10], "MOYENNE", sort118.index(EPS128[j])+1, (EPS128[j] >=10), creditS1STAPS1[10] ],

                    [ EPS129[j], coefS1STAPS1[11], EPS129[j]*coefS1STAPS1[11], "MOYENNE", sort119.index(EPS129[j])+1, (EPS129[j] >=10), creditS1STAPS1[11] ],

                    [ 
                        ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ),

                        round( EPS121[j]*coefS1STAPS1[0]+EPS122[j]*coefS1STAPS1[1]+EPS123[j]*coefS1STAPS1[2]+EPS124[j]*coefS1STAPS1[3]+EPS125a[j]*coefS1STAPS1[4]+EPS125b[j]*coefS1STAPS1[5]+EPS125j[j]*coefS1STAPS1[6]+EPS125l[j]*coefS1STAPS1[7]+EPS126[j]*coefS1STAPS1[8]+EPS127[j]*coefS1STAPS1[9]+EPS128[j]*coefS1STAPS1[10]+EPS129[j]*coefS1STAPS1[11], 2),

                        round(( EPS121[j]*coefS1STAPS1[0]+EPS122[j]*coefS1STAPS1[1]+EPS123[j]*coefS1STAPS1[2]+EPS124[j]*coefS1STAPS1[3]+EPS125a[j]*coefS1STAPS1[4]+EPS125b[j]*coefS1STAPS1[5]+EPS125j[j]*coefS1STAPS1[6]+EPS125l[j]*coefS1STAPS1[7]+EPS126[j]*coefS1STAPS1[8]+EPS127[j]*coefS1STAPS1[9]+EPS128[j]*coefS1STAPS1[10]+EPS129[j]*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2 ),

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
#EPS2 SEMESTRE3
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

    ############################################# NOTES RATTRAPAGES SEMESTRE 3 #######################################################################################
    EPS111R = list(Evaluation.objects.filter(uniteEnseignement_id=62, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))

    EPS112R = list(Evaluation.objects.filter(uniteEnseignement_id=63, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))

    EPS113R = list(Evaluation.objects.filter(uniteEnseignement_id=64, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort113 = epurationTriCroissant(EPS113R)

    EPS114R = list(Evaluation.objects.filter(uniteEnseignement_id=65, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort114 = epurationTriCroissant(EPS114)

    EPS115aR = list(Evaluation.objects.filter(uniteEnseignement_id=66, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort115a = epurationTriCroissant(EPS115a)

    EPS115bR = list(Evaluation.objects.filter(uniteEnseignement_id=67, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort115b = epurationTriCroissant(EPS115b) 

    EPS115fR = list(Evaluation.objects.filter(uniteEnseignement_id=68, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort115f = epurationTriCroissant(EPS115f)

    EPS115gR = list(Evaluation.objects.filter(uniteEnseignement_id=69, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort115g = epurationTriCroissant(EPS115g)

    EPS115jR = list(Evaluation.objects.filter(uniteEnseignement_id=70, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort115j = epurationTriCroissant(EPS115j)

    EPS115lR = list(Evaluation.objects.filter(uniteEnseignement_id=71, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort115l = epurationTriCroissant(EPS115l)

    EPS116R = list(Evaluation.objects.filter(uniteEnseignement_id=72, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort116 = epurationTriCroissant(EPS116)

    EPS117R = list(Evaluation.objects.filter(uniteEnseignement_id=73, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort117 = epurationTriCroissant(EPS117)

    EPS118R = list(Evaluation.objects.filter(uniteEnseignement_id=74, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort118 = epurationTriCroissant(EPS118)

    EPS119R = list(Evaluation.objects.filter(uniteEnseignement_id=75, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #sort119 = epurationTriCroissant(EPS119)
    listeR = [EPS111R, EPS112R, EPS113R, EPS114R, EPS115aR, EPS115bR, EPS115fR, EPS115gR, EPS115jR, EPS115lR, EPS116R, EPS117R, EPS118R, EPS119R]

    listeMatriceR = []
    
    for j in range ( len(infoEtudiantSTAPS1) ):

        matriceR = [
            infoEtudiantSTAPS1[j],

            EPS111R[j],

            EPS112R[j],

            EPS113R[j],

            EPS114R[j],

            EPS115aR[j],

            EPS115bR[j],

            EPS115fR[j],

            EPS115gR[j],

            EPS115jR[j],

            EPS115lR[j],

            EPS116R[j],

            EPS117R[j],

            EPS118R[j],

            EPS119R[j]
        ]

        listeMatriceR.append(matriceR)
    
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

    semestre1MDS = [filiere , listeMatrice, staps1Moyenne, moy, session, listeMatriceR]

    return render(request,'bulletin/BulletinTemplate/bullS1eps.html', {'semestre1MDS': semestre1MDS} ) 

#EPS2 SEMESTRE4
def bulls4eps2(request, filiere):
################################################## SEMESTRE 3 #####################################################################################
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

################################################## SEMESTRE 4 #####################################################################################

    infoEtudiantSTAPS2 =list(Etudiant.objects.filter(filiere="STAPS", niveau=2).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS2 = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("coefficient"))
    coefS1STAPS2 = epurationCoef(coefS1STAPS2)

    creditS1STAPS2 = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS2 = epurationCre(creditS1STAPS2)

    intitule_UE = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("intitule_UE"))
    code_UE = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("code_UE"))
    
    EPS1112 = list(Evaluation.objects.filter(uniteEnseignement_id=112).values('note_Examen'))
    EPS1112cc = list(Evaluation.objects.filter(uniteEnseignement_id=112).values('note_cc'))
    EPS1112sn = list(Evaluation.objects.filter(uniteEnseignement_id=112).values('note_sn'))
    sort1112 = epurationTriCroissant(EPS1112)

    EPS115a2 = list(Evaluation.objects.filter(uniteEnseignement_id=113).values('note_Examen'))
    EPS115a2cc = list(Evaluation.objects.filter(uniteEnseignement_id=113).values('note_cc'))
    EPS115a2sn = list(Evaluation.objects.filter(uniteEnseignement_id=113).values('note_sn'))
    sort115a2 = epurationTriCroissant(EPS115a2)

    EPS115f2 = list(Evaluation.objects.filter(uniteEnseignement_id=114).values('note_Examen'))
    EPS115f2cc = list(Evaluation.objects.filter(uniteEnseignement_id=114).values('note_cc'))
    EPS115f2sn = list(Evaluation.objects.filter(uniteEnseignement_id=114).values('note_sn'))
    sort115f2 = epurationTriCroissant(EPS115f2)

    EPS115j2 = list(Evaluation.objects.filter(uniteEnseignement_id=115).values('note_Examen'))
    EPS115j2cc = list(Evaluation.objects.filter(uniteEnseignement_id=115).values('note_cc'))
    EPS115j2sn = list(Evaluation.objects.filter(uniteEnseignement_id=115).values('note_sn'))
    sort115j2 = epurationTriCroissant(EPS115j2) 

    EPS115g2 = list(Evaluation.objects.filter(uniteEnseignement_id=116).values('note_Examen'))
    EPS115g2cc = list(Evaluation.objects.filter(uniteEnseignement_id=116).values('note_cc'))
    EPS115g2sn = list(Evaluation.objects.filter(uniteEnseignement_id=116).values('note_sn'))
    sort115g2 = epurationTriCroissant(EPS115g2)


    EPS1122 = list(Evaluation.objects.filter(uniteEnseignement_id=117).values('note_Examen'))
    EPS1122cc = list(Evaluation.objects.filter(uniteEnseignement_id=117).values('note_cc'))
    EPS1122sn = list(Evaluation.objects.filter(uniteEnseignement_id=117).values('note_sn'))
    sort1122 = epurationTriCroissant(EPS1122)

    EPS1133 = list(Evaluation.objects.filter(uniteEnseignement_id=118).values('note_Examen')) 
    EPS1133cc = list(Evaluation.objects.filter(uniteEnseignement_id=118).values('note_cc'))
    EPS1133sn = list(Evaluation.objects.filter(uniteEnseignement_id=118).values('note_sn'))
    sort1133 = epurationTriCroissant(EPS1133)

    EPS1144 = list(Evaluation.objects.filter(uniteEnseignement_id=119).values('note_Examen'))
    EPS1144cc = list(Evaluation.objects.filter(uniteEnseignement_id=119).values('note_cc'))
    EPS1144sn = list(Evaluation.objects.filter(uniteEnseignement_id=119).values('note_sn'))
    sort1144 = epurationTriCroissant(EPS1144)

    
    EPS1166 = list(Evaluation.objects.filter(uniteEnseignement_id=120).values('note_Examen'))
    EPS1166cc = list(Evaluation.objects.filter(uniteEnseignement_id=120).values('note_cc'))
    EPS1166sn = list(Evaluation.objects.filter(uniteEnseignement_id=120).values('note_sn'))
    sort1166 = epurationTriCroissant(EPS1166)

    EPS1177 = list(Evaluation.objects.filter(uniteEnseignement_id=121).values('note_Examen')) 
    EPS1177cc = list(Evaluation.objects.filter(uniteEnseignement_id=121).values('note_cc'))
    EPS1177sn = list(Evaluation.objects.filter(uniteEnseignement_id=121).values('note_sn'))
    sort1177 = epurationTriCroissant(EPS1177)

    EPS1188 = list(Evaluation.objects.filter(uniteEnseignement_id=122).values('note_Examen'))
    EPS1188cc = list(Evaluation.objects.filter(uniteEnseignement_id=122).values('note_cc'))
    EPS1188sn = list(Evaluation.objects.filter(uniteEnseignement_id=122).values('note_sn'))
    sort1188 = epurationTriCroissant(EPS1188)

    EPS1199 = list(Evaluation.objects.filter(uniteEnseignement_id=123).values('note_Examen'))
    EPS1199cc = list(Evaluation.objects.filter(uniteEnseignement_id=123).values('note_cc')) 
    EPS1199sn = list(Evaluation.objects.filter(uniteEnseignement_id=123).values('note_sn'))
    sort1199 = epurationTriCroissant(EPS1199)

    stapsMoyenne2 = []
    listeMatrice2 = []

    for j in range( len(infoEtudiantSTAPS2) ):
        
            matrice2 = [
                    infoEtudiantSTAPS2[j],

                    #STAGE-PROFESSIONNEL
                    [ EPS1112[j], coefS1STAPS2[0], EPS1112[j]*coefS1STAPS2[0], "MOYENNE", sort1112.index(EPS1112[j])+1,(EPS1112[j]>=10), creditS1STAPS2[0], creditS1STAPS2[0] if (EPS1112[j]>=10) else 0, EPS1112cc[j]['note_cc'], EPS1112sn[j]['note_sn'] ],

                    #DIDACTIQUE DES APS
                    [ EPS115a2[j], coefS1STAPS2[1], EPS115a2[j]*coefS1STAPS2[1], "MOYENNE", sort115a2.index(EPS115a2[j])+1, (EPS115a2[j] >=10), creditS1STAPS2[1], creditS1STAPS2[1] if (EPS115a2[j] >=10) else 0, EPS115a2cc[j]['note_cc'], EPS115a2sn[j]['note_sn'] ], 

                    [ EPS115f2[j], coefS1STAPS2[2], EPS115f2[j]*coefS1STAPS2[2], "MOYENNE", sort115f2.index(EPS115f2[j])+1, (EPS115f2[j] >=10), creditS1STAPS2[2], creditS1STAPS2[2] if (EPS115f2[j] >=10) else 0, EPS115f2cc[j]['note_cc'], EPS115f2sn[j]['note_sn'] ],

                    [ EPS115j2[j], coefS1STAPS2[3], EPS115j2[j]*coefS1STAPS2[3], "MOYENNE", sort115j2.index(EPS115j2[j])+1, (EPS115j2[j] >=10), creditS1STAPS2[3], creditS1STAPS2[3] if (EPS115j2[j] >=10) else 0, EPS115j2cc[j]['note_cc'], EPS115j2sn[j]['note_sn'] ],

                    [ EPS115g2[j], coefS1STAPS2[4], EPS115g2[j]*coefS1STAPS2[4], 

                    round( (EPS115a2[j]*coefS1STAPS2[1]+EPS115f2[j]*coefS1STAPS2[2]+EPS115j2[j]*coefS1STAPS2[3]+EPS115g2[j]*coefS1STAPS2[4])/(coefS1STAPS2[1]+coefS1STAPS2[2]+coefS1STAPS2[3]+coefS1STAPS2[4]), 2 ), 
                    
                    sort115g2.index(EPS115g2[j])+1, (EPS115g2[j] >=10), creditS1STAPS2[4], creditS1STAPS2[4] if ( (EPS115a2[j]+EPS115f2[j]+EPS115j2[j]+EPS115g2[j]) >=40) else 0, EPS115g2cc[j]['note_cc'], EPS115g2sn[j]['note_sn'] 

                    ],

                    #ANATOMIE
                    [ EPS1122[j], coefS1STAPS2[5], EPS1122[j]*coefS1STAPS2[5], "MOYENNE", sort1122.index(EPS1122[j])+1, (EPS1122[j]>=10), creditS1STAPS2[5], creditS1STAPS2[5] if (EPS1122[j]>=10) else 0 , EPS1122cc[j]['note_cc'], EPS1122sn[j]['note_sn'] ],

                    #PHYSIOLOGIE
                    [ EPS1133[j], coefS1STAPS2[6], EPS1133[j]*coefS1STAPS2[6], "MOYENNE", sort1133.index(EPS1133[j])+1, (EPS1133[j] >=10), creditS1STAPS2[6], creditS1STAPS2[6] if (EPS1133[j] >=10) else 0, EPS1133cc[j]['note_cc'], EPS1133sn[j]['note_sn'] ],

                    #EDUCATION PHYSIQUE : LOISIRS II
                    [ EPS1144[j],  coefS1STAPS2[7], EPS1144[j]*coefS1STAPS2[7], "MOYENNE", sort1144.index(EPS1144[j])+1, (EPS1144[j] >=10), creditS1STAPS2[7], creditS1STAPS2[7] if (EPS1144[j] >=10) else 0, EPS1144cc[j]['note_cc'], EPS1144sn[j]['note_sn'] ],

                    #TRAUMATOLOGIE - PREMIERS SECOURS
                    [ EPS1166[j],  coefS1STAPS2[8], EPS1166[j]*coefS1STAPS2[8], "MOYENNE", sort1166.index(EPS1166[j])+1, (EPS1166[j] >=10), creditS1STAPS2[8], creditS1STAPS2[8] if (EPS1166[j] >=10) else 0, EPS1166cc[j]['note_cc'], EPS1166sn[j]['note_sn'] ],

                    #PEDAGOGIE PRATIQUE III
                    [ EPS1177[j],  coefS1STAPS2[9], EPS1177[j]*coefS1STAPS2[9], 

                        round( (EPS1122[j]*coefS1STAPS2[0]+EPS115a2[j]*coefS1STAPS2[1]+EPS115f2[j]*coefS1STAPS2[2]+EPS115j2[j]*coefS1STAPS2[3]+EPS115g2[j]*coefS1STAPS2[4]+EPS1122[j]*coefS1STAPS2[5]+EPS1133[j]*coefS1STAPS2[6]+EPS1144[j]*coefS1STAPS2[7]+EPS1166[j]*coefS1STAPS2[8]+EPS1177[j]*coefS1STAPS2[9])/(coefS1STAPS2[0]+coefS1STAPS2[1]+coefS1STAPS2[2]+coefS1STAPS2[3]+coefS1STAPS2[4]+coefS1STAPS2[5]+coefS1STAPS2[6]+coefS1STAPS2[7]+coefS1STAPS2[8]+coefS1STAPS2[9]), 2),
                        
                        sort1177.index(EPS1177[j])+1, 

                        (EPS1177[j] >=10), 

                        creditS1STAPS2[9], 

                        creditS1STAPS2[9] if (EPS1177[j] >=10) else 0,

                        EPS1177cc[j]['note_cc'], 

                        EPS1177sn[j]['note_sn'] 
                    ],

                    #ECONOMIE  
                    [ EPS1188[j],  coefS1STAPS2[10], EPS1188[j]*coefS1STAPS2[10], 

                        "MOYENNE", 

                        sort1188.index(EPS1188[j])+1, 

                        (EPS1188[j] >=10), 

                        creditS1STAPS2[10], 

                        creditS1STAPS2[10] if (EPS1188[j] >=10) else 0, 

                        EPS1188cc[j]['note_cc'], 

                        EPS1188sn[j]['note_sn'] 
                    ],

                    #FRANCAIS
                    [ EPS1199[j],  coefS1STAPS2[11], EPS1199[j]*coefS1STAPS2[11], 

                        round( (EPS1188[j]*coefS1STAPS2[10]+EPS1199[j]*coefS1STAPS2[11]) / (coefS1STAPS2[10]+coefS1STAPS2[11]) ,2), #"MOYENNE",

                        sort1199.index(EPS1199[j])+1, 

                        (EPS1199[j] >=10), 

                        creditS1STAPS2[11], creditS1STAPS2[11] if (EPS1199[j] >=10) else 0, 

                        EPS1199cc[j]['note_cc'], 

                        EPS1199sn[j]['note_sn'] 
                    ],

                    
                    #SOMME
                    [ 
                        ( coefS1STAPS2[0]+coefS1STAPS2[1]+coefS1STAPS2[2]+coefS1STAPS2[3]+coefS1STAPS2[4]+coefS1STAPS2[5]+coefS1STAPS2[6]+coefS1STAPS2[7]+coefS1STAPS2[8]+coefS1STAPS2[9]+coefS1STAPS2[10]+coefS1STAPS2[11]), 
                    
                    round( EPS1122[j]*coefS1STAPS2[0]+EPS115a2[j]*coefS1STAPS2[1]+EPS115f2[j]*coefS1STAPS2[2]+EPS115j2[j]*coefS1STAPS2[3]+EPS115g2[j]*coefS1STAPS2[4]+EPS1122[j]*coefS1STAPS2[5]+EPS1133[j]*coefS1STAPS2[6]+EPS1144[j]*coefS1STAPS2[7]+EPS1166[j]*coefS1STAPS2[8]+EPS1177[j]*coefS1STAPS2[9]+EPS1188[j]*coefS1STAPS2[10]+EPS1199[j]*coefS1STAPS2[11] ,2), 

                    round(( EPS1122[j]*coefS1STAPS2[0]+EPS115a2[j]*coefS1STAPS2[1]+EPS115f2[j]*coefS1STAPS2[2]+EPS115j2[j]*coefS1STAPS2[3]+EPS115g2[j]*coefS1STAPS2[4]+EPS1122[j]*coefS1STAPS2[5]+EPS1133[j]*coefS1STAPS2[6]+EPS1144[j]*coefS1STAPS2[7]+EPS1166[j]*coefS1STAPS2[8]+EPS1177[j]*coefS1STAPS2[9]+EPS1188[j]*coefS1STAPS2[10]+EPS1199[j]*coefS1STAPS2[11] ) / ( coefS1STAPS2[0]+coefS1STAPS2[1]+coefS1STAPS2[2]+coefS1STAPS2[3]+coefS1STAPS2[4]+coefS1STAPS2[5]+coefS1STAPS2[6]+coefS1STAPS2[7]+coefS1STAPS2[8]+coefS1STAPS2[9]+coefS1STAPS2[10]+coefS1STAPS2[11]), 2), #moyenne
                        
                        4,

                        5
                    ]
            ]
            
            listeMatrice2.append(matrice2)

            stapsMoyenne2.append(matrice2[13][2])
            stapsMoyenne2.sort(reverse=True)

            moy2 = stat.mean(stapsMoyenne2)
            moy2 = round(moy2, 2)
            session2 = 'Mai 2023'

    semestre1MDS.append(listeMatrice2) #= [filiere , listeMatrice, staps1Moyenne, moy, session]
    semestre1MDS.append(stapsMoyenne2)
    semestre1MDS.append(moy2)
    semestre1MDS.append(session2)

################################################## MATRICE RATTRAPPAGE SEMESTRE 4 #################################################################   
    EPS1112R = list(Evaluation.objects.filter(uniteEnseignement_id=112,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS1112cc = list(Evaluation.objects.filter(uniteEnseignement_id=112).values('note_cc'))
    #EPS1112sn = list(Evaluation.objects.filter(uniteEnseignement_id=112).values('note_sn'))
    sort1112R = epurationRattrapage(EPS1112R)

    EPS115a2R = list(Evaluation.objects.filter(uniteEnseignement_id=113,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS115a2cc = list(Evaluation.objects.filter(uniteEnseignement_id=113).values('note_cc'))
    #EPS115a2sn = list(Evaluation.objects.filter(uniteEnseignement_id=113).values('note_sn'))
    sort115a2R = epurationRattrapage(EPS115a2R)

    EPS115f2R = list(Evaluation.objects.filter(uniteEnseignement_id=114,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS115f2cc = list(Evaluation.objects.filter(uniteEnseignement_id=114).values('note_cc'))
    #EPS115f2sn = list(Evaluation.objects.filter(uniteEnseignement_id=114).values('note_sn'))
    sort115f2R = epurationRattrapage(EPS115f2R)

    EPS115j2R = list(Evaluation.objects.filter(uniteEnseignement_id=115,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS115j2cc = list(Evaluation.objects.filter(uniteEnseignement_id=115).values('note_cc'))
    #EPS115j2sn = list(Evaluation.objects.filter(uniteEnseignement_id=115).values('note_sn'))
    sort115j2R = epurationRattrapage(EPS115j2R) 

    EPS115g2R = list(Evaluation.objects.filter(uniteEnseignement_id=116,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS115g2cc = list(Evaluation.objects.filter(uniteEnseignement_id=116).values('note_cc'))
    #EPS115g2sn = list(Evaluation.objects.filter(uniteEnseignement_id=116).values('note_sn'))
    sort115g2R = epurationRattrapage(EPS115g2R)


    EPS1122R = list(Evaluation.objects.filter(uniteEnseignement_id=117,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS1122cc = list(Evaluation.objects.filter(uniteEnseignement_id=117).values('note_cc'))
    #EPS1122sn = list(Evaluation.objects.filter(uniteEnseignement_id=117).values('note_sn'))
    sort1122R = epurationRattrapage(EPS1122R)

    EPS1133R = list(Evaluation.objects.filter(uniteEnseignement_id=118,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS1133cc = list(Evaluation.objects.filter(uniteEnseignement_id=118).values('note_cc'))
    #EPS1133sn = list(Evaluation.objects.filter(uniteEnseignement_id=118).values('note_sn'))
    sort1133R = epurationRattrapage(EPS1133R)

    EPS1144R = list(Evaluation.objects.filter(uniteEnseignement_id=119,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS1144cc = list(Evaluation.objects.filter(uniteEnseignement_id=119).values('note_cc'))
    #EPS1144sn = list(Evaluation.objects.filter(uniteEnseignement_id=119).values('note_sn'))
    sort1144R = epurationRattrapage(EPS1144R)

    
    EPS1166R = list(Evaluation.objects.filter(uniteEnseignement_id=120,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS1166cc = list(Evaluation.objects.filter(uniteEnseignement_id=120).values('note_cc'))
    #EPS1166sn = list(Evaluation.objects.filter(uniteEnseignement_id=120).values('note_sn'))
    sort1166R = epurationRattrapage(EPS1166R)

    EPS1177R = list(Evaluation.objects.filter(uniteEnseignement_id=121,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS1177cc = list(Evaluation.objects.filter(uniteEnseignement_id=121).values('note_cc'))
    #EPS1177sn = list(Evaluation.objects.filter(uniteEnseignement_id=121).values('note_sn'))
    sort1177R = epurationRattrapage(EPS1177R)

    EPS1188R = list(Evaluation.objects.filter(uniteEnseignement_id=122,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS1188cc = list(Evaluation.objects.filter(uniteEnseignement_id=122).values('note_cc'))
    #EPS1188sn = list(Evaluation.objects.filter(uniteEnseignement_id=122).values('note_sn'))
    sort1188R = epurationRattrapage(EPS1188R)

    EPS1199R = list(Evaluation.objects.filter(uniteEnseignement_id=123,natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS1199cc = list(Evaluation.objects.filter(uniteEnseignement_id=123).values('note_cc')) 
    #EPS1199sn = list(Evaluation.objects.filter(uniteEnseignement_id=123).values('note_sn'))
    sort1199R = epurationRattrapage(EPS1199R)

    listMatriceRattrapage = []

    for j in range( len(infoEtudiantSTAPS2) ):

        matriceR = [
            infoEtudiantSTAPS2[j],

            EPS1112R[j],

            EPS115a2R[j],

            EPS115f2R[j],

            EPS115j2R[j],

            EPS115g2R[j],

            EPS1122R[j],

            EPS1133R[j],

            EPS1144R[j],

            EPS1166R[j],

            EPS1177R[j],

            EPS1188R[j],

            EPS1199R[j]  
        ]

        #matrice de Rattrapage
        listMatriceRattrapage.append(matriceR)
        
    semestre1MDS.append(listMatriceRattrapage)

################################################## MATRICE DE SYNTHESE SEMESTRE 4 #################################################################

    return render(request,'bulletin/BulletinTemplate/bullS4eps.html', {'semestre1MDS': semestre1MDS} ) #


#################################################################################################################################### NIVEAU 3###############################
#EVE SEMESTRE5
def bulls5msoeve(request, filiere):

    infoEtudiantEVE = list( Etudiant.objects.filter(filiere="MAS", niveau=3, Specialite="EVENEMENTIEL").values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))
    
    coefS5EVE = list( UniteEnseignement.objects.filter(semestre_id=5,filiere="MAS").values("coefficient", "intitule_UE"))
    coefS5EVE = epurationCoef(coefS5EVE)

    creditS5EVE = list(UniteEnseignement.objects.filter(semestre_id=5,filiere="MAS").values("nombre_credit"))
    creditS5EVE = epurationCre(creditS5EVE)

    MAS315 = list(Evaluation.objects.filter(uniteEnseignement_id=76).values('note_Examen','note_cc','note_sn'))
    sort315 = epurationTriCroissant(MAS315)

    MAS325 = list(Evaluation.objects.filter(uniteEnseignement_id=77).values('note_Examen'))
    sort325 = epurationTriCroissant(MAS325)

    MAS335 = list(Evaluation.objects.filter(uniteEnseignement_id=78).values('note_Examen'))
    sort335 = epurationTriCroissant(MAS335)

    MAS345 = list(Evaluation.objects.filter(uniteEnseignement_id=79).values('note_Examen'))
    sort345 = epurationTriCroissant(MAS345)

    EVE355 = list(Evaluation.objects.filter(uniteEnseignement_id=80).values('note_Examen'))
    sort355 = epurationTriCroissant(EVE355)

    EVE365 = list(Evaluation.objects.filter(uniteEnseignement_id=81).values('note_Examen'))
    sort365 = epurationTriCroissant(EVE365)

    listeMatrice = []
    EVEMoyenne = []

    for j in range( len(infoEtudiantEVE) ):

        matrice = [
            
            infoEtudiantEVE[j],

            [ MAS315[j], coefS5EVE[0], round(MAS315[j]*coefS5EVE[0], 2),

                round( ((MAS315[j]*coefS5EVE[0]) + (MAS325[j]*coefS5EVE[1]) + (MAS335[j]*coefS5EVE[2]) + (MAS345[j]*coefS5EVE[3])) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]), 2), 

                sort315.index(MAS315[j])+1, 

                (MAS315[j] >=10),

                creditS5EVE[0] 
            ],
            
            [ MAS325[j], coefS5EVE[1], round(MAS325[j]*coefS5EVE[1], 2), 'MOYENNE', sort325.index(MAS325[j])+1, (MAS325[j]>=10) ,creditS5EVE[1] ],
            
            [ MAS335[j], coefS5EVE[2], round(MAS335[j]*coefS5EVE[2], 2), 'MOYENNE', sort335.index(MAS335[j])+1, (MAS335[j]>=10), creditS5EVE[2] ],
            
            [ MAS345[j], coefS5EVE[3], round(MAS345[j]*coefS5EVE[3], 2), 'MOYENNE', sort345.index(MAS345[j])+1, (MAS345[j]>=10), creditS5EVE[3] ],
            
            [ EVE355[j], coefS5EVE[4], round(EVE355[j]*coefS5EVE[4], 2), 

                round((EVE355[j]*coefS5EVE[4] + EVE365[j]*coefS5EVE[5] )/(coefS5EVE[4]+coefS5EVE[5]), 2), 

                sort355.index(EVE355[j])+1, 

                (EVE355[j]>=10),

                creditS5EVE[4] 
            ],
            
            [ EVE365[j], coefS5EVE[5], round(EVE365[j]*coefS5EVE[5], 2), 'MOYENNE', sort365.index(EVE365[j])+1, (EVE365[j]>=10), creditS5EVE[5] ],
        
            [ 
                (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),
    
                round( (MAS315[j]*coefS5EVE[0] + MAS325[j]*coefS5EVE[1] + MAS325[j]*coefS5EVE[2] + MAS345[j]*coefS5EVE[3]+EVE355[j]*coefS5EVE[4] + EVE365[j]*coefS5EVE[5] ), 2),

                round((MAS315[j]*coefS5EVE[0] + MAS325[j]*coefS5EVE[1] + MAS325[j]*coefS5EVE[2] + MAS345[j]*coefS5EVE[3]+EVE355[j]*coefS5EVE[4] + EVE365[j]*coefS5EVE[5])/(coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),2)
            ]
        ]

        creditObtenus = 0
        listeCredit = []

       
        listeMatrice.append(matrice)
        EVEMoyenne.append(matrice[7][2])
        EVEMoyenne.sort(reverse=True)

        moy = stat.mean(EVEMoyenne)
        moy = round(moy, 2)
        session = ''

    semestre1MDS = [filiere, listeMatrice, EVEMoyenne, moy, session, MAS315]


    return render(request,'bulletin/BulletinTemplate/bullS1eps.html', {'semestre1MDS': semestre1MDS} )

#EVE SEMESTRE6
def bulls6msoeve(request, filiere):
    return render(request,'bulletin/BulletinTemplate/bullS1eps.html' ) #, {'semestre1MDS': semestre1MDS}






################################# PROCES VERBAUX #########################################################################################################################################################################################################################
#PV EPS1 SEMESTRE1
def resultatCommunepsmds(request):

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = epurationCoef(coefS1STAPS1)

    creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS1 = epurationCre(creditS1STAPS1)

    val1 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val2 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val3 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val4 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val5 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val6 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val7 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val8 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val9 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val10 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val11 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val12 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    

    e111 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e112 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e113= {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e114 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115a = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115b = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115j = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115l = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e116 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e117 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e118 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e119 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }

    EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=50).values('note_Examen'))
    EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=50).values('note_cc'))
    EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=50).values('note_sn'))
    sort111 = epurationTriCroissant(EPS111)

    EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=51).values('note_Examen'))
    EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=51).values('note_cc'))
    EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=51).values('note_sn'))
    sort112 = epurationTriCroissant(EPS112)

    EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=52).values('note_Examen'))
    EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=52).values('note_cc'))
    EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=52).values('note_sn'))
    sort113 = epurationTriCroissant(EPS113)

    EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=53).values('note_Examen'))
    EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=53).values('note_cc'))
    EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=53).values('note_sn'))
    sort114 = epurationTriCroissant(EPS114)

    EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=54).values('note_Examen'))
    EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=54).values('note_cc'))
    EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=54).values('note_sn'))
    sort115a = epurationTriCroissant(EPS115a)

    EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=55).values('note_Examen'))
    EPS115bcc = list(Evaluation.objects.filter(uniteEnseignement_id=55).values('note_cc'))
    EPS115bsn = list(Evaluation.objects.filter(uniteEnseignement_id=55).values('note_sn'))
    sort115b = epurationTriCroissant(EPS115b) 

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=56).values('note_Examen'))
    EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=56).values('note_cc'))
    EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=56).values('note_sn'))
    sort115j = epurationTriCroissant(EPS115j)

    EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=57).values('note_Examen'))
    EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=57).values('note_cc'))
    EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=57).values('note_sn'))
    sort115l = epurationTriCroissant(EPS115l)

    EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=58).values('note_Examen'))
    EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=58).values('note_cc'))
    EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=58).values('note_sn'))
    sort116 = epurationTriCroissant(EPS116)

    EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=59).values('note_Examen'))
    EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=59).values('note_cc')) 
    EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=59).values('note_sn')) 
    sort117 = epurationTriCroissant(EPS117)

    EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=60).values('note_Examen'))
    EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=60).values('note_cc'))
    EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=60).values('note_sn'))
    sort118 = epurationTriCroissant(EPS118)

    EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=61).values('note_Examen'))
    EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=61).values('note_cc'))
    EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=61).values('note_sn'))
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

                        [ EPS111[j], coefS1STAPS1[0], EPS111[j]*coefS1STAPS1[0], round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2), sort111.index(EPS111[j])+1,(EPS111[j]>=10), creditS1STAPS1[0], creditS1STAPS1[0] if (EPS111[j]>=10) else 0, EPS111cc[j]['note_cc'], EPS111sn[j]['note_sn'] ],

                        [ EPS112[j], coefS1STAPS1[1], EPS112[j]*coefS1STAPS1[1], "MOYENNE", sort112.index(EPS112[j])+1,(EPS112[j]>=10), creditS1STAPS1[1], creditS1STAPS1[1] if (EPS112[j]>=10) else 0, EPS112cc[j]['note_cc'], EPS112sn[j]['note_sn'] ],

                        [ EPS113[j], 

                            coefS1STAPS1[2], 

                            EPS113[j]*coefS1STAPS1[2], 

                            round( ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5]) + (EPS115j[j]*coefS1STAPS1[6]) + (EPS115l[j]*coefS1STAPS1[7]) + (EPS116[j]*coefS1STAPS1[8]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]) ,2), 
                            
                            sort113.index(EPS113[j])+1,
                            
                            (EPS113[j] >=10),
                            
                            creditS1STAPS1[2], 
                            creditS1STAPS1[2] if(EPS113[j] >=10) else 0,

                            EPS113cc[j]['note_cc'], 
                            EPS113sn[j]['note_sn']
                        ],

                        [ EPS114[j],  coefS1STAPS1[3], EPS114[j]*coefS1STAPS1[3], "MOYENNE", sort114.index(EPS114[j])+1, (EPS114[j] >=10), creditS1STAPS1[3], creditS1STAPS1[3] if (EPS114[j] >=10) else 0, EPS114cc[j]['note_cc'], EPS114sn[j]['note_sn']  ],

                        [ EPS115a[j], coefS1STAPS1[4], EPS115a[j]*coefS1STAPS1[4], "MOYENNE", sort115a.index(EPS115a[j])+1, (EPS115a[j] >=10), creditS1STAPS1[4], creditS1STAPS1[4] if (EPS115a[j] >=10) else 0, EPS115acc[j]['note_cc'], EPS115asn[j]['note_sn'] ], #crédits

                        [ EPS115b[j], coefS1STAPS1[5], EPS115b[j]*coefS1STAPS1[5], "MOYENNE", sort115b.index(EPS115b[j])+1, (EPS115b[j] >=10), creditS1STAPS1[5], creditS1STAPS1[5] if (EPS115b[j] >=10) else 0, EPS115bcc[j]['note_cc'], EPS115bsn[j]['note_sn'] ],

                        [ EPS115j[j], coefS1STAPS1[6], EPS115j[j]*coefS1STAPS1[6], "MOYENNE", sort115j.index(EPS115j[j])+1, (EPS115j[j] >=10), creditS1STAPS1[6], creditS1STAPS1[6] if (EPS115j[j] >=10) else 0, EPS115jcc[j]['note_cc'], EPS115jsn[j]['note_sn'] ],

                        [ EPS115l[j], coefS1STAPS1[7], EPS115l[j]*coefS1STAPS1[7], "MOYENNE", sort115l.index(EPS115l[j])+1, (EPS115l[j] >=10), creditS1STAPS1[7], creditS1STAPS1[7] if ((EPS115a[j]+EPS115b[j]+EPS115j[j]+EPS115l[j]) >=40) else 0, EPS115lcc[j]['note_cc'], EPS115lsn[j]['note_sn']  ],

                        [ EPS116[j],  coefS1STAPS1[8], EPS116[j]*coefS1STAPS1[8], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[8], creditS1STAPS1[8] if (EPS116[j] >=10) else 0, EPS116cc[j]['note_cc'], EPS116sn[j]['note_sn'] ],

                        [ EPS117[j], coefS1STAPS1[9], 

                            EPS117[j]*coefS1STAPS1[9], 

                            round( ((EPS117[j]*coefS1STAPS1[9]) + (EPS118[j]*coefS1STAPS1[10]) + (EPS119[j]*coefS1STAPS1[11])) / ( coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]) ,2), 

                            sort117.index(EPS117[j])+1, 

                            (EPS117[j] >=10), 
                            
                            creditS1STAPS1[9],
                            creditS1STAPS1[9] if (EPS117[j] >=10) else 0,

                            EPS117cc[j]['note_cc'], EPS117sn[j]['note_sn']
                        ],

                        [ EPS118[j], coefS1STAPS1[10], EPS118[j]*coefS1STAPS1[10], "MOYENNE", sort118.index(EPS118[j])+1, (EPS118[j] >=10), creditS1STAPS1[10], creditS1STAPS1[10] if (EPS118[j] >=10) else 0, EPS118cc[j]['note_cc'], EPS118sn[j]['note_sn'] ],

                        [ EPS119[j], coefS1STAPS1[11], EPS119[j]*coefS1STAPS1[11], "MOYENNE", sort119.index(EPS119[j])+1, (EPS119[j] >=10), creditS1STAPS1[11], creditS1STAPS1[11] if (EPS119[j] >=10) else 0, EPS119cc[j]['note_cc'], EPS119sn[j]['note_sn'] ],

                        [ 
                            ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ), #coefsomme

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
    
    #STATS VALIDATION
    for i in range (len(EPS111)):
        if EPS111[i] >= 10:
            val1['nombre']+=1
    val1['pourcentage']= round(((val1['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS112)):
        if EPS112[i] >= 10:
            val2['nombre']+=1
    val2['pourcentage']= round(((val2['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS113)):
        if EPS113[i] >= 10:
            val3['nombre']+=1
    val3['pourcentage']= round(((val3['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS114)):
        if EPS114[i] >= 10:
            val4['nombre']+=1
    val4['pourcentage']= round(((val4['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115a)):
        if EPS115a[i] >= 10:
            val5['nombre']+=1
    val5['pourcentage']= round(((val5['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115b)):
        if EPS115b[i] >= 10:
            val6['nombre']+=1
    val6['pourcentage']= round(((val6['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115j)):
        if EPS115j[i] >= 10:
            val7['nombre']+=1
    val7['pourcentage']= round(((val7['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115l)):
        if EPS115l[i] >= 10:
            val8['nombre']+=1
    val8['pourcentage']= round(((val8['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS116)):
        if EPS116[i] >= 10:
            val9['nombre']+=1
    val9['pourcentage']= round(((val9['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS117)):
        if EPS117[i] >= 10:
            val10['nombre']+=1
    val10['pourcentage']= round(((val10['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS118)):
        if EPS118[i] >= 10:
            val11['nombre']+=1
    val11['pourcentage']= round(((val11['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS119)):
        if EPS119[i] >= 10:
            val12['nombre']+=1
    val12['pourcentage']= round(((val12['nombre']/ len(infoEtudiantSTAPS1))*100), 2)


    #STATS MENTION
    statMention(EPS111,e111)
    pourcentageMention(e111, len(infoEtudiantSTAPS1))

    statMention(EPS112,e112)
    pourcentageMention(e112, len(infoEtudiantSTAPS1))

    statMention(EPS113,e113)
    pourcentageMention(e113, len(infoEtudiantSTAPS1))

    statMention(EPS114,e114)
    pourcentageMention(e114, len(infoEtudiantSTAPS1))

    statMention(EPS115a,e115a)
    pourcentageMention(e115a, len(infoEtudiantSTAPS1))

    statMention(EPS115b,e115b)
    pourcentageMention(e115b, len(infoEtudiantSTAPS1))

    statMention(EPS115j,e115j)
    pourcentageMention(e115j, len(infoEtudiantSTAPS1))

    statMention(EPS115l,e115l)
    pourcentageMention(e115l, len(infoEtudiantSTAPS1))

    statMention(EPS116,e116)
    pourcentageMention(e116, len(infoEtudiantSTAPS1))

    statMention(EPS117,e117)
    pourcentageMention(e117, len(infoEtudiantSTAPS1))

    statMention(EPS118,e118)
    pourcentageMention(e118, len(infoEtudiantSTAPS1))

    statMention(EPS119,e119)
    pourcentageMention(e119, len(infoEtudiantSTAPS1))


    UEStats = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12]
    UEstats_mention = [e111, e112, e113, e114, e115a, e115b, e115j, e115l, e116, e117, e118, e119]
                
    semestre1MDS = [filiere, listeMatrice, staps1Moyenne, moy, session , creditS1STAPS1, UEStats, UEstats_mention ] #

    return render(request, 'bulletin/releveCommun/releveCommun.html', {'semestre1MDS': semestre1MDS})

#PV EPS1 SEMESTRE2
def resultatCommuns2staps(request):

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = epurationCoef(coefS1STAPS1)

    creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS1 = epurationCre(creditS1STAPS1)

    val1 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val2 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val3 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val4 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val5 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val6 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val7 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val8 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val9 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val10 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val11 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val12 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    

    e111 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e112 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e113= {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e114 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115a = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115b = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115j = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115l = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e116 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e117 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e118 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e119 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }

    EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=99).values('note_Examen'))
    EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=99).values('note_cc'))
    EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=99).values('note_sn'))
    sort111 = epurationTriCroissant(EPS111)

    EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=100).values('note_Examen'))
    EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=100).values('note_cc'))
    EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=100).values('note_sn'))
    sort112 = epurationTriCroissant(EPS112)

    EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=101).values('note_Examen'))
    EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=101).values('note_cc'))
    EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=101).values('note_sn'))
    sort113 = epurationTriCroissant(EPS113)

    EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=102).values('note_Examen'))
    EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=102).values('note_cc'))
    EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=102).values('note_sn'))
    sort114 = epurationTriCroissant(EPS114)

    EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=103).values('note_Examen'))
    EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=103).values('note_cc'))
    EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=103).values('note_sn'))
    sort115a = epurationTriCroissant(EPS115a)

    EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=104).values('note_Examen'))
    EPS115bcc = list(Evaluation.objects.filter(uniteEnseignement_id=104).values('note_cc'))
    EPS115bsn = list(Evaluation.objects.filter(uniteEnseignement_id=104).values('note_sn'))
    sort115b = epurationTriCroissant(EPS115b) 

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=105).values('note_Examen'))
    EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=105).values('note_cc'))
    EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=105).values('note_sn'))
    sort115j = epurationTriCroissant(EPS115j)

    EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=106).values('note_Examen'))
    EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=106).values('note_cc'))
    EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=106).values('note_sn'))
    sort115l = epurationTriCroissant(EPS115l)

    EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=108).values('note_Examen'))
    EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=108).values('note_cc'))
    EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=108).values('note_sn'))
    sort116 = epurationTriCroissant(EPS116)

    EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=109).values('note_Examen'))
    EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=109).values('note_cc')) 
    EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=109).values('note_sn')) 
    sort117 = epurationTriCroissant(EPS117)

    EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=110).values('note_Examen'))
    EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=110).values('note_cc'))
    EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=110).values('note_sn'))
    sort118 = epurationTriCroissant(EPS118)

    EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=111).values('note_Examen'))
    EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=111).values('note_cc'))
    EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=111).values('note_sn'))
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

                        [ EPS111[j], coefS1STAPS1[0], EPS111[j]*coefS1STAPS1[0], round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2), sort111.index(EPS111[j])+1,(EPS111[j]>=10), creditS1STAPS1[0], creditS1STAPS1[0] if (EPS111[j]>=10) else 0, EPS111cc[j]['note_cc'], EPS111sn[j]['note_sn'] ],

                        [ EPS112[j], coefS1STAPS1[1], EPS112[j]*coefS1STAPS1[1], "MOYENNE", sort112.index(EPS112[j])+1,(EPS112[j]>=10), creditS1STAPS1[1], creditS1STAPS1[1] if (EPS112[j]>=10) else 0, EPS112cc[j]['note_cc'], EPS112sn[j]['note_sn'] ],

                        [ EPS113[j], 

                            coefS1STAPS1[2], 

                            EPS113[j]*coefS1STAPS1[2], 

                            round( ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5]) + (EPS115j[j]*coefS1STAPS1[6]) + (EPS115l[j]*coefS1STAPS1[7]) + (EPS116[j]*coefS1STAPS1[8]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]) ,2), 
                            
                            sort113.index(EPS113[j])+1,
                            
                            (EPS113[j] >=10),
                            
                            creditS1STAPS1[2], 
                            creditS1STAPS1[2] if(EPS113[j] >=10) else 0,

                            EPS113cc[j]['note_cc'], 
                            EPS113sn[j]['note_sn']
                        ],

                        [ EPS114[j],  coefS1STAPS1[3], EPS114[j]*coefS1STAPS1[3], "MOYENNE", sort114.index(EPS114[j])+1, (EPS114[j] >=10), creditS1STAPS1[3], creditS1STAPS1[3] if (EPS114[j] >=10) else 0, EPS114cc[j]['note_cc'], EPS114sn[j]['note_sn']  ],

                        [ EPS115a[j], coefS1STAPS1[4], EPS115a[j]*coefS1STAPS1[4], "MOYENNE", sort115a.index(EPS115a[j])+1, (EPS115a[j] >=10), creditS1STAPS1[4], creditS1STAPS1[4] if (EPS115a[j] >=10) else 0, EPS115acc[j]['note_cc'], EPS115asn[j]['note_sn'] ], #crédits

                        [ EPS115b[j], coefS1STAPS1[5], EPS115b[j]*coefS1STAPS1[5], "MOYENNE", sort115b.index(EPS115b[j])+1, (EPS115b[j] >=10), creditS1STAPS1[5], creditS1STAPS1[5] if (EPS115b[j] >=10) else 0, EPS115bcc[j]['note_cc'], EPS115bsn[j]['note_sn'] ],

                        [ EPS115j[j], coefS1STAPS1[6], EPS115j[j]*coefS1STAPS1[6], "MOYENNE", sort115j.index(EPS115j[j])+1, (EPS115j[j] >=10), creditS1STAPS1[6], creditS1STAPS1[6] if (EPS115j[j] >=10) else 0, EPS115jcc[j]['note_cc'], EPS115jsn[j]['note_sn'] ],

                        [ EPS115l[j], coefS1STAPS1[7], EPS115l[j]*coefS1STAPS1[7], "MOYENNE", sort115l.index(EPS115l[j])+1, (EPS115l[j] >=10), creditS1STAPS1[7], creditS1STAPS1[7] if ((EPS115a[j]+EPS115b[j]+EPS115j[j]+EPS115l[j]) >=40) else 0, EPS115lcc[j]['note_cc'], EPS115lsn[j]['note_sn']  ],

                        [ EPS116[j],  coefS1STAPS1[8], EPS116[j]*coefS1STAPS1[8], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[8], creditS1STAPS1[8] if (EPS116[j] >=10) else 0, EPS116cc[j]['note_cc'], EPS116sn[j]['note_sn'] ],

                        [ EPS117[j], coefS1STAPS1[9], 

                            EPS117[j]*coefS1STAPS1[9], 

                            round( ((EPS117[j]*coefS1STAPS1[9]) + (EPS118[j]*coefS1STAPS1[10]) + (EPS119[j]*coefS1STAPS1[11])) / ( coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]) ,2), 

                            sort117.index(EPS117[j])+1, 

                            (EPS117[j] >=10), 
                            
                            creditS1STAPS1[9],
                            creditS1STAPS1[9] if (EPS117[j] >=10) else 0,

                            EPS117cc[j]['note_cc'], EPS117sn[j]['note_sn']
                        ],

                        [ EPS118[j], coefS1STAPS1[10], EPS118[j]*coefS1STAPS1[10], "MOYENNE", sort118.index(EPS118[j])+1, (EPS118[j] >=10), creditS1STAPS1[10], creditS1STAPS1[10] if (EPS118[j] >=10) else 0, EPS118cc[j]['note_cc'], EPS118sn[j]['note_sn'] ],

                        [ EPS119[j], coefS1STAPS1[11], EPS119[j]*coefS1STAPS1[11], "MOYENNE", sort119.index(EPS119[j])+1, (EPS119[j] >=10), creditS1STAPS1[11], creditS1STAPS1[11] if (EPS119[j] >=10) else 0, EPS119cc[j]['note_cc'], EPS119sn[j]['note_sn'] ],

                        [ 
                            ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ), #coefsomme

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

    #STATS VALIDATION
    for i in range (len(EPS111)):
        if EPS111[i] >= 10:
            val1['nombre']+=1
    val1['pourcentage']= round(((val1['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS112)):
        if EPS112[i] >= 10:
            val2['nombre']+=1
    val2['pourcentage']= round(((val2['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS113)):
        if EPS113[i] >= 10:
            val3['nombre']+=1
    val3['pourcentage']= round(((val3['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS114)):
        if EPS114[i] >= 10:
            val4['nombre']+=1
    val4['pourcentage']= round(((val4['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115a)):
        if EPS115a[i] >= 10:
            val5['nombre']+=1
    val5['pourcentage']= round(((val5['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115b)):
        if EPS115b[i] >= 10:
            val6['nombre']+=1
    val6['pourcentage']= round(((val6['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115j)):
        if EPS115j[i] >= 10:
            val7['nombre']+=1
    val7['pourcentage']= round(((val7['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115l)):
        if EPS115l[i] >= 10:
            val8['nombre']+=1
    val8['pourcentage']= round(((val8['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS116)):
        if EPS116[i] >= 10:
            val9['nombre']+=1
    val9['pourcentage']= round(((val9['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS117)):
        if EPS117[i] >= 10:
            val10['nombre']+=1
    val10['pourcentage']= round(((val10['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS118)):
        if EPS118[i] >= 10:
            val11['nombre']+=1
    val11['pourcentage']= round(((val11['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS119)):
        if EPS119[i] >= 10:
            val12['nombre']+=1
    val12['pourcentage']= round(((val12['nombre']/ len(infoEtudiantSTAPS1))*100), 2)  


    #STATS MENTION
    statMention(EPS111,e111)
    pourcentageMention(e111, len(infoEtudiantSTAPS1))

    statMention(EPS112,e112)
    pourcentageMention(e112, len(infoEtudiantSTAPS1))

    statMention(EPS113,e113)
    pourcentageMention(e113, len(infoEtudiantSTAPS1))

    statMention(EPS114,e114)
    pourcentageMention(e114, len(infoEtudiantSTAPS1))

    statMention(EPS115a,e115a)
    pourcentageMention(e115a, len(infoEtudiantSTAPS1))

    statMention(EPS115b,e115b)
    pourcentageMention(e115b, len(infoEtudiantSTAPS1))

    statMention(EPS115j,e115j)
    pourcentageMention(e115j, len(infoEtudiantSTAPS1))

    statMention(EPS115l,e115l)
    pourcentageMention(e115l, len(infoEtudiantSTAPS1))

    statMention(EPS116,e116)
    pourcentageMention(e116, len(infoEtudiantSTAPS1))

    statMention(EPS117,e117)
    pourcentageMention(e117, len(infoEtudiantSTAPS1))

    statMention(EPS118,e118)
    pourcentageMention(e118, len(infoEtudiantSTAPS1))

    statMention(EPS119,e119)
    pourcentageMention(e119, len(infoEtudiantSTAPS1))


    UEStats = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12]
    UEstats_mention = [e111, e112, e113, e114, e115a, e115b, e115j, e115l, e116, e117, e118, e119]
                
    semestre1MDS = [filiere, listeMatrice, staps1Moyenne, moy, session , creditS1STAPS1, UEStats, UEstats_mention ] 

    return render(request, 'bulletin/releveCommun/releveCommun2.html')
##########################################################################################################################################################################################################################################################################

#PV MDS1 SEMESTRE1
def resultatCommunmds(request):
    

    infoEtudiantMDS =list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("coefficient", "intitule_UE"))
    coefS1MDS1 = epurationCoef(coefS1MDS1)

    creditS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("nombre_credit"))
    creditS1MDS1 = epurationCre(creditS1MDS1)

    val1 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val2 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val3 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val4 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val5 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val6 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val7 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val8 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val9 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val10 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    

    m111 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m111b = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m112 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m112b = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m113 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m114 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m115 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m116 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m117 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m117b = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }

        
    MDS111 =list(Evaluation.objects.filter(uniteEnseignement_id=40).values('note_Examen'))
    MDS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=40).values('note_cc'))
    MDS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=40).values('note_sn'))
    sort111 = epurationTriCroissant(MDS111)

    MDS111b =list(Evaluation.objects.filter(uniteEnseignement_id=41).values('note_Examen'))
    MDS111bcc =list(Evaluation.objects.filter(uniteEnseignement_id=41).values('note_cc'))
    MDS111bsn =list(Evaluation.objects.filter(uniteEnseignement_id=41).values('note_sn'))
    sort111b = epurationTriCroissant(MDS111b)

    MDS112 =list(Evaluation.objects.filter(uniteEnseignement_id=42).values('note_Examen'))
    MDS112cc =list(Evaluation.objects.filter(uniteEnseignement_id=42).values('note_cc'))
    MDS112sn =list(Evaluation.objects.filter(uniteEnseignement_id=42).values('note_sn'))
    sort112 = epurationTriCroissant(MDS112)

    MDS112b =list(Evaluation.objects.filter(uniteEnseignement_id=43).values('note_Examen'))
    MDS112bcc =list(Evaluation.objects.filter(uniteEnseignement_id=43).values('note_cc'))
    MDS112bsn =list(Evaluation.objects.filter(uniteEnseignement_id=43).values('note_sn'))
    sort112b = epurationTriCroissant(MDS112b)

    MDS113 =list(Evaluation.objects.filter(uniteEnseignement_id=44).values('note_Examen'))
    MDS113cc =list(Evaluation.objects.filter(uniteEnseignement_id=44).values('note_cc'))
    MDS113sn =list(Evaluation.objects.filter(uniteEnseignement_id=44).values('note_sn'))
    sort113 = epurationTriCroissant(MDS113)

    MDS114 =list(Evaluation.objects.filter(uniteEnseignement_id=45).values('note_Examen'))
    MDS114cc =list(Evaluation.objects.filter(uniteEnseignement_id=45).values('note_cc'))
    MDS114sn =list(Evaluation.objects.filter(uniteEnseignement_id=45).values('note_sn'))
    sort114 = epurationTriCroissant(MDS114)

    MDS115 =list(Evaluation.objects.filter(uniteEnseignement_id=46).values('note_Examen'))
    MDS115cc =list(Evaluation.objects.filter(uniteEnseignement_id=46).values('note_cc'))
    MDS115sn =list(Evaluation.objects.filter(uniteEnseignement_id=46).values('note_sn'))
    sort115 = epurationTriCroissant(MDS115)

    MDS116 =list(Evaluation.objects.filter(uniteEnseignement_id=47).values('note_Examen'))
    MDS116cc =list(Evaluation.objects.filter(uniteEnseignement_id=47).values('note_cc'))
    MDS116sn =list(Evaluation.objects.filter(uniteEnseignement_id=47).values('note_sn'))
    sort116 = epurationTriCroissant(MDS116)

    MDS117 =list(Evaluation.objects.filter(uniteEnseignement_id=48).values('note_Examen'))
    MDS117cc =list(Evaluation.objects.filter(uniteEnseignement_id=48).values('note_cc'))
    MDS117sn =list(Evaluation.objects.filter(uniteEnseignement_id=48).values('note_sn'))
    sort117 = epurationTriCroissant(MDS117)

    MDS117b =list(Evaluation.objects.filter(uniteEnseignement_id=49).values('note_Examen'))
    MDS117bcc =list(Evaluation.objects.filter(uniteEnseignement_id=49).values('note_cc'))
    MDS117bsn =list(Evaluation.objects.filter(uniteEnseignement_id=49).values('note_sn'))
    sort117b = epurationTriCroissant(MDS117b)

    listeMatrice = []
    mds1Moyenne = []

    for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

        matrice = [
                infoEtudiantMDS[j],

                [ MDS111[j], coefS1MDS1[0], MDS111[j]*coefS1MDS1[0], round( ((MDS111[j]*coefS1MDS1[0]) + (MDS111b[j]*coefS1MDS1[1]) + ( MDS112[j]*coefS1MDS1[2]) + (MDS112b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2), sort111.index(MDS111[j])+1,(MDS111[j]>=10), creditS1MDS1[0], creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0 , MDS111cc[j]['note_cc'], MDS111sn[j]['note_sn']  ],

                [ MDS111b[j], coefS1MDS1[1], MDS111b[j]*coefS1MDS1[1], "MOYENNE", sort111b.index(MDS111b[j])+1,(MDS111b[j]>=10), creditS1MDS1[1], creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0, MDS111bcc[j]['note_cc'], MDS111bsn[j]['note_sn'] ],

                [ MDS112[j], coefS1MDS1[2], MDS112[j]*coefS1MDS1[2], "MOYENNE", sort112.index(MDS112[j])+1,(MDS112[j]>=10), creditS1MDS1[2], creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0 ,MDS112cc[j]['note_cc'], MDS112sn[j]['note_sn']],

                [ MDS112b[j], coefS1MDS1[3], MDS112b[j]*coefS1MDS1[3], "MOYENNE", sort112b.index(MDS112b[j])+1,(MDS112b[j]>=10), creditS1MDS1[3], creditS1MDS1[3] if((MDS112[j]+MDS112b[j])>=20) else 0, MDS112cc[j]['note_cc'], MDS112sn[j]['note_sn'] ],


                [ MDS113[j], coefS1MDS1[4], MDS113[j]*coefS1MDS1[4], 

                    round( ((MDS113[j]*coefS1MDS1[4]) + (MDS114[j]*coefS1MDS1[5]) + MDS115[j]*coefS1MDS1[6] + MDS116[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2), 
                    
                    sort113.index(MDS113[j])+1,
                    (MDS113[j]>=10), 

                    creditS1MDS1[4],
                     creditS1MDS1[4] if (MDS113[j]>=10) else 0,

                     MDS113cc[j]['note_cc'],
                     MDS113sn[j]['note_sn']
                ],

                [ MDS114[j], coefS1MDS1[5], MDS114[j]*coefS1MDS1[5], "MOYENNE", sort114.index(MDS114[j])+1,(MDS114[j]>=10), creditS1MDS1[5], creditS1MDS1[5] if (MDS114[j]>=10) else 0, MDS114cc[j]['note_cc'], MDS114sn[j]['note_sn'] ],

                [ MDS115[j], coefS1MDS1[6], MDS115[j]*coefS1MDS1[6], "MOYENNE", sort115.index(MDS115[j])+1,(MDS115[j]>=10), creditS1MDS1[6], creditS1MDS1[6] if (MDS115[j]>=10) else 0, MDS115cc[j]['note_cc'], MDS115sn[j]['note_sn'] ],

                [ MDS116[j], coefS1MDS1[7], MDS116[j]*coefS1MDS1[7], "MOYENNE", sort116.index(MDS116[j])+1,(MDS116[j]>=10), creditS1MDS1[7], creditS1MDS1[7] if (MDS116[j]>=10) else 0, MDS116cc[j]['note_cc'], MDS116sn[j]['note_sn'] ],


                [ MDS117[j], coefS1MDS1[8], MDS117[j]*coefS1MDS1[8], 
                
                round(( MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2), 
                    sort117.index(MDS117[j])+1,
                    (MDS117[j]>=10), 

                    creditS1MDS1[8],
                     creditS1MDS1[8] if (MDS117[j]>=10) else 0,

                     MDS117cc[j]['note_cc'],
                     MDS117sn[j]['note_sn']

                ],

                [ MDS117b[j], coefS1MDS1[9], MDS117b[j]*coefS1MDS1[9], "MOYENNE", sort117b.index(MDS117b[j])+1,(MDS117b[j]>=10), creditS1MDS1[9], creditS1MDS1[9] if ( (MDS117b[j]+MDS117[j]) >=20) else 0, MDS117bcc[j]['note_cc'], MDS117bsn[j]['note_sn'] ],

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

    #STATS VALIDATION
    for i in range (len(MDS111)):
        if MDS111[i] >= 10:
            val1['nombre']+=1
    val1['pourcentage']= round(((val1['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS111b)):
        if MDS111b[i] >= 10:
            val2['nombre']+=1
    val2['pourcentage']= round(((val2['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS112)):
        if MDS112[i] >= 10:
            val3['nombre']+=1
    val3['pourcentage']= round(((val3['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS112b)):
        if MDS112b[i] >= 10:
            val4['nombre']+=1
    val4['pourcentage']= round(((val4['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS113)):
        if MDS113[i] >= 10:
            val5['nombre']+=1
    val5['pourcentage']= round(((val5['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS114)):
        if MDS114[i] >= 10:
            val6['nombre']+=1
    val6['pourcentage']= round(((val6['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS115)):
        if MDS115[i] >= 10:
            val7['nombre']+=1
    val7['pourcentage']= round(((val7['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS116)):
        if MDS116[i] >= 10:
            val8['nombre']+=1
    val8['pourcentage']= round(((val8['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS117)):
        if MDS117[i] >= 10:
            val9['nombre']+=1
    val9['pourcentage']= round(((val9['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS117b)):
        if MDS117b[i] >= 10:
            val10['nombre']+=1
    val10['pourcentage']= round(((val10['nombre']/ len(infoEtudiantMDS))*100), 2)


    #STATS MENTION
    statMention(MDS111,m111)
    pourcentageMention(m111, len(infoEtudiantMDS))

    statMention(MDS111b,m111b)
    pourcentageMention(m111b, len(infoEtudiantMDS))

    statMention(MDS112,m112)
    pourcentageMention(m112, len(infoEtudiantMDS))

    statMention(MDS112b,m112b)
    pourcentageMention(m112b, len(infoEtudiantMDS))

    statMention(MDS113,m113)
    pourcentageMention(m113, len(infoEtudiantMDS))

    statMention(MDS114,m114)
    pourcentageMention(m114, len(infoEtudiantMDS))

    statMention(MDS115,m115)
    pourcentageMention(m115, len(infoEtudiantMDS))

    statMention(MDS116,m116)
    pourcentageMention(m116, len(infoEtudiantMDS))

    statMention(MDS117,m117)
    pourcentageMention(m117, len(infoEtudiantMDS))

    statMention(MDS117b,m117b)
    pourcentageMention(m117b, len(infoEtudiantMDS))



    UEStats = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
    UEstats_mention = [m111, m111b, m112, m112b, m113, m114, m115, m116, m117, m117b]


    semestre1MDS = [filiere, listeMatrice, mds1Moyenne, moy, session, creditS1MDS1, UEStats, UEstats_mention] #filiere, listeMatrice, staps1Moyenne, moy, session

    return render(request, 'bulletin/releveCommun/releveCommunmds.html', {'semestre1MDS': semestre1MDS})

#PV MDS1 SEMESTRE2
def resultatCommuns2mds(request):

    infoEtudiantMDS =list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("coefficient", "intitule_UE"))
    coefS1MDS1 = epurationCoef(coefS1MDS1)

    creditS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("nombre_credit"))
    creditS1MDS1 = epurationCre(creditS1MDS1)

    val1 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val2 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val3 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val4 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val5 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val6 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val7 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val8 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val9 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val10 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    

    m111 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m111b = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m112 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m112b = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m113 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m114 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m115 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m116 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m117 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m117b = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }

    MDS111 =list(Evaluation.objects.filter(uniteEnseignement_id=88).values('note_Examen'))
    MDS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=88).values('note_cc'))
    MDS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=88).values('note_sn'))
    sort111 = epurationTriCroissant(MDS111)

    MDS111b =list(Evaluation.objects.filter(uniteEnseignement_id=89).values('note_Examen'))
    MDS111bcc =list(Evaluation.objects.filter(uniteEnseignement_id=89).values('note_cc'))
    MDS111bsn =list(Evaluation.objects.filter(uniteEnseignement_id=89).values('note_sn'))
    sort111b = epurationTriCroissant(MDS111b)

    MDS112 =list(Evaluation.objects.filter(uniteEnseignement_id=90).values('note_Examen'))
    MDS112cc =list(Evaluation.objects.filter(uniteEnseignement_id=90).values('note_cc'))
    MDS112sn =list(Evaluation.objects.filter(uniteEnseignement_id=90).values('note_sn'))
    sort112 = epurationTriCroissant(MDS112)

    MDS112b =list(Evaluation.objects.filter(uniteEnseignement_id=91).values('note_Examen'))
    MDS112bcc =list(Evaluation.objects.filter(uniteEnseignement_id=91).values('note_cc'))
    MDS112bsn =list(Evaluation.objects.filter(uniteEnseignement_id=91).values('note_sn'))
    sort112b = epurationTriCroissant(MDS112b)

    MDS113 =list(Evaluation.objects.filter(uniteEnseignement_id=92).values('note_Examen'))
    MDS113cc =list(Evaluation.objects.filter(uniteEnseignement_id=92).values('note_cc'))
    MDS113sn =list(Evaluation.objects.filter(uniteEnseignement_id=92).values('note_sn'))
    sort113 = epurationTriCroissant(MDS113)

    MDS114 =list(Evaluation.objects.filter(uniteEnseignement_id=93).values('note_Examen'))
    MDS114cc =list(Evaluation.objects.filter(uniteEnseignement_id=93).values('note_cc'))
    MDS114sn =list(Evaluation.objects.filter(uniteEnseignement_id=93).values('note_sn'))
    sort114 = epurationTriCroissant(MDS114)

    MDS115 =list(Evaluation.objects.filter(uniteEnseignement_id=95).values('note_Examen'))
    MDS115cc =list(Evaluation.objects.filter(uniteEnseignement_id=95).values('note_cc'))
    MDS115sn =list(Evaluation.objects.filter(uniteEnseignement_id=95).values('note_sn'))
    sort115 = epurationTriCroissant(MDS115)

    MDS116 =list(Evaluation.objects.filter(uniteEnseignement_id=96).values('note_Examen'))
    MDS116cc =list(Evaluation.objects.filter(uniteEnseignement_id=96).values('note_cc'))
    MDS116sn =list(Evaluation.objects.filter(uniteEnseignement_id=96).values('note_sn'))
    sort116 = epurationTriCroissant(MDS116)

    MDS117 =list(Evaluation.objects.filter(uniteEnseignement_id=97).values('note_Examen'))
    MDS117cc =list(Evaluation.objects.filter(uniteEnseignement_id=97).values('note_cc'))
    MDS117sn =list(Evaluation.objects.filter(uniteEnseignement_id=97).values('note_sn'))
    sort117 = epurationTriCroissant(MDS117)

    MDS117b =list(Evaluation.objects.filter(uniteEnseignement_id=98).values('note_Examen'))
    MDS117bcc =list(Evaluation.objects.filter(uniteEnseignement_id=98).values('note_cc'))
    MDS117bsn =list(Evaluation.objects.filter(uniteEnseignement_id=98).values('note_sn'))
    sort117b = epurationTriCroissant(MDS117b)

    listeMatrice = []
    mds1Moyenne = []

    for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

        matrice = [
                infoEtudiantMDS[j],

                [ MDS111[j], coefS1MDS1[0], MDS111[j]*coefS1MDS1[0], round( ((MDS111[j]*coefS1MDS1[0]) + (MDS111b[j]*coefS1MDS1[1]) + ( MDS112[j]*coefS1MDS1[2]) + (MDS112b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2), sort111.index(MDS111[j])+1,(MDS111[j]>=10), creditS1MDS1[0], creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0 , MDS111cc[j]['note_cc'], MDS111sn[j]['note_sn']  ],

                [ MDS111b[j], coefS1MDS1[1], MDS111b[j]*coefS1MDS1[1], "MOYENNE", sort111b.index(MDS111b[j])+1,(MDS111b[j]>=10), creditS1MDS1[1], creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0, MDS111bcc[j]['note_cc'], MDS111bsn[j]['note_sn'] ],

                [ MDS112[j], coefS1MDS1[2], MDS112[j]*coefS1MDS1[2], "MOYENNE", sort112.index(MDS112[j])+1,(MDS112[j]>=10), creditS1MDS1[2], creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0 ,MDS112cc[j]['note_cc'], MDS112sn[j]['note_sn']],

                [ MDS112b[j], coefS1MDS1[3], MDS112b[j]*coefS1MDS1[3], "MOYENNE", sort112b.index(MDS112b[j])+1,(MDS112b[j]>=10), creditS1MDS1[3], creditS1MDS1[3] if((MDS112[j]+MDS112b[j])>=20) else 0, MDS112cc[j]['note_cc'], MDS112sn[j]['note_sn'] ],


                [ MDS113[j], coefS1MDS1[4], MDS113[j]*coefS1MDS1[4], 

                    round( ((MDS113[j]*coefS1MDS1[4]) + (MDS114[j]*coefS1MDS1[5]) + MDS115[j]*coefS1MDS1[6] + MDS116[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2), 
                    
                    sort113.index(MDS113[j])+1,
                    (MDS113[j]>=10), 

                    creditS1MDS1[4],
                     creditS1MDS1[4] if (MDS113[j]>=10) else 0,

                     MDS113cc[j]['note_cc'],
                     MDS113sn[j]['note_sn']
                ],

                [ MDS114[j], coefS1MDS1[5], MDS114[j]*coefS1MDS1[5], "MOYENNE", sort114.index(MDS114[j])+1,(MDS114[j]>=10), creditS1MDS1[5], creditS1MDS1[5] if (MDS114[j]>=10) else 0, MDS114cc[j]['note_cc'], MDS114sn[j]['note_sn'] ],

                [ MDS115[j], coefS1MDS1[6], MDS115[j]*coefS1MDS1[6], "MOYENNE", sort115.index(MDS115[j])+1,(MDS115[j]>=10), creditS1MDS1[6], creditS1MDS1[6] if (MDS115[j]>=10) else 0, MDS115cc[j]['note_cc'], MDS115sn[j]['note_sn'] ],

                [ MDS116[j], coefS1MDS1[7], MDS116[j]*coefS1MDS1[7], "MOYENNE", sort116.index(MDS116[j])+1,(MDS116[j]>=10), creditS1MDS1[7], creditS1MDS1[7] if (MDS116[j]>=10) else 0, MDS116cc[j]['note_cc'], MDS116sn[j]['note_sn'] ],


                [ MDS117[j], coefS1MDS1[8], MDS117[j]*coefS1MDS1[8], 
                
                round(( MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2), 
                    sort117.index(MDS117[j])+1,
                    (MDS117[j]>=10), 

                    creditS1MDS1[8],
                     creditS1MDS1[8] if (MDS117[j]>=10) else 0,

                     MDS117cc[j]['note_cc'],
                     MDS117sn[j]['note_sn']

                ],

                [ MDS117b[j], coefS1MDS1[9], MDS117b[j]*coefS1MDS1[9], "MOYENNE", sort117b.index(MDS117b[j])+1,(MDS117b[j]>=10), creditS1MDS1[9], creditS1MDS1[9] if ( (MDS117b[j]+MDS117[j]) >=20) else 0, MDS117bcc[j]['note_cc'], MDS117bsn[j]['note_sn'] ],

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
    
    #STATS VALIDATION
    for i in range (len(MDS111)):
        if MDS111[i] >= 10:
            val1['nombre']+=1
    val1['pourcentage']= round(((val1['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS111b)):
        if MDS111b[i] >= 10:
            val2['nombre']+=1
    val2['pourcentage']= round(((val2['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS112)):
        if MDS112[i] >= 10:
            val3['nombre']+=1
    val3['pourcentage']= round(((val3['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS112b)):
        if MDS112b[i] >= 10:
            val4['nombre']+=1
    val4['pourcentage']= round(((val4['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS113)):
        if MDS113[i] >= 10:
            val5['nombre']+=1
    val5['pourcentage']= round(((val5['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS114)):
        if MDS114[i] >= 10:
            val6['nombre']+=1
    val6['pourcentage']= round(((val6['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS115)):
        if MDS115[i] >= 10:
            val7['nombre']+=1
    val7['pourcentage']= round(((val7['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS116)):
        if MDS116[i] >= 10:
            val8['nombre']+=1
    val8['pourcentage']= round(((val8['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS117)):
        if MDS117[i] >= 10:
            val9['nombre']+=1
    val9['pourcentage']= round(((val9['nombre']/ len(infoEtudiantMDS))*100), 2)
    for i in range (len(MDS117b)):
        if MDS117b[i] >= 10:
            val10['nombre']+=1
    val10['pourcentage']= round(((val10['nombre']/ len(infoEtudiantMDS))*100), 2)


    #STATS MENTION
    statMention(MDS111,m111)
    pourcentageMention(m111, len(infoEtudiantMDS))

    statMention(MDS111b,m111b)
    pourcentageMention(m111b, len(infoEtudiantMDS))

    statMention(MDS112,m112)
    pourcentageMention(m112, len(infoEtudiantMDS))

    statMention(MDS112b,m112b)
    pourcentageMention(m112b, len(infoEtudiantMDS))

    statMention(MDS113,m113)
    pourcentageMention(m113, len(infoEtudiantMDS))

    statMention(MDS114,m114)
    pourcentageMention(m114, len(infoEtudiantMDS))

    statMention(MDS115,m115)
    pourcentageMention(m115, len(infoEtudiantMDS))

    statMention(MDS116,m116)
    pourcentageMention(m116, len(infoEtudiantMDS))

    statMention(MDS117,m117)
    pourcentageMention(m117, len(infoEtudiantMDS))

    statMention(MDS117b,m117b)
    pourcentageMention(m117b, len(infoEtudiantMDS))



    UEStats = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
    UEstats_mention = [m111, m111b, m112, m112b, m113, m114, m115, m116, m117, m117b]


    semestre1MDS = [filiere, listeMatrice, mds1Moyenne, moy, session, creditS1MDS1, UEStats, UEstats_mention] #filiere, listeMatrice, staps1Moyenne, moy, session

    return render(request, 'bulletin/releveCommun/releveCommuns2mds.html', {'semestre1MDS': semestre1MDS})
##########################################################################################################################################################################################################################################################################
#PV EPS2 SEMESTRE3
def resultatCommunstaps2(request):

    filiere = ["STAPS2"]

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=2).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=3,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = epurationCoef(coefS1STAPS1)

    creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=3,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS1 = epurationCre(creditS1STAPS1)


    val1 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val2 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val3 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val4 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val5 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val6 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val7 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val8 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val9 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val10 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val11 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val12 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val13 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val14 = {
        'nombre': 0,
        'pourcentage': 0,
    }


    e111 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e112 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e113= {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e114 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115a = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115b = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115f = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115g = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115j = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115l = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e116 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e117 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e118 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e119 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }


    EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=62).values('note_Examen'))
    EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=62).values('note_cc'))
    EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=62).values('note_sn'))
    sort111 = epurationTriCroissant(EPS111)

    EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=63).values('note_Examen'))
    EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=63).values('note_cc'))
    EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=63).values('note_sn'))
    sort112 = epurationTriCroissant(EPS112)

    EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=64).values('note_Examen'))
    EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=64).values('note_cc'))
    EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=64).values('note_sn'))
    sort113 = epurationTriCroissant(EPS113)

    EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=65).values('note_Examen'))
    EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=65).values('note_cc'))
    EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=65).values('note_sn'))
    sort114 = epurationTriCroissant(EPS114)

    EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=66).values('note_Examen'))
    EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=66).values('note_cc'))
    EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=66).values('note_sn'))
    sort115a = epurationTriCroissant(EPS115a)

    EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=67).values('note_Examen'))
    EPS115bcc = list(Evaluation.objects.filter(uniteEnseignement_id=67).values('note_cc'))
    EPS115bsn = list(Evaluation.objects.filter(uniteEnseignement_id=67).values('note_sn'))
    sort115b = epurationTriCroissant(EPS115b) 

    EPS115f = list(Evaluation.objects.filter(uniteEnseignement_id=68).values('note_Examen'))
    EPS115fcc = list(Evaluation.objects.filter(uniteEnseignement_id=68).values('note_cc'))
    EPS115fsn = list(Evaluation.objects.filter(uniteEnseignement_id=68).values('note_sn'))
    sort115f = epurationTriCroissant(EPS115f)

    EPS115g = list(Evaluation.objects.filter(uniteEnseignement_id=69).values('note_Examen'))
    EPS115gcc = list(Evaluation.objects.filter(uniteEnseignement_id=69).values('note_cc'))
    EPS115gsn = list(Evaluation.objects.filter(uniteEnseignement_id=69).values('note_sn'))
    sort115g = epurationTriCroissant(EPS115g)

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=70).values('note_Examen'))
    EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=70).values('note_cc'))
    EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=70).values('note_sn'))
    sort115j = epurationTriCroissant(EPS115j)

    EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=71).values('note_Examen')) 
    EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=71).values('note_cc'))
    EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=71).values('note_sn'))
    sort115l = epurationTriCroissant(EPS115l)

    EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=72).values('note_Examen'))
    EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=72).values('note_cc'))
    EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=72).values('note_sn'))
    sort116 = epurationTriCroissant(EPS116)

    EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=73).values('note_Examen'))
    EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=73).values('note_cc')) 
    EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=73).values('note_sn'))
    sort117 = epurationTriCroissant(EPS117)

    EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=74).values('note_Examen'))
    EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=74).values('note_cc'))
    EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=74).values('note_sn'))
    sort118 = epurationTriCroissant(EPS118)
    
    EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=75).values('note_Examen'))
    EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=75).values('note_cc'))
    EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=75).values('note_sn'))
    sort119 = epurationTriCroissant(EPS119)

    staps1Moyenne = []
    listeMatrice = []

    for j in range( len(infoEtudiantSTAPS1) ):

            matrice = [
                    infoEtudiantSTAPS1[j],

                    [ EPS111[j], coefS1STAPS1[0], EPS111[j]*coefS1STAPS1[0], round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1])) / (coefS1STAPS1[0]+coefS1STAPS1[1]), 2 ), sort111.index(EPS111[j])+1,(EPS111[j]>=10), creditS1STAPS1[0], creditS1STAPS1[0] if (EPS111[j]>=10) else 0, EPS111cc[j]['note_cc'], EPS111sn[j]['note_sn'] ],

                    [ EPS112[j], coefS1STAPS1[1], EPS112[j]*coefS1STAPS1[1], "MOYENNE", sort112.index(EPS112[j])+1,(EPS112[j]>=10), creditS1STAPS1[1], creditS1STAPS1[1] if (EPS112[j]>=10) else 0 , EPS112cc[j]['note_cc'], EPS112sn[j]['note_sn'] ],

                    [ EPS113[j], coefS1STAPS1[2], EPS113[j]*coefS1STAPS1[2], round(  ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5]) + (EPS115f[j]*coefS1STAPS1[6]) + (EPS115g[j]*coefS1STAPS1[7]) + (EPS115j[j]*coefS1STAPS1[8]) + (EPS115l[j]*coefS1STAPS1[9]) + (EPS116[j]*coefS1STAPS1[10]) ) / (coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]), 2 ), 
                    
                      sort113.index(EPS113[j])+1, 

                      (EPS113[j] >=10), 

                      creditS1STAPS1[2],
                      creditS1STAPS1[2] if (EPS113[j] >=10) else 0,

                      EPS113cc[j]['note_cc'], 
                      EPS113sn[j]['note_sn']
                    ],

                    [ EPS114[j],  coefS1STAPS1[3], EPS114[j]*coefS1STAPS1[3], "MOYENNE", sort114.index(EPS114[j])+1, (EPS114[j] >=10), creditS1STAPS1[3], creditS1STAPS1[3] if (EPS114[j] >=10) else 0, EPS114cc[j]['note_cc'], EPS114sn[j]['note_sn'] ],

                    [ EPS115a[j], coefS1STAPS1[4], EPS115a[j]*coefS1STAPS1[4], "MOYENNE", sort115a.index(EPS115a[j])+1, (EPS115a[j] >=10), creditS1STAPS1[4], creditS1STAPS1[4] if (EPS115a[j] >=10) else 0, EPS115acc[j]['note_cc'], EPS115asn[j]['note_sn'] ], #crédits

                    [ EPS115b[j], coefS1STAPS1[5], EPS115b[j]*coefS1STAPS1[5], "MOYENNE", sort115b.index(EPS115b[j])+1, (EPS115b[j] >=10), creditS1STAPS1[5], creditS1STAPS1[5] if (EPS115b[j] >=10) else 0, EPS115bcc[j]['note_cc'], EPS115bsn[j]['note_sn'] ],

                    [ EPS115f[j], coefS1STAPS1[6], EPS115f[j]*coefS1STAPS1[6], "MOYENNE", sort115f.index(EPS115f[j])+1, (EPS115f[j] >=10), creditS1STAPS1[6], creditS1STAPS1[6] if (EPS115f[j] >=10) else 0, EPS115fcc[j]['note_cc'], EPS115fsn[j]['note_sn'] ],

                    [ EPS115g[j], coefS1STAPS1[7], EPS115g[j]*coefS1STAPS1[7], "MOYENNE", sort115g.index(EPS115g[j])+1, (EPS115g[j] >=10), creditS1STAPS1[7], creditS1STAPS1[7] if (EPS115g[j] >=10) else 0, EPS115gcc[j]['note_cc'], EPS115gsn[j]['note_sn'] ],

                    [ EPS115j[j], coefS1STAPS1[8], EPS115j[j]*coefS1STAPS1[8], "MOYENNE", sort115j.index(EPS115j[j])+1, (EPS115j[j] >=10), creditS1STAPS1[8], creditS1STAPS1[8] if (EPS115j[j] >=10) else 0, EPS115jcc[j]['note_cc'], EPS115jsn[j]['note_sn'] ],

                    [ EPS115l[j], coefS1STAPS1[9], EPS115l[j]*coefS1STAPS1[9], "MOYENNE", sort115l.index(EPS115l[j])+1, (EPS115l[j] >=10), creditS1STAPS1[9], creditS1STAPS1[9] if ((EPS115a[j]+EPS115b[j]+EPS115f[j]+EPS115g[j]+EPS115j[j]+EPS115l[j])>=60) else 0, EPS115lcc[j]['note_cc'], EPS115lsn[j]['note_sn'] ],

                    [ EPS116[j],  coefS1STAPS1[10], EPS116[j]*coefS1STAPS1[10], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[10], creditS1STAPS1[10] if (EPS116[j] >=10) else 0, EPS116cc[j]['note_cc'], EPS116sn[j]['note_sn'] ],

                    
                    
                    [ EPS117[j],  coefS1STAPS1[11], EPS117[j]*coefS1STAPS1[11], 

                        round( ( (EPS117[j]*coefS1STAPS1[11]) + (EPS118[j]*coefS1STAPS1[12]) + (EPS119[j]*coefS1STAPS1[13]) ) / ( coefS1STAPS1[11]+coefS1STAPS1[12]+coefS1STAPS1[13]), 2 ),  

                        sort117.index(EPS117[j])+1, 

                        (EPS117[j] >=10), 

                        creditS1STAPS1[11],
                        creditS1STAPS1[11] if (EPS117[j] >=10) else 0,

                        EPS117cc[j]['note_cc'], EPS117sn[j]['note_sn']
                        
                    ],

                    [ EPS118[j],  coefS1STAPS1[12], EPS118[j]*coefS1STAPS1[12], "MOYENNE", sort118.index(EPS118[j])+1, (EPS118[j] >=10), creditS1STAPS1[12], creditS1STAPS1[12] if (EPS118[j] >=10) else 0, EPS118cc[j]['note_cc'], EPS118sn[j]['note_sn'] ],

                    [ EPS119[j],  coefS1STAPS1[13], EPS119[j]*coefS1STAPS1[13], "MOYENNE", sort119.index(EPS119[j])+1, (EPS119[j] >=10), creditS1STAPS1[13], creditS1STAPS1[13] if (EPS119[j] >=10) else 0, EPS119cc[j]['note_cc'], EPS119sn[j]['note_sn'] ],

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
    
    #STATS VALIDATION
    for i in range (len(EPS111)):
        if EPS111[i] >= 10:
            val1['nombre']+=1
    val1['pourcentage']= round(((val1['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS112)):
        if EPS112[i] >= 10:
            val2['nombre']+=1
    val2['pourcentage']= round(((val2['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS113)):
        if EPS113[i] >= 10:
            val3['nombre']+=1
    val3['pourcentage']= round(((val3['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS114)):
        if EPS114[i] >= 10:
            val4['nombre']+=1
    val4['pourcentage']= round(((val4['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115a)):
        if EPS115a[i] >= 10:
            val5['nombre']+=1
    val5['pourcentage']= round(((val5['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115b)):
        if EPS115b[i] >= 10:
            val6['nombre']+=1
    val6['pourcentage']= round(((val6['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS115f)):
        if EPS115f[i] >= 10:
            val13['nombre']+=1
    val13['pourcentage']= round(((val13['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115g)):
        if EPS115g[i] >= 10:
            val14['nombre']+=1
    val14['pourcentage']= round(((val14['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS115j)):
        if EPS115j[i] >= 10:
            val7['nombre']+=1
    val7['pourcentage']= round(((val7['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115l)):
        if EPS115l[i] >= 10:
            val8['nombre']+=1
    val8['pourcentage']= round(((val8['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS116)):
        if EPS116[i] >= 10:
            val9['nombre']+=1
    val9['pourcentage']= round(((val9['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS117)):
        if EPS117[i] >= 10:
            val10['nombre']+=1
    val10['pourcentage']= round(((val10['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS118)):
        if EPS118[i] >= 10:
            val11['nombre']+=1
    val11['pourcentage']= round(((val11['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS119)):
        if EPS119[i] >= 10:
            val12['nombre']+=1
    val12['pourcentage']= round(((val12['nombre']/ len(infoEtudiantSTAPS1))*100), 2)


    #STATS MENTION
    statMention(EPS111,e111)
    pourcentageMention(e111, len(infoEtudiantSTAPS1))

    statMention(EPS112,e112)
    pourcentageMention(e112, len(infoEtudiantSTAPS1))

    statMention(EPS113,e113)
    pourcentageMention(e113, len(infoEtudiantSTAPS1))

    statMention(EPS114,e114)
    pourcentageMention(e114, len(infoEtudiantSTAPS1))

    statMention(EPS115a,e115a)
    pourcentageMention(e115a, len(infoEtudiantSTAPS1))

    statMention(EPS115b,e115b)
    pourcentageMention(e115b, len(infoEtudiantSTAPS1))

    statMention(EPS115f,e115f)
    pourcentageMention(e115f, len(infoEtudiantSTAPS1))

    statMention(EPS115g,e115g)
    pourcentageMention(e115g, len(infoEtudiantSTAPS1))

    statMention(EPS115j,e115j)
    pourcentageMention(e115j, len(infoEtudiantSTAPS1))

    statMention(EPS115l,e115l)
    pourcentageMention(e115l, len(infoEtudiantSTAPS1))

    statMention(EPS116,e116)
    pourcentageMention(e116, len(infoEtudiantSTAPS1))

    statMention(EPS117,e117)
    pourcentageMention(e117, len(infoEtudiantSTAPS1))

    statMention(EPS118,e118)
    pourcentageMention(e118, len(infoEtudiantSTAPS1))

    statMention(EPS119,e119)
    pourcentageMention(e119, len(infoEtudiantSTAPS1))

    UEStats = [val1, val2, val3, val4, val5, val6, val13, val14,  val7, val8, val9, val10, val11, val12]
    UEstats_mention = [e111, e112, e113, e114, e115a, e115b, e115f, e115g, e115j, e115l, e116, e117, e118, e119]

    semestre1MDS = [filiere , listeMatrice, staps1Moyenne, moy, session, creditS1STAPS1, UEStats, UEstats_mention ]


    return render(request, 'bulletin/releveCommun/releveCommunstaps2.html',{'semestre1MDS': semestre1MDS})

#PV EPS2 SEMESTRE4
def resultatCommuns4staps2(request):

    filiere = ["STAPS2"]

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=2).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = epurationCoef(coefS1STAPS1)

    creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS1 = epurationCre(creditS1STAPS1)

    intitule_UE = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("intitule_UE"))
    code_UE = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("code_UE"))


    val1 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val2 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val3 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val4 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val5 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val6 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val7 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val8 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val9 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val10 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val11 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val12 = {
        'nombre': 0,
        'pourcentage': 0,
    }

    e111 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e112 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e113= {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e114 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115a = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115f = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115g = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e115j = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e116 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e117 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e118 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e119 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }

    EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=112).values('note_Examen'))
    EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=112).values('note_cc'))
    EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=112).values('note_sn'))
    sort111 = epurationTriCroissant(EPS111)

    EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=113).values('note_Examen'))
    EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=113).values('note_cc'))
    EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=113).values('note_sn'))
    sort115a = epurationTriCroissant(EPS115a)

    EPS115f = list(Evaluation.objects.filter(uniteEnseignement_id=114).values('note_Examen'))
    EPS115fcc = list(Evaluation.objects.filter(uniteEnseignement_id=114).values('note_cc'))
    EPS115fsn = list(Evaluation.objects.filter(uniteEnseignement_id=114).values('note_sn'))
    sort115f = epurationTriCroissant(EPS115f)

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=115).values('note_Examen'))
    EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=115).values('note_cc'))
    EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=115).values('note_sn'))
    sort115j = epurationTriCroissant(EPS115j) 

    EPS115g = list(Evaluation.objects.filter(uniteEnseignement_id=116).values('note_Examen'))
    EPS115gcc = list(Evaluation.objects.filter(uniteEnseignement_id=116).values('note_cc'))
    EPS115gsn = list(Evaluation.objects.filter(uniteEnseignement_id=116).values('note_sn'))
    sort115g = epurationTriCroissant(EPS115g)


    EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=117).values('note_Examen'))
    EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=117).values('note_cc'))
    EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=117).values('note_sn'))
    sort112 = epurationTriCroissant(EPS112)

    EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=118).values('note_Examen'))
    EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=118).values('note_cc'))
    EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=118).values('note_sn'))
    sort113 = epurationTriCroissant(EPS113)

    EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=119).values('note_Examen'))
    EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=119).values('note_cc'))
    EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=119).values('note_sn'))
    sort114 = epurationTriCroissant(EPS114)

    
    EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=120).values('note_Examen'))
    EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=120).values('note_cc'))
    EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=120).values('note_sn'))
    sort116 = epurationTriCroissant(EPS116)

    EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=121).values('note_Examen')) 
    EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=121).values('note_cc'))
    EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=121).values('note_sn'))
    sort117 = epurationTriCroissant(EPS117)

    EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=122).values('note_Examen'))
    EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=122).values('note_cc'))
    EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=122).values('note_sn'))
    sort118 = epurationTriCroissant(EPS118)

    EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=123).values('note_Examen'))
    EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=123).values('note_cc')) 
    EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=123).values('note_sn'))
    sort119 = epurationTriCroissant(EPS119)

    staps1Moyenne = []
    listeMatrice = []

    for j in range( len(infoEtudiantSTAPS1) ):

            matrice = [
                    infoEtudiantSTAPS1[j],

                    #STAGE-PROFESSIONNEL
                    [ EPS111[j], coefS1STAPS1[0], EPS111[j]*coefS1STAPS1[0], "MOYENNE", sort111.index(EPS111[j])+1,(EPS111[j]>=10), creditS1STAPS1[0], creditS1STAPS1[0] if (EPS111[j]>=10) else 0, EPS111cc[j]['note_cc'], EPS111sn[j]['note_sn'] ],

                    #DIDACTIQUE DES APS
                    [ EPS115a[j], coefS1STAPS1[1], EPS115a[j]*coefS1STAPS1[1], "MOYENNE", sort115a.index(EPS115a[j])+1, (EPS115a[j] >=10), creditS1STAPS1[1], creditS1STAPS1[1] if (EPS115a[j] >=10) else 0, EPS115acc[j]['note_cc'], EPS115asn[j]['note_sn'] ], 

                    [ EPS115f[j], coefS1STAPS1[2], EPS115f[j]*coefS1STAPS1[2], "MOYENNE", sort115f.index(EPS115f[j])+1, (EPS115f[j] >=10), creditS1STAPS1[2], creditS1STAPS1[2] if (EPS115f[j] >=10) else 0, EPS115fcc[j]['note_cc'], EPS115fsn[j]['note_sn'] ],

                    [ EPS115j[j], coefS1STAPS1[3], EPS115j[j]*coefS1STAPS1[3], "MOYENNE", sort115j.index(EPS115j[j])+1, (EPS115j[j] >=10), creditS1STAPS1[3], creditS1STAPS1[3] if (EPS115j[j] >=10) else 0, EPS115jcc[j]['note_cc'], EPS115jsn[j]['note_sn'] ],

                    [ EPS115g[j], coefS1STAPS1[4], EPS115g[j]*coefS1STAPS1[4], 

                    round( (EPS115a[j]*coefS1STAPS1[1]+EPS115f[j]*coefS1STAPS1[2]+EPS115j[j]*coefS1STAPS1[3]+EPS115g[j]*coefS1STAPS1[4])/(coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]), 2 ), 
                    
                    sort115g.index(EPS115g[j])+1, (EPS115g[j] >=10), creditS1STAPS1[4], creditS1STAPS1[4] if ( (EPS115a[j]+EPS115f[j]+EPS115j[j]+EPS115g[j]) >=40) else 0, EPS115gcc[j]['note_cc'], EPS115gsn[j]['note_sn'] 

                    ],

                    #ANATOMIE
                    [ EPS112[j], coefS1STAPS1[5], EPS112[j]*coefS1STAPS1[5], "MOYENNE", sort112.index(EPS112[j])+1, (EPS112[j]>=10), creditS1STAPS1[5], creditS1STAPS1[5] if (EPS112[j]>=10) else 0 , EPS112cc[j]['note_cc'], EPS112sn[j]['note_sn'] ],

                    #PHYSIOLOGIE
                    [ EPS113[j], coefS1STAPS1[6], EPS113[j]*coefS1STAPS1[6], "MOYENNE", sort113.index(EPS113[j])+1, (EPS113[j] >=10), creditS1STAPS1[6], creditS1STAPS1[6] if (EPS113[j] >=10) else 0, EPS113cc[j]['note_cc'], EPS113sn[j]['note_sn'] ],

                    #EDUCATION PHYSIQUE : LOISIRS II
                    [ EPS114[j],  coefS1STAPS1[7], EPS114[j]*coefS1STAPS1[7], "MOYENNE", sort114.index(EPS114[j])+1, (EPS114[j] >=10), creditS1STAPS1[7], creditS1STAPS1[7] if (EPS114[j] >=10) else 0, EPS114cc[j]['note_cc'], EPS114sn[j]['note_sn'] ],

                    #TRAUMATOLOGIE - PREMIERS SECOURS
                    [ EPS116[j],  coefS1STAPS1[8], EPS116[j]*coefS1STAPS1[8], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[8], creditS1STAPS1[8] if (EPS116[j] >=10) else 0, EPS116cc[j]['note_cc'], EPS116sn[j]['note_sn'] ],

                    #PEDAGOGIE PRATIQUE III
                    [ EPS117[j],  coefS1STAPS1[9], EPS117[j]*coefS1STAPS1[9], 

                        round( (EPS111[j]*coefS1STAPS1[0]+EPS115a[j]*coefS1STAPS1[1]+EPS115f[j]*coefS1STAPS1[2]+EPS115j[j]*coefS1STAPS1[3]+EPS115g[j]*coefS1STAPS1[4]+EPS112[j]*coefS1STAPS1[5]+EPS113[j]*coefS1STAPS1[6]+EPS114[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9])/(coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]), 2),
                        
                        sort117.index(EPS117[j])+1, 

                        (EPS117[j] >=10), 

                        creditS1STAPS1[9], 

                        creditS1STAPS1[9] if (EPS117[j] >=10) else 0,

                        EPS117cc[j]['note_cc'], 

                        EPS117sn[j]['note_sn'] 
                    ],

                    #ECONOMIE  
                    [ EPS118[j],  coefS1STAPS1[10], EPS118[j]*coefS1STAPS1[10], 

                        "MOYENNE", 

                        sort118.index(EPS118[j])+1, 

                        (EPS118[j] >=10), 

                        creditS1STAPS1[10], 

                        creditS1STAPS1[10] if (EPS118[j] >=10) else 0, 

                        EPS118cc[j]['note_cc'], 

                        EPS118sn[j]['note_sn'] 
                    ],

                    #FRANCAIS
                    [ EPS119[j],  coefS1STAPS1[11], EPS119[j]*coefS1STAPS1[11], 

                        round( (EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11]) / (coefS1STAPS1[10]+coefS1STAPS1[11]) ,2), #"MOYENNE",

                        sort119.index(EPS119[j])+1, 

                        (EPS119[j] >=10), 

                        creditS1STAPS1[11], creditS1STAPS1[11] if (EPS119[j] >=10) else 0, 

                        EPS119cc[j]['note_cc'], 

                        EPS119sn[j]['note_sn'] 
                    ],

                    
                    #SOMME
                    [ 
                        ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 
                    
                    round( EPS111[j]*coefS1STAPS1[0]+EPS115a[j]*coefS1STAPS1[1]+EPS115f[j]*coefS1STAPS1[2]+EPS115j[j]*coefS1STAPS1[3]+EPS115g[j]*coefS1STAPS1[4]+EPS112[j]*coefS1STAPS1[5]+EPS113[j]*coefS1STAPS1[6]+EPS114[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11] ,2), 

                    round(( EPS111[j]*coefS1STAPS1[0]+EPS115a[j]*coefS1STAPS1[1]+EPS115f[j]*coefS1STAPS1[2]+EPS115j[j]*coefS1STAPS1[3]+EPS115g[j]*coefS1STAPS1[4]+EPS112[j]*coefS1STAPS1[5]+EPS113[j]*coefS1STAPS1[6]+EPS114[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2), #moyenne
                        
                        4,

                        5
                    ]
            ]
            
            listeMatrice.append(matrice)

            staps1Moyenne.append(matrice[13][2])
            staps1Moyenne.sort(reverse=True)

            moy = stat.mean(staps1Moyenne)
            moy = round(moy, 2)
            session = 'Mai 2023'
    
    #STATS VALIDATION
    for i in range (len(EPS111)):
        if EPS111[i] >= 10:
            val1['nombre']+=1
    val1['pourcentage']= round(((val1['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS115a)):
        if EPS115a[i] >= 10:
            val2['nombre']+=1
    val2['pourcentage']= round(((val2['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS115f)):
        if EPS115f[i] >= 10:
            val3['nombre']+=1
    val3['pourcentage']= round(((val3['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS115j)):
        if EPS115j[i] >= 10:
            val4['nombre']+=1
    val4['pourcentage']= round(((val4['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    
    for i in range (len(EPS115g)):
        if EPS115g[i] >= 10:
            val5['nombre']+=1
    val5['pourcentage']= round(((val5['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS112)):
        if EPS112[i] >= 10:
            val6['nombre']+=1
    val6['pourcentage']= round(((val6['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS113)):
        if EPS113[i] >= 10:
            val7['nombre']+=1
    val7['pourcentage']= round(((val7['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS114)):
        if EPS114[i] >= 10:
            val8['nombre']+=1
    val8['pourcentage']= round(((val8['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS116)):
        if EPS116[i] >= 10:
            val9['nombre']+=1
    val9['pourcentage']= round(((val9['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS117)):
        if EPS117[i] >= 10:
            val10['nombre']+=1
    val10['pourcentage']= round(((val10['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS118)):
        if EPS118[i] >= 10:
            val11['nombre']+=1
    val11['pourcentage']= round(((val11['nombre']/ len(infoEtudiantSTAPS1))*100), 2)

    for i in range (len(EPS119)):
        if EPS119[i] >= 10:
            val12['nombre']+=1
    val12['pourcentage']= round(((val12['nombre']/ len(infoEtudiantSTAPS1))*100), 2)


    #STATS MENTION
    statMention(EPS111,e111)
    pourcentageMention(e111, len(infoEtudiantSTAPS1))

    statMention(EPS115a,e115a)
    pourcentageMention(e115a, len(infoEtudiantSTAPS1))

    statMention(EPS115f,e115f)
    pourcentageMention(e115f, len(infoEtudiantSTAPS1))

    statMention(EPS115j,e115j)
    pourcentageMention(e115j, len(infoEtudiantSTAPS1))

    statMention(EPS115g,e115g)
    pourcentageMention(e115g, len(infoEtudiantSTAPS1))

    statMention(EPS112,e112)
    pourcentageMention(e112, len(infoEtudiantSTAPS1))

    statMention(EPS113,e113)
    pourcentageMention(e113, len(infoEtudiantSTAPS1))

    statMention(EPS114,e114)
    pourcentageMention(e114, len(infoEtudiantSTAPS1))


    statMention(EPS116,e116)
    pourcentageMention(e116, len(infoEtudiantSTAPS1))

    statMention(EPS117,e117)
    pourcentageMention(e117, len(infoEtudiantSTAPS1))

    statMention(EPS118,e118)
    pourcentageMention(e118, len(infoEtudiantSTAPS1))

    statMention(EPS119,e119)
    pourcentageMention(e119, len(infoEtudiantSTAPS1))

    UEStats = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12]
    UEstats_mention = [e111, e115a, e115f, e115j, e115g, e112, e113, e114, e116, e117, e118, e119]

    semestre1MDS = [filiere , listeMatrice, staps1Moyenne, moy, session, creditS1STAPS1, UEStats, UEstats_mention, code_UE, intitule_UE ]


    return render(request, 'bulletin/releveCommun/releveCommuns2staps2.html', {'semestre1MDS': semestre1MDS})

##########################################################################################################################################################################################################################################################################
#PV EVE SEMESTRE5
def resultatCommunEve(request):

    filiere = 'EVE'

    infoEtudiantEVE = list( Etudiant.objects.filter(filiere="MAS", niveau=3, Specialite="EVENEMENTIEL").values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance','id'))
    
    coefS5EVE = list( UniteEnseignement.objects.filter(semestre_id=5,filiere="MAS").values("coefficient", "intitule_UE"))
    coefS5EVE = epurationCoef(coefS5EVE)

    creditS5EVE = list(UniteEnseignement.objects.filter(semestre_id=5,filiere="MAS").values("nombre_credit"))
    creditS5EVE = epurationCre(creditS5EVE)


    val1 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val2 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val3 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val4 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val5 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val6 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    

    m315 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m325 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m335 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    m345 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e355 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }
    e365 = {
        'Très Bien': 0,
        'Bien': 0,
        'Assez Bien': 0,
        'Passable': 0,
        'Ccnf': 0,
        'Echec':0,

        'pourcentageTB': 0,
        'pourcentageB': 0,
        'pourcentageAB': 0,
        'pourcentageP': 0,
        'pourcentageCc': 0,
        'pourcentageEc': 0,
    }


    MAS315 = list(Evaluation.objects.filter(uniteEnseignement_id=76).values('note_Examen'))
    MAS315cc = list(Evaluation.objects.filter(uniteEnseignement_id=76).values('note_cc'))
    MAS315sn = list(Evaluation.objects.filter(uniteEnseignement_id=76).values('note_sn'))
    sort315 = epurationTriCroissant(MAS315)

    MAS325 = list(Evaluation.objects.filter(uniteEnseignement_id=77).values('note_Examen'))
    MAS325cc = list(Evaluation.objects.filter(uniteEnseignement_id=77).values('note_cc'))
    MAS325sn = list(Evaluation.objects.filter(uniteEnseignement_id=77).values('note_sn'))
    sort325 = epurationTriCroissant(MAS325)

    MAS335 = list(Evaluation.objects.filter(uniteEnseignement_id=78).values('note_Examen'))
    MAS335cc = list(Evaluation.objects.filter(uniteEnseignement_id=78).values('note_cc'))
    MAS335sn = list(Evaluation.objects.filter(uniteEnseignement_id=78).values('note_sn'))
    sort335 = epurationTriCroissant(MAS335)

    MAS345 = list(Evaluation.objects.filter(uniteEnseignement_id=79).values('note_Examen'))
    MAS345cc = list(Evaluation.objects.filter(uniteEnseignement_id=79).values('note_cc'))
    MAS345sn = list(Evaluation.objects.filter(uniteEnseignement_id=79).values('note_sn'))
    sort345 = epurationTriCroissant(MAS345)

    EVE355 = list(Evaluation.objects.filter(uniteEnseignement_id=80).values('note_Examen'))
    EVE355cc = list(Evaluation.objects.filter(uniteEnseignement_id=80).values('note_cc'))
    EVE355sn = list(Evaluation.objects.filter(uniteEnseignement_id=80).values('note_sn'))
    sort355 = epurationTriCroissant(EVE355)

    EVE365 = list(Evaluation.objects.filter(uniteEnseignement_id=81, note_rattrapage=None).values('note_Examen'))
    EVE365cc = list(Evaluation.objects.filter(uniteEnseignement_id=81).values('note_cc'))
    EVE365sn = list(Evaluation.objects.filter(uniteEnseignement_id=81).values('note_sn'))
    sort365 = epurationTriCroissant(EVE365)

    #########################################################################################
    #RATTRAPAGE
    infoMAS315R = ""
    MAS315R = list(Evaluation.objects.filter(uniteEnseignement_id=76, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))

    infoMAS325R = ""
    MAS325R = list(Evaluation.objects.filter(uniteEnseignement_id=77, note_Examen=0, note_cc=0, note_sn=0).values('note_rattrapage'))
    #sort325 = epurationTriCroissant(MAS325)

    infoMAS335R =""
    MAS335R = list(Evaluation.objects.filter(uniteEnseignement_id=78, note_Examen=0, note_cc=0, note_sn=0).values('note_rattrapage'))
    #sort335 = epurationTriCroissant(MAS335)

    infoMAS345R =""
    MAS345R = list(Evaluation.objects.filter(uniteEnseignement_id=79, note_Examen=0, note_cc=0, note_sn=0).values('note_rattrapage'))
    #sort345 = epurationTriCroissant(MAS345)

    infoEVE355R = ""
    EVE355R = list(Evaluation.objects.filter(uniteEnseignement_id=80, note_Examen=0, note_cc=0, note_sn=0).values('note_rattrapage'))
    #sort355 = epurationTriCroissant(EVE355)

    infoEVE365R = ""
    EVE365R = list(Evaluation.objects.filter(uniteEnseignement_id=81, note_Examen=0, note_cc=0, note_sn=0).values('note_rattrapage'))
    #sort365 = epurationTriCroissant(EVE365)


    listeMatrice = []
    EVEMoyenne = []

    for j in range( len(infoEtudiantEVE) ):

        matrice = [
            
            infoEtudiantEVE[j],

            [ MAS315[j], coefS5EVE[0], round(MAS315[j]*coefS5EVE[0], 2),

                round( ((MAS315[j]*coefS5EVE[0]) + (MAS325[j]*coefS5EVE[1]) + (MAS335[j]*coefS5EVE[2]) + (MAS345[j]*coefS5EVE[3])) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]), 2), 

                sort315.index(MAS315[j])+1, 

                (MAS315[j] >=10),

                creditS5EVE[0],

                creditS5EVE[0] if((MAS315[j] >=10)) else 0,#crédit obtenu

                MAS315cc[j]['note_cc'],

                MAS315sn[j]['note_sn'],

                #RATTRAPAGE
                MAS315R[j]['note_rattrapage']

            ],
            
            [ MAS325[j], coefS5EVE[1], round(MAS325[j]*coefS5EVE[1], 2), 'MOYENNE', sort325.index(MAS325[j])+1, (MAS325[j]>=10) ,creditS5EVE[1], creditS5EVE[1] if (MAS325[j]>=10) else 0, MAS325cc[j]['note_cc'],MAS325sn[j]['note_sn'],  ],
            
            [ MAS335[j], coefS5EVE[2], round(MAS335[j]*coefS5EVE[2], 2), 'MOYENNE', sort335.index(MAS335[j])+1, (MAS335[j]>=10), creditS5EVE[2], creditS5EVE[2] if (MAS335[j]>=10) else 0, MAS335cc[j]['note_cc'],MAS335sn[j]['note_sn'] ],
            
            [ MAS345[j], coefS5EVE[3], round(MAS345[j]*coefS5EVE[3], 2), 'MOYENNE', sort345.index(MAS345[j])+1, (MAS345[j]>=10), creditS5EVE[3], creditS5EVE[3] if (MAS345[j]>=10) else 0, MAS345cc[j]['note_cc'],MAS345sn[j]['note_sn'], [ MAS315[j], MAS325[j], MAS335[j], MAS345[j]], MAS345R[j] ],
            
            #MODULE 2
            [ EVE355[j], coefS5EVE[4], round(EVE355[j]*coefS5EVE[4], 2), 

                round((EVE355[j]*coefS5EVE[4] + EVE365[j]*coefS5EVE[5] )/(coefS5EVE[4]+coefS5EVE[5]), 2), 

                sort355.index(EVE355[j])+1, 

                (EVE355[j]>=10),

                creditS5EVE[4],
                creditS5EVE[4] if((EVE355[j]>=10)) else 0,

                EVE355cc[j]['note_cc'],
                EVE355sn[j]['note_sn'],

                EVE355R[j]['note_rattrapage']
            ],
            
            [ EVE365[j], coefS5EVE[5], round(EVE365[j]*coefS5EVE[5], 2), 'MOYENNE', sort365.index(EVE365[j])+1, (EVE365[j]>=10), creditS5EVE[5], creditS5EVE[5] if (EVE365[j]>=10) else 0, EVE365cc[j]['note_cc'],EVE365sn[j]['note_sn'], [ EVE355[j], EVE365[j] ], EVE365R[j] ],
        
            [ 
                (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),
    
                round( (MAS315[j]*coefS5EVE[0] + MAS325[j]*coefS5EVE[1] + MAS325[j]*coefS5EVE[2] + MAS345[j]*coefS5EVE[3]+EVE355[j]*coefS5EVE[4] + EVE365[j]*coefS5EVE[5] ), 2),

                round((MAS315[j]*coefS5EVE[0] + MAS325[j]*coefS5EVE[1] + MAS325[j]*coefS5EVE[2] + MAS345[j]*coefS5EVE[3]+EVE355[j]*coefS5EVE[4] + EVE365[j]*coefS5EVE[5])/(coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]), 2)
            ],
        
        ]

        """matriceR = [

            MAS315R[j], 

            MAS325R[j],

            MAS335R[j],

            MAS345R[j],

            EVE355R[j],

            EVE365R[j]
        ]"""

        creditObtenus = 0
        listeCredit = []
        #print(listeMatrice[1])
        #print(listeMatrice[])

        listeMatrice.append(matrice)
        EVEMoyenne.append(matrice[7][2])
        EVEMoyenne.sort(reverse=True)

        moy = stat.mean(EVEMoyenne)
        moy = round(moy, 2)
        session = ''

    #STATS VALIDATION
    for i in range (len(MAS315)):
        if MAS315[i] >= 10:
            val1['nombre']+=1
    val1['pourcentage']= round(((val1['nombre']/ len(infoEtudiantEVE))*100), 2) #round(2,(val1['nombre']/ len(infoEtudiantEVE))*100)
    for i in range (len(MAS325)):
        if MAS325[i] >= 10:
            val2['nombre']+=1
    val2['pourcentage']= round(((val2['nombre']/ len(infoEtudiantEVE))*100),2)
    for i in range (len(MAS335)):
        if MAS335[i] >= 10:
            val3['nombre']+=1
    val3['pourcentage']= round(((val3['nombre']/ len(infoEtudiantEVE))*100),2)
    for i in range (len(MAS345)):
        if MAS345[i] >= 10:
            val4['nombre']+=1
    val4['pourcentage']= round(((val4['nombre']/ len(infoEtudiantEVE))*100),2)
    for i in range (len(EVE355)):
        if EVE355[i] >= 10:
            val5['nombre']+=1
    val5['pourcentage']= round(((val5['nombre']/ len(infoEtudiantEVE))*100),2)
    for i in range (len(EVE365)):
        if EVE365[i] >= 10:
            val6['nombre']+=1
    val6['pourcentage']= round(((val6['nombre']/ len(infoEtudiantEVE))*100),2)
    
    #STATS VALIDATION RATTRAPAGE
    for i in range (len(MAS315R)):
        if MAS315[i] >= 10:
            val1['nombre']+=1
    val1['pourcentage']= round(((val1['nombre']/ len(infoEtudiantEVE))*100), 2) #round(2,(val1['nombre']/ len(infoEtudiantEVE))*100)

    #STAT MENTION
    statMention(MAS315,m315)
    pourcentageMention(m315, len(infoEtudiantEVE))

    statMention(MAS325,m325)
    pourcentageMention(m325, len(infoEtudiantEVE))

    statMention(MAS335,m335)
    pourcentageMention(m335, len(infoEtudiantEVE))

    statMention(MAS345,m345)
    pourcentageMention(m345, len(infoEtudiantEVE))

    statMention(EVE355,e355)
    pourcentageMention(e355, len(infoEtudiantEVE))

    statMention(EVE365,e365)
    pourcentageMention(e365, len(infoEtudiantEVE))

    UEStats = [val1, val2, val3, val4, val5, val6]
    UEstats_mention = [m315, m325, m335, m345, e355, e365]

    semestre1MDS = [filiere, listeMatrice, EVEMoyenne, moy, session, creditS5EVE, UEStats, UEstats_mention]

    return render(request, 'bulletin/releveCommun/releveCommunEve.html', {'semestre1MDS': semestre1MDS})

#PV EVE SEMESTRE6
def resultatCommuns6Eve(request):

    return render(request, 'bulletin/releveCommun/releveCommunEve.html') #, {'semestre1MDS': semestre1MDS}

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

        for i in range(len(key)):
            
            setKey = key[i]
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

def saveDataR(key, value):

    if (len(key) == len(value)):

        for i in range(len(key)):

            print(key) 

            setKey = key[i]
        
            natureEvaluation = "RATTRAPAGE"
            matricule = setKey[1]
            codeUe = setKey[2]
            note_rattrapage = value[i]
            note_rattrapage = float("{:.2f}".format(note_rattrapage))


            etudiant_Query = Etudiant.objects.filter(matricule=matricule)
            etudiant = etudiant_Query[0]

            ue_Query = UniteEnseignement.objects.filter(code_UE=codeUe)#.values('id')
            ue = ue_Query[0]

            date_Rattrapage = "2023-05-29"

            evaluation = Evaluation( natureEvaluation=natureEvaluation, note_cc=0, note_sn=0, etudiant=etudiant, note_Examen=0, uniteEnseignement=ue, note_rattrapage=note_rattrapage, date_Rattrapage=date_Rattrapage )
                
            #print(evaluation)
            #print("JE suis au charbon ++++++")

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

def extractR(a):
    key = list(a.keys())
    val = list(a.values())

    keys = epurationR(key)
    values = brokeR(val)

    print(keys)
    print(values)

    return (keys, values)


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

#RATTRAPAGE
def epurationR(a):
    keys = []
    for i in range(1,len(a)):
        k = a[i]
        a[i] = k.split()
        keys.append(a[i])
    return keys   
def brokeR(a):
    values=[]
    for i in range(1,len(a)):#décalage afin d'éviter la clé token du formulaire
        e = a[i]
        v = float((e))
        #a[i] = v
        values.append(v)
    return values
































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

def epurationRattrapage(b):
    for i in range(len(b)):
        tmp = b[i]["note_rattrapage"]
        b[i] = tmp

    #b.sort()
    return b

#STATS MENTION
def statMention(ue, uestat):
    for i in range(len(ue)):
        if ue[i]>= 16:
            uestat['Très Bien'] = uestat['Très Bien'] + 1
        if ( ue[i] >= 14 and ue[i] < 16 ):
            uestat['Bien'] = uestat['Bien'] + 1
        if ( ue[i] >= 12 and ue[i] < 14 ):
            uestat['Assez Bien'] = uestat['Assez Bien'] + 1
        if ( ue[i] >= 10 and ue[i] < 12 ):
            uestat['Passable'] = uestat['Passable'] + 1
        if ( ue[i] >= 7 and ue[i] < 10 ):
            uestat['Ccnf'] = uestat['Ccnf'] + 1
        if ( ue[i] >= 0 and ue[i] < 7 ):
            uestat['Echec'] = uestat['Echec'] + 1

def statValidation(ue, val):
    for i in range (len(ue)):
        if ue[i] >= 10:
            val+=1

def pourcentageMention(ue, b):
    ue['pourcentageTB'] = round( ((ue['Très Bien']/b)*100), 2)
    ue['pourcentageB'] = round( ((ue['Bien']/b)*100), 2)
    ue['pourcentageAB'] = round( ((ue['Assez Bien']/b)*100), 2)
    ue['pourcentageP'] = round( ((ue['Passable']/b)*100), 2)
    ue['pourcentageCc'] = round( ((ue['Ccnf']/b)*100), 2)
    ue['pourcentageEc'] = round( ((ue['Echec']/b)*100), 2)


#TRANSFORMATION MATRICE INITALE, MATRICE RATTRAPAGE, MATRICE SYNTHESE
def Rattrapage(noteRattrapage):

    pass