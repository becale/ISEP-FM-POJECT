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
import copy
#import numpy as np

#Importation des modules de bulletin
from bulletin.view_bull_module.Eps1Mds1_S1 import  *


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

    s1 = list(UniteEnseignement.objects.filter(semestre_id=1).values())
    s3 = list(UniteEnseignement.objects.filter(semestre_id=3).values())
    #s5 = list(UniteEnseignement.objects.filter(semestre_id=5).values())
    ueSemestre135 = []
    ueSemestre135 += s1
    ueSemestre135 += s3
    #ueSemestre135 += s5
    #ueSemestre135.append(s1)
    #ueSemestre135.append(s3)
    #ueSemestre135.append(s5)

    s2 = list(UniteEnseignement.objects.filter(semestre_id=2).values())
    s4 = list(UniteEnseignement.objects.filter(semestre_id=4).values())
    #s6 = list(UniteEnseignement.objects.filter(semestre_id=6).values())
    ueSemestre246 = []
    ueSemestre246 += s2
    ueSemestre246 += s4
    #ueSemestre246 += s6
    #ueSemestre246.append(s2)
    #ueSemestre246.append(s4)
    #ueSemestre246.append(s6)

    mydata = []
    mydata += ueSemestre135
    mydata += ueSemestre246
    #mydata.append(ueSemestre135)
    #mydata.append(ueSemestre246)

    #mydata = list(UniteEnseignement.objects.all().values())

    return JsonResponse(mydata, safe=False)


############### API REQUETTES POST ###########################################################
def AddNoteEtudiant(request):
    if request.method == 'POST':
        data = request.POST

    key,values = extract(data)

    saveData(key,values)

    return JsonResponse(data, safe=False)

def ModifyNoteEtudiant(request):
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





###########################################################  REQUETES POUR BULLETIN SEMESTRE 1 3 5 | SEMESTRE 2 4 6 #############################################################
#EPS1 ET MDS1 SEMESTRE 1
def bulls1epsmds(request, filiere):

    if (filiere =='GESTION'):

###########################################################  SEMESTRE 1 MDS   ############################################################################################################################        
        infoEtudiantMDS =list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

        coefS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("coefficient", "intitule_UE"))
        coefS1MDS1 = epurationCoef(coefS1MDS1)

        creditS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("nombre_credit"))
        creditS1MDS1 = epurationCre(creditS1MDS1)

        MDS111 =list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='EXAMEN').values('note_cc'))
        MDS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='EXAMEN').values('note_sn'))
        sort111 = epurationTriCroissant(MDS111)

        MDS111b =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS111bcc =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='EXAMEN').values('note_cc'))
        MDS111bsn =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='EXAMEN').values('note_sn'))
        sort111b = epurationTriCroissant(MDS111b)

        MDS112 =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS112cc =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='EXAMEN').values('note_cc'))
        MDS112sn =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='EXAMEN').values('note_sn'))
        sort112 = epurationTriCroissant(MDS112)

        MDS112b =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS112bcc =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='EXAMEN').values('note_cc'))
        MDS112bsn =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='EXAMEN').values('note_sn'))
        sort112b = epurationTriCroissant(MDS112b)

        MDS113 =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS113cc =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='EXAMEN').values('note_cc'))
        MDS113sn =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='EXAMEN').values('note_sn'))
        sort113 = epurationTriCroissant(MDS113)

        MDS114 =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS114cc =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='EXAMEN').values('note_cc'))
        MDS114sn =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='EXAMEN').values('note_sn'))
        sort114 = epurationTriCroissant(MDS114)

        MDS115 =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS115cc =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='EXAMEN').values('note_cc'))
        MDS115sn =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='EXAMEN').values('note_sn'))
        sort115 = epurationTriCroissant(MDS115)

        MDS116 =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS116cc =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='EXAMEN').values('note_cc'))
        MDS116sn =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='EXAMEN').values('note_sn'))
        sort116 = epurationTriCroissant(MDS116)

        MDS117 =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS117cc =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='EXAMEN').values('note_cc'))
        MDS117sn =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='EXAMEN').values('note_sn'))
        sort117 = epurationTriCroissant(MDS117)

        MDS117b =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS117bcc =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='EXAMEN').values('note_cc'))
        MDS117bsn =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='EXAMEN').values('note_sn'))
        sort117b = epurationTriCroissant(MDS117b)
        #print(sort117b)

        listeMatrice = []
        mds1Moyenne = []

        for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

            matrice = [
                infoEtudiantMDS[j],
                #1
                [ MDS111[j], coefS1MDS1[0], MDS111[j]*coefS1MDS1[0], round( ((MDS111[j]*coefS1MDS1[0]) + (MDS111b[j]*coefS1MDS1[1]) + ( MDS112[j]*coefS1MDS1[2]) + (MDS112b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2), sort111.index(MDS111[j])+1,(creditS1MDS1[0] if MDS111[j]>=10 else 0), creditS1MDS1[0] ],

                #2
                [ MDS111b[j], coefS1MDS1[1], MDS111b[j]*coefS1MDS1[1], "MOYENNE", sort111b.index(MDS111b[j])+1,(MDS111b[j]>=10), creditS1MDS1[1]],

                #3
                [ MDS112[j], coefS1MDS1[2], MDS112[j]*coefS1MDS1[2], "MOYENNE", sort112.index(MDS112[j])+1,(MDS112[j]>=10), creditS1MDS1[2]],

                #4
                [ MDS112b[j], coefS1MDS1[3], MDS112b[j]*coefS1MDS1[3], "MOYENNE", sort112b.index(MDS112b[j])+1,(MDS112b[j]>=10), creditS1MDS1[3]],

                #5
                [ MDS113[j], coefS1MDS1[4], MDS113[j]*coefS1MDS1[4], 

                round( ((MDS113[j]*coefS1MDS1[4]) + (MDS114[j]*coefS1MDS1[5]) + MDS115[j]*coefS1MDS1[6] + MDS116[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2), 
                
                sort113.index(MDS113[j])+1,
                (MDS113[j]>=10), 
                creditS1MDS1[4]],

                #6
                [ MDS114[j], coefS1MDS1[5], MDS114[j]*coefS1MDS1[5], "MOYENNE", sort114.index(MDS114[j])+1,(MDS114[j]>=10), creditS1MDS1[5]],

                #7
                [ MDS115[j], coefS1MDS1[6], MDS115[j]*coefS1MDS1[6], "MOYENNE", sort115.index(MDS115[j])+1,(MDS115[j]>=10), creditS1MDS1[6]],
                
                #8
                [ MDS116[j], coefS1MDS1[7], MDS116[j]*coefS1MDS1[7], "MOYENNE", sort116.index(MDS116[j])+1,(MDS116[j]>=10), creditS1MDS1[7]],

                #9
                [ MDS117[j], coefS1MDS1[8], MDS117[j]*coefS1MDS1[8], 
                
                round(( MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2), 
                sort117.index(MDS117[j])+1,
                (MDS117[j]>=10), 
                creditS1MDS1[8]],

                #10
                [ MDS117b[j], coefS1MDS1[9], MDS117b[j]*coefS1MDS1[9], "MOYENNE", sort117b.index(MDS117b[j])+1,(MDS117b[j]>=10), creditS1MDS1[9]],

                #11
                [
                    ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),

                   round (MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] , 2),

                   round (( MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                ]

            ]

            #Décompte du nombre de crédit
            MDSCreditCount(matrice)

            listeMatrice.append(matrice)
            mds1Moyenne.append(matrice[11][2])

            mds1Moyenne.sort(reverse=True)

            moy = stat.mean(mds1Moyenne)
            moy = round(moy, 2)
            session = 'Janvier 2023'

###########################################################  SEMESTRE 1 MDS RATTRAPAGE ############################################################################################################################
        MDS111R =list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort111R = epurationRattrapage(MDS111R)

        MDS111bR =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort111bR = epurationRattrapage(MDS111bR)

        MDS112R =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort112R = epurationRattrapage(MDS112R)

        MDS112bR =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort112bR = epurationRattrapage(MDS112bR)

        MDS113R =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort113R = epurationRattrapage(MDS113R)

        MDS114R =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort114R = epurationRattrapage(MDS114R)

        MDS115R =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort115R = epurationRattrapage(MDS115R)

        MDS116R =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort116R = epurationRattrapage(MDS116R)

        MDS117R =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort117R = epurationRattrapage(MDS117R)

        MDS117bR =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort117bR = epurationRattrapage(MDS117bR)

        #Liste matrice Rattrapage
        listeMatriceS1GesR = []
        matriceS1mdsR = [] 
        for j in range( len(infoEtudiantMDS) ):
            matriceS1mdsR = [
                    infoEtudiantMDS[j],

                    MDS111R[j],

                    MDS111bR[j],

                    MDS112R[j],

                    MDS112bR[j],

                    MDS113R[j],

                    MDS114R[j],

                    MDS115R[j],

                    MDS116R[j],

                    MDS117R[j],

                    MDS117bR[j],
            ]
            listeMatriceS1GesR.append(matriceS1mdsR)
        #Liste matrice CC
        listeMatrices1GesCC = []
        for j in range(len(infoEtudiantMDS)):
            matrices1GesCC = [

                infoEtudiantMDS[j],

                MDS111cc[j],

                MDS111bcc[j],

                MDS112cc[j],

                MDS112bcc[j],

                MDS113cc[j],

                MDS114cc[j],

                MDS115cc[j],

                MDS116cc[j],

                MDS117cc[j],

                MDS117bcc[j],

            ]
            listeMatrices1GesCC.append(matrices1GesCC)

###########################################################  SEMESTRE 1 MDS SYNTHESE   ############################################################################################################################
        listeMatriceSynthese = []
        mds1MoyenneSyn = []

        for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

            matriceS = [
                    infoEtudiantMDS[j],

                    [ 
                        ( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] )
                        , coefS1MDS1[0]
                        , (round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] ) * coefS1MDS1[0]
                        #, round( ((MDS111[j]*coefS1MDS1[0]) + (MDS111b[j]*coefS1MDS1[1]) + ( MDS112[j]*coefS1MDS1[2]) + (MDS112b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2)
                        , round( (( (round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] )*coefS1MDS1[0] ) + ( ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1]) + ( ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] )*coefS1MDS1[2]) + (( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] )*coefS1MDS1[3])) / (coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2)
                        #, sort111.index(MDS111[j])+1
                        , len(sort111)+1 if (listeMatriceS1GesR[j][1]> 0) else (sort111.index((round( listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111[j]))+1 )
                        #, (MDS111[j]>=10)
                        , ( ( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if ( listeMatriceS1GesR[j][1]> 0) else MDS111[j] ) >= 10 ) 
                        , creditS1MDS1[0]
                        #, creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0 
                        , creditS1MDS1[1] if ((( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] ) + ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] ) )>=20) else 0 
                        , 'Rattrapage' if (listeMatriceS1GesR[j][1]> 0)  else ''
                        #, MDS111cc[j]['note_cc']
                        #, MDS111sn[j]['note_sn']  
                    ],

                    [ 
                        #MDS111b[j]
                        ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] )
                        , coefS1MDS1[1]
                        #, MDS111b[j]*coefS1MDS1[1]
                        , ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1]
                        , "MOYENNE"
                        #, sort111b.index(MDS111b[j])+1
                        ,len(sort11b)+1 if (listeMatriceS1GesR[j][2]> 0) else (sort111b.index((round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j]))+1 )
                        #,(MDS111b[j]>=10)
                        , ((round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j])>=10)
                        , creditS1MDS1[1]
                        #, creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0
                        , creditS1MDS1[1] if ((( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j]) + (round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j]))>=20) else 0
                        , 'Rattrapage' if (listeMatriceS1GesR[j][2]> 0)  else ''
                        #, MDS111bcc[j]['note_cc']
                        #, MDS111bsn[j]['note_sn'] 
                    ],

                    [ 
                        #MDS112[j]
                        ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] )
                        , coefS1MDS1[2]
                        #, MDS112[j]*coefS1MDS1[2]
                        ,( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] )*coefS1MDS1[2]
                        , "MOYENNE"
                        , len(sort112)+1 if (listeMatriceS1GesR[j][3]> 0) else (sort112.index((round( listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j]))+1 )
                        #,(MDS112[j]>=10)
                        , ( ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] ) >= 10 )
                        , creditS1MDS1[2]
                        #, creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0 
                        , creditS1MDS1[1] if (( ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] ) + ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS112b[j] ) )>=20) else 0 
                        , 'Rattrapage' if (listeMatriceS1GesR[j][3]> 0)  else ''
                        #, MDS112cc[j]['note_cc']
                        #, MDS112sn[j]['note_sn']
                    ],

                    [ 
                        #MDS112b[j]
                        ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] )
                        , coefS1MDS1[3]
                        #, MDS112b[j]*coefS1MDS1[3]
                        , ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] )*coefS1MDS1[3]
                        , "MOYENNE"

                        , len(sort112b)+1 if (listeMatriceS1GesR[j][4]> 0) else (sort112b.index((round( listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j]))+1 )
                        #,(MDS112b[j]>=10)
                        , (( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] )>=10)
                        , creditS1MDS1[3]
                        #, creditS1MDS1[3] if((MDS112[j]+MDS112b[j])>=20) else 0
                        , creditS1MDS1[3] if((( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] ) + ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] ))>=20) else 0
                        , 'Rattrapage' if (listeMatriceS1GesR[j][4]> 0)  else ''
                        #, MDS112cc[j]['note_cc']
                        #, MDS112sn[j]['note_sn'] 
                    ],


                    [ 
                        #MDS113[j]
                        ( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] )
                        , coefS1MDS1[4]
                        #, MDS113[j]*coefS1MDS1[4] 
                        , ( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] )*coefS1MDS1[4]
                        #,round( ((MDS113[j]*coefS1MDS1[4]) + (MDS114[j]*coefS1MDS1[5]) + MDS115[j]*coefS1MDS1[6] + MDS116[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2)
                        , round( ((( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] )*coefS1MDS1[4]) + (( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] )*coefS1MDS1[5]) + ( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] )*coefS1MDS1[6] + ( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] )*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2)
                        ,len(sort113)+1 if (listeMatriceS1GesR[j][5]> 0) else (sort113.index((round( listeMatriceS1GesR[j][5]*0.7 + MDS1113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j]))+1 )
                        #,(MDS113[j]>=10)
                        , (( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] )>=10) 
                        ,creditS1MDS1[4]
                        #,creditS1MDS1[4] if (MDS113[j]>=10) else 0
                        , creditS1MDS1[4] if (( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] )>=10) else 0
                        , 'Rattrapage' if (listeMatriceS1GesR[j][5]> 0)  else ''
                        #,MDS113cc[j]['note_cc']
                        #,MDS113sn[j]['note_sn']
                    ],

                    [ 
                        #MDS114[j]
                        ( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] )
                    
                        , coefS1MDS1[5]
                        #, MDS114[j]*coefS1MDS1[5]
                        , ( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] )*coefS1MDS1[5]
                        , "MOYENNE"
                        #, sort114.index(MDS114[j])+1
                        ,len(sort114)+1 if (listeMatriceS1GesR[j][6]> 0) else (sort114.index((round( listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j]))+1 )
                        #, (MDS114[j]>=10)
                        , (( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] )>=10)
                        , creditS1MDS1[5]
                        #, creditS1MDS1[5] if (MDS114[j]>=10) else 0
                        , creditS1MDS1[5] if (( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] )>=10) else 0
                        , 'Rattrapage' if (listeMatriceS1GesR[j][6]> 0)  else ''
                        #, MDS114cc[j]['note_cc']
                        #, MDS114sn[j]['note_sn'] 
                    ],

                    [ 
                        #MDS115[j]
                        ( round(listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j])
                        , coefS1MDS1[6]
                        #, MDS115[j]*coefS1MDS1[6]
                        ,( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] )*coefS1MDS1[6]
                        , "MOYENNE"
                        , len(sort115)+1 if (listeMatriceS1GesR[j][7]> 0) else (sort115.index((round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j]))+1 )
                        #,(MDS115[j]>=10)
                        , ( ( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] )>=10 )
                        , creditS1MDS1[6]
                        #, creditS1MDS1[6] if (MDS115[j]>=10) else 0
                        , creditS1MDS1[6] if (( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] )>=10) else 0
                        , 'Rattrapage' if (listeMatriceS1GesR[j][7]> 0)  else ''
                        #, MDS115cc[j]['note_cc']
                        #, MDS115sn[j]['note_sn'] 
                    ],

                    [ 
                        #MDS116[j]
                        ( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] )
                        , coefS1MDS1[7]

                        #, MDS116[j]*coefS1MDS1[7]
                        , ( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] )*coefS1MDS1[7]
                        , "MOYENNE"

                        ,len(sort116)+1 if (listeMatriceS1GesR[j][8]> 0) else (sort116.index((round( listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j]))+1 )
                        #,(MDS116[j]>=10)
                        , (( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] )>=10)
                        , creditS1MDS1[7]
                        #, creditS1MDS1[7] if (MDS116[j]>=10) else 0
                        , creditS1MDS1[7] if (( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] )>=10) else 0
                        , 'Rattrapage' if (listeMatriceS1GesR[j][8]> 0)  else ''
                        #, MDS116cc[j]['note_cc']
                        #, MDS116sn[j]['note_sn'] 
                    ],


                    [ 
                        #MDS117[j]
                        ( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )
                        , coefS1MDS1[8]
                        #, MDS117[j]*coefS1MDS1[8]
                        ,( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )*coefS1MDS1[8]
                        #, round(( MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2) 
                        , round(( ( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )*coefS1MDS1[8] + ( ( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] ) )*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2)
                        #,sort117.index(MDS117[j])+1
                        , len(sort117)+1 if (listeMatriceS1GesR[j][9]> 0) else (sort117.index((round( listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j]))+1 )
                        #,(MDS117[j]>=10)
                        , (( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )>=10)
                        ,creditS1MDS1[8]
                        #,creditS1MDS1[8] if (MDS117[j]>=10) else 0
                        , creditS1MDS1[8] if (( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )>=10) else 0
                        , 'Rattrapage' if (listeMatriceS1GesR[j][9]> 0)  else ''
                        #,MDS117cc[j]['note_cc']
                        #,MDS117sn[j]['note_sn']
                    ],

                    [ 
                        #MDS117b[j]
                        ( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] )
                        , coefS1MDS1[9]
                        #, MDS117b[j]*coefS1MDS1[9]
                        , ( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] )*coefS1MDS1[9]
                        , "MOYENNE"
                        ,len(sort117b)+1 if (listeMatriceS1GesR[j][10]> 0) else (sort117b.index( (round( listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j]))+1 )
                        , (( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] )>=10)
                        , creditS1MDS1[9]
                        #, creditS1MDS1[9] if ( (MDS117b[j]+MDS117[j]) >=20) else 0
                        , creditS1MDS1[9] if ( (( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] )+( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )) >=20) else 0
                        , 'Rattrapage' if (listeMatriceS1GesR[j][10]> 0)  else ''
                        #, MDS117bcc[j]['note_cc']
                        #, MDS117bsn[j]['note_sn'] 
                    ],

                    [
                        ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),

                    #round (MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] , 2),

                    #round (( MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                    round ( ( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] ) *coefS1MDS1[0] + ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1] + ( ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] ) )*coefS1MDS1[2] + ( ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] ) )*coefS1MDS1[3] + ( ( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] ) )*coefS1MDS1[4] + ( ( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] ) )*coefS1MDS1[5] + ( ( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] ) )*coefS1MDS1[6] + ( ( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] ) )*coefS1MDS1[7] + ( ( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] ) )*coefS1MDS1[8] + ( ( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] ) )*coefS1MDS1[9] , 2),

                    round (( ( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] ) *coefS1MDS1[0] + ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1] + ( ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] ) )*coefS1MDS1[2] + ( ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] ) )*coefS1MDS1[3] + ( ( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] ) )*coefS1MDS1[4] + ( ( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] ) )*coefS1MDS1[5] + ( ( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] ) )*coefS1MDS1[6] + ( ( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] ) )*coefS1MDS1[7] + ( ( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] ))*coefS1MDS1[8] + ( ( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] ) )*coefS1MDS1[9] ) / ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                    ]
            ]
            #Décompte nombre crédit total
            MDSCreditCount(matriceS)

            listeMatriceSynthese.append(matriceS)
            mds1MoyenneSyn.append(matriceS[11][2])

            #Enregistrement des notes et crédits de Semestre1 en MDS1
            e_matri = infoEtudiantMDS[j]["matricule"]
            student = Etudiant.objects.get(matricule = e_matri)
            student.moyS1 = matriceS[11][2] 
            student.crS1 = matriceS[11][3]
            student.save()

        #listeMatricemdsS1Synthese, listeMoyenne = matriceSynthesemds1( listeMatrice, listeMatriceS1GesR, listeMatrice, listeMatrices1GesCC  )

        semestre1MDS = [filiere,  listeMatriceSynthese, mds1Moyenne,  moy, session , listeMatrice ]#, listeMatricemdsS1Synthese,  #listeMatrice ,  #infoEtudiantMDS, coefS1MDS1, creditS1MDS1, MDS111, MDS111b, MDS112, MDS112b, MDS113, MDS114, MDS115, MDS116, MDS117, MDS117b,


    elif (filiere == 'STAPS1'):

###########################################################  SEMESTRE 1 EPS   ############################################################################################################################               
        infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

        coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("coefficient"))
        coefS1STAPS1 = epurationCoef(coefS1STAPS1)

        creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("nombre_credit"))
        creditS1STAPS1 = epurationCre(creditS1STAPS1)

        EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN').values('note_cc'))
        EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN').values('note_sn'))
        sort111 = epurationTriCroissant(EPS111)

        EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='EXAMEN').values('note_cc'))
        EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='EXAMEN').values('note_sn'))
        sort112 = epurationTriCroissant(EPS112)

        EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='EXAMEN').values('note_cc'))
        EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='EXAMEN').values('note_sn'))
        sort113 = epurationTriCroissant(EPS113)

        EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN').values('note_cc'))
        EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN').values('note_sn'))
        sort114 = epurationTriCroissant(EPS114)

        EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN').values('note_cc'))
        EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN').values('note_sn'))
        sort115a = epurationTriCroissant(EPS115a)

        EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS115bcc = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN').values('note_cc'))
        EPS115bsn = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN').values('note_sn'))
        sort115b = epurationTriCroissant(EPS115b)

        EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN').values('note_cc'))
        EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN').values('note_sn'))
        sort115j = epurationTriCroissant(EPS115j)

        EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN').values('note_cc'))
        EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN').values('note_sn'))
        sort115l = epurationTriCroissant(EPS115l)

        EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN').values('note_cc'))
        EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN').values('note_sn'))
        sort116 = epurationTriCroissant(EPS116)

        EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='EXAMEN').values('note_cc'))
        EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='EXAMEN').values('note_sn'))
        sort117 = epurationTriCroissant(EPS117)

        EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN').values('note_cc'))
        EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN').values('note_sn'))
        sort118 = epurationTriCroissant(EPS118)

        EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN').values('note_cc'))
        EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN').values('note_sn'))
        sort119 = epurationTriCroissant(EPS119)

        student = {}
        temp = {}
        staps1 = []
        staps1Moyenne = []
        listeMatrice = [ ]

        for j in range( len(infoEtudiantSTAPS1) ):

            matrice = [
                    infoEtudiantSTAPS1[j],

                    [ 
                        EPS111[j]
                        , coefS1STAPS1[0]
                        , EPS111[j]*coefS1STAPS1[0]
                        , round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2)
                        , sort111.index(EPS111[j])+1
                        , (EPS111[j]>=10)
                        , creditS1STAPS1[0]
                    ],

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
                    ]
            ]
            staps1Moyenne.append(matrice[13][2])
            listeMatrice.append(matrice)

###########################################################  SEMESTRE 1 EPS RATTRAPAGE ############################################################################################################################

        EPS111R = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='RATTRAPAGE').values('note_rattrapage')) 
        sort111R = epurationRattrapage(EPS111R)

        EPS112R = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort112R = epurationRattrapage(EPS112R)

        EPS113R = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort113R = epurationRattrapage(EPS113R)

        EPS114R = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort114R = epurationRattrapage(EPS114R)

        EPS115aR = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort115aR = epurationRattrapage(EPS115aR)

        EPS115bR = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort115bR = epurationRattrapage(EPS115bR) 

        EPS115jR = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort115jR = epurationRattrapage(EPS115jR)

        EPS115lR = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort115lR = epurationRattrapage(EPS115lR)

        EPS116R = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort116R = epurationRattrapage(EPS116R)

        EPS117R = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort117R = epurationRattrapage(EPS117R)

        EPS118R = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort118R = epurationRattrapage(EPS118R)

        EPS119R = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort119R = epurationRattrapage(EPS119R)

        listeMatriceRs1EPS1 = []
        listeMatriceRs1EPS1ex = []

        for j in range (len(infoEtudiantSTAPS1)):
            matriceRs1EPS1 = [

                infoEtudiantSTAPS1[j],

                EPS111R[j],

                EPS112R[j],

                EPS113R[j],

                EPS114R[j],

                EPS115aR[j],

                EPS115bR[j],

                EPS115jR[j],

                EPS115lR[j],

                EPS116R[j],

                EPS117R[j],

                EPS118R[j],

                EPS119R[j]
            ]

            matriceRs1EPS1ex = [
                infoEtudiantSTAPS1[j],

                ( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] ) ,

                ( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] ) ,

                ( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] ) ,

                ( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] ) ,

                ( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] ) ,

                ( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] ) ,

                ( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] ) ,

                ( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] ) ,

                ( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] ) ,

                ( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] ) ,

                ( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] ) ,

                ( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] ) ,
            ]
            listeMatriceRs1EPS1.append(matriceRs1EPS1)
            listeMatriceRs1EPS1ex.append(matriceRs1EPS1ex)

###########################################################  SEMESTRE 1 EPS SYNTHESE   ############################################################################################################################

        listeMatrices1epsSynthese = []
        staps1Moyenne = []

        for j in range( len(infoEtudiantSTAPS1) ):

            matriceS1EPSSynthese = [
                    infoEtudiantSTAPS1[j],
                    #1
                    [ #EPS111[j]
                        ( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )
                        , coefS1STAPS1[0]
                        , (( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] ))*coefS1STAPS1[0]
                        , round( ((( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )*coefS1STAPS1[0]) + (( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2)
                        , len(sort111)+1 if (EPS111R[j] > 0) else (sort111.index(( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j]))+1 )
                        ,(( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )>=10)
                        , creditS1STAPS1[0]
                        , creditS1STAPS1[0] if ( (round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] ) >= 10) else 0
                        , 'Rattrapage' if (EPS111R[j] > 0)  else ''
                        #, EPS111cc[j]['note_cc']
                        #, EPS111sn[j]['note_sn'] 
                    ],

                    #2
                    [ 
                        ( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )
                        , coefS1STAPS1[1]
                        , ( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )*coefS1STAPS1[1]
                        , "MOYENNE"
                        , len(sort112)+1 if (EPS112R[j] > 0) else (sort112.index(( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j]))+1 )#, sort112.index(EPS112[j])+1
                        , (( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )>=10)
                        , creditS1STAPS1[1]
                        , creditS1STAPS1[1] if (( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )>=10) else 0
                        , 'Rattrapage' if (EPS112R[j] > 0)  else ''
                        #, EPS112cc[j]['note_cc']
                        #, EPS112sn[j]['note_sn'] 
                    ],

                    #3
                    [ 
                        ( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] )
                        , coefS1STAPS1[2]
                        , ( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] )*coefS1STAPS1[2]
                        , round( ( (( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] )*coefS1STAPS1[2]) + (( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )*coefS1STAPS1[3]) + (( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )*coefS1STAPS1[4]) + (( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] ) *coefS1STAPS1[5]) + (( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )*coefS1STAPS1[6]) + (( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]) + (( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )*coefS1STAPS1[8]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]) ,2)    
                        , len(sort113)+1 if (EPS113R[j] > 0) else (sort113.index(( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j]))+1 )#, sort113.index(EPS113[j])+1
                        , (( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] )>=10),creditS1STAPS1[2]
                        , creditS1STAPS1[2] if(( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] ) >=10) else 0
                        , 'Rattrapage' if (EPS113R[j] > 0)  else ''
                        #, EPS113cc[j]['note_cc']
                        #, EPS113sn[j]['note_sn']
                    ],

                    #4
                    [ 
                        ( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )
                        , coefS1STAPS1[3]
                        , ( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )*coefS1STAPS1[3]
                        , "MOYENNE"
                        , len(sort114)+1 if (EPS114R[j] > 0) else (sort114.index(( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j]))+1 )#, sort114.index(EPS114[j])+1
                        , (( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] ) >=10)
                        , creditS1STAPS1[3]
                        , creditS1STAPS1[3] if (( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] ) >=10) else 0
                        , 'Rattrapage' if (EPS114R[j] > 0)  else ''
                        #, EPS114cc[j]['note_cc']
                        #, EPS114sn[j]['note_sn']  
                    ],

                    #5
                    [ 
                        ( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )
                        , coefS1STAPS1[4]
                        , ( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )*coefS1STAPS1[4]
                        , "MOYENNE"
                        , len(sort115a)+1 if (EPS115aR[j] > 0) else (sort115a.index(( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j]))+1 )#, sort115a.index(EPS115a[j])+1
                        , (( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] ) >=10)
                        , creditS1STAPS1[4]
                        , creditS1STAPS1[4] if (( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] ) >=10) else 0
                        , 'Rattrapage' if (EPS115aR[j] > 0)  else ''
                        #, EPS115acc[j]['note_cc']
                        #, EPS115asn[j]['note_sn'] 
                    ], #crédits

                    #6
                    [ 
                        ( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )
                        , coefS1STAPS1[5]
                        ,  ( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )*coefS1STAPS1[5]
                        , "MOYENNE"
                        , len(sort115b)+1 if (EPS115bR[j] > 0) else (sort115b.index(( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j]))+1 )#, sort115a.index(EPS115a[j])+1#, sort115b.index(EPS115b[j])+1
                        , ( ( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] ) >=10)
                        , creditS1STAPS1[5]
                        , creditS1STAPS1[5] if ( ( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] ) >=10) else 0
                        , 'Rattrapage' if (EPS115bR[j] > 0)  else ''
                        #, EPS115bcc[j]['note_cc']
                        #, EPS115bsn[j]['note_sn'] 
                    ],

                    #7
                    [ 
                        ( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )
                        , coefS1STAPS1[6]
                        , ( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )*coefS1STAPS1[6]
                        , "MOYENNE"
                        , len(sort115j)+1 if (EPS115jR[j] > 0) else (sort115j.index(( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j]))+1 )#, sort115a.index(EPS115a[j])+1#, sort115j.index(EPS115j[j])+1
                        , (( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] ) >=10)
                        , creditS1STAPS1[6]
                        , creditS1STAPS1[6] if (( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] ) >=10) else 0
                        , 'Rattrapage' if (EPS115jR[j] > 0)  else ''
                        #, EPS115jcc[j]['note_cc']
                        #, EPS115jsn[j]['note_sn'] 
                    ],

                    #8
                    [ 
                        ( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )
                        , coefS1STAPS1[7]
                        , ( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]
                        , "MOYENNE"
                        , len(sort115l)+1 if (EPS115lR[j] > 0) else (sort115l.index(( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j]))+1 )#, sort115l.index(EPS115l[j])+1
                        , (( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] ) >=10)
                        , creditS1STAPS1[7]
                        , creditS1STAPS1[7] if ((( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )+( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )) >=40) else 0
                        , 'Rattrapage' if (EPS115lR[j] > 0)  else ''
                        #, EPS115lcc[j]['note_cc']
                        #, EPS115lsn[j]['note_sn']  
                    ],

                    #9
                    [ 
                        ( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )
                        ,  coefS1STAPS1[8]
                        , ( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )*coefS1STAPS1[8]
                        , "MOYENNE"
                        , len(sort116)+1 if (EPS116R[j] > 0) else (sort116.index(( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j]))+1 )#, sort116.index(EPS116[j])+1
                        , (( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] ) >=10)
                        , creditS1STAPS1[8]
                        , creditS1STAPS1[8] if (( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] ) >=10) else 0
                        , 'Rattrapage' if (EPS116R[j] > 0)  else ''
                        #, EPS116cc[j]['note_cc']
                        #, EPS116sn[j]['note_sn'] 
                    ],

                    #10
                    [ 
                        ( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] ) 
                        , coefS1STAPS1[9]
                        , ( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] ) *coefS1STAPS1[9]
                        , round( ((( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] ) *coefS1STAPS1[9]) + (( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )*coefS1STAPS1[10]) + (( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )*coefS1STAPS1[11])) / ( coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]) ,2)
                        , len(sort117)+1 if (EPS117R[j] > 0) else (sort117.index(( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j]))+1 )#sort117.index(EPS117[j])+1, 
                        , (( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] )  >=10)
                        , creditS1STAPS1[9]
                        , creditS1STAPS1[9] if (( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] )  >=10) else 0
                        , 'Rattrapage' if (EPS117R[j] > 0)  else ''
                        #, EPS117cc[j]['note_cc']
                        #, EPS117sn[j]['note_sn']
                    ],

                    #11
                    [ 
                        ( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )
                        , coefS1STAPS1[10]
                        , ( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )*coefS1STAPS1[10]
                        , "MOYENNE"
                        , len(sort118)+1 if (EPS118R[j] > 0) else (sort118.index(( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j]))+1 )#, sort118.index(EPS118[j])+1
                        , (( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] ) >=10)
                        , creditS1STAPS1[10]
                        , creditS1STAPS1[10] if (( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] ) >=10) else 0
                        , 'Rattrapage' if (EPS118R[j] > 0)  else ''
                        #, EPS118cc[j]['note_cc']
                        #, EPS118sn[j]['note_sn'] 
                    ],

                    #12
                    [ 
                        ( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )
                        , coefS1STAPS1[11]
                        , ( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )*coefS1STAPS1[11]
                        , "MOYENNE"
                        , len(sort119)+1 if (EPS119R[j] > 0) else (sort119.index(( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j]))+1 )#, sort119.index(EPS119[j])+1
                        , (( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] ) >=10)
                        , creditS1STAPS1[11]
                        , creditS1STAPS1[11] if (( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] ) >=10) else 0
                        , 'Rattrapage' if (EPS119R[j] > 0)  else ''
                        #, EPS119cc[j]['note_cc']
                        #, EPS119sn[j]['note_sn'] 
                    ],

                    #13
                    [ 
                        ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ), #coefsomme

                        round( ( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )*coefS1STAPS1[0]+( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )*coefS1STAPS1[1]+( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] ) *coefS1STAPS1[2]+( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )*coefS1STAPS1[3]+( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )*coefS1STAPS1[4]+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )*coefS1STAPS1[5]+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )*coefS1STAPS1[6]+( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]+( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )*coefS1STAPS1[8]+( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] )*coefS1STAPS1[9]+( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )*coefS1STAPS1[10]+( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )*coefS1STAPS1[11], 2),

                        round(( ( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )*coefS1STAPS1[0]+( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )*coefS1STAPS1[1]+( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] ) *coefS1STAPS1[2]+( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )*coefS1STAPS1[3]+( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )*coefS1STAPS1[4]+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )*coefS1STAPS1[5]+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )*coefS1STAPS1[6]+( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]+( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )*coefS1STAPS1[8]+( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] )*coefS1STAPS1[9]+( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )*coefS1STAPS1[10]+( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2 ),
                    ]
            ]

            #Décompte nombre de Crédits
            EPSCreditCount(matriceS1EPSSynthese)


            listeMatrices1epsSynthese.append(matriceS1EPSSynthese)

            #Enregistrement des notes et crédits de Semestre1 en EPS1
            e_matri = infoEtudiantSTAPS1[j]["matricule"]
            student = Etudiant.objects.get(matricule = e_matri)
            student.moyS1 = matriceS1EPSSynthese[13][2] 
            student.crS1 = matriceS1EPSSynthese[13][3]
            student.save()

            staps1Moyenne.append(matriceS1EPSSynthese[13][2])
            staps1Moyenne.sort(reverse=True)

            moy = stat.mean(staps1Moyenne)
            moy = round(moy, 2)
            session = 'Janvier 2023'

        #La liste de matrice possédant le décompte de crédit(listeMatrices1epsSynthese) est située en position 1 aprés filière
        semestre1MDS = [filiere, listeMatrices1epsSynthese, staps1Moyenne, moy, session, listeMatrice ] #listeMatrices1epsSynthese

    return render(request,'bulletin/BulletinTemplate/bullS1eps.html', {'semestre1MDS': semestre1MDS})


#EPS1 ET MDS1 SEMESTRE2
def bulls2epsmds(request, filiere):


    if (filiere =='GESTION'):

################################################## SEMESTRE 1 GESTION #######################################################################################
        infoEtudiantMDS = list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

        coefS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("coefficient", "intitule_UE"))
        coefS1MDS1 = epurationCoef(coefS1MDS1)

        creditS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("nombre_credit"))
        creditS1MDS1 = epurationCre(creditS1MDS1)

        MDS111 =list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='EXAMEN').values('note_cc'))
        sort111 = epurationTriCroissant(MDS111)


        MDS111b =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS111bcc =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='EXAMEN').values('note_cc'))
        sort111b = epurationTriCroissant(MDS111b)

        MDS112 =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS112cc =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='EXAMEN').values('note_cc'))
        sort112 = epurationTriCroissant(MDS112)

        MDS112b =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS112bcc =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='EXAMEN').values('note_cc'))
        sort112b = epurationTriCroissant(MDS112b)

        MDS113 =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS113cc =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='EXAMEN').values('note_cc'))
        sort113 = epurationTriCroissant(MDS113)

        MDS114 =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS114cc =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='EXAMEN').values('note_cc'))
        sort114 = epurationTriCroissant(MDS114)

        MDS115 =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS115cc =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='EXAMEN').values('note_cc'))
        sort115 = epurationTriCroissant(MDS115)

        MDS116 =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS116cc =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='EXAMEN').values('note_cc'))
        sort116 = epurationTriCroissant(MDS116)

        MDS117 =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS117cc =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='EXAMEN').values('note_cc'))
        sort117 = epurationTriCroissant(MDS117)

        MDS117b =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS117bcc =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='EXAMEN').values('note_cc'))
        sort117b = epurationTriCroissant(MDS117b)

        listeMatriceS1Ges = []
        mdsS1Moyenne = []

        for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

            matriceS1mds = [
                infoEtudiantMDS[j],

                [
                    MDS111[j]
                    , coefS1MDS1[0]
                    , MDS111[j]*coefS1MDS1[0]
                    , round( ((MDS111[j]*coefS1MDS1[0]) + (MDS111b[j]*coefS1MDS1[1]) + ( MDS112[j]*coefS1MDS1[2]) + (MDS112b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2)
                    , sort111.index(MDS111[j])+1
                    , (MDS111[j]>=10)
                    , creditS1MDS1[0]
                ],

                [ MDS111b[j], coefS1MDS1[1], MDS111b[j]*coefS1MDS1[1], "MOYENNE", sort111b.index(MDS111b[j])+1,(MDS111b[j]>=10), creditS1MDS1[1]],

                [ MDS112[j], coefS1MDS1[2], MDS112[j]*coefS1MDS1[2], "MOYENNE", sort112.index(MDS112[j])+1,(MDS112[j]>=10), creditS1MDS1[2]],

                [ MDS112b[j], coefS1MDS1[3], MDS112b[j]*coefS1MDS1[3], "MOYENNE", sort112b.index(MDS112b[j])+1,(MDS112b[j]>=10), creditS1MDS1[3]],


                [
                    MDS113[j]
                    , coefS1MDS1[4]
                    , MDS113[j]*coefS1MDS1[4]
                    , round( ((MDS113[j]*coefS1MDS1[4]) + (MDS114[j]*coefS1MDS1[5]) + MDS115[j]*coefS1MDS1[6] + MDS116[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2)
                    , sort113.index(MDS113[j])+1
                    ,(MDS113[j]>=10)
                    ,creditS1MDS1[4]
                ],

                [ MDS114[j], coefS1MDS1[5], MDS114[j]*coefS1MDS1[5], "MOYENNE", sort114.index(MDS114[j])+1,(MDS114[j]>=10), creditS1MDS1[5]],

                [ MDS115[j], coefS1MDS1[6], MDS115[j]*coefS1MDS1[6], "MOYENNE", sort115.index(MDS115[j])+1,(MDS115[j]>=10), creditS1MDS1[6]],

                [ MDS116[j], coefS1MDS1[7], MDS116[j]*coefS1MDS1[7], "MOYENNE", sort116.index(MDS116[j])+1,(MDS116[j]>=10), creditS1MDS1[7]],


                [
                    MDS117[j]
                    , coefS1MDS1[8]
                    , MDS117[j]*coefS1MDS1[8]
                    , round(( MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2)
                    , sort117.index(MDS117[j])+1
                    , (MDS117[j]>=10)
                    , creditS1MDS1[8]
                ],

                [ MDS117b[j], coefS1MDS1[9], MDS117b[j]*coefS1MDS1[9], "MOYENNE", sort117b.index(MDS117b[j])+1,(MDS117b[j]>=10), creditS1MDS1[9]],

                [
                    ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),

                   round (MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] , 2),

                   round (( MDS111[j]*coefS1MDS1[0] + MDS111b[j]*coefS1MDS1[1] + MDS112[j]*coefS1MDS1[2] + MDS112b[j]*coefS1MDS1[3] + MDS113[j]*coefS1MDS1[4] + MDS114[j]*coefS1MDS1[5] + MDS115[j]*coefS1MDS1[6] + MDS116[j]*coefS1MDS1[7] + MDS117[j]*coefS1MDS1[8] + MDS117b[j]*coefS1MDS1[9] )/( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                ]

            ]
            MDSCreditCount(matriceS1mds)

            listeMatriceS1Ges.append(matriceS1mds)
            mdsS1Moyenne.append(matriceS1mds[11][2])
            mdsS1Moyenne.sort(reverse=True)

            moymdsS1 = stat.mean(mdsS1Moyenne)
            moymdsS1 = round(moymdsS1, 2)
            session = 'Janvier 2023'

            #filiere, listeMatrice, staps1Moyenne, moy, session
        #semestre1MDS = [filiere,  listeMatriceS1Ges, mdsS1Moyenne,  moymdsS1, session] 

################################################## SEMESTRE 1 GESTION RATTRAPAGE ############################################################################
        MDS111R =list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort111R = epurationRattrapage(MDS111R)

        MDS111bR =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort111bR = epurationRattrapage(MDS111bR)

        MDS112R =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort112R = epurationRattrapage(MDS112R)

        MDS112bR =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort112bR = epurationRattrapage(MDS112bR)

        MDS113R =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort113R = epurationRattrapage(MDS113R)

        MDS114R =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort114R = epurationRattrapage(MDS114R)

        MDS115R =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort115R = epurationRattrapage(MDS115R)

        MDS116R =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort116R = epurationRattrapage(MDS116R)

        MDS117R =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort117R = epurationRattrapage(MDS117R)

        MDS117bR =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort117b = epurationRattrapage(MDS117bR)

################################################## SEMESTRE 1 GESTION CC ##############################################################################
        listeMatrices1GesCC = []
        for j in range(len(infoEtudiantMDS)):

            matrices1GesCC = [

                infoEtudiantMDS[j],

                MDS111cc[j],

                MDS111bcc[j],

                MDS112cc[j],

                MDS112bcc[j],

                MDS113cc[j],

                MDS114cc[j],

                MDS115cc[j],

                MDS116cc[j],

                MDS117cc[j],

                MDS117bcc[j],

            ]
            listeMatrices1GesCC.append(matrices1GesCC)

        #Liste matrice Rattrapage
        listeMatrices1GesR = []

        for j in range( len(infoEtudiantMDS) ):

            matrices1mdsR = [

                infoEtudiantMDS[j],

                MDS111R[j],

                MDS111bR[j],

                MDS112R[j],

                MDS111bR[j],

                MDS113R[j],

                MDS114R[j],

                MDS115R[j],

                MDS116R[j],

                MDS117R[j],

                MDS117bR[j]
            ]
            listeMatrices1GesR.append(matrices1mdsR)

################################################## SEMESTRE 1 GESTION SYNTHESE ##############################################################################
        listeMatricemdsS1Synthese, listeMoyenne = matriceSynthesemds1( listeMatriceS1Ges, listeMatrices1GesR, listeMatriceS1Ges, listeMatrices1GesCC  ) #, listeMatrices2GesCC
        #MDSCreditCount(listeMatricemdsS1Synthese)

        #semestre1MDS = [filiere,  listeMatriceS1Ges, mdsS1Moyenne,  moymdsS1, session, listeMatrices1GesR, listeMatricemdsS1Synthese ]  #, listeMatricemdsS1Synthese

################################################## SEMESTRE 2 GESTION #######################################################################################

        infoEtudiantMDS =list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

        coefS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="GESTION").values("coefficient", "intitule_UE"))
        coefS1MDS1 = epurationCoef(coefS1MDS1)

        creditS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="GESTION").values("nombre_credit"))
        creditS1MDS1 = epurationCre(creditS1MDS1)

        MDS121 =list(Evaluation.objects.filter(uniteEnseignement_id=88, natureEvaluation='EXAMEN').values('note_Examen'))
        sort121 = epurationTriCroissant(MDS121)
        MDS121cc = list(Evaluation.objects.filter(uniteEnseignement_id=88).values('note_cc'))
        MDS121cc = epurationCC(MDS121cc)

        MDS121b =list(Evaluation.objects.filter(uniteEnseignement_id=89, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS121bcc =list(Evaluation.objects.filter(uniteEnseignement_id=89).values('note_cc'))
        MDS121bcc = epurationCC(MDS121bcc)
        sort121b = epurationTriCroissant(MDS121b)

        MDS122 =list(Evaluation.objects.filter(uniteEnseignement_id=90, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS122cc =list(Evaluation.objects.filter(uniteEnseignement_id=90).values('note_cc'))
        MDS122cc = epurationCC(MDS122cc)
        sort122 = epurationTriCroissant(MDS122)

        MDS122b =list(Evaluation.objects.filter(uniteEnseignement_id=91, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS122bcc =list(Evaluation.objects.filter(uniteEnseignement_id=91).values('note_cc'))
        MDS122bcc = epurationCC(MDS122bcc)
        sort122b = epurationTriCroissant(MDS122b)

        MDS123 =list(Evaluation.objects.filter(uniteEnseignement_id=92, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS123cc =list(Evaluation.objects.filter(uniteEnseignement_id=92).values('note_cc'))
        MDS123cc = epurationCC(MDS123cc)
        sort123 = epurationTriCroissant(MDS123)

        MDS124 =list(Evaluation.objects.filter(uniteEnseignement_id=93, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS124cc =list(Evaluation.objects.filter(uniteEnseignement_id=93).values('note_cc'))
        MDS124cc = epurationCC(MDS124cc)
        sort124 = epurationTriCroissant(MDS124)

        MDS125 =list(Evaluation.objects.filter(uniteEnseignement_id=95, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS125cc =list(Evaluation.objects.filter(uniteEnseignement_id=95).values('note_cc'))
        MDS125cc = epurationCC(MDS125cc)
        sort125 = epurationTriCroissant(MDS125)

        MDS126 =list(Evaluation.objects.filter(uniteEnseignement_id=96, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS126cc =list(Evaluation.objects.filter(uniteEnseignement_id=96).values('note_cc'))
        MDS126cc = epurationCC(MDS126cc)
        sort126 = epurationTriCroissant(MDS126)

        MDS127 =list(Evaluation.objects.filter(uniteEnseignement_id=97, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS127cc =list(Evaluation.objects.filter(uniteEnseignement_id=97).values('note_cc'))
        MDS127cc = epurationCC(MDS127cc)
        sort127 = epurationTriCroissant(MDS127)

        MDS127b =list(Evaluation.objects.filter(uniteEnseignement_id=98, natureEvaluation='EXAMEN').values('note_Examen'))
        MDS127bcc =list(Evaluation.objects.filter(uniteEnseignement_id=98).values('note_cc'))
        MDS127bcc = epurationCC(MDS127bcc)
        sort127b = epurationTriCroissant(MDS127b)

        #Liste Matrice CC
        listeMatrices2GesCC = []

        for j in range(len(infoEtudiantMDS)):

            matrices2GesCC = [

                infoEtudiantMDS[j],

                MDS121cc[j],

                MDS121bcc[j],

                MDS122cc[j],

                MDS122bcc[j],

                MDS123cc[j],

                MDS124cc[j],

                MDS125cc[j],

                MDS126cc[j],

                MDS127cc[j],

                MDS127bcc[j],

            ]
            
            listeMatrices2GesCC.append(matrices2GesCC)


        #LISTE MATRICE SESSION NORMALE 2 MDS GES
        listeMatrices2Ges = []
        mds1Moyenne = []

        for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

                matrice = [
                    infoEtudiantMDS[j],

                    #Ligne 1
                    [
                        MDS121[j]
                        , coefS1MDS1[0]
                        , MDS121[j]*coefS1MDS1[0]
                        , round( ((MDS121[j]*coefS1MDS1[0]) + (MDS121b[j]*coefS1MDS1[1]) + ( MDS122[j]*coefS1MDS1[2]) + (MDS122b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2)
                        , sort121.index(MDS121[j])+1
                        , (MDS121[j]>=10)
                        , creditS1MDS1[0]
                        , creditS1MDS1[0] if (MDS121[j]>=10) else 0
                    ],

                    [ MDS121b[j], coefS1MDS1[1], MDS121b[j]*coefS1MDS1[1], "MOYENNE", sort121b.index(MDS121b[j])+1,(MDS121b[j]>=10), creditS1MDS1[1], creditS1MDS1[1] if (MDS121b[j]>=10) else 0],

                    [ MDS122[j], coefS1MDS1[2], MDS122[j]*coefS1MDS1[2], "MOYENNE", sort122.index(MDS122[j])+1,(MDS122[j]>=10), creditS1MDS1[2], creditS1MDS1[2] if (MDS122[j]>=10) else 0],

                    [ MDS122b[j], coefS1MDS1[3], MDS122b[j]*coefS1MDS1[3], "MOYENNE", sort122b.index(MDS122b[j])+1,(MDS122b[j]>=10), creditS1MDS1[3], creditS1MDS1[3] if (MDS122b[j]>=10) else 0 ],

                    #Ligne 5
                    [ MDS123[j], coefS1MDS1[4], MDS123[j]*coefS1MDS1[4],

                        round( ((MDS123[j]*coefS1MDS1[4]) + (MDS124[j]*coefS1MDS1[5]) + MDS125[j]*coefS1MDS1[6] + MDS126[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2), 

                        sort123.index(MDS123[j])+1,

                        (MDS123[j]>=10), 

                        creditS1MDS1[4], 

                        creditS1MDS1[4] if (MDS123[j]>=10) else 0
                    ],

                    [ MDS124[j], coefS1MDS1[5], MDS124[j]*coefS1MDS1[5], "MOYENNE", sort124.index(MDS124[j])+1,(MDS124[j]>=10), creditS1MDS1[5] , creditS1MDS1[5] if (MDS124[j]>=10) else 0 ],

                    [ MDS125[j], coefS1MDS1[6], MDS125[j]*coefS1MDS1[6], "MOYENNE", sort125.index(MDS125[j])+1,(MDS125[j]>=10), creditS1MDS1[6],  creditS1MDS1[6] if (MDS125[j]>=10) else 0 ],

                    [ MDS126[j], coefS1MDS1[7], MDS126[j]*coefS1MDS1[7], "MOYENNE", sort126.index(MDS126[j])+1,(MDS126[j]>=10), creditS1MDS1[7],  creditS1MDS1[7] if (MDS126[j]>=10) else 0 ],

                    #Ligne 9
                    [ MDS127[j], coefS1MDS1[8], MDS127[j]*coefS1MDS1[8], 
                    
                        round(( MDS127[j]*coefS1MDS1[8]+MDS127b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2), 

                        sort127.index(MDS127[j])+1,

                        (MDS127[j]>=10), 

                        creditS1MDS1[8],

                        creditS1MDS1[8] if (MDS127[j]>=10) else 0
                    ],

                    [ MDS127b[j], coefS1MDS1[9], MDS127b[j]*coefS1MDS1[9], "MOYENNE", sort127b.index(MDS127b[j])+1,(MDS127b[j]>=10), creditS1MDS1[9], creditS1MDS1[9] if (MDS127b[j]>=10) else 0 ],

                    #SOMME SOMME
                    [
                        ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),

                        round (MDS121[j]*coefS1MDS1[0]+MDS121b[j]*coefS1MDS1[1]+MDS122[j]*coefS1MDS1[2]+MDS122b[j]*coefS1MDS1[3]+MDS123[j]*coefS1MDS1[4]+MDS124[j]*coefS1MDS1[5]+MDS125[j]*coefS1MDS1[6]+MDS126[j]*coefS1MDS1[7]+ MDS127[j]*coefS1MDS1[8]+MDS127b[j]*coefS1MDS1[9] , 2),

                        round (( MDS121[j]*coefS1MDS1[0]+MDS121b[j]*coefS1MDS1[1]+MDS122[j]*coefS1MDS1[2]+MDS122b[j]*coefS1MDS1[3]+MDS123[j]*coefS1MDS1[4]+MDS124[j]*coefS1MDS1[5]+MDS125[j]*coefS1MDS1[6]+MDS126[j]*coefS1MDS1[7]+ MDS127[j]*coefS1MDS1[8]+MDS127b[j]*coefS1MDS1[9] )/( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                    ]
                ]

                #Decompte du total de crédits
                #MDSCreditCount(matrice)

                listeMatrices2Ges.append(matrice)
                mds1Moyenne.append(matrice[11][2])
                mds1Moyenne.sort(reverse=True)

                moy = stat.mean(mds1Moyenne)
                moy = round(moy, 2)
                session = 'Janvier 2023'

                #filiere, listeMatrice, staps1Moyenne, moy, session

        #semestre1MDS = [filiere,  listeMatrice, mds1Moyenne,  moy, session]

################################################## SEMESTRE 2 GESTION RATTRAPAGE ############################################################################

        MDS121R =list(Evaluation.objects.filter(uniteEnseignement_id=88, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort121R = epurationRattrapage(MDS121R)

        MDS121bR =list(Evaluation.objects.filter(uniteEnseignement_id=89, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort121bR = epurationRattrapage(MDS121bR)

        MDS122R =list(Evaluation.objects.filter(uniteEnseignement_id=90, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort122R = epurationRattrapage(MDS122R)

        MDS122bR =list(Evaluation.objects.filter(uniteEnseignement_id=91, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort122bR = epurationRattrapage(MDS122bR)

        MDS123R =list(Evaluation.objects.filter(uniteEnseignement_id=92, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort123R = epurationRattrapage(MDS123R)

        MDS124R =list(Evaluation.objects.filter(uniteEnseignement_id=93, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort124R = epurationRattrapage(MDS124R)

        MDS125R =list(Evaluation.objects.filter(uniteEnseignement_id=95, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort125R = epurationRattrapage(MDS125R)

        MDS126R =list(Evaluation.objects.filter(uniteEnseignement_id=96, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort126R = epurationRattrapage(MDS126R)

        MDS127R =list(Evaluation.objects.filter(uniteEnseignement_id=97, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort127R = epurationRattrapage(MDS127R)

        MDS127bR =list(Evaluation.objects.filter(uniteEnseignement_id=98, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort127bR = epurationRattrapage(MDS127bR)

        listeMatrices2GesR = []

        for j in range( len(infoEtudiantMDS) ):

            matrices2mdsR = [

                infoEtudiantMDS[j],

                MDS121R[j],

                MDS121bR[j],

                MDS122R[j],

                MDS122bR[j],

                MDS123R[j],

                MDS124R[j],

                MDS125R[j],

                MDS126R[j],

                MDS127R[j],

                MDS127bR[j]
            ]
            listeMatrices2GesR.append(matrices2mdsR)

################################################## SEMESTRE 2 GESTION SYNTHESE ##############################################################################
        #LIGNE FONCTION SYNTHESE
        listeMatricemdsS2Synthese = matriceSynthesemds( listeMatrices2Ges, listeMatrices2GesR, listeMatriceS1Ges, listeMatrices2GesCC ) #

        MDSCreditCountS2(listeMatricemdsS2Synthese)

        sessionD = "Mai 2023"

        semestre1MDS = [filiere,  listeMatriceS1Ges, mdsS1Moyenne,  moy, session, listeMatrices2Ges, listeMatrices2GesR, listeMatricemdsS2Synthese, sessionD, listeMatrices2GesCC, listeMatricemdsS1Synthese] #mds1Moyenne , listeMatricemdsS1Synthese


################################################## SEMESTRE 1 EPS ########################################################################################################################################################
    elif (filiere == 'STAPS1'):

        infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

        coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("coefficient"))
        coefS1STAPS1 = epurationCoef(coefS1STAPS1)

        creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("nombre_credit"))
        creditS1STAPS1 = epurationCre(creditS1STAPS1)

        EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN').values('note_cc'))
        EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN').values('note_sn'))
        sort111 = epurationTriCroissant(EPS111)

        EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='EXAMEN').values('note_cc'))
        EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='EXAMEN').values('note_sn'))
        sort112 = epurationTriCroissant(EPS112)

        EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='EXAMEN').values('note_cc'))
        EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='EXAMEN').values('note_sn'))
        sort113 = epurationTriCroissant(EPS113)

        EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN').values('note_cc'))
        EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN').values('note_sn'))
        sort114 = epurationTriCroissant(EPS114)

        EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN').values('note_cc'))
        EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN').values('note_sn'))
        sort115a = epurationTriCroissant(EPS115a)

        EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS115bcc = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN').values('note_cc'))
        EPS115bsn = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN').values('note_sn'))
        sort115b = epurationTriCroissant(EPS115b) 

        EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN').values('note_cc'))
        EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN').values('note_sn'))
        sort115j = epurationTriCroissant(EPS115j)

        EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN').values('note_cc'))
        EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN').values('note_sn'))
        sort115l = epurationTriCroissant(EPS115l)

        EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN').values('note_cc'))
        EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN').values('note_sn'))
        sort116 = epurationTriCroissant(EPS116)

        EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='EXAMEN').values('note_cc')) 
        EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='EXAMEN').values('note_sn')) 
        sort117 = epurationTriCroissant(EPS117)

        EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN').values('note_cc'))
        EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN').values('note_sn'))
        sort118 = epurationTriCroissant(EPS118)

        EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN').values('note_cc'))
        EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN').values('note_sn'))
        sort119 = epurationTriCroissant(EPS119)

        #student = {}
        #temp = {}
        #staps1 = []

        staps1MoyenneS1Eps = []
        listeMatriceS1Eps = [ ]

        for j in range( len(infoEtudiantSTAPS1) ):

            #for j in range( len(coefS1STAPS1) ):
            matriceS1Eps = [
                    infoEtudiantSTAPS1[j],

                    [ 
                        EPS111[j]
                        , coefS1STAPS1[0]
                        , EPS111[j]*coefS1STAPS1[0]
                        , round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2)
                        , sort111.index(EPS111[j])+1
                        , (EPS111[j]>=10)
                        , creditS1STAPS1[0]
                    ],

                    [ 
                        EPS112[j]
                        , coefS1STAPS1[1]
                        , EPS112[j]*coefS1STAPS1[1]
                        , "MOYENNE"
                        , sort112.index(EPS112[j])+1
                        , (EPS112[j]>=10)
                        , creditS1STAPS1[1]
                    ],

                    [ 
                        EPS113[j], 

                        coefS1STAPS1[2], 

                        EPS113[j]*coefS1STAPS1[2], 

                        round( ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5]) + (EPS115j[j]*coefS1STAPS1[6]) + (EPS115l[j]*coefS1STAPS1[7]) + (EPS116[j]*coefS1STAPS1[8]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]) ,2), 

                        sort113.index(EPS113[j])+1,

                        (EPS113[j] >=10),

                        creditS1STAPS1[2]
                    ],

                    [ EPS114[j],  coefS1STAPS1[3], EPS114[j]*coefS1STAPS1[3], "MOYENNE", sort114.index(EPS114[j])+1, (EPS114[j] >=10), creditS1STAPS1[3] ],

                    [ EPS115a[j], coefS1STAPS1[4], EPS115a[j]*coefS1STAPS1[4], "MOYENNE", sort115a.index(EPS115a[j])+1, (EPS115a[j] >=10), creditS1STAPS1[4] ], #crédits

                    [ 
                        EPS115b[j]
                        , coefS1STAPS1[5]
                        , EPS115b[j]*coefS1STAPS1[5]
                        , "MOYENNE"
                        , sort115b.index(EPS115b[j])+1
                        , (EPS115b[j] >=10)
                        , creditS1STAPS1[5] 
                    ],

                    [ EPS115j[j], coefS1STAPS1[6], EPS115j[j]*coefS1STAPS1[6], "MOYENNE", sort115j.index(EPS115j[j])+1, (EPS115j[j] >=10), creditS1STAPS1[6] ],

                    [ EPS115l[j], coefS1STAPS1[7], EPS115l[j]*coefS1STAPS1[7], "MOYENNE", sort115l.index(EPS115l[j])+1, (EPS115l[j] >=10), creditS1STAPS1[7] ],

                    [ EPS116[j],  coefS1STAPS1[8], EPS116[j]*coefS1STAPS1[8], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[8] ],

                    [ 
                        EPS117[j]
                        , coefS1STAPS1[9] 
                        , EPS117[j]*coefS1STAPS1[9]
                        , round( ((EPS117[j]*coefS1STAPS1[9]) + (EPS118[j]*coefS1STAPS1[10]) + (EPS119[j]*coefS1STAPS1[11])) / ( coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]) ,2) 
                        , sort117.index(EPS117[j])+1
                        , (EPS117[j] >=10)
                        ,creditS1STAPS1[9] 
                    ],

                    [ 
                        EPS118[j]
                        , coefS1STAPS1[10]
                        , EPS118[j]*coefS1STAPS1[10]
                        , "MOYENNE"
                        , sort118.index(EPS118[j])+1
                        , (EPS118[j] >=10)
                        , creditS1STAPS1[10] 
                    ],

                    [ 
                        EPS119[j]
                        , coefS1STAPS1[11]
                        , EPS119[j]*coefS1STAPS1[11]
                        , "MOYENNE"
                        , sort119.index(EPS119[j])+1
                        , (EPS119[j] >=10)
                        , creditS1STAPS1[11] 
                    ],

                    [
                        ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ),

                        round( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115j[j]*coefS1STAPS1[6]+EPS115l[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11], 2),

                        round(( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115j[j]*coefS1STAPS1[6]+EPS115l[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2 ),

                    ]
            ]
            staps1MoyenneS1Eps.append(matriceS1Eps[13][2])

            listeMatriceS1Eps.append(matriceS1Eps)

        #infoEtudiantSTAPS1, coefS1STAPS1, creditS1STAPS1, EPS111, EPS112, EPS113, EPS114, EPS115a ,EPS115b, EPS115j, EPS115l, EPS116, EPS117, EPS118, EPS119, 

        staps1MoyenneS1Eps.sort(reverse=True)
        moyS1Eps = stat.mean(staps1MoyenneS1Eps)
        moyS1Eps = round(moyS1Eps, 2)
        session = 'Janvier 2023'

        #semestre1MDS = [filiere, listeMatriceS1Eps, staps1MoyenneS1Eps, moyS1Eps, session ]

################################################## SEMESTRE 1 EPS CC ########################################################################################################################################################
        listeMatriceS1EpsCC = []

        for j in range( len(infoEtudiantSTAPS1) ):

            matriceS1EpsCC = [

                infoEtudiantSTAPS1[j],

                EPS111cc[j]["note_cc"],

                EPS112cc[j]["note_cc"],

                EPS113cc[j]["note_cc"],

                EPS114cc[j]["note_cc"],

                EPS115acc[j]["note_cc"],

                EPS115bcc[j]["note_cc"],

                EPS115jcc[j]["note_cc"],

                EPS115lcc[j]["note_cc"],

                EPS116cc[j]["note_cc"],

                EPS117cc[j]["note_cc"],

                EPS118cc[j]["note_cc"],

                EPS119cc[j]["note_cc"],
            ]
            listeMatriceS1EpsCC.append(matriceS1EpsCC)

################################################## SEMESTRE 1 EPS RATTRAPAGE ################################################################################
        EPS111R = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort111R = epurationRattrapage(EPS111R)

        EPS112R = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort112R = epurationRattrapage(EPS112R)

        EPS113R = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort113R = epurationRattrapage(EPS113R)

        EPS114R = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort114R = epurationRattrapage(EPS114R)

        EPS115aR = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort115aR = epurationRattrapage(EPS115aR)

        EPS115bR = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort115b = epurationRattrapage(EPS115bR)

        EPS115jR = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort115jR = epurationRattrapage(EPS115jR)

        EPS115lR = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort115lR = epurationRattrapage(EPS115lR)

        EPS116R = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort116R = epurationRattrapage(EPS116R)

        EPS117R = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='RATTRAPAGE').values('note_rattrapage')) 
        sort117R = epurationRattrapage(EPS117R)

        EPS118R = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort118R = epurationRattrapage(EPS118R)

        EPS119R = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort119R = epurationRattrapage(EPS119R)

        listeMatriceS1EpsR = []

        for j in range( len(infoEtudiantSTAPS1) ):

            matriceS1EpsR = [

                infoEtudiantSTAPS1[j],

                EPS111R[j],

                EPS112R[j],

                EPS113R[j],

                EPS114R[j],

                EPS115aR[j],

                EPS115bR[j],

                EPS115jR[j],

                EPS115lR[j],

                EPS116R[j],

                EPS117R[j],

                EPS118R[j],

                EPS119R[j],

            ]
            listeMatriceS1EpsR.append(matriceS1EpsR)

################################################## SEMESTRE 1 EPS SYNTHESE ##################################################################################
        #Synhèse EPS1 Semestre 1

        listeMatriceS1EpsSynthese = matriceSyntheseEPS1(listeMatriceS1Eps, listeMatriceS1EpsR, listeMatriceS1Eps, listeMatriceS1EpsCC)

        #Décompte de crédit
        EPSCreditCount2(listeMatriceS1EpsSynthese)

        semestre1MDS = [filiere, listeMatriceS1Eps, staps1MoyenneS1Eps, moyS1Eps, session, listeMatriceS1EpsSynthese] #,listeMatriceS1Eps , listeMatriceS1EpsSynthese  #, listeMatriceS2EpsSynthese

################################################## SEMESTRE 2 EPS ########################################################################################################################################################     
        infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

        coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="STAPS").values("coefficient"))
        coefS1STAPS1 = epurationCoef(coefS1STAPS1)

        creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="STAPS").values("nombre_credit"))
        creditS1STAPS1 = epurationCre(creditS1STAPS1)

        EPS121 = list(Evaluation.objects.filter(uniteEnseignement_id=99, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS121cc = list(Evaluation.objects.filter(uniteEnseignement_id=99, natureEvaluation='EXAMEN').values('note_cc'))
        EPS121sn = list(Evaluation.objects.filter(uniteEnseignement_id=99, natureEvaluation='EXAMEN').values('note_sn'))
        sort121 = epurationTriCroissant(EPS121)

        EPS122 = list(Evaluation.objects.filter(uniteEnseignement_id=100, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS122cc = list(Evaluation.objects.filter(uniteEnseignement_id=100, natureEvaluation='EXAMEN').values('note_cc'))
        EPS122sn = list(Evaluation.objects.filter(uniteEnseignement_id=100, natureEvaluation='EXAMEN').values('note_sn'))
        sort122 = epurationTriCroissant(EPS122)

        EPS123 = list(Evaluation.objects.filter(uniteEnseignement_id=101, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS123cc = list(Evaluation.objects.filter(uniteEnseignement_id=101, natureEvaluation='EXAMEN').values('note_cc'))
        EPS123sn = list(Evaluation.objects.filter(uniteEnseignement_id=101, natureEvaluation='EXAMEN').values('note_sn'))
        sort123 = epurationTriCroissant(EPS123)

        EPS124 = list(Evaluation.objects.filter(uniteEnseignement_id=102, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS124cc = list(Evaluation.objects.filter(uniteEnseignement_id=102, natureEvaluation='EXAMEN').values('note_cc'))
        EPS124sn = list(Evaluation.objects.filter(uniteEnseignement_id=102, natureEvaluation='EXAMEN').values('note_sn'))
        sort124 = epurationTriCroissant(EPS124)

        EPS125a = list(Evaluation.objects.filter(uniteEnseignement_id=103, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS125acc = list(Evaluation.objects.filter(uniteEnseignement_id=103, natureEvaluation='EXAMEN').values('note_cc'))
        EPS125asn = list(Evaluation.objects.filter(uniteEnseignement_id=103, natureEvaluation='EXAMEN').values('note_sn'))
        sort125a = epurationTriCroissant(EPS125a)

        EPS125b = list(Evaluation.objects.filter(uniteEnseignement_id=104, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS125bcc = list(Evaluation.objects.filter(uniteEnseignement_id=104, natureEvaluation='EXAMEN').values('note_cc'))
        EPS125bsn = list(Evaluation.objects.filter(uniteEnseignement_id=104, natureEvaluation='EXAMEN').values('note_sn'))
        sort125b = epurationTriCroissant(EPS125b) 

        EPS125g = list(Evaluation.objects.filter(uniteEnseignement_id=124, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS125gcc = list(Evaluation.objects.filter(uniteEnseignement_id=124, natureEvaluation='EXAMEN').values('note_cc'))
        EPS125gsn = list(Evaluation.objects.filter(uniteEnseignement_id=124, natureEvaluation='EXAMEN').values('note_sn'))
        sort125g = epurationTriCroissant(EPS125g)

        EPS125j = list(Evaluation.objects.filter(uniteEnseignement_id=105, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS125jcc = list(Evaluation.objects.filter(uniteEnseignement_id=105, natureEvaluation='EXAMEN').values('note_cc'))
        EPS125jsn = list(Evaluation.objects.filter(uniteEnseignement_id=105, natureEvaluation='EXAMEN').values('note_sn'))
        sort125j = epurationTriCroissant(EPS125j)

        EPS125l = list(Evaluation.objects.filter(uniteEnseignement_id=106, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS125lcc = list(Evaluation.objects.filter(uniteEnseignement_id=106, natureEvaluation='EXAMEN').values('note_cc'))
        EPS125lsn = list(Evaluation.objects.filter(uniteEnseignement_id=106, natureEvaluation='EXAMEN').values('note_sn'))
        sort125l = epurationTriCroissant(EPS125l)

        EPS125f = list(Evaluation.objects.filter(uniteEnseignement_id=107, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS125fcc = list(Evaluation.objects.filter(uniteEnseignement_id=107, natureEvaluation='EXAMEN').values('note_cc'))
        EPS125fsn = list(Evaluation.objects.filter(uniteEnseignement_id=107, natureEvaluation='EXAMEN').values('note_sn'))
        sort125f = epurationTriCroissant(EPS125f)

        EPS126 = list(Evaluation.objects.filter(uniteEnseignement_id=108, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS126cc = list(Evaluation.objects.filter(uniteEnseignement_id=108, natureEvaluation='EXAMEN').values('note_cc'))
        EPS126sn = list(Evaluation.objects.filter(uniteEnseignement_id=108, natureEvaluation='EXAMEN').values('note_sn'))
        sort126 = epurationTriCroissant(EPS126)

        EPS127 = list(Evaluation.objects.filter(uniteEnseignement_id=109, natureEvaluation='EXAMEN').values('note_Examen')) 
        EPS127cc = list(Evaluation.objects.filter(uniteEnseignement_id=109, natureEvaluation='EXAMEN').values('note_cc'))
        EPS127sn = list(Evaluation.objects.filter(uniteEnseignement_id=109, natureEvaluation='EXAMEN').values('note_sn'))
        sort127 = epurationTriCroissant(EPS127)

        EPS128 = list(Evaluation.objects.filter(uniteEnseignement_id=110, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS128cc = list(Evaluation.objects.filter(uniteEnseignement_id=110, natureEvaluation='EXAMEN').values('note_cc'))
        EPS128sn = list(Evaluation.objects.filter(uniteEnseignement_id=110, natureEvaluation='EXAMEN').values('note_sn'))
        sort128 = epurationTriCroissant(EPS128)

        EPS129 = list(Evaluation.objects.filter(uniteEnseignement_id=111, natureEvaluation='EXAMEN').values('note_Examen'))
        EPS129cc = list(Evaluation.objects.filter(uniteEnseignement_id=111, natureEvaluation='EXAMEN').values('note_cc'))
        EPS129sn = list(Evaluation.objects.filter(uniteEnseignement_id=111, natureEvaluation='EXAMEN').values('note_sn'))
        sort129 = epurationTriCroissant(EPS129)

        student = {}
        temp = {}
        staps1 = []
        staps2Moyenne = []
        listeMatriceS2Eps = [ ]

        for j in range( len(infoEtudiantSTAPS1) ):

            #for j in range( len(coefS1STAPS1) ):
            matrice = [
                    infoEtudiantSTAPS1[j],

                    [ 
                        EPS121[j]
                        , coefS1STAPS1[0]
                        , EPS121[j]*coefS1STAPS1[0]
                        , round( ((EPS121[j]*coefS1STAPS1[0]) + (EPS122[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2)
                        , sort121.index(EPS121[j])+1,(EPS121[j]>=10)
                        , creditS1STAPS1[0]
                        , creditS1STAPS1[0] if(EPS121[j]>=10) else 0 
                    ],

                    [ 
                        EPS122[j]
                        , coefS1STAPS1[1]
                        , EPS122[j]*coefS1STAPS1[1]
                        , "MOYENNE"
                        , sort122.index(EPS122[j])+1
                        #, (EPS122[j]>=10)
                        , creditS1STAPS1[1]
                        , creditS1STAPS1[1] if(EPS122[j]>=10) else 0 
                    ],

                    [ 
                        EPS123[j]
                        , coefS1STAPS1[2]
                        , EPS123[j]*coefS1STAPS1[2]
                        , round( ( (EPS123[j]*coefS1STAPS1[2]) + (EPS124[j]*coefS1STAPS1[3]) + (EPS125a[j]*coefS1STAPS1[4]) + (EPS125g[j]*coefS1STAPS1[5]) + (EPS125j[j]*coefS1STAPS1[6]) + (EPS125f[j]*coefS1STAPS1[7]) + (EPS126[j]*coefS1STAPS1[8]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]) ,2)  #EPS125b[j] , EPS125l[j]
                        , sort123.index(EPS123[j])+1
                        #, (EPS123[j] >=10)
                        , creditS1STAPS1[2]
                        , creditS1STAPS1[2] if (EPS123[j] >=10) else 0
                    ],

                    [ 
                        EPS124[j]
                        , coefS1STAPS1[3]
                        , EPS124[j]*coefS1STAPS1[3]
                        , "MOYENNE"
                        , sort124.index(EPS124[j])+1
                        #, (EPS124[j] >=10)
                        , creditS1STAPS1[3]
                        , creditS1STAPS1[3] if (EPS124[j] >=10) else 0  
                    ],

                    [ 
                        EPS125a[j]
                        , coefS1STAPS1[4]
                        , EPS125a[j]*coefS1STAPS1[4]
                        , "MOYENNE"
                        , sort125a.index(EPS125a[j])+1
                        #, (EPS125a[j] >=10)
                        , creditS1STAPS1[4]
                        , creditS1STAPS1[4] if((EPS125a[j]+EPS125g[j]+EPS125f[j]+EPS125j[j]) >= 40) else 0 
                    ], #crédits

                    #[ EPS125b[j], coefS1STAPS1[5], EPS125b[j]*coefS1STAPS1[5], "MOYENNE", sort125b.index(EPS125b[j])+1, (EPS125b[j] >=10), creditS1STAPS1[5], creditS1STAPS1[5] if(EPS125b[j] >=10) else 0 ],
                    [ 
                        EPS125g[j]
                        , coefS1STAPS1[13]
                        , EPS125g[j]*coefS1STAPS1[13]
                        , "MOYENNE"
                        , sort125g.index(EPS125g[j])+1
                        #, (EPS125g[j] >=10)
                        , creditS1STAPS1[13]
                        , creditS1STAPS1[13] if(EPS125g[j] >=10) else 0 
                    ],

                    [ 
                        EPS125j[j]
                        , coefS1STAPS1[6]
                        , EPS125j[j]*coefS1STAPS1[6]
                        , "MOYENNE"
                        , sort125j.index(EPS125j[j])+1
                        #, (EPS125j[j] >=10)
                        , creditS1STAPS1[6]
                        , creditS1STAPS1[6] if(EPS125j[j] >=10) else 0 
                    ],

                    #[ EPS125l[j], coefS1STAPS1[7], EPS125l[j]*coefS1STAPS1[7], "MOYENNE", sort125l.index(EPS125l[j])+1, (EPS125l[j] >=10), creditS1STAPS1[7], creditS1STAPS1[7] if (EPS125l[j] >=10) else 0  ],
                    [ 
                        EPS125f[j]
                        , coefS1STAPS1[8]
                        , EPS125f[j]*coefS1STAPS1[8]
                        , "MOYENNE"
                        , sort125f.index(EPS125f[j])+1
                        #, (EPS125f[j] >=10)
                        , creditS1STAPS1[8]
                        , creditS1STAPS1[8] if(EPS125f[j] >=10) else 0 
                    ],

                    [ 
                        EPS126[j]
                        , coefS1STAPS1[9]
                        , EPS126[j]*coefS1STAPS1[9]
                        , "MOYENNE"
                        , sort126.index(EPS126[j])+1
                        #, (EPS126[j] >=10)
                        , creditS1STAPS1[9]
                        , creditS1STAPS1[9] if(EPS126[j] >=10) else 0 
                    ],

                    [ 
                        EPS127[j]
                        , coefS1STAPS1[10]
                        , EPS127[j]*coefS1STAPS1[10]
                        , round( ((EPS127[j]*coefS1STAPS1[10]) + (EPS128[j]*coefS1STAPS1[10]) + (EPS129[j]*coefS1STAPS1[12])) / ( coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]) ,2)
                        , sort127.index(EPS127[j])+1
                        #, (EPS127[j] >=10)    
                        , creditS1STAPS1[10]
                        , creditS1STAPS1[10] if(EPS127[j] >=10) else 0
                    ],

                    [ 
                        EPS128[j]
                        , coefS1STAPS1[11]
                        , EPS128[j]*coefS1STAPS1[11]
                        , "MOYENNE"
                        , sort128.index(EPS128[j])+1
                        #, (EPS128[j] >=10)
                        , creditS1STAPS1[10]
                        , creditS1STAPS1[11] if(EPS128[j] >=10) else 0  
                    ],

                    [ 
                        EPS129[j]
                        , coefS1STAPS1[12]
                        , EPS129[j]*coefS1STAPS1[12]
                        , "MOYENNE"
                        , sort129.index(EPS129[j])+1
                        #, (EPS129[j] >=10)
                        , creditS1STAPS1[12] 
                        , creditS1STAPS1[12] if(EPS129[j] >=10) else 0 
                    ],

                    [ 
                        ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[13]+coefS1STAPS1[6]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12] ),

                        round( EPS121[j]*coefS1STAPS1[0]+EPS122[j]*coefS1STAPS1[1]+EPS123[j]*coefS1STAPS1[2]+EPS124[j]*coefS1STAPS1[3]+EPS125a[j]*coefS1STAPS1[4]+EPS125g[j]*coefS1STAPS1[13]+EPS125j[j]*coefS1STAPS1[6]+EPS125f[j]*coefS1STAPS1[8]+EPS126[j]*coefS1STAPS1[9]+EPS127[j]*coefS1STAPS1[10]+EPS128[j]*coefS1STAPS1[11]+EPS129[j]*coefS1STAPS1[12], 2),

                        round(( EPS121[j]*coefS1STAPS1[0]+EPS122[j]*coefS1STAPS1[1]+EPS123[j]*coefS1STAPS1[2]+EPS124[j]*coefS1STAPS1[3]+EPS125a[j]*coefS1STAPS1[4]+EPS125g[j]*coefS1STAPS1[13]+EPS125j[j]*coefS1STAPS1[6]+EPS125f[j]*coefS1STAPS1[8]+EPS126[j]*coefS1STAPS1[9]+EPS127[j]*coefS1STAPS1[10]+EPS128[j]*coefS1STAPS1[11]+EPS129[j]*coefS1STAPS1[12] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[13]+coefS1STAPS1[6]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]), 2 ),

                    ]
            ]
            staps2Moyenne.append(matrice[13][2])

            listeMatriceS2Eps.append(matrice)

        #infoEtudiantSTAPS1, coefS1STAPS1, creditS1STAPS1, EPS121, EPS122, EPS123, EPS124, EPS125a ,EPS125b, EPS125j, EPS125l, EPS126, EPS127, EPS128, EPS129, 

        staps2Moyenne.sort(reverse=True)
        moy2 = stat.mean(staps2Moyenne)
        moy2 = round(moy2, 2)
        session2 = 'Mai 2023'

        #semestre1MDS = [filiere, listeMatriceS1Eps, staps1MoyenneS1Eps, moyS1Eps, session, listeMatriceS1Eps ]  Venant du haut S1
        #semestre1MDS = [filiere, listeMatriceS1Eps, staps1MoyenneS1Eps, moyS1Eps, session, listeMatriceS1EpsSynthese, listeMatriceS2Eps ,staps2Moyenne ,moy2 ,session2]
        #semestre1MDS += [listeMatriceS2Eps ,staps2Moyenne ,moy2 ,session2]#[filiere, listeMatrice, staps1Moyenne, moy, session ]

################################################## SEMESTRE 2 EPS CC ########################################################################################################################################################
        listeMatriceS2EpsCC = []

        for j in range( len(infoEtudiantSTAPS1) ):

            matriceS2EpsCC = [

                infoEtudiantSTAPS1[j],

                EPS121cc[j]['note_cc'],

                EPS122cc[j]['note_cc'],

                EPS123cc[j]['note_cc'],

                EPS124cc[j]['note_cc'],

                EPS125acc[j]['note_cc'],

                #EPS125bcc[j]['note_cc'],

                EPS125gcc[j]['note_cc'],

                EPS125jcc[j]['note_cc'],

                #EPS125lcc[j]['note_cc'],

                EPS125fcc[j]['note_cc'],

                EPS126cc[j]['note_cc'],

                EPS127cc[j]['note_cc'],

                EPS128cc[j]['note_cc'],

                EPS129cc[j]['note_cc'],

            ]
            listeMatriceS2EpsCC.append(matriceS2EpsCC)

################################################## SEMESTRE 2 EPS RATTRAPAGE ################################################################################
        EPS121R = list(Evaluation.objects.filter(uniteEnseignement_id=99, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort121R = epurationRattrapage(EPS121R)

        EPS122R = list(Evaluation.objects.filter(uniteEnseignement_id=100, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort122R = epurationRattrapage(EPS122R)

        EPS123R = list(Evaluation.objects.filter(uniteEnseignement_id=101, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort123R = epurationRattrapage(EPS123R)

        EPS124R = list(Evaluation.objects.filter(uniteEnseignement_id=102, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort124R = epurationRattrapage(EPS124R)

        EPS125aR = list(Evaluation.objects.filter(uniteEnseignement_id=103, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort125aR = epurationRattrapage(EPS125aR)

        EPS125bR = list(Evaluation.objects.filter(uniteEnseignement_id=104, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort125bR= epurationRattrapage(EPS125bR) 

        EPS125gR = list(Evaluation.objects.filter(uniteEnseignement_id=124, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort125gR= epurationRattrapage(EPS125gR) 

        EPS125jR = list(Evaluation.objects.filter(uniteEnseignement_id=105, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort125jR = epurationRattrapage(EPS125jR)

        EPS125lR = list(Evaluation.objects.filter(uniteEnseignement_id=106, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort125lR = epurationRattrapage(EPS125lR)

        EPS125fR = list(Evaluation.objects.filter(uniteEnseignement_id=107, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort125fR = epurationRattrapage(EPS125fR)

        EPS126R = list(Evaluation.objects.filter(uniteEnseignement_id=108, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort126R = epurationRattrapage(EPS126R)

        EPS127R = list(Evaluation.objects.filter(uniteEnseignement_id=109, natureEvaluation='RATTRAPAGE').values('note_rattrapage')) 
        sort127R = epurationRattrapage(EPS127R)

        EPS128R = list(Evaluation.objects.filter(uniteEnseignement_id=110, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort128R = epurationRattrapage(EPS128R)

        EPS129R = list(Evaluation.objects.filter(uniteEnseignement_id=111, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
        sort129R = epurationRattrapage(EPS129R)


        listeMatriceS2epsR = [ ]

        for j in range( len(infoEtudiantSTAPS1)):

            matriceS2epsR = [

                infoEtudiantSTAPS1[j],

                EPS121R[j],

                EPS122R[j],

                EPS123R[j],

                EPS124R[j],

                EPS125aR[j],

                #EPS125bR[j],
                EPS125gR[j],

                EPS125jR[j],

                #EPS125lR[j],
                EPS125fR[j],

                EPS126R[j],

                EPS127R[j],

                EPS128R[j],

                EPS129R[j]
            ]
            listeMatriceS2epsR.append(matriceS2epsR)

################################################## SEMESTRE 2 EPS SYNTHESE ##################################################################################
        #Synthèse EPS2 Semestre 2

        #print(listeMatriceS2Eps)
        #print(listeMatriceS1Eps)

        #print(len(listeMatriceS2Eps))
        #print(len(listeMatriceS1Eps))

        listeMatriceS2EpsSynthese = matriceSyntheseEPS1(listeMatriceS2Eps, listeMatriceS2epsR, listeMatriceS1Eps, listeMatriceS2EpsCC)


        #Décompte de crédit
        EPSCreditCount2(listeMatriceS2EpsSynthese)

        #semestre1MDS = [filiere, listeMatriceS1Eps, staps1MoyenneS1Eps, moyS1Eps, session, listeMatriceS1Eps, listeMatriceS2EpsSynthese ] #, listeMatriceS2EpsSynthese
        semestre1MDS = [filiere, listeMatriceS1Eps, staps1MoyenneS1Eps, moyS1Eps, session, listeMatriceS1EpsSynthese, listeMatriceS2EpsSynthese[0] ,staps2Moyenne ,moy2 ,session2, listeMatriceS2EpsSynthese]#,listeMatriceS2Eps listeMatriceS2EpsSynthese]

    return render(request,'bulletin/BulletinTemplate/bullS2epsmds.html', {'semestre1MDS': semestre1MDS}) 







## NIVEAU 2 ##
################################################## STAPS2 ###############################################################################
#EPS2 SEMESTRE3
def bulls3eps2(request, filiere):
################################################## STAPS2 S3 ###############################################################################
    filiere = filiere

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=2).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=3,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = epurationCoef(coefS1STAPS1)

    creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=3,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS1 = epurationCre(creditS1STAPS1)

    EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=62, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=62, natureEvaluation='EXAMEN').values('note_cc'))
    EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=62, natureEvaluation='EXAMEN').values('note_sn'))
    sort111 = epurationTriCroissant(EPS111)

    EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=63, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=63, natureEvaluation='EXAMEN').values('note_cc'))
    EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=63, natureEvaluation='EXAMEN').values('note_sn'))
    sort112 = epurationTriCroissant(EPS112)

    EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=64, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=64, natureEvaluation='EXAMEN').values('note_cc'))
    EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=64, natureEvaluation='EXAMEN').values('note_sn'))
    sort113 = epurationTriCroissant(EPS113)

    EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=65, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=65, natureEvaluation='EXAMEN').values('note_cc'))
    EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=65, natureEvaluation='EXAMEN').values('note_sn'))
    sort114 = epurationTriCroissant(EPS114)

    EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=66, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=66, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=66, natureEvaluation='EXAMEN').values('note_sn'))
    sort115a = epurationTriCroissant(EPS115a)

    EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=67, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115bcc = list(Evaluation.objects.filter(uniteEnseignement_id=67, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115bsn = list(Evaluation.objects.filter(uniteEnseignement_id=67, natureEvaluation='EXAMEN').values('note_sn'))
    sort115b = epurationTriCroissant(EPS115b)

    EPS115f = list(Evaluation.objects.filter(uniteEnseignement_id=68, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115fcc = list(Evaluation.objects.filter(uniteEnseignement_id=68, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115fsn = list(Evaluation.objects.filter(uniteEnseignement_id=68, natureEvaluation='EXAMEN').values('note_sn'))
    sort115f = epurationTriCroissant(EPS115f)

    EPS115g = list(Evaluation.objects.filter(uniteEnseignement_id=69, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115gcc = list(Evaluation.objects.filter(uniteEnseignement_id=69, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115gsn = list(Evaluation.objects.filter(uniteEnseignement_id=69, natureEvaluation='EXAMEN').values('note_sn'))
    sort115g = epurationTriCroissant(EPS115g)

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=70, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=70, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=70, natureEvaluation='EXAMEN').values('note_sn'))
    sort115j = epurationTriCroissant(EPS115j)

    EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=71, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=71, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=71, natureEvaluation='EXAMEN').values('note_sn')) 
    sort115l = epurationTriCroissant(EPS115l)

    EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=72, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=72, natureEvaluation='EXAMEN').values('note_cc'))
    EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=72, natureEvaluation='EXAMEN').values('note_sn'))
    sort116 = epurationTriCroissant(EPS116)

    EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=73, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=73, natureEvaluation='EXAMEN').values('note_cc')) 
    EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=73, natureEvaluation='EXAMEN').values('note_sn')) 
    sort117 = epurationTriCroissant(EPS117)

    EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=74, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=74, natureEvaluation='EXAMEN').values('note_cc'))
    EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=74, natureEvaluation='EXAMEN').values('note_sn'))
    sort118 = epurationTriCroissant(EPS118)

    EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=75, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=75, natureEvaluation='EXAMEN').values('note_cc'))
    EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=75, natureEvaluation='EXAMEN').values('note_sn'))
    sort119 = epurationTriCroissant(EPS119)

    staps1Moyenne = []
    listeMatrice = []

    for j in range( len(infoEtudiantSTAPS1) ):
            matrice = [
                    infoEtudiantSTAPS1[j],

                    #ligne1
                    [
                        EPS111[j]
                        , coefS1STAPS1[0]
                        , EPS111[j]*coefS1STAPS1[0]
                        , round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1])) / (coefS1STAPS1[0]+coefS1STAPS1[1]), 2 )
                        , sort111.index(EPS111[j])+1
                        ,(EPS111[j]>=10)
                        , creditS1STAPS1[0]
                    ],

                    #ligne2
                    [
                        EPS112[j]
                        , coefS1STAPS1[1]
                        , EPS112[j]*coefS1STAPS1[1]
                        , "MOYENNE"
                        , sort112.index(EPS112[j])+1
                        , (EPS112[j]>=10)
                        , creditS1STAPS1[1]
                    ],

                    #ligne3
                    [
                        EPS113[j]
                        , coefS1STAPS1[2]
                        , EPS113[j]*coefS1STAPS1[2]
                        , round(  ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5])  + (EPS115f[j]*coefS1STAPS1[6]) + (EPS115g[j]*coefS1STAPS1[7]) + (EPS115j[j]*coefS1STAPS1[8]) + (EPS115l[j]*coefS1STAPS1[9]) + (EPS116[j]*coefS1STAPS1[10]) ) / ( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5] +coefS1STAPS1[6] +coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10] ), 2 )
                         #+ (EPS115f[j]*coefS1STAPS1[6]) +coefS1STAPS1[6]
                        , sort113.index(EPS113[j])+1
                        , (EPS113[j] >=10)
                        ,creditS1STAPS1[2]
                    ],

                    #ligne4
                    [
                        EPS114[j]
                        ,  coefS1STAPS1[3]
                        , EPS114[j]*coefS1STAPS1[3]
                        , "MOYENNE"
                        , sort114.index(EPS114[j])+1
                        , (EPS114[j] >=10)
                        , creditS1STAPS1[3]
                    ],

                    #ligne5
                    [
                        EPS115a[j]
                        , coefS1STAPS1[4]
                        , EPS115a[j]*coefS1STAPS1[4]
                        , "MOYENNE"
                        , sort115a.index(EPS115a[j])+1
                        , (EPS115a[j] >=10)
                        , creditS1STAPS1[4]
                    ], #crédits

                    #ligne6
                    [
                        EPS115b[j]
                        , coefS1STAPS1[5]
                        , EPS115b[j]*coefS1STAPS1[5]
                        , "MOYENNE"
                        , sort115b.index(EPS115b[j])+1
                        , (EPS115b[j] >=10)
                        , creditS1STAPS1[5]
                    ],

                    #ligne7
                    [
                        EPS115f[j]
                        , coefS1STAPS1[6]
                        , EPS115f[j]*coefS1STAPS1[6]
                        , "MOYENNE"
                        , sort115f.index(EPS115f[j])+1
                        , (EPS115f[j] >=10)
                        , creditS1STAPS1[6]
                    ],

                    #ligne8
                    [
                        EPS115g[j]
                        , coefS1STAPS1[7]
                        , EPS115g[j]*coefS1STAPS1[7]
                        , "MOYENNE"
                        , sort115g.index(EPS115g[j])+1
                        , (EPS115g[j] >=10)
                        , creditS1STAPS1[7]
                    ],

                    #ligne9
                    [
                        EPS115j[j]
                        , coefS1STAPS1[8]
                        , EPS115j[j]*coefS1STAPS1[8]
                        , "MOYENNE"
                        , sort115j.index(EPS115j[j])+1
                        , (EPS115j[j] >=10)
                        , creditS1STAPS1[8]
                    ],

                    #ligne10
                    [
                        EPS115l[j]
                        , coefS1STAPS1[9]
                        , EPS115l[j]*coefS1STAPS1[9]
                        , "MOYENNE"
                        , sort115l.index(EPS115l[j])+1
                        , (EPS115l[j] >=10)
                        , creditS1STAPS1[9]
                    ],

                    #ligne11
                    [
                        EPS116[j]
                        ,  coefS1STAPS1[10]
                        , EPS116[j]*coefS1STAPS1[10]
                        , "MOYENNE"
                        , sort116.index(EPS116[j])+1
                        , (EPS116[j] >=10)
                        , creditS1STAPS1[10]
                    ],

                    #ligne12
                    [
                        EPS117[j]
                        ,  coefS1STAPS1[11]
                        , EPS117[j]*coefS1STAPS1[11]
                        , round( ( (EPS117[j]*coefS1STAPS1[11]) + (EPS118[j]*coefS1STAPS1[12]) + (EPS119[j]*coefS1STAPS1[13]) ) / ( coefS1STAPS1[11]+coefS1STAPS1[12]+coefS1STAPS1[13]), 2 )
                        , sort117.index(EPS117[j])+1
                        , (EPS117[j] >=10)
                        , creditS1STAPS1[11]
                    ],

                    #ligne13
                    [
                        EPS118[j]
                        ,  coefS1STAPS1[12]
                        , EPS118[j]*coefS1STAPS1[12]
                        , "MOYENNE"
                        , sort118.index(EPS118[j])+1
                        , (EPS118[j] >=10)
                        , creditS1STAPS1[12]
                    ],

                    #ligne14
                    [
                        EPS119[j]
                        , coefS1STAPS1[13]
                        , EPS119[j]*coefS1STAPS1[13]
                        , "MOYENNE"
                        , sort119.index(EPS119[j])+1
                        , (EPS119[j] >=10)
                        , creditS1STAPS1[13]
                    ],

                    #ligne15
                    [
                        ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]  +coefS1STAPS1[6]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]+coefS1STAPS1[13]),  #+coefS1STAPS1[7]

                        round( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115f[j]*coefS1STAPS1[6] +EPS115g[j]*coefS1STAPS1[7] +EPS115j[j]*coefS1STAPS1[8]+EPS115l[j]*coefS1STAPS1[9]+EPS116[j]*coefS1STAPS1[10]+EPS117[j]*coefS1STAPS1[11]+EPS118[j]*coefS1STAPS1[12]+EPS119[j]*coefS1STAPS1[13] ,2), #+EPS115g[j]*coefS1STAPS1[7], 

                        round(( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115f[j]*coefS1STAPS1[6] + EPS115g[j]*coefS1STAPS1[7]  +EPS115j[j]*coefS1STAPS1[8]+EPS115l[j]*coefS1STAPS1[9]+EPS116[j]*coefS1STAPS1[10]+EPS117[j]*coefS1STAPS1[11]+EPS118[j]*coefS1STAPS1[12]+EPS119[j]*coefS1STAPS1[13] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]  +coefS1STAPS1[6] +coefS1STAPS1[7] +coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]+coefS1STAPS1[13] ), 2), #moyenne , , +coefS1STAPS1[7] , +EPS115g[j]*coefS1STAPS1[7]
                    ]
            ]

            listeMatrice.append(matrice)

            staps1Moyenne.append(matrice[15][2])
            staps1Moyenne.sort(reverse=True)

            moy = stat.mean(staps1Moyenne)
            moy = round(moy, 2)
            session = 'Janvier 2023'

################################################## STAPS2 S3 CC ###############################################################################
    listeMatriceEPS2s3CC = []

    for j in range( len(infoEtudiantSTAPS1) ):
        matriceS3Eps2CC = [

            infoEtudiantSTAPS1[j],

            EPS111cc[j]["note_cc"],

            EPS112cc[j]["note_cc"],

            EPS113cc[j]["note_cc"],

            EPS114cc[j]["note_cc"],

            EPS115acc[j]["note_cc"],

            EPS115bcc[j]["note_cc"],

            EPS115fcc[j]["note_cc"],

            EPS115gcc[j]["note_cc"],

            EPS115jcc[j]["note_cc"],

            EPS115lcc[j]["note_cc"],

            EPS116cc[j]["note_cc"],

            EPS117cc[j]["note_cc"],

            EPS118cc[j]["note_cc"],

            EPS119cc[j]["note_cc"],
        ]
        listeMatriceEPS2s3CC.append(matriceS3Eps2CC)

################################################## STAPS2 RATTRAPAGE SEMESTRE 3 ############################################################
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

            EPS111R[j]['note_rattrapage'],

            EPS112R[j]['note_rattrapage'],

            EPS113R[j]['note_rattrapage'],

            EPS114R[j]['note_rattrapage'],

            EPS115aR[j]['note_rattrapage'],

            EPS115bR[j]['note_rattrapage'],

            EPS115fR[j]['note_rattrapage'],

            EPS115gR[j]['note_rattrapage'],

            EPS115jR[j]['note_rattrapage'],

            EPS115lR[j]['note_rattrapage'],

            EPS116R[j]['note_rattrapage'],

            EPS117R[j]['note_rattrapage'],

            EPS118R[j]['note_rattrapage'],

            EPS119R[j]['note_rattrapage']
        ]
        listeMatriceR.append(matriceR)

################################################## STAPS2 SYNTHESE SEMESTRE 3 ############################################################

    listeMatriceSyntheseEps2S3, listeMoyenneEps2S3 = matriceSyntheseEPS2S3(listeMatrice, listeMatriceR, listeMatriceEPS2s3CC)

    #Décompte de crédits obtenus
    EPS2CreditCountS3(listeMatriceSyntheseEps2S3)


    semestre1MDS = [filiere , listeMatriceSyntheseEps2S3, staps1Moyenne, moy, session, listeMatriceR, listeMatrice]

    return render(request,'bulletin/BulletinTemplate/bullS1eps.html', {'semestre1MDS': semestre1MDS} )


#EPS2 SEMESTRE4
def bulls4eps2(request, filiere):
################################################## STAPS2 S3 #####################################################################################
    filiere = filiere

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=2).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=3,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = epurationCoef(coefS1STAPS1)

    creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=3,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS1 = epurationCre(creditS1STAPS1)

    EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=62, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=62, natureEvaluation='EXAMEN').values('note_cc'))
    EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=62, natureEvaluation='EXAMEN').values('note_sn'))
    sort111 = epurationTriCroissant(EPS111)

    EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=63, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=63, natureEvaluation='EXAMEN').values('note_cc'))
    EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=63, natureEvaluation='EXAMEN').values('note_sn'))
    sort112 = epurationTriCroissant(EPS112)

    EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=64, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=64, natureEvaluation='EXAMEN').values('note_cc'))
    EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=64, natureEvaluation='EXAMEN').values('note_sn'))
    sort113 = epurationTriCroissant(EPS113)

    EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=65, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=65, natureEvaluation='EXAMEN').values('note_cc'))
    EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=65, natureEvaluation='EXAMEN').values('note_sn'))
    sort114 = epurationTriCroissant(EPS114)

    EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=66, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=66, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=66, natureEvaluation='EXAMEN').values('note_sn'))
    sort115a = epurationTriCroissant(EPS115a)

    EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=67, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115bcc = list(Evaluation.objects.filter(uniteEnseignement_id=67, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115bsn = list(Evaluation.objects.filter(uniteEnseignement_id=67, natureEvaluation='EXAMEN').values('note_sn'))
    sort115b = epurationTriCroissant(EPS115b)

    EPS115f = list(Evaluation.objects.filter(uniteEnseignement_id=68, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115fcc = list(Evaluation.objects.filter(uniteEnseignement_id=68, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115fsn = list(Evaluation.objects.filter(uniteEnseignement_id=68, natureEvaluation='EXAMEN').values('note_sn'))
    sort115f = epurationTriCroissant(EPS115f)

    EPS115g = list(Evaluation.objects.filter(uniteEnseignement_id=69, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115gcc = list(Evaluation.objects.filter(uniteEnseignement_id=69, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115gsn = list(Evaluation.objects.filter(uniteEnseignement_id=69, natureEvaluation='EXAMEN').values('note_sn'))
    sort115g = epurationTriCroissant(EPS115g)

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=70, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=70, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=70, natureEvaluation='EXAMEN').values('note_sn'))
    sort115j = epurationTriCroissant(EPS115j)

    EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=71, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=71, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=71, natureEvaluation='EXAMEN').values('note_sn')) 
    sort115l = epurationTriCroissant(EPS115l)

    EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=72, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=72, natureEvaluation='EXAMEN').values('note_cc'))
    EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=72, natureEvaluation='EXAMEN').values('note_sn'))
    sort116 = epurationTriCroissant(EPS116)

    EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=73, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=73, natureEvaluation='EXAMEN').values('note_cc')) 
    EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=73, natureEvaluation='EXAMEN').values('note_sn')) 
    sort117 = epurationTriCroissant(EPS117)

    EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=74, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=74, natureEvaluation='EXAMEN').values('note_cc'))
    EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=74, natureEvaluation='EXAMEN').values('note_sn'))
    sort118 = epurationTriCroissant(EPS118)

    EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=75, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=75, natureEvaluation='EXAMEN').values('note_cc'))
    EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=75, natureEvaluation='EXAMEN').values('note_sn'))
    sort119 = epurationTriCroissant(EPS119)

    staps1Moyenne = []
    listeMatrice = []

    for j in range( len(infoEtudiantSTAPS1) ):
            matrice = [
                    infoEtudiantSTAPS1[j],

                    #ligne1
                    [
                        EPS111[j]
                        , coefS1STAPS1[0]
                        , EPS111[j]*coefS1STAPS1[0]
                        , round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1])) / (coefS1STAPS1[0]+coefS1STAPS1[1]), 2 )
                        , sort111.index(EPS111[j])+1
                        ,(EPS111[j]>=10)
                        , creditS1STAPS1[0]
                    ],

                    #ligne2
                    [
                        EPS112[j]
                        , coefS1STAPS1[1]
                        , EPS112[j]*coefS1STAPS1[1]
                        , "MOYENNE"
                        , sort112.index(EPS112[j])+1
                        , (EPS112[j]>=10)
                        , creditS1STAPS1[1]
                    ],

                    #ligne3
                    [
                        EPS113[j]
                        , coefS1STAPS1[2]
                        , EPS113[j]*coefS1STAPS1[2]
                        , round(  ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5])  + (EPS115f[j]*coefS1STAPS1[6]) + (EPS115g[j]*coefS1STAPS1[7]) + (EPS115j[j]*coefS1STAPS1[8]) + (EPS115l[j]*coefS1STAPS1[9]) + (EPS116[j]*coefS1STAPS1[10]) ) / ( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5] +coefS1STAPS1[6] +coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10] ), 2 )
                         #+ (EPS115f[j]*coefS1STAPS1[6]) +coefS1STAPS1[6]
                        , sort113.index(EPS113[j])+1
                        , (EPS113[j] >=10)
                        ,creditS1STAPS1[2]
                    ],

                    #ligne4
                    [
                        EPS114[j]
                        ,  coefS1STAPS1[3]
                        , EPS114[j]*coefS1STAPS1[3]
                        , "MOYENNE"
                        , sort114.index(EPS114[j])+1
                        , (EPS114[j] >=10)
                        , creditS1STAPS1[3]
                    ],

                    #ligne5
                    [
                        EPS115a[j]
                        , coefS1STAPS1[4]
                        , EPS115a[j]*coefS1STAPS1[4]
                        , "MOYENNE"
                        , sort115a.index(EPS115a[j])+1
                        , (EPS115a[j] >=10)
                        , creditS1STAPS1[4]
                    ], #crédits

                    #ligne6
                    [
                        EPS115b[j]
                        , coefS1STAPS1[5]
                        , EPS115b[j]*coefS1STAPS1[5]
                        , "MOYENNE"
                        , sort115b.index(EPS115b[j])+1
                        , (EPS115b[j] >=10)
                        , creditS1STAPS1[5]
                    ],

                    #ligne7
                    [
                        EPS115f[j]
                        , coefS1STAPS1[6]
                        , EPS115f[j]*coefS1STAPS1[6]
                        , "MOYENNE"
                        , sort115f.index(EPS115f[j])+1
                        , (EPS115f[j] >=10)
                        , creditS1STAPS1[6]
                    ],

                    #ligne8
                    [
                        EPS115g[j]
                        , coefS1STAPS1[7]
                        , EPS115g[j]*coefS1STAPS1[7]
                        , "MOYENNE"
                        , sort115g.index(EPS115g[j])+1
                        , (EPS115g[j] >=10)
                        , creditS1STAPS1[7]
                    ],

                    #ligne9
                    [
                        EPS115j[j]
                        , coefS1STAPS1[8]
                        , EPS115j[j]*coefS1STAPS1[8]
                        , "MOYENNE"
                        , sort115j.index(EPS115j[j])+1
                        , (EPS115j[j] >=10)
                        , creditS1STAPS1[8]
                    ],

                    #ligne10
                    [
                        EPS115l[j]
                        , coefS1STAPS1[9]
                        , EPS115l[j]*coefS1STAPS1[9]
                        , "MOYENNE"
                        , sort115l.index(EPS115l[j])+1
                        , (EPS115l[j] >=10)
                        , creditS1STAPS1[9]
                    ],

                    #ligne11
                    [
                        EPS116[j]
                        ,  coefS1STAPS1[10]
                        , EPS116[j]*coefS1STAPS1[10]
                        , "MOYENNE"
                        , sort116.index(EPS116[j])+1
                        , (EPS116[j] >=10)
                        , creditS1STAPS1[10]
                    ],

                    #ligne12
                    [
                        EPS117[j]
                        ,  coefS1STAPS1[11]
                        , EPS117[j]*coefS1STAPS1[11]
                        , round( ( (EPS117[j]*coefS1STAPS1[11]) + (EPS118[j]*coefS1STAPS1[12]) + (EPS119[j]*coefS1STAPS1[13]) ) / ( coefS1STAPS1[11]+coefS1STAPS1[12]+coefS1STAPS1[13]), 2 )
                        , sort117.index(EPS117[j])+1
                        , (EPS117[j] >=10)
                        , creditS1STAPS1[11]
                    ],

                    #ligne13
                    [
                        EPS118[j]
                        ,  coefS1STAPS1[12]
                        , EPS118[j]*coefS1STAPS1[12]
                        , "MOYENNE"
                        , sort118.index(EPS118[j])+1
                        , (EPS118[j] >=10)
                        , creditS1STAPS1[12]
                    ],

                    #ligne14
                    [
                        EPS119[j]
                        , coefS1STAPS1[13]
                        , EPS119[j]*coefS1STAPS1[13]
                        , "MOYENNE"
                        , sort119.index(EPS119[j])+1
                        , (EPS119[j] >=10)
                        , creditS1STAPS1[13]
                    ],

                    #ligne15
                    [
                        ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]  +coefS1STAPS1[6]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]+coefS1STAPS1[13]),  #+coefS1STAPS1[7]

                        round( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115f[j]*coefS1STAPS1[6] +EPS115g[j]*coefS1STAPS1[7] +EPS115j[j]*coefS1STAPS1[8]+EPS115l[j]*coefS1STAPS1[9]+EPS116[j]*coefS1STAPS1[10]+EPS117[j]*coefS1STAPS1[11]+EPS118[j]*coefS1STAPS1[12]+EPS119[j]*coefS1STAPS1[13] ,2), #+EPS115g[j]*coefS1STAPS1[7], 

                        round(( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115f[j]*coefS1STAPS1[6] + EPS115g[j]*coefS1STAPS1[7]  +EPS115j[j]*coefS1STAPS1[8]+EPS115l[j]*coefS1STAPS1[9]+EPS116[j]*coefS1STAPS1[10]+EPS117[j]*coefS1STAPS1[11]+EPS118[j]*coefS1STAPS1[12]+EPS119[j]*coefS1STAPS1[13] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]  +coefS1STAPS1[6] +coefS1STAPS1[7] +coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]+coefS1STAPS1[13] ), 2), #moyenne , , +coefS1STAPS1[7] , +EPS115g[j]*coefS1STAPS1[7]
                    ]
            ]

            listeMatrice.append(matrice)

            staps1Moyenne.append(matrice[15][2])
            staps1Moyenne.sort(reverse=True)

            moy = stat.mean(staps1Moyenne)
            moy = round(moy, 2)
            session = 'Janvier 2023'

################################################## STAPS2 S3 CC ##################################################################################
    listeMatriceEPS2s3CC = []

    for j in range( len(infoEtudiantSTAPS1) ):
        matriceS3Eps2CC = [

            infoEtudiantSTAPS1[j],

            EPS111cc[j]["note_cc"],

            EPS112cc[j]["note_cc"],

            EPS113cc[j]["note_cc"],

            EPS114cc[j]["note_cc"],

            EPS115acc[j]["note_cc"],

            EPS115bcc[j]["note_cc"],

            EPS115fcc[j]["note_cc"],

            EPS115gcc[j]["note_cc"],

            EPS115jcc[j]["note_cc"],

            EPS115lcc[j]["note_cc"],

            EPS116cc[j]["note_cc"],

            EPS117cc[j]["note_cc"],

            EPS118cc[j]["note_cc"],

            EPS119cc[j]["note_cc"],
        ]
        listeMatriceEPS2s3CC.append(matriceS3Eps2CC)

################################################## STAPS2 RATTRAPAGE SEMESTRE 3 ##################################################################
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

            EPS111R[j]['note_rattrapage'],

            EPS112R[j]['note_rattrapage'],

            EPS113R[j]['note_rattrapage'],

            EPS114R[j]['note_rattrapage'],

            EPS115aR[j]['note_rattrapage'],

            EPS115bR[j]['note_rattrapage'],

            EPS115fR[j]['note_rattrapage'],

            EPS115gR[j]['note_rattrapage'],

            EPS115jR[j]['note_rattrapage'],

            EPS115lR[j]['note_rattrapage'],

            EPS116R[j]['note_rattrapage'],

            EPS117R[j]['note_rattrapage'],

            EPS118R[j]['note_rattrapage'],

            EPS119R[j]['note_rattrapage']
        ]
        listeMatriceR.append(matriceR)

################################################## STAPS2 SYNTHESE SEMESTRE 3 ####################################################################
    listeMatriceSyntheseEps2S3, listeMoyenneEps2S3 = matriceSyntheseEPS2S3(listeMatrice, listeMatriceR, listeMatriceEPS2s3CC)

    #Décompte de crédits obtenus
    EPS2CreditCountS3(listeMatriceSyntheseEps2S3)

    semestre1MDS = [filiere , listeMatriceSyntheseEps2S3, staps1Moyenne, moy, session]

################################################## SEMESTRE 4 #####################################################################################
    infoEtudiantSTAPS2 =list(Etudiant.objects.filter(filiere="STAPS", niveau=2).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS2 = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("coefficient"))
    coefS1STAPS2 = epurationCoef(coefS1STAPS2)

    creditS1STAPS2 = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS2 = epurationCre(creditS1STAPS2)

    intitule_UE = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("intitule_UE"))
    code_UE = list(UniteEnseignement.objects.filter(semestre_id=4,filiere="STAPS").values("code_UE"))

    ##EPS240

    ##EPS241
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

                    #STAGE-PROFESSIONNEL 1
                    [
                        EPS1112[j]
                     , coefS1STAPS2[0]
                     , EPS1112[j]*coefS1STAPS2[0]
                     , round( (EPS1112[j]*coefS1STAPS2[0]+EPS115a2[j]*coefS1STAPS2[1]+EPS115f2[j]*coefS1STAPS2[2]+EPS115j2[j]*coefS1STAPS2[3]+EPS115g2[j]*coefS1STAPS2[4]+EPS1122[j]*coefS1STAPS2[5]+EPS1133[j]*coefS1STAPS2[6]+EPS1144[j]*coefS1STAPS2[7]+EPS1166[j]*coefS1STAPS2[8]+EPS1177[j]*coefS1STAPS2[9])/(coefS1STAPS2[0]+coefS1STAPS2[1]+coefS1STAPS2[2]+coefS1STAPS2[3]+coefS1STAPS2[4]+coefS1STAPS2[5]+coefS1STAPS2[6]+coefS1STAPS2[7]+coefS1STAPS2[8]+coefS1STAPS2[9]), 2)
                     , sort1112.index(EPS1112[j])+1
                     , (EPS1112[j]>=10)
                     , creditS1STAPS2[0]
                     , creditS1STAPS2[0] if (EPS1112[j]>=10) else 0
                     , EPS1112cc[j]['note_cc']
                     , EPS1112sn[j]['note_sn']
                    ],

                    #DIDACTIQUE DES APS 2
                    [
                        EPS115a2[j]
                        , coefS1STAPS2[1]
                        , EPS115a2[j]*coefS1STAPS2[1]
                        , round( (EPS115a2[j]*coefS1STAPS2[1]+EPS115f2[j]*coefS1STAPS2[2]+EPS115j2[j]*coefS1STAPS2[3]+EPS115g2[j]*coefS1STAPS2[4])/(coefS1STAPS2[1]+coefS1STAPS2[2]+coefS1STAPS2[3]+coefS1STAPS2[4]), 2 ) #Moyenne des APS
                        , sort115a2.index(EPS115a2[j])+1
                        , (EPS115a2[j] >=10)
                        , creditS1STAPS2[1]
                        , creditS1STAPS2[1] if (EPS115a2[j] >=10) else 0
                        , EPS115a2cc[j]['note_cc']
                        , EPS115a2sn[j]['note_sn']
                    ],

                    [
                        EPS115f2[j]
                        , coefS1STAPS2[2]
                        , EPS115f2[j]*coefS1STAPS2[2]
                        , "MOYENNE"
                        , sort115f2.index(EPS115f2[j])+1
                        , (EPS115f2[j] >=10)
                        , creditS1STAPS2[2]
                        , creditS1STAPS2[2] if (EPS115f2[j] >=10) else 0
                        , EPS115f2cc[j]['note_cc']
                        , EPS115f2sn[j]['note_sn']
                    ],

                    [
                        EPS115j2[j]
                        , coefS1STAPS2[3]
                        , EPS115j2[j]*coefS1STAPS2[3]
                        , "MOYENNE"
                        , sort115j2.index(EPS115j2[j])+1
                        , (EPS115j2[j] >=10)
                        , creditS1STAPS2[3]
                        , creditS1STAPS2[3] if (EPS115j2[j] >=10) else 0
                        , EPS115j2cc[j]['note_cc']
                        , EPS115j2sn[j]['note_sn']
                    ],

                    [
                        EPS115g2[j]
                        , coefS1STAPS2[4]
                        , EPS115g2[j]*coefS1STAPS2[4]
                        , round( (EPS115a2[j]*coefS1STAPS2[1]+EPS115f2[j]*coefS1STAPS2[2]+EPS115j2[j]*coefS1STAPS2[3]+EPS115g2[j]*coefS1STAPS2[4])/(coefS1STAPS2[1]+coefS1STAPS2[2]+coefS1STAPS2[3]+coefS1STAPS2[4]), 2 )
                        , sort115g2.index(EPS115g2[j])+1
                        , (EPS115g2[j] >=10)
                        , creditS1STAPS2[4]
                        , creditS1STAPS2[4] if ( (EPS115a2[j]+EPS115f2[j]+EPS115j2[j]+EPS115g2[j]) >=40) else 0
                        , EPS115g2cc[j]['note_cc']
                        , EPS115g2sn[j]['note_sn']
                    ],

                    #ANATOMIE 6
                    [
                        EPS1122[j]
                        , coefS1STAPS2[5]
                        , EPS1122[j]*coefS1STAPS2[5]
                        , "MOYENNE"
                        , sort1122.index(EPS1122[j])+1
                        , (EPS1122[j]>=10)
                        , creditS1STAPS2[5]
                        , creditS1STAPS2[5] if (EPS1122[j]>=10) else 0
                        , EPS1122cc[j]['note_cc']
                        , EPS1122sn[j]['note_sn']
                    ],

                    #PHYSIOLOGIE 7
                    [ 
                        EPS1133[j]
                        , coefS1STAPS2[6]
                        , EPS1133[j]*coefS1STAPS2[6]
                        , "MOYENNE"
                        , sort1133.index(EPS1133[j])+1
                        , (EPS1133[j] >=10)
                        , creditS1STAPS2[6]
                        , creditS1STAPS2[6] if (EPS1133[j] >=10) else 0
                        , EPS1133cc[j]['note_cc']
                        , EPS1133sn[j]['note_sn'] 
                    ],

                    #EDUCATION PHYSIQUE : LOISIRS II 8 
                    [
                        EPS1144[j]
                        ,  coefS1STAPS2[7]
                        , EPS1144[j]*coefS1STAPS2[7]
                        , "MOYENNE"
                        , sort1144.index(EPS1144[j])+1
                        , (EPS1144[j] >=10)
                        , creditS1STAPS2[7]
                        , creditS1STAPS2[7] if (EPS1144[j] >=10) else 0
                        , EPS1144cc[j]['note_cc']
                        , EPS1144sn[j]['note_sn']
                    ],

                    #TRAUMATOLOGIE - PREMIERS SECOURS 9
                    [ 
                        EPS1166[j]
                        ,  coefS1STAPS2[8]
                        , EPS1166[j]*coefS1STAPS2[8]
                        , "MOYENNE"
                        , sort1166.index(EPS1166[j])+1
                        , (EPS1166[j] >=10)
                        , creditS1STAPS2[8]
                        , creditS1STAPS2[8] if (EPS1166[j] >=10) else 0
                        , EPS1166cc[j]['note_cc']
                        , EPS1166sn[j]['note_sn'] 
                    ],

                    #PEDAGOGIE PRATIQUE III 10
                    [ 
                        EPS1177[j]
                        ,  coefS1STAPS2[9]
                        , EPS1177[j]*coefS1STAPS2[9]
                        , round( (EPS1112[j]*coefS1STAPS2[0]+EPS115a2[j]*coefS1STAPS2[1]+EPS115f2[j]*coefS1STAPS2[2]+EPS115j2[j]*coefS1STAPS2[3]+EPS115g2[j]*coefS1STAPS2[4]+EPS1122[j]*coefS1STAPS2[5]+EPS1133[j]*coefS1STAPS2[6]+EPS1144[j]*coefS1STAPS2[7]+EPS1166[j]*coefS1STAPS2[8]+EPS1177[j]*coefS1STAPS2[9])/(coefS1STAPS2[0]+coefS1STAPS2[1]+coefS1STAPS2[2]+coefS1STAPS2[3]+coefS1STAPS2[4]+coefS1STAPS2[5]+coefS1STAPS2[6]+coefS1STAPS2[7]+coefS1STAPS2[8]+coefS1STAPS2[9]), 2)
                        , sort1177.index(EPS1177[j])+1
                        , (EPS1177[j] >=10)
                        , creditS1STAPS2[9]
                        , creditS1STAPS2[9] if (EPS1177[j] >=10) else 0
                        , EPS1177cc[j]['note_cc']
                        , EPS1177sn[j]['note_sn'] 
                    ],

                    #ECONOMIE  11
                    [
                        EPS1188[j]
                        ,  coefS1STAPS2[10]
                        , EPS1188[j]*coefS1STAPS2[10]
                        , 'MOYENNE'#round( (EPS1188[j]*coefS1STAPS2[10]+EPS1199[j]*coefS1STAPS2[11]) / (coefS1STAPS2[10]+coefS1STAPS2[11]) ,2)
                        , sort1188.index(EPS1188[j])+1
                        , (EPS1188[j] >=10)
                        , creditS1STAPS2[10]
                        , creditS1STAPS2[10] if (EPS1188[j] >=10) else 0
                        , EPS1188cc[j]['note_cc']
                        , EPS1188sn[j]['note_sn']
                    ],

                    #FRANCAIS 12
                    [
                        EPS1199[j]
                        , coefS1STAPS2[11]
                        , EPS1199[j]*coefS1STAPS2[11]
                        , round( (EPS1188[j]*coefS1STAPS2[10]+EPS1199[j]*coefS1STAPS2[11]) / (coefS1STAPS2[10]+coefS1STAPS2[11]) ,2)
                        , sort1199.index(EPS1199[j])+1
                        , (EPS1199[j] >=10)
                        , creditS1STAPS2[11]
                        #, creditS1STAPS2[11] if (EPS1199[j] >=10) else 0
                        , EPS1199cc[j]['note_cc']
                        , EPS1199sn[j]['note_sn']
                    ],


                    #SOMME 13
                    [
                        ( coefS1STAPS2[0]+coefS1STAPS2[1]+coefS1STAPS2[2]+coefS1STAPS2[3]+coefS1STAPS2[4]+coefS1STAPS2[5]+coefS1STAPS2[6]+coefS1STAPS2[7]+coefS1STAPS2[8]+coefS1STAPS2[9]+coefS1STAPS2[10]+coefS1STAPS2[11]), 

                        round( EPS1112[j]*coefS1STAPS2[0]+EPS115a2[j]*coefS1STAPS2[1]+EPS115f2[j]*coefS1STAPS2[2]+EPS115j2[j]*coefS1STAPS2[3]+EPS115g2[j]*coefS1STAPS2[4]+EPS1122[j]*coefS1STAPS2[5]+EPS1133[j]*coefS1STAPS2[6]+EPS1144[j]*coefS1STAPS2[7]+EPS1166[j]*coefS1STAPS2[8]+EPS1177[j]*coefS1STAPS2[9]+EPS1188[j]*coefS1STAPS2[10]+EPS1199[j]*coefS1STAPS2[11] ,2),

                        round(( EPS1112[j]*coefS1STAPS2[0]+EPS115a2[j]*coefS1STAPS2[1]+EPS115f2[j]*coefS1STAPS2[2]+EPS115j2[j]*coefS1STAPS2[3]+EPS115g2[j]*coefS1STAPS2[4]+EPS1122[j]*coefS1STAPS2[5]+EPS1133[j]*coefS1STAPS2[6]+EPS1144[j]*coefS1STAPS2[7]+EPS1166[j]*coefS1STAPS2[8]+EPS1177[j]*coefS1STAPS2[9]+EPS1188[j]*coefS1STAPS2[10]+EPS1199[j]*coefS1STAPS2[11] ) / ( coefS1STAPS2[0]+coefS1STAPS2[1]+coefS1STAPS2[2]+coefS1STAPS2[3]+coefS1STAPS2[4]+coefS1STAPS2[5]+coefS1STAPS2[6]+coefS1STAPS2[7]+coefS1STAPS2[8]+coefS1STAPS2[9]+coefS1STAPS2[10]+coefS1STAPS2[11]), 2), #moyenne
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

################################################## STAPS2 S4 CC ##################################################################################
    listeMatriceEPS2s4CC = []

    for j in range( len(infoEtudiantSTAPS1) ):
        matriceS4Eps2CC = [

            infoEtudiantSTAPS1[j],

            ##EPS240

            ##EPS241

            EPS1112cc[j]["note_cc"],

            EPS115a2cc[j]["note_cc"],

            EPS115f2cc[j]["note_cc"],

            EPS115j2cc[j]["note_cc"],

            EPS115g2cc[j]["note_cc"],

            EPS1122cc[j]["note_cc"],

            EPS1133cc[j]["note_cc"],

            EPS1144cc[j]["note_cc"],

            EPS1166cc[j]["note_cc"],

            EPS115lcc[j]["note_cc"],

            EPS116cc[j]["note_cc"],

            EPS1177cc[j]["note_cc"],

            EPS1188cc[j]["note_cc"],

            EPS1199cc[j]["note_cc"],
        ]
        listeMatriceEPS2s4CC.append(matriceS4Eps2CC)

################################################## MATRICE RATTRAPPAGE SEMESTRE 4 #################################################################
    ##EPS240

    ##EPS241

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
    listematriceSynthese = matriceSynthese(listeMatrice2, listMatriceRattrapage, listeMatriceSyntheseEps2S3)
    EPS2CreditCountS4(listematriceSynthese[0])
    semestre1MDS.append(listematriceSynthese)

    listeSyntheseTest, listeR, listeE = matriceSyntheseEPS2S4( listeMatrice2, listMatriceRattrapage, listeMatriceEPS2s4CC, listeMatriceSyntheseEps2S3 )
    #Test
    semestre1MDS.append(listeSyntheseTest)
    semestre1MDS.append(listeR)
    #semestre1MDS.append(listeE)
    #semestre1MDS.append(listeMatriceSyntheseEps2S3)

    #Decompte Semestre 4
    # Ligne commentée afin d'éviter l'effet de bord
    #EPS2CreditCountS4(listeSyntheseTest)
    semestre1MDS.append(listeSyntheseTest)

    return render( request,'bulletin/BulletinTemplate/bullS4eps.html', {'semestre1MDS': semestre1MDS} )




## NIVEAU 3##
#EVE SEMESTRE5
def bulls5msoeve(request, filiere):

    infoEtudiantEVE = list( Etudiant.objects.filter(filiere="MAS", niveau=3, Specialite="EVENEMENTIEL").values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS5EVE = list( UniteEnseignement.objects.filter(semestre_id=5,filiere="MAS").values("coefficient", "intitule_UE"))
    coefS5EVE = epurationCoef(coefS5EVE)

    creditS5EVE = list(UniteEnseignement.objects.filter(semestre_id=5,filiere="MAS").values("nombre_credit"))
    creditS5EVE = epurationCre(creditS5EVE)

    MAS315 = list(Evaluation.objects.filter(uniteEnseignement_id=76, natureEvaluation='EXAMEN').values('note_Examen')) #,'note_cc','note_sn'))
    sort315 = epurationTriCroissant(MAS315)

    MAS325 = list(Evaluation.objects.filter(uniteEnseignement_id=77, natureEvaluation='EXAMEN').values('note_Examen'))
    sort325 = epurationTriCroissant(MAS325)

    MAS335 = list(Evaluation.objects.filter(uniteEnseignement_id=78, natureEvaluation='EXAMEN').values('note_Examen'))
    sort335 = epurationTriCroissant(MAS335)

    MAS345 = list(Evaluation.objects.filter(uniteEnseignement_id=79, natureEvaluation='EXAMEN').values('note_Examen'))
    sort345 = epurationTriCroissant(MAS345)

    EVE355 = list(Evaluation.objects.filter(uniteEnseignement_id=80, natureEvaluation='EXAMEN').values('note_Examen'))
    sort355 = epurationTriCroissant(EVE355)

    EVE365 = list(Evaluation.objects.filter(uniteEnseignement_id=81, natureEvaluation='EXAMEN').values('note_Examen'))
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
    
                round( (MAS315[j]*coefS5EVE[0] + MAS325[j]*coefS5EVE[1] + MAS335[j]*coefS5EVE[2] + MAS345[j]*coefS5EVE[3] + EVE355[j]*coefS5EVE[4] + EVE365[j]*coefS5EVE[5] ), 2),

                round((MAS315[j]*coefS5EVE[0] + MAS325[j]*coefS5EVE[1] + MAS335[j]*coefS5EVE[2] + MAS345[j]*coefS5EVE[3] + EVE355[j]*coefS5EVE[4] + EVE365[j]*coefS5EVE[5])/(coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),2)
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
############################################################### SEMESTRE 5 EVE ###################################################################################################
    infoEtudiantEVE = list( Etudiant.objects.filter(filiere="MAS", niveau=3, Specialite="EVENEMENTIEL").values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS5EVE = list( UniteEnseignement.objects.filter(semestre_id=5,filiere="MAS").values("coefficient", "intitule_UE"))
    coefS5EVE = epurationCoef(coefS5EVE)

    creditS5EVE = list(UniteEnseignement.objects.filter(semestre_id=5,filiere="MAS").values("nombre_credit"))
    creditS5EVE = epurationCre(creditS5EVE)

    MAS315 = list(Evaluation.objects.filter(uniteEnseignement_id=76, natureEvaluation='EXAMEN').values('note_Examen')) #,'note_cc','note_sn'))
    sort315 = epurationTriCroissant(MAS315)
    MAS315cc = list(Evaluation.objects.filter(uniteEnseignement_id=76, natureEvaluation='EXAMEN').values('note_cc'))

    MAS325 = list(Evaluation.objects.filter(uniteEnseignement_id=77, natureEvaluation='EXAMEN').values('note_Examen'))
    sort325 = epurationTriCroissant(MAS325)
    MAS325cc = list(Evaluation.objects.filter(uniteEnseignement_id=77, natureEvaluation='EXAMEN').values('note_cc'))

    MAS335 = list(Evaluation.objects.filter(uniteEnseignement_id=78, natureEvaluation='EXAMEN').values('note_Examen'))
    sort335 = epurationTriCroissant(MAS335)
    MAS335cc = list(Evaluation.objects.filter(uniteEnseignement_id=78, natureEvaluation='EXAMEN').values('note_cc'))

    MAS345 = list(Evaluation.objects.filter(uniteEnseignement_id=79, natureEvaluation='EXAMEN').values('note_Examen'))
    sort345 = epurationTriCroissant(MAS345)
    MAS345cc = list(Evaluation.objects.filter(uniteEnseignement_id=79, natureEvaluation='EXAMEN').values('note_cc'))

    EVE355 = list(Evaluation.objects.filter(uniteEnseignement_id=80, natureEvaluation='EXAMEN').values('note_Examen'))
    sort355 = epurationTriCroissant(EVE355)
    EVE355cc = list(Evaluation.objects.filter(uniteEnseignement_id=80, natureEvaluation='EXAMEN').values('note_cc'))

    EVE365 = list(Evaluation.objects.filter(uniteEnseignement_id=81, natureEvaluation='EXAMEN').values('note_Examen'))
    sort365 = epurationTriCroissant(EVE365)
    EVE365cc = list(Evaluation.objects.filter(uniteEnseignement_id=81, natureEvaluation='EXAMEN').values('note_cc'))

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
        session = 'Janvier 2023'

############################################################### SEMESTRE 5 EVE RATTRAPAGE ###################################################################################################    
    MAS315R = list(Evaluation.objects.filter(uniteEnseignement_id=76, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort316 = epurationRattrapage(MAS315R)

    MAS325R = list(Evaluation.objects.filter(uniteEnseignement_id=77, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort326 = epurationRattrapage(MAS325R)

    MAS335R = list(Evaluation.objects.filter(uniteEnseignement_id=78, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort336 = epurationRattrapage(MAS335R)

    MAS345R = list(Evaluation.objects.filter(uniteEnseignement_id=79, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort346 = epurationRattrapage(MAS345R)

    EVE355R = list(Evaluation.objects.filter(uniteEnseignement_id=80, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort356 = epurationRattrapage(EVE355R)

    EVE365R = list(Evaluation.objects.filter(uniteEnseignement_id=81, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort366 = epurationRattrapage(EVE365R)

    listeMatriceRs5EVE = []
    listeMatriceRs5EVEex = []
    

    for j in range (len(infoEtudiantEVE)):
        matriceRs5EVE = [

            infoEtudiantEVE[j],
            
            MAS315R[j],

            MAS325R[j],
            
            MAS335R[j],
            
            MAS345R[j],
            
            EVE355R[j],
            
            EVE365R[j],
        ]

        matriceRs5EVEex = [

            infoEtudiantEVE[j],
            
            ( round( MAS315R[j]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (MAS315R[j] > 0) else MAS315R[j] ) ,

            ( round( MAS325R[j]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (MAS325R[j] > 0) else MAS325R[j] ) ,
            
            ( round( MAS335R[j]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (MAS335R[j] > 0) else MAS335R[j] ) ,
            
            ( round( MAS345R[j]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (MAS345R[j] > 0) else MAS345R[j] ) ,
            
            ( round( EVE355R[j]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (EVE355R[j] > 0) else EVE355R[j] ) ,
            
            ( round( EVE365R[j]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (EVE365R[j] > 0) else EVE365R[j] ) ,
        ]
        listeMatriceRs5EVE.append(matriceRs5EVE)
        listeMatriceRs5EVEex.append(matriceRs5EVEex)

############################################################### SEMESTRE 5 EVE SYNTHESE   ###################################################################################################
    listeMatriceS5 =  []
    EVEMoyennes5 = []

    for j in range( len(infoEtudiantEVE) ):

        matricesS5EVE = [
            
            infoEtudiantEVE[j],

            [ 
                ( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) 
                
                , coefS5EVE[0]
                
                , round(( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0], 2)

                , round( ((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0]) + (MAS325[j]*coefS5EVE[1]) + (MAS335[j]*coefS5EVE[2]) + (MAS345[j]*coefS5EVE[3])) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]), 2)
                
                , sort315.index(( MAS315[j] ) )+1 #round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else

                , (( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] )  >=10)

                , creditS5EVE[0]

                , creditS5EVE[0] if((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] )  >=10)) else 0

                , ("RATTRAPAGE" if listeMatriceRs5EVE[j][1]> 0 else " ")
                
                #, MAS315cc[j]['note_cc']
                
                #, MAS315sn[j]['note_sn'],
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) 
                
                , coefS5EVE[1]
                
                , round(( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) *coefS5EVE[1], 2)
                
                , 'MOYENNE'
                
                , sort325.index((  MAS325[j] ) )+1 #round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else
                
                , (( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) >=10)

                , creditS5EVE[1]
                
                , creditS5EVE[1] if (( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) >=10) else 0

                , ("RATTRAPAGE" if listeMatriceRs5EVE[j][2]> 0 else " ")
                
                #, MAS325cc[j]['note_cc']
                
                #, MAS325sn[j]['note_sn'],  
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) 
                
                , coefS5EVE[2]
                
                , round(( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) *coefS5EVE[2], 2)
                
                , 'MOYENNE'
                
                , sort335.index((  MAS335[j] ) )+1 #round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else
                
                , (( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) >=10)
                
                , creditS5EVE[2]
                
                , creditS5EVE[2] if (( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) >=10) else 0

                , ("RATTRAPAGE" if listeMatriceRs5EVE[j][3]> 0 else " ")
                
                #, MAS335cc[j]['note_cc']
                
                #, MAS335sn[j]['note_sn'] 
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )
                
                , coefS5EVE[3]
                
                , round(( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3], 2)
                
                , 'MOYENNE'
                
                , sort345.index((  MAS345[j] ))+1 #round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else
                 
                , (( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )>=10)
                
                , creditS5EVE[3]
                
                , creditS5EVE[3] if (( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )>=10) else 0

                , ("RATTRAPAGE" if listeMatriceRs5EVE[j][4]> 0 else " ")
                
                #, MAS345cc[j]['note_cc']
                
                #, MAS345sn[j]['note_sn']
                
                #, [ ( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) , ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) , ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) , ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )], MAS345R[j] 
                
                ],
            
            #MODULE 2
            [ 
                ( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )
                
                , coefS5EVE[4]
                
                , round(( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4], 2)

                , round((( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4] + ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] ) *coefS5EVE[5] )/(coefS5EVE[4]+coefS5EVE[5]), 2)

                , sort355.index((  EVE355[j] ))+1 #round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else

                , (( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )>=10)

                , creditS5EVE[4]

                , creditS5EVE[4] if((( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )>=10)) else 0

                , ("RATTRAPAGE" if listeMatriceRs5EVE[j][5]> 0 else " ")

                #, EVE355cc[j]['note_cc']
                
                #, EVE355sn[j]['note_sn']

                #, EVE355R[j]['note_rattrapage']
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] ) 
                
                , coefS5EVE[5]
                
                , round(( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )*coefS5EVE[5], 2)
                
                , 'MOYENNE'
                
                , sort365.index((  EVE365[j] ))+1 #round(listeMatriceRs5EVE[j][6]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else
                
                , (( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )>=10)
                
                , creditS5EVE[5]
                
                , creditS5EVE[5] if (( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )>=10) else 0

                , ("RATTRAPAGE" if listeMatriceRs5EVE[j][6]> 0 else " ")
                
                #, EVE365cc[j]['note_cc']
                
                #, EVE365sn[j]['note_sn']
                
                #, [ ( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] ), ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] ) ], EVE365R[j] 
            ],

            [ 
                (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),
    
                round( (( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0] + ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) *coefS5EVE[1] + ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) *coefS5EVE[2] + ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3]+( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4] + ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )*coefS5EVE[5] ), 2),

                round((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0] + MAS325[j]*coefS5EVE[1] + ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) *coefS5EVE[2] + ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3] + ( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4] + ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )*coefS5EVE[5])/(coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]), 2)
            ],
        ]

        listeMatriceS5.append(matricesS5EVE)
        EVEMoyennes5.append(matricesS5EVE[7][2])
    
    EVEMoyennes5.sort(reverse=True)

    moys5 = stat.mean(EVEMoyennes5)
    moys5 = round(moys5, 2)
    sessions5 = 'Janvier 2023'


    semestre1MDS = [filiere, listeMatriceS5, EVEMoyennes5, moy, sessions5] #listeMatriceS5 , EVEMoyennes5,  sessions5


############################################################### SEMESTRE 6 EVE ###################################################################################################
    infoEtudiantEVE = list( Etudiant.objects.filter(filiere="MAS", niveau=3, Specialite="EVENEMENTIEL").values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS5EVE = list( UniteEnseignement.objects.filter(semestre_id=6,filiere="MAS").values("coefficient", "intitule_UE"))
    coefS5EVE = epurationCoef(coefS5EVE)

    creditS5EVE = list(UniteEnseignement.objects.filter(semestre_id=6,filiere="MAS").values("nombre_credit"))
    creditS5EVE = epurationCre(creditS5EVE)

    MAS316 = list(Evaluation.objects.filter(uniteEnseignement_id=82, natureEvaluation='EXAMEN').values('note_Examen'))#,'note_cc','note_sn'))
    sort316 = epurationTriCroissant(MAS316)

    MAS326 = list(Evaluation.objects.filter(uniteEnseignement_id=83, natureEvaluation='EXAMEN').values('note_Examen'))
    sort326 = epurationTriCroissant(MAS326)

    MAS336 = list(Evaluation.objects.filter(uniteEnseignement_id=84, natureEvaluation='EXAMEN').values('note_Examen'))
    sort336 = epurationTriCroissant(MAS336)

    MAS346 = list(Evaluation.objects.filter(uniteEnseignement_id=85, natureEvaluation='EXAMEN').values('note_Examen'))
    sort346 = epurationTriCroissant(MAS346)

    EVE356 = list(Evaluation.objects.filter(uniteEnseignement_id=86, natureEvaluation='EXAMEN').values('note_Examen'))
    sort356 = epurationTriCroissant(EVE356)

    EVE366 = list(Evaluation.objects.filter(uniteEnseignement_id=87, natureEvaluation='EXAMEN').values('note_Examen'))
    sort366 = epurationTriCroissant(EVE366)

    listeMatrice2 = []
    EVEMoyenne2 = []

    for j in range( len(infoEtudiantEVE) ):

        matrice = [
            
            infoEtudiantEVE[j],

            [ MAS316[j], coefS5EVE[0], round(MAS316[j]*coefS5EVE[0], 2),

                round( ((MAS316[j]*coefS5EVE[0]) + (MAS326[j]*coefS5EVE[1]) + (MAS336[j]*coefS5EVE[2]+ (MAS346[j]*coefS5EVE[3])) ) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3] ), 2), #, 

                sort316.index(MAS316[j])+1, 

                (MAS316[j] >=10),

                creditS5EVE[0],

                creditS5EVE[0] if (MAS316[j] >=10) else 0 
            ],
            
            [ MAS326[j], coefS5EVE[1], round(MAS326[j]*coefS5EVE[1], 2), 'MOYENNE', sort326.index(MAS326[j])+1, (MAS326[j]>=10) ,creditS5EVE[1], creditS5EVE[1] if (MAS326[j]>=10) else 0 ],
            
            [ MAS336[j], coefS5EVE[2], round(MAS336[j]*coefS5EVE[2], 2), 'MOYENNE', sort336.index(MAS336[j])+1, (MAS336[j]>=10), creditS5EVE[2], creditS5EVE[2] if (MAS336[j]>=10) else 0 ],
            
            [ MAS346[j], coefS5EVE[3], round(MAS346[j]*coefS5EVE[3], 2), 'MOYENNE', sort346.index(MAS346[j])+1, (MAS346[j]>=10), creditS5EVE[3], creditS5EVE[3] if (MAS346[j]>=10) else 0 ],
            
            [ EVE356[j], coefS5EVE[4], round(EVE356[j]*coefS5EVE[4], 2), 

                round((EVE356[j]*coefS5EVE[4] + EVE366[j]*coefS5EVE[5] )/(coefS5EVE[4]+coefS5EVE[5]), 2), 

                sort356.index(EVE356[j])+1, 

                (EVE356[j]>=10),

                creditS5EVE[4],

                creditS5EVE[4] if (EVE356[j]>=10) else 0
            ],
            
            [ EVE366[j], coefS5EVE[5], round(EVE366[j]*coefS5EVE[5], 2), 'MOYENNE', sort366.index(EVE366[j])+1, (EVE366[j]>=10), creditS5EVE[5], creditS5EVE[5] if(EVE366[j]>=10)  else 0 ],
        
            [ 
                (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),
    
                round( (MAS316[j]*coefS5EVE[0] + MAS326[j]*coefS5EVE[1] + MAS336[j]*coefS5EVE[2]+ MAS346[j]*coefS5EVE[3] +EVE356[j]*coefS5EVE[4] + EVE366[j]*coefS5EVE[5] ), 2), #

                round( (MAS316[j]*coefS5EVE[0] + MAS326[j]*coefS5EVE[1] + MAS336[j]*coefS5EVE[2]+ MAS346[j]*coefS5EVE[3]  +EVE356[j]*coefS5EVE[4] + EVE366[j]*coefS5EVE[5])/(coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),2) # , 
            ]
        ]

        creditObtenus = 0
        listeCredit = []

       
        listeMatrice2.append(matrice)
        EVEMoyenne2.append(matrice[7][2])
        EVEMoyenne2.sort(reverse=True)

        moy2 = stat.mean(EVEMoyenne2)
        moy2 = round(moy2, 2)
        session2 = 'Mai 2023'

############################################################### SEMESTRE 6 EVE RATTRAPAGE ###################################################################################################
    infoMAS316R = ""
    MAS316R = list(Evaluation.objects.filter(uniteEnseignement_id=82, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort315 = epurationRattrapage(MAS316R)

    infoMAS326R = ""
    MAS326R = list(Evaluation.objects.filter(uniteEnseignement_id=83, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort325 = epurationRattrapage(MAS326R)

    infoMAS336R =""
    MAS336R = list(Evaluation.objects.filter(uniteEnseignement_id=84, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort335 = epurationRattrapage(MAS336R)

    infoMAS346R =""
    MAS346R = list(Evaluation.objects.filter(uniteEnseignement_id=85, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort345 = epurationRattrapage(MAS346R)

    infoEVE356R = ""
    EVE356R = list(Evaluation.objects.filter(uniteEnseignement_id=86, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort355 = epurationRattrapage(EVE356R)

    infoEVE366R = ""
    EVE366R = list(Evaluation.objects.filter(uniteEnseignement_id=87, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort365 = epurationRattrapage(EVE366R)

    listeMatriceRs6EVE = []
    listeMatriceRs6EVEex = []

    for j in range (len(infoEtudiantEVE)):
        matriceRs6EVE = [

            infoEtudiantEVE[j],
            
            MAS316R[j],

            MAS326R[j],
            
            MAS336R[j],
            
            MAS346R[j],
            
            EVE356R[j],
            
            EVE366R[j],
        ]

        matriceRs6EVEex = [

            infoEtudiantEVE[j],
            
            ( round( MAS316R[j]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (MAS316R[j] > 0) else MAS316R[j] ) ,

            ( round( MAS326R[j]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (MAS326R[j] > 0) else MAS326R[j] ) ,
            
            ( round( MAS336R[j]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (MAS336R[j] > 0) else MAS336R[j] ) ,
            
            ( round( MAS346R[j]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (MAS346R[j] > 0) else MAS346R[j] ) ,
            
            ( round( EVE356R[j]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (EVE356R[j] > 0) else EVE356R[j] ) ,
            
            ( round( EVE366R[j]*0.7 + EVE366cc[j]['note_cc']*0.3, 2) if (EVE366R[j] > 0) else EVE366R[j] ) ,
        ]
        listeMatriceRs6EVE.append(matriceRs6EVE)
        listeMatriceRs6EVEex.append(matriceRs6EVEex)

############################################################### SEMESTRE 6 EVE SYNTHESE   ###################################################################################################
    listeMatriceS =  []
    EVEMoyennes6 = []
    TotalPoint = []

    for j in range( len(infoEtudiantEVE) ):

        matricesS6EVE = [
            
            infoEtudiantEVE[j],

            [ 
                ( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) 
                
                , coefS5EVE[0]
                
                , round(( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) *coefS5EVE[0], 2)

                , round( ((( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) *coefS5EVE[0]) + (MAS326[j]*coefS5EVE[1]) + (MAS336[j]*coefS5EVE[2]) + (MAS346[j]*coefS5EVE[3])) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]), 2)
                
                , sort316.index(( MAS316[j] ) )+1 #round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else

                , (( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] )  >=10)

                , creditS5EVE[0]

                , creditS5EVE[0] if((( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] )  >=10)) else 0

                , ("RATTRAPAGE" if listeMatriceRs6EVE[j][1]> 0 else " ")

                #, ("RATTRAPAGE" if listeMatriceRs6EVE[j][1]> 0)
                
                #, MAS316cc[j]['note_cc']
                
                #, MAS316sn[j]['note_sn'],
            ],
            
            [ 
                ( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) 
                
                , coefS5EVE[1]
                
                , round(( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) *coefS5EVE[1], 2)
                
                , 'MOYENNE'
                
                , sort326.index((  MAS326[j] ) )+1 #round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else
                
                , (( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) >=10)

                , creditS5EVE[1]
                
                , creditS5EVE[1] if (( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) >=10) else 0

                , ("RATTRAPAGE" if listeMatriceRs6EVE[j][2]> 0 else " ")
                
                #, MAS326cc[j]['note_cc']
                
                #, MAS326sn[j]['note_sn'],  
            ],
            
            [ 
                ( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) 
                
                , coefS5EVE[2]
                
                , round(( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) *coefS5EVE[2], 2)
                
                , 'MOYENNE'
                
                , sort336.index((  MAS336[j] ) )+1 #round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else
                
                , (( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) >=10)
                
                , creditS5EVE[2]
                
                , creditS5EVE[2] if (( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) >=10) else 0

                , ("RATTRAPAGE" if listeMatriceRs6EVE[j][3]> 0 else " ")
                
                #, MAS336cc[j]['note_cc']
                
                #, MAS336sn[j]['note_sn'] 
            ],
            
            [ 
                ( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )
                
                , coefS5EVE[3]
                
                , round(( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )*coefS5EVE[3], 2)
                
                , 'MOYENNE'
                
                , sort346.index((  MAS346[j] ))+1 #round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else
                 
                , (( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )>=10)
                
                , creditS5EVE[3]
                
                , creditS5EVE[3] if (( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )>=10) else 0

                , ("RATTRAPAGE" if listeMatriceRs6EVE[j][4]> 0 else " ")
                
                #, MAS346cc[j]['note_cc']
                
                #, MAS346sn[j]['note_sn']
                
                #, [ ( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) , ( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) , ( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) , ( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )], MAS346R[j] 

                ],

            #MODULE 2
            [ 
                ( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )

                , coefS5EVE[4]

                , round(( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )*coefS5EVE[4], 2)

                , round((( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )*coefS5EVE[4] + EVE366[j]*coefS5EVE[5] )/(coefS5EVE[4]+coefS5EVE[5]), 2)

                , sort356.index((  EVE356[j] ))+1 #round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else

                , (( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )>=10)

                , creditS5EVE[4]

                , creditS5EVE[4] if((( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )>=10)) else 0

                , ("RATTRAPAGE" if listeMatriceRs6EVE[j][5]> 0 else " ")

                #, EVE356cc[j]['note_cc']

                #, EVE356sn[j]['note_sn']

                #, EVE356R[j]['note_rattrapage']
            ],

            [ 
                ( round(listeMatriceRs6EVE[j][6]*0.7 + EVE366cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] ) 

                , coefS5EVE[5]

                , round(( round(listeMatriceRs6EVE[j][6]*0.7 + EVE366cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] )*coefS5EVE[5], 2)

                , 'MOYENNE'

                , sort366.index((  EVE366[j] ))+1 #round(listeMatriceRs6EVE[j][6]*0.7 + EVE366cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else

                , (( round(listeMatriceRs6EVE[j][6]*0.7 + EVE366cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] )>=10)

                , creditS5EVE[5]

                , creditS5EVE[5] if (( round(listeMatriceRs6EVE[j][6]*0.7 + EVE366cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] )>=10) else 0

                , ("RATTRAPAGE" if listeMatriceRs6EVE[j][6]> 0 else " ")

                #, EVE366cc[j]['note_cc']

                #, EVE366sn[j]['note_sn']

                #, [ ( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] ), ( round(listeMatriceRs6EVE[j][6]*0.7 + EVE366cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] ) ], EVE366R[j] 
            ],

            [ 
                (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),
    
                round( (( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) *coefS5EVE[0] + ( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) *coefS5EVE[1] + ( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) *coefS5EVE[2] + ( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )*coefS5EVE[3]+( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )*coefS5EVE[4] + ( round(listeMatriceRs6EVE[j][6]*0.7 + EVE366cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] )*coefS5EVE[5] ), 2),

                round( (( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) *coefS5EVE[0] + MAS326[j]*coefS5EVE[1] + ( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) *coefS5EVE[2] + ( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )*coefS5EVE[3] + ( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )*coefS5EVE[4] + ( round(listeMatriceRs6EVE[j][6]*0.7 + EVE366cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] )*coefS5EVE[5])/(coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]), 2)
            ],
        ]

        listeMatriceS.append(matricesS6EVE)

        EVEMoyennes6.append(matricesS6EVE[7][2])

        TotalPoint.append(  round(listeMatriceS5[j][7][1] + listeMatriceS[j][7][1], 2) ) #round(listeMatriceS5[j][7][1], 2)


    EVEMoyennes6.sort(reverse=True)    
    TotalPoint.sort(reverse=True)
    moy6 = stat.mean(EVEMoyennes6)
    moy6 = round(moy6, 2)
    session6 = ''


    semestre1MDS += [listeMatrice2, EVEMoyenne2, moy2, session2, listeMatriceS, EVEMoyennes6, TotalPoint]

    return render(request,'bulletin/BulletinTemplate/bullS6eve.html', {'semestre1MDS': semestre1MDS} ) #, {'semestre1MDS': semestre1MDS}







########################################################### PROCES VERBAUX #########################################################################################################################################################################################################################

#PV EPS1 SEMESTRE1
def resultatCommunepsmds(request):

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = epurationCoef(coefS1STAPS1)

    creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS1 = epurationCre(creditS1STAPS1)

########################################################### S1 STATS VAL     ############################################################################################################################
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

########################################################### PV SEMESTRE 1 EPS   ############################################################################################################################
    EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN').values('note_cc'))
    EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN').values('note_sn'))
    sort111 = epurationTriCroissant(EPS111)

    EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='EXAMEN').values('note_cc'))
    EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='EXAMEN').values('note_sn'))
    sort112 = epurationTriCroissant(EPS112)

    EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='EXAMEN').values('note_cc'))
    EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='EXAMEN').values('note_sn'))
    sort113 = epurationTriCroissant(EPS113)

    EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN').values('note_cc'))
    EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN').values('note_sn'))
    sort114 = epurationTriCroissant(EPS114)

    EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN').values('note_sn'))
    sort115a = epurationTriCroissant(EPS115a)

    EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115bcc = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115bsn = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN').values('note_sn'))
    sort115b = epurationTriCroissant(EPS115b)

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN').values('note_sn'))
    sort115j = epurationTriCroissant(EPS115j)

    EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN').values('note_cc'))
    EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN').values('note_sn'))
    sort115l = epurationTriCroissant(EPS115l)

    EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN').values('note_cc'))
    EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN').values('note_sn'))
    sort116 = epurationTriCroissant(EPS116)

    EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='EXAMEN').values('note_cc'))
    EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='EXAMEN').values('note_sn'))
    sort117 = epurationTriCroissant(EPS117)

    EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN').values('note_cc'))
    EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN').values('note_sn'))
    sort118 = epurationTriCroissant(EPS118)

    EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN').values('note_cc'))
    EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN').values('note_sn'))
    sort119 = epurationTriCroissant(EPS119)


    staps1 = []
    staps1Moyenne = []
    listeMatrice = [ ]

    for j in range( len(infoEtudiantSTAPS1) ):

        matrice = [
                        infoEtudiantSTAPS1[j],

                        [
                            EPS111[j]
                            , coefS1STAPS1[0]
                            , EPS111[j]*coefS1STAPS1[0]
                            , round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2)
                            , sort111.index(EPS111[j])+1
                            , (EPS111[j]>=10)
                            , creditS1STAPS1[0]
                            , creditS1STAPS1[0] if (EPS111[j]>=10) else 0
                            , EPS111cc[j]['note_cc']
                            , EPS111sn[j]['note_sn']
                        ],

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
                        
                        #7
                        [ 
                            EPS115j[j]
                            , coefS1STAPS1[6]
                            , EPS115j[j]*coefS1STAPS1[6]
                            , "MOYENNE"
                            , sort115j.index(EPS115j[j])+1
                            , (EPS115j[j] >=10)
                            , creditS1STAPS1[6]
                            , creditS1STAPS1[6] if (EPS115j[j] >=10) else 0
                            , EPS115jcc[j]['note_cc']
                            , EPS115jsn[j]['note_sn'] 
                        ],

                        [ EPS115l[j], coefS1STAPS1[7], EPS115l[j]*coefS1STAPS1[7], "MOYENNE", sort115l.index(EPS115l[j])+1, (EPS115l[j] >=10), creditS1STAPS1[7], creditS1STAPS1[7] if ((EPS115a[j]+EPS115b[j]+EPS115j[j]+EPS115l[j]) >=40) else 0, EPS115lcc[j]['note_cc'], EPS115lsn[j]['note_sn']  ],

                        [ EPS116[j],  coefS1STAPS1[8], EPS116[j]*coefS1STAPS1[8], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[8], creditS1STAPS1[8] if (EPS116[j] >=10) else 0, EPS116cc[j]['note_cc'], EPS116sn[j]['note_sn'] ],

                        [ 
                            EPS117[j]
                            
                            , coefS1STAPS1[9] 

                            , EPS117[j]*coefS1STAPS1[9]

                            , round( ((EPS117[j]*coefS1STAPS1[9]) + (EPS118[j]*coefS1STAPS1[10]) + (EPS119[j]*coefS1STAPS1[11])) / ( coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]) ,2)

                            , sort117.index(EPS117[j])+1

                            , (EPS117[j] >=10) 
                            
                            , creditS1STAPS1[9]

                            , creditS1STAPS1[9] if (EPS117[j] >=10) else 0
                            , EPS117cc[j]['note_cc']
                            , EPS117sn[j]['note_sn']
                        ],

                        #11
                        [ 
                            EPS118[j]
                            , coefS1STAPS1[10]
                            , EPS118[j]*coefS1STAPS1[10]
                            , "MOYENNE"
                            , sort118.index(EPS118[j])+1
                            , (EPS118[j] >=10)
                            , creditS1STAPS1[10]
                            #7
                            , creditS1STAPS1[10] if (EPS118[j] >=10) else 0

                            , EPS118cc[j]['note_cc']
                            , EPS118sn[j]['note_sn']
                        ],

                        [ EPS119[j], coefS1STAPS1[11], EPS119[j]*coefS1STAPS1[11], "MOYENNE", sort119.index(EPS119[j])+1, (EPS119[j] >=10), creditS1STAPS1[11], creditS1STAPS1[11] if (EPS119[j] >=10) else 0, EPS119cc[j]['note_cc'], EPS119sn[j]['note_sn'] ],

                        [
                            ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ), #coefsomme

                            round( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115j[j]*coefS1STAPS1[6]+EPS115l[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11], 2),

                            round(( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115j[j]*coefS1STAPS1[6]+EPS115l[j]*coefS1STAPS1[7]+EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2 ),

                            #4,
                            #5
                        ]
        ]

        staps1Moyenne.append(matrice[13][2])

        EPSCreditCount(matrice)
        listeMatrice.append(matrice)

        staps1Moyenne.sort(reverse=True)
        moy = stat.mean(staps1Moyenne)
        moy = round(moy, 2)
        session = 'Janvier 2023'

        filiere = 'STAPS'

########################################################### PV SEMESTRE 1 EPS CC     ########################################################################################################################################################
    listeMatriceS1EpsCC = []

    for j in range( len(infoEtudiantSTAPS1) ):

            matriceS1EpsCC = [

                infoEtudiantSTAPS1[j],

                EPS111cc[j]["note_cc"],

                EPS112cc[j]["note_cc"],

                EPS113cc[j]["note_cc"],

                EPS114cc[j]["note_cc"],

                EPS115acc[j]["note_cc"],

                EPS115bcc[j]["note_cc"],

                EPS115jcc[j]["note_cc"],

                EPS115lcc[j]["note_cc"],

                EPS116cc[j]["note_cc"],

                EPS117cc[j]["note_cc"],

                EPS118cc[j]["note_cc"],

                EPS119cc[j]["note_cc"],
            ]
            listeMatriceS1EpsCC.append(matriceS1EpsCC)

########################################################### PV SEMESTRE 1 EPS RATTRAPAGE ############################################################################################################################
    EPS111R = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='RATTRAPAGE').values('note_rattrapage')) 
    sort111R = epurationRattrapage(EPS111R)

    EPS112R = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort112R = epurationRattrapage(EPS112R)

    EPS113R = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort113R = epurationRattrapage(EPS113R)

    EPS114R = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort114R = epurationRattrapage(EPS114R)

    EPS115aR = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort115aR = epurationRattrapage(EPS115aR)

    EPS115bR = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort115bR = epurationRattrapage(EPS115bR) 

    EPS115jR = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort115jR = epurationRattrapage(EPS115jR)

    EPS115lR = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort115lR = epurationRattrapage(EPS115lR)

    EPS116R = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort116R = epurationRattrapage(EPS116R)

    EPS117R = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort117R = epurationRattrapage(EPS117R)

    EPS118R = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort118R = epurationRattrapage(EPS118R)

    EPS119R = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort119R = epurationRattrapage(EPS119R)

    listeMatriceRs1EPS1 = []
    listeMatriceRs1EPS1ex = []

    for j in range (len(infoEtudiantSTAPS1)):
        matriceRs1EPS1 = [

            infoEtudiantSTAPS1[j],

            EPS111R[j],

            EPS112R[j],

            EPS113R[j],

            EPS114R[j],

            EPS115aR[j],

            EPS115bR[j],

            EPS115jR[j],

            EPS115lR[j],

            EPS116R[j],

            EPS117R[j],

            EPS118R[j],

            EPS119R[j]
        ]

        matriceRs1EPS1ex = [
            infoEtudiantSTAPS1[j],

            ( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] ) ,

            ( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] ) ,

            ( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] ) ,

            ( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] ) ,

            ( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] ) ,

            ( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] ) ,

            ( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] ) ,

            ( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] ) ,

            ( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] ) ,

            ( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] ) ,

            ( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] ) ,

            ( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] ) ,

        ]
        listeMatriceRs1EPS1.append(matriceRs1EPS1)
        listeMatriceRs1EPS1ex.append(matriceRs1EPS1ex)

########################################################### PV SEMESTRE 1 EPS SYNTHESE   ############################################################################################################################

    #listeMatrices1eps = []
    #staps1Moyenne = []

    """for j in range( len(infoEtudiantSTAPS1) ):

        matriceS1EPS = [
                infoEtudiantSTAPS1[j],

                [ #EPS111[j]
                    ( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )
                    , coefS1STAPS1[0]
                    , (( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] ))*coefS1STAPS1[0]
                    , round( ((( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2)
                    #, sort111.index(EPS111[j])+1
                    ,(( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )>=10)
                    , creditS1STAPS1[0]
                    , creditS1STAPS1[0] if (( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )>=10) else 0
                    , EPS111cc[j]['note_cc']
                    , EPS111sn[j]['note_sn'] 
                ],

                [ 
                    ( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )
                    , coefS1STAPS1[1]
                    , ( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )*coefS1STAPS1[1]
                    , "MOYENNE"
                    #, sort112.index(EPS112[j])+1
                    , (( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )>=10)
                    , creditS1STAPS1[1]
                    , creditS1STAPS1[1] if (( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )>=10) else 0
                    , EPS112cc[j]['note_cc']
                    , EPS112sn[j]['note_sn'] 
                ],

                [ 
                    ( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] )
                    , coefS1STAPS1[2]
                    , ( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] )*coefS1STAPS1[2]
                    , round( ( (( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] )*coefS1STAPS1[2]) + (( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )*coefS1STAPS1[3]) + (( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )*coefS1STAPS1[4]) + (( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] ) *coefS1STAPS1[5]) + (( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )*coefS1STAPS1[6]) + (( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]) + (( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )*coefS1STAPS1[8]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]) ,2)    
                    #, sort113.index(EPS113[j])+1
                    , (( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] )>=10),creditS1STAPS1[2]
                    , creditS1STAPS1[2] if(( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] ) >=10) else 0
                    , EPS113cc[j]['note_cc']
                    , EPS113sn[j]['note_sn']
                ],

                [ 
                    ( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )
                    , coefS1STAPS1[3]
                    , ( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )*coefS1STAPS1[3]
                    , "MOYENNE"
                    #, sort114.index(EPS114[j])+1
                    , (( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] ) >=10)
                    , creditS1STAPS1[3]
                    , creditS1STAPS1[3] if (( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] ) >=10) else 0
                    , EPS114cc[j]['note_cc']
                    , EPS114sn[j]['note_sn']  
                ],

                [ 
                    ( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )
                    , coefS1STAPS1[4]
                    , ( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )*coefS1STAPS1[4]
                    , "MOYENNE"
                    #, sort115a.index(EPS115a[j])+1
                    , (( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] ) >=10)
                    , creditS1STAPS1[4]
                    , creditS1STAPS1[4] if (( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] ) >=10) else 0
                    , EPS115acc[j]['note_cc']
                    , EPS115asn[j]['note_sn'] 
                ], #crédits

                [ 
                     ( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )
                    , coefS1STAPS1[5]
                    ,  ( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )*coefS1STAPS1[5]
                    , "MOYENNE"
                    #, sort115b.index(EPS115b[j])+1
                    , ( ( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] ) >=10)
                    , creditS1STAPS1[5]
                    , creditS1STAPS1[5] if ( ( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] ) >=10) else 0
                    , EPS115bcc[j]['note_cc']
                    , EPS115bsn[j]['note_sn'] 
                ],

                [ 
                    ( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )
                    , coefS1STAPS1[6]
                    , ( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )*coefS1STAPS1[6]
                    , "MOYENNE"
                    #, sort115j.index(EPS115j[j])+1
                    , (( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] ) >=10)
                    , creditS1STAPS1[6]
                    , creditS1STAPS1[6] if (( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] ) >=10) else 0
                    , EPS115jcc[j]['note_cc']
                    , EPS115jsn[j]['note_sn'] 
                ],

                [ 
                    ( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )
                    , coefS1STAPS1[7]
                    , ( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]
                    , "MOYENNE"
                    #, sort115l.index(EPS115l[j])+1
                    , (( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] ) >=10)
                    , creditS1STAPS1[7]
                    , creditS1STAPS1[7] if ((( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )+( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )) >=40) else 0
                    , EPS115lcc[j]['note_cc']
                    , EPS115lsn[j]['note_sn']  
                ],

                [ 
                    ( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )
                    ,  coefS1STAPS1[8]
                    , ( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )*coefS1STAPS1[8]
                    , "MOYENNE"
                    #, sort116.index(EPS116[j])+1
                    , (( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] ) >=10)
                    , creditS1STAPS1[8]
                    , creditS1STAPS1[8] if (( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] ) >=10) else 0
                    , EPS116cc[j]['note_cc']
                    , EPS116sn[j]['note_sn'] 
                ],

                [ 
                    ( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] ) 
                    , coefS1STAPS1[9]
                    , ( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] ) *coefS1STAPS1[9]
                    , round( ((( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] ) *coefS1STAPS1[9]) + (EPS118[j]*coefS1STAPS1[10]) + (EPS119[j]*coefS1STAPS1[11])) / ( coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]) ,2), 
                    #sort117.index(EPS117[j])+1, 
                     (( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] )  >=10)
                    , creditS1STAPS1[9]
                    , creditS1STAPS1[9] if (( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] )  >=10) else 0
                    , EPS117cc[j]['note_cc']
                    , EPS117sn[j]['note_sn']
                 ],

                [ 
                    ( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )
                    , coefS1STAPS1[10]
                    , ( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )*coefS1STAPS1[10]
                    , "MOYENNE"
                    #, sort118.index(EPS118[j])+1
                    , (( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] ) >=10)
                    , creditS1STAPS1[10]
                    , creditS1STAPS1[10] if (( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] ) >=10) else 0
                    , EPS118cc[j]['note_cc']
                    , EPS118sn[j]['note_sn'] 
                ],

                [ 
                    ( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )
                    , coefS1STAPS1[11]
                    , ( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )*coefS1STAPS1[11]
                    , "MOYENNE"
                    #, sort119.index(EPS119[j])+1
                    , (( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] ) >=10)
                    , creditS1STAPS1[11]
                    , creditS1STAPS1[11] if (( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] ) >=10) else 0
                    , EPS119cc[j]['note_cc']
                    , EPS119sn[j]['note_sn'] 
                ],

                [ 
                    ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ), #coefsomme

                    round( ( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )*coefS1STAPS1[0]+( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )*coefS1STAPS1[1]+( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] ) *coefS1STAPS1[2]+( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )*coefS1STAPS1[3]+( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )*coefS1STAPS1[4]+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )*coefS1STAPS1[5]+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )*coefS1STAPS1[6]+( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]+( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )*coefS1STAPS1[8]+( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] )*coefS1STAPS1[9]+( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )*coefS1STAPS1[10]+( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )*coefS1STAPS1[11], 2),

                    round(( ( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )*coefS1STAPS1[0]+( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )*coefS1STAPS1[1]+( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] ) *coefS1STAPS1[2]+( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )*coefS1STAPS1[3]+( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )*coefS1STAPS1[4]+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )*coefS1STAPS1[5]+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )*coefS1STAPS1[6]+( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]+( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )*coefS1STAPS1[8]+( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] )*coefS1STAPS1[9]+( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )*coefS1STAPS1[10]+( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2 ),

                    4,
                    5
                ]
        ]
                
        staps1Moyenne.append(matrice[13][2])

        listeMatrices1eps.append(matriceS1EPS)
    """
    #Synhèse EPS1 Semestre 1

    listeMatriceS1EpsSynthese = matriceSyntheseEPS1(listeMatrice, listeMatriceRs1EPS1, listeMatrice, listeMatriceS1EpsCC)

    #Décompte de crédit
    EPSCreditCount22(listeMatriceS1EpsSynthese)
    #listeMatriceS1EpsSynthese = EPSCreditCount22(listeMatriceS1EpsSynthese)

########################################################### STATS VALIDATION ####################################################################################################################################
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

########################################################### STATS MENTION ###############################################################################################################################################
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

    #La liste de matrice qui contient les décomptes de crédit(listeMatriceS1EpsSynthese[0])          
    semestre1MDS = [filiere, listeMatrice, staps1Moyenne, moy, session , creditS1STAPS1, UEStats, UEstats_mention, listeMatriceRs1EPS1, listeMatriceS1EpsSynthese[0],  listeMatriceS1EpsSynthese ] #, listeMatrices1eps

    return render(request, 'bulletin/releveCommun/releveCommun.html', {'semestre1MDS': semestre1MDS})




#PV EPS1 SEMESTRE2
def resultatCommuns2staps(request):

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

########################################################### PV SEMESTRE 2 ###############################################################################################################################
    #UE NOM ET CODE
    UeNomCode = list( UniteEnseignement.objects.filter(semestre_id = 2, Specialite="EPS").values("code_UE","intitule_UE", "semestre_id", "nombre_credit") )

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = epurationCoef(coefS1STAPS1)

    creditS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="STAPS").values("nombre_credit"))
    creditS1STAPS1 = epurationCre(creditS1STAPS1)

    EPS121 = list(Evaluation.objects.filter(uniteEnseignement_id=99, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS121cc = list(Evaluation.objects.filter(uniteEnseignement_id=99, natureEvaluation='EXAMEN').values('note_cc'))
    EPS121sn = list(Evaluation.objects.filter(uniteEnseignement_id=99, natureEvaluation='EXAMEN').values('note_sn'))
    sort121 = epurationTriCroissant(EPS121)

    EPS122 = list(Evaluation.objects.filter(uniteEnseignement_id=100, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS122cc = list(Evaluation.objects.filter(uniteEnseignement_id=100, natureEvaluation='EXAMEN').values('note_cc'))
    EPS122sn = list(Evaluation.objects.filter(uniteEnseignement_id=100, natureEvaluation='EXAMEN').values('note_sn'))
    sort122 = epurationTriCroissant(EPS122)

    EPS123 = list(Evaluation.objects.filter(uniteEnseignement_id=101, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS123cc = list(Evaluation.objects.filter(uniteEnseignement_id=101, natureEvaluation='EXAMEN').values('note_cc'))
    EPS123sn = list(Evaluation.objects.filter(uniteEnseignement_id=101, natureEvaluation='EXAMEN').values('note_sn'))
    sort123 = epurationTriCroissant(EPS123)

    EPS124 = list(Evaluation.objects.filter(uniteEnseignement_id=102, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS124cc = list(Evaluation.objects.filter(uniteEnseignement_id=102, natureEvaluation='EXAMEN').values('note_cc'))
    EPS124sn = list(Evaluation.objects.filter(uniteEnseignement_id=102, natureEvaluation='EXAMEN').values('note_sn'))
    sort124 = epurationTriCroissant(EPS124)

    EPS125a = list(Evaluation.objects.filter(uniteEnseignement_id=103, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS125acc = list(Evaluation.objects.filter(uniteEnseignement_id=103, natureEvaluation='EXAMEN').values('note_cc'))
    EPS125asn = list(Evaluation.objects.filter(uniteEnseignement_id=103, natureEvaluation='EXAMEN').values('note_sn'))
    sort125a = epurationTriCroissant(EPS125a)

    EPS125b = list(Evaluation.objects.filter(uniteEnseignement_id=104, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS125bcc = list(Evaluation.objects.filter(uniteEnseignement_id=104, natureEvaluation='EXAMEN').values('note_cc'))
    EPS125bsn = list(Evaluation.objects.filter(uniteEnseignement_id=104, natureEvaluation='EXAMEN').values('note_sn'))
    sort125b = epurationTriCroissant(EPS125b) 

    EPS125g = list(Evaluation.objects.filter(uniteEnseignement_id=124, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS125gcc = list(Evaluation.objects.filter(uniteEnseignement_id=124, natureEvaluation='EXAMEN').values('note_cc'))
    EPS125gsn = list(Evaluation.objects.filter(uniteEnseignement_id=124, natureEvaluation='EXAMEN').values('note_sn'))
    sort125g = epurationTriCroissant(EPS125g)

    EPS125j = list(Evaluation.objects.filter(uniteEnseignement_id=105, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS125jcc = list(Evaluation.objects.filter(uniteEnseignement_id=105, natureEvaluation='EXAMEN').values('note_cc'))
    EPS125jsn = list(Evaluation.objects.filter(uniteEnseignement_id=105, natureEvaluation='EXAMEN').values('note_sn'))
    sort125j = epurationTriCroissant(EPS125j)

    EPS125l = list(Evaluation.objects.filter(uniteEnseignement_id=106, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS125lcc = list(Evaluation.objects.filter(uniteEnseignement_id=106, natureEvaluation='EXAMEN').values('note_cc'))
    EPS125lsn = list(Evaluation.objects.filter(uniteEnseignement_id=106, natureEvaluation='EXAMEN').values('note_sn'))
    sort125l = epurationTriCroissant(EPS125l)

    EPS125f = list(Evaluation.objects.filter(uniteEnseignement_id=107, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS125fcc = list(Evaluation.objects.filter(uniteEnseignement_id=107, natureEvaluation='EXAMEN').values('note_cc'))
    EPS125fsn = list(Evaluation.objects.filter(uniteEnseignement_id=107, natureEvaluation='EXAMEN').values('note_sn'))
    sort125f = epurationTriCroissant(EPS125f)

    EPS126 = list(Evaluation.objects.filter(uniteEnseignement_id=108, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS126cc = list(Evaluation.objects.filter(uniteEnseignement_id=108, natureEvaluation='EXAMEN').values('note_cc'))
    EPS126sn = list(Evaluation.objects.filter(uniteEnseignement_id=108, natureEvaluation='EXAMEN').values('note_sn'))
    sort126 = epurationTriCroissant(EPS126)

    EPS127 = list(Evaluation.objects.filter(uniteEnseignement_id=109, natureEvaluation='EXAMEN').values('note_Examen')) 
    EPS127cc = list(Evaluation.objects.filter(uniteEnseignement_id=109, natureEvaluation='EXAMEN').values('note_cc'))
    EPS127sn = list(Evaluation.objects.filter(uniteEnseignement_id=109, natureEvaluation='EXAMEN').values('note_sn'))
    sort127 = epurationTriCroissant(EPS127)

    EPS128 = list(Evaluation.objects.filter(uniteEnseignement_id=110, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS128cc = list(Evaluation.objects.filter(uniteEnseignement_id=110, natureEvaluation='EXAMEN').values('note_cc'))
    EPS128sn = list(Evaluation.objects.filter(uniteEnseignement_id=110, natureEvaluation='EXAMEN').values('note_sn'))
    sort128 = epurationTriCroissant(EPS128)

    EPS129 = list(Evaluation.objects.filter(uniteEnseignement_id=111, natureEvaluation='EXAMEN').values('note_Examen'))
    EPS129cc = list(Evaluation.objects.filter(uniteEnseignement_id=111, natureEvaluation='EXAMEN').values('note_cc'))
    EPS129sn = list(Evaluation.objects.filter(uniteEnseignement_id=111, natureEvaluation='EXAMEN').values('note_sn'))
    sort129 = epurationTriCroissant(EPS129)

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

    student = {}
    temp = {}
    staps1 = []
    staps2Moyenne = []
    listeMatriceS2Eps = []

    for j in range( len(infoEtudiantSTAPS1) ):

        #for j in range( len(coefS1STAPS1) ):
        matrice = [
                infoEtudiantSTAPS1[j],

                [ 
                    EPS121[j]
                    , coefS1STAPS1[0]
                    , EPS121[j]*coefS1STAPS1[0]
                    , round( ((EPS121[j]*coefS1STAPS1[0]) + (EPS122[j]*coefS1STAPS1[1]))/(coefS1STAPS1[0]+coefS1STAPS1[1]), 2)
                    , sort121.index(EPS121[j])+1,(EPS121[j]>=10)
                    , creditS1STAPS1[0]
                    , creditS1STAPS1[0] if(EPS121[j]>=10) else 0 
                ],

                [ 
                    EPS122[j]
                    , coefS1STAPS1[1]
                    , EPS122[j]*coefS1STAPS1[1]
                    , "MOYENNE"
                    , sort122.index(EPS122[j])+1
                    #, (EPS122[j]>=10)
                    , creditS1STAPS1[1]
                    , creditS1STAPS1[1] if(EPS122[j]>=10) else 0 
                ],

                [ 
                    EPS123[j]
                    , coefS1STAPS1[2]
                    , EPS123[j]*coefS1STAPS1[2]
                    , round( ( (EPS123[j]*coefS1STAPS1[2]) + (EPS124[j]*coefS1STAPS1[3]) + (EPS125a[j]*coefS1STAPS1[4]) + (EPS125g[j]*coefS1STAPS1[5]) + (EPS125j[j]*coefS1STAPS1[6]) + (EPS125f[j]*coefS1STAPS1[7]) + (EPS126[j]*coefS1STAPS1[8]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]) ,2)  #EPS125b[j] , EPS125l[j]
                    , sort123.index(EPS123[j])+1
                    #, (EPS123[j] >=10)
                    , creditS1STAPS1[2]
                    , creditS1STAPS1[2] if (EPS123[j] >=10) else 0
                ],

                [ 
                    EPS124[j]
                    , coefS1STAPS1[3]
                    , EPS124[j]*coefS1STAPS1[3]
                    , "MOYENNE"
                    , sort124.index(EPS124[j])+1
                    #, (EPS124[j] >=10)
                    , creditS1STAPS1[3]
                    , creditS1STAPS1[3] if (EPS124[j] >=10) else 0  
                ],

                [ 
                    EPS125a[j]
                    , coefS1STAPS1[4]
                    , EPS125a[j]*coefS1STAPS1[4]
                    , "MOYENNE"
                    , sort125a.index(EPS125a[j])+1
                    #, (EPS125a[j] >=10)
                    , creditS1STAPS1[4]
                    , creditS1STAPS1[4] if((EPS125a[j]+EPS125g[j]+EPS125f[j]+EPS125j[j]) >= 40) else 0 
                ], #crédits

                #[ EPS125b[j], coefS1STAPS1[5], EPS125b[j]*coefS1STAPS1[5], "MOYENNE", sort125b.index(EPS125b[j])+1, (EPS125b[j] >=10), creditS1STAPS1[5], creditS1STAPS1[5] if(EPS125b[j] >=10) else 0 ],
                [ 
                    EPS125g[j]
                    , coefS1STAPS1[13]
                    , EPS125g[j]*coefS1STAPS1[13]
                    , "MOYENNE"
                    , sort125g.index(EPS125g[j])+1
                    #, (EPS125g[j] >=10)
                    , creditS1STAPS1[13]
                    , creditS1STAPS1[13] if(EPS125g[j] >=10) else 0 
                ],

                [ 
                    EPS125j[j]
                    , coefS1STAPS1[6]
                    , EPS125j[j]*coefS1STAPS1[6]
                    , "MOYENNE"
                    , sort125j.index(EPS125j[j])+1
                    #, (EPS125j[j] >=10)
                    , creditS1STAPS1[6]
                    , creditS1STAPS1[6] if(EPS125j[j] >=10) else 0 
                ],

                #[ EPS125l[j], coefS1STAPS1[7], EPS125l[j]*coefS1STAPS1[7], "MOYENNE", sort125l.index(EPS125l[j])+1, (EPS125l[j] >=10), creditS1STAPS1[7], creditS1STAPS1[7] if (EPS125l[j] >=10) else 0  ],
                [ 
                    EPS125f[j]
                    , coefS1STAPS1[8]
                    , EPS125f[j]*coefS1STAPS1[8]
                    , "MOYENNE"
                    , sort125f.index(EPS125f[j])+1
                    #, (EPS125f[j] >=10)
                    , creditS1STAPS1[8]
                    , creditS1STAPS1[8] if(EPS125f[j] >=10) else 0 
                ],

                [ 
                    EPS126[j]
                    , coefS1STAPS1[9]
                    , EPS126[j]*coefS1STAPS1[9]
                    , "MOYENNE"
                    , sort126.index(EPS126[j])+1
                    #, (EPS126[j] >=10)
                    , creditS1STAPS1[9]
                    , creditS1STAPS1[9] if(EPS126[j] >=10) else 0 
                ],

                [ 
                    EPS127[j]
                    , coefS1STAPS1[10]
                    , EPS127[j]*coefS1STAPS1[10]
                    , round( ((EPS127[j]*coefS1STAPS1[10]) + (EPS128[j]*coefS1STAPS1[10]) + (EPS129[j]*coefS1STAPS1[12])) / ( coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]) ,2)
                    , sort127.index(EPS127[j])+1
                    #, (EPS127[j] >=10)    
                    , creditS1STAPS1[10]
                    , creditS1STAPS1[10] if(EPS127[j] >=10) else 0
                ],

                [ 
                    EPS128[j]
                    , coefS1STAPS1[11]
                    , EPS128[j]*coefS1STAPS1[11]
                    , "MOYENNE"
                    , sort128.index(EPS128[j])+1
                    #, (EPS128[j] >=10)
                    , creditS1STAPS1[10]
                    , creditS1STAPS1[11] if(EPS128[j] >=10) else 0  
                ],

                [ 
                    EPS129[j]
                    , coefS1STAPS1[12]
                    , EPS129[j]*coefS1STAPS1[12]
                    , "MOYENNE"
                    , sort129.index(EPS129[j])+1
                    #, (EPS129[j] >=10)
                    , creditS1STAPS1[12] 
                    , creditS1STAPS1[12] if(EPS129[j] >=10) else 0 
                ],

                [ 
                    ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[13]+coefS1STAPS1[6]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12] ),

                    round( EPS121[j]*coefS1STAPS1[0]+EPS122[j]*coefS1STAPS1[1]+EPS123[j]*coefS1STAPS1[2]+EPS124[j]*coefS1STAPS1[3]+EPS125a[j]*coefS1STAPS1[4]+EPS125g[j]*coefS1STAPS1[13]+EPS125j[j]*coefS1STAPS1[6]+EPS125f[j]*coefS1STAPS1[8]+EPS126[j]*coefS1STAPS1[9]+EPS127[j]*coefS1STAPS1[10]+EPS128[j]*coefS1STAPS1[11]+EPS129[j]*coefS1STAPS1[12], 2),

                    round(( EPS121[j]*coefS1STAPS1[0]+EPS122[j]*coefS1STAPS1[1]+EPS123[j]*coefS1STAPS1[2]+EPS124[j]*coefS1STAPS1[3]+EPS125a[j]*coefS1STAPS1[4]+EPS125g[j]*coefS1STAPS1[13]+EPS125j[j]*coefS1STAPS1[6]+EPS125f[j]*coefS1STAPS1[8]+EPS126[j]*coefS1STAPS1[9]+EPS127[j]*coefS1STAPS1[10]+EPS128[j]*coefS1STAPS1[11]+EPS129[j]*coefS1STAPS1[12] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[13]+coefS1STAPS1[6]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]), 2 ),

                ]
        ]
        staps2Moyenne.append(matrice[13][2])

        listeMatriceS2Eps.append(matrice)

        #infoEtudiantSTAPS1, coefS1STAPS1, creditS1STAPS1, EPS121, EPS122, EPS123, EPS124, EPS125a ,EPS125b, EPS125j, EPS125l, EPS126, EPS127, EPS128, EPS129, 

        staps2Moyenne.sort(reverse=True)
        moy2 = stat.mean(staps2Moyenne)
        moy2 = round(moy2, 2)
        session2 = 'Mai 2023'

########################################################### PV SEMESTRE 2 RATTRAPAGE ##############################################################################################################################
    EPS121R = list(Evaluation.objects.filter(uniteEnseignement_id=99, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort121R = epurationRattrapage(EPS121R)

    EPS122R = list(Evaluation.objects.filter(uniteEnseignement_id=100, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort122R = epurationRattrapage(EPS122R)

    EPS123R = list(Evaluation.objects.filter(uniteEnseignement_id=101, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort123R = epurationRattrapage(EPS123R)

    EPS124R = list(Evaluation.objects.filter(uniteEnseignement_id=102, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort124R = epurationRattrapage(EPS124R)

    EPS125aR = list(Evaluation.objects.filter(uniteEnseignement_id=103, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort125aR = epurationRattrapage(EPS125aR)

    EPS125bR = list(Evaluation.objects.filter(uniteEnseignement_id=104, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort125bR= epurationRattrapage(EPS125bR) 

    EPS125gR = list(Evaluation.objects.filter(uniteEnseignement_id=124, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort125gR= epurationRattrapage(EPS125gR) 

    EPS125jR = list(Evaluation.objects.filter(uniteEnseignement_id=105, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort125jR = epurationRattrapage(EPS125jR)

    EPS125lR = list(Evaluation.objects.filter(uniteEnseignement_id=106, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort125lR = epurationRattrapage(EPS125lR)

    EPS125fR = list(Evaluation.objects.filter(uniteEnseignement_id=107, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort125fR = epurationRattrapage(EPS125fR)

    EPS126R = list(Evaluation.objects.filter(uniteEnseignement_id=108, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort126R = epurationRattrapage(EPS126R)

    EPS127R = list(Evaluation.objects.filter(uniteEnseignement_id=109, natureEvaluation='RATTRAPAGE').values('note_rattrapage')) 
    sort127R = epurationRattrapage(EPS127R)

    EPS128R = list(Evaluation.objects.filter(uniteEnseignement_id=110, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort128R = epurationRattrapage(EPS128R)

    EPS129R = list(Evaluation.objects.filter(uniteEnseignement_id=111, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort129R = epurationRattrapage(EPS129R)



    listeMatriceS2epsR = [ ]

    for j in range( len(infoEtudiantSTAPS1)):

        matriceS2epsR = [

            infoEtudiantSTAPS1[j],

            EPS121R[j],

            EPS122R[j],

            EPS123R[j],

            EPS124R[j],

            EPS125aR[j],

            #EPS125bR[j],
            EPS125gR[j],

            EPS125jR[j],

            #EPS125lR[j],
            EPS125fR[j],
                
            EPS126R[j],

            EPS127R[j],

            EPS128R[j],

            EPS129R[j]
        ]
        listeMatriceS2epsR.append(matriceS2epsR)

########################################################### PV SEMESTRE 2 EPS CC  ########################################################################################################################################################
    listeMatriceS2EpsCC = []

    for j in range( len(infoEtudiantSTAPS1) ):

            matriceS2EpsCC = [

                infoEtudiantSTAPS1[j],

                EPS121cc[j]['note_cc'],

                EPS122cc[j]['note_cc'],

                EPS123cc[j]['note_cc'],

                EPS124cc[j]['note_cc'],

                EPS125acc[j]['note_cc'],

                #EPS125bcc[j]['note_cc'],

                EPS125gcc[j]['note_cc'],

                EPS125jcc[j]['note_cc'],

                #EPS125lcc[j]['note_cc'],

                EPS125fcc[j]['note_cc'],

                EPS126cc[j]['note_cc'],

                EPS127cc[j]['note_cc'],

                EPS128cc[j]['note_cc'],

                EPS129cc[j]['note_cc'],

            ]
            listeMatriceS2EpsCC.append(matriceS2EpsCC)

########################################################### PV SEMESTRE 2 SYNTHESE  ############################################################################################################################
    listeMatriceS2EpsSynthese  = matriceSyntheseEPS1PV(listeMatriceS2Eps, listeMatriceS2epsR, listeMatriceS2EpsCC)
    #listeMatriceS2EpsSynthese = []

    #Décompte de crédit
    EPSCreditCount2(listeMatriceS2EpsSynthese)

########################################################### STAT MENTION ###############################################################################################################################################

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
    #e115b = {'Très Bien': 0, 'Bien': 0,'Assez Bien': 0,'Passable': 0,'Ccnf': 0,'Echec':0,  'pourcentageTB': 0, 'pourcentageB': 0,'pourcentageAB': 0,'pourcentageP': 0,'pourcentageCc': 0,'pourcentageEc': 0, }
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
    #e115l = {'Très Bien': 0,'Bien': 0,'Assez Bien': 0,'Passable': 0,'Ccnf': 0,'Echec':0,  'pourcentageTB': 0,'pourcentageB': 0,'pourcentageAB': 0, 'pourcentageP': 0,'pourcentageCc': 0,'pourcentageEc': 0, }
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

    EPS115g = list(Evaluation.objects.filter(uniteEnseignement_id=124).values('note_Examen'))
    EPS115gcc = list(Evaluation.objects.filter(uniteEnseignement_id=124).values('note_cc'))
    EPS115gsn = list(Evaluation.objects.filter(uniteEnseignement_id=124).values('note_sn'))
    sort115g = epurationTriCroissant(EPS115g) 

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=105).values('note_Examen'))
    EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=105).values('note_cc'))
    EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=105).values('note_sn'))
    sort115j = epurationTriCroissant(EPS115j)

    EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=106).values('note_Examen'))
    EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=106).values('note_cc'))
    EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=106).values('note_sn'))
    sort115l = epurationTriCroissant(EPS115l)

    EPS115f = list(Evaluation.objects.filter(uniteEnseignement_id=107).values('note_Examen'))
    EPS115fcc = list(Evaluation.objects.filter(uniteEnseignement_id=107).values('note_cc'))
    EPS115fsn = list(Evaluation.objects.filter(uniteEnseignement_id=107).values('note_sn'))
    sort115f = epurationTriCroissant(EPS115f)

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

                            round( ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115g[j]*coefS1STAPS1[13]) + (EPS115j[j]*coefS1STAPS1[6]) + (EPS115f[j]*coefS1STAPS1[8]) + (EPS116[j]*coefS1STAPS1[9]) )/( coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[13]+coefS1STAPS1[6]+coefS1STAPS1[8]+coefS1STAPS1[9]) ,2), 
                            
                            sort113.index(EPS113[j])+1,
                            
                            (EPS113[j] >=10),
                            
                            creditS1STAPS1[2], 
                            creditS1STAPS1[2] if(EPS113[j] >=10) else 0,

                            EPS113cc[j]['note_cc'], 
                            EPS113sn[j]['note_sn']
                        ],

                        [ EPS114[j],  coefS1STAPS1[3], EPS114[j]*coefS1STAPS1[3], "MOYENNE", sort114.index(EPS114[j])+1, (EPS114[j] >=10), creditS1STAPS1[3], creditS1STAPS1[3] if (EPS114[j] >=10) else 0, EPS114cc[j]['note_cc'], EPS114sn[j]['note_sn']  ],

                        [ EPS115a[j], coefS1STAPS1[4], EPS115a[j]*coefS1STAPS1[4], "MOYENNE", sort115a.index(EPS115a[j])+1, (EPS115a[j] >=10), creditS1STAPS1[4], creditS1STAPS1[4] if ( (EPS115a[j] + EPS115g[j] + EPS115j[j] + EPS115f[j] ) >=40 ) else 0, EPS115acc[j]['note_cc'], EPS115asn[j]['note_sn'] ], #crédits

                        #[ EPS115b[j], coefS1STAPS1[5], EPS115b[j]*coefS1STAPS1[5], "MOYENNE", sort115b.index(EPS115b[j])+1, (EPS115b[j] >=10), creditS1STAPS1[5], creditS1STAPS1[5] if (EPS115b[j] >=10) else 0, EPS115bcc[j]['note_cc'], EPS115bsn[j]['note_sn'] ],

                        [ EPS115g[j], coefS1STAPS1[13], EPS115g[j]*coefS1STAPS1[13], "MOYENNE", sort115g.index(EPS115g[j])+1, (EPS115g[j] >=10), creditS1STAPS1[13], creditS1STAPS1[13] if (EPS115g[j] >=10) else 0, EPS115gcc[j]['note_cc'], EPS115gsn[j]['note_sn'] ],

                        [ EPS115j[j], coefS1STAPS1[6], EPS115j[j]*coefS1STAPS1[6], "MOYENNE", sort115j.index(EPS115j[j])+1, (EPS115j[j] >=10), creditS1STAPS1[6], creditS1STAPS1[6] if (EPS115j[j] >=10) else 0, EPS115jcc[j]['note_cc'], EPS115jsn[j]['note_sn'] ],

                        #[ EPS115l[j], coefS1STAPS1[7], EPS115l[j]*coefS1STAPS1[7], "MOYENNE", sort115l.index(EPS115l[j])+1, (EPS115l[j] >=10), creditS1STAPS1[7], creditS1STAPS1[7] if ((EPS115a[j]+EPS115g[j]+EPS115j[j]+EPS115l[j]) >=40) else 0, EPS115lcc[j]['note_cc'], EPS115lsn[j]['note_sn']  ],

                        [ EPS115f[j], coefS1STAPS1[8], EPS115f[j]*coefS1STAPS1[8], "MOYENNE", sort115f.index(EPS115f[j])+1, (EPS115f[j] >=10), creditS1STAPS1[8], creditS1STAPS1[8] if ((EPS115a[j]+EPS115g[j]+EPS115j[j]+EPS115f[j]) >=40) else 0, EPS115fcc[j]['note_cc'], EPS115fsn[j]['note_sn']  ],

                        [ EPS116[j],  coefS1STAPS1[9], EPS116[j]*coefS1STAPS1[9], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[9], creditS1STAPS1[9] if (EPS116[j] >=10) else 0, EPS116cc[j]['note_cc'], EPS116sn[j]['note_sn'] ],

                        [ EPS117[j], coefS1STAPS1[10], 

                            EPS117[j]*coefS1STAPS1[10], 

                            round( ((EPS117[j]*coefS1STAPS1[10]) + (EPS118[j]*coefS1STAPS1[11]) + (EPS119[j]*coefS1STAPS1[12])) / ( coefS1STAPS1[10]+coefS1STAPS1[11]+coefS1STAPS1[12]) ,2), 

                            sort117.index(EPS117[j])+1, 

                            (EPS117[j] >=10), 
                            
                            creditS1STAPS1[10],
                            creditS1STAPS1[10] if (EPS117[j] >=10) else 0,

                            EPS117cc[j]['note_cc'], EPS117sn[j]['note_sn']
                        ],

                        [ EPS118[j], coefS1STAPS1[11], EPS118[j]*coefS1STAPS1[11], "MOYENNE", sort118.index(EPS118[j])+1, (EPS118[j] >=10), creditS1STAPS1[11], creditS1STAPS1[11] if (EPS118[j] >=10) else 0, EPS118cc[j]['note_cc'], EPS118sn[j]['note_sn'] ],

                        [ EPS119[j], coefS1STAPS1[11], EPS119[j]*coefS1STAPS1[11], "MOYENNE", sort119.index(EPS119[j])+1, (EPS119[j] >=10), creditS1STAPS1[11], creditS1STAPS1[11] if (EPS119[j] >=10) else 0, EPS119cc[j]['note_cc'], EPS119sn[j]['note_sn'] ],

                        [ 
                            ( coefS1STAPS1[0] + coefS1STAPS1[1] + coefS1STAPS1[2] + coefS1STAPS1[3] + coefS1STAPS1[4] + coefS1STAPS1[13] + coefS1STAPS1[6] + coefS1STAPS1[8] + coefS1STAPS1[9] + coefS1STAPS1[10] + coefS1STAPS1[11] + coefS1STAPS1[12] ), #coefsomme

                            round( EPS111[j]*coefS1STAPS1[0] + EPS112[j]*coefS1STAPS1[1] + EPS113[j]*coefS1STAPS1[2] + EPS114[j]*coefS1STAPS1[3] + EPS115a[j]*coefS1STAPS1[4] + EPS115g[j]*coefS1STAPS1[13] + EPS115j[j]*coefS1STAPS1[6] + EPS115f[j]*coefS1STAPS1[8] + EPS116[j]*coefS1STAPS1[9] + EPS117[j]*coefS1STAPS1[10] + EPS118[j]*coefS1STAPS1[11] + EPS119[j]*coefS1STAPS1[12], 2),

                            round(( EPS111[j]*coefS1STAPS1[0] + EPS112[j]*coefS1STAPS1[1] + EPS113[j]*coefS1STAPS1[2] + EPS114[j]*coefS1STAPS1[3] + EPS115a[j]*coefS1STAPS1[4] + EPS115g[j]*coefS1STAPS1[13] + EPS115j[j]*coefS1STAPS1[6] + EPS115f[j]*coefS1STAPS1[8] + EPS116[j]*coefS1STAPS1[9]  + EPS117[j]*coefS1STAPS1[10] + EPS118[j]*coefS1STAPS1[11] + EPS119[j]*coefS1STAPS1[12] ) / ( coefS1STAPS1[0] + coefS1STAPS1[1] + coefS1STAPS1[2] + coefS1STAPS1[3] + coefS1STAPS1[4] + coefS1STAPS1[13] + coefS1STAPS1[6] + coefS1STAPS1[8] + coefS1STAPS1[9] + coefS1STAPS1[10] + coefS1STAPS1[11] + coefS1STAPS1[12]), 2 ),
                        ]
        ]
                
        staps1Moyenne.append(matrice[13][2])

        listeMatrice.append(matrice)

        staps1Moyenne.sort(reverse=True)
        moy = stat.mean(staps1Moyenne)
        moy = round(moy, 2)
        session = 'Janvier 2023'

        filiere = 'STAPS'

########################################################### STATS VALIDATION ####################################################################################################################################
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
    #for i in range (len(EPS115b)):
    #    if EPS115b[i] >= 10:
    #        val6['nombre']+=1
    for i in range (len(EPS115g)):
        if EPS115g[i] >= 10:
            val6['nombre']+=1
    val6['pourcentage']= round(((val6['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(EPS115j)):
        if EPS115j[i] >= 10:
            val7['nombre']+=1
    val7['pourcentage']= round(((val7['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    #for i in range (len(EPS115l)):
    #    if EPS115l[i] >= 10:
    #        val8['nombre']+=1
    for i in range (len(EPS115f)):
        if EPS115f[i] >= 10:
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

    #statMention(EPS115b,e115b)
    #pourcentageMention(e115b, len(infoEtudiantSTAPS1))

    statMention(EPS115g,e115g)
    pourcentageMention(e115g, len(infoEtudiantSTAPS1))

    statMention(EPS115j,e115j)
    pourcentageMention(e115j, len(infoEtudiantSTAPS1))

    #statMention(EPS115l,e115l)
    #pourcentageMention(e115l, len(infoEtudiantSTAPS1))

    statMention(EPS115f,e115f)
    pourcentageMention(e115f, len(infoEtudiantSTAPS1))

    statMention(EPS116,e116)
    pourcentageMention(e116, len(infoEtudiantSTAPS1))

    statMention(EPS117,e117)
    pourcentageMention(e117, len(infoEtudiantSTAPS1))

    statMention(EPS118,e118)
    pourcentageMention(e118, len(infoEtudiantSTAPS1))

    statMention(EPS119,e119)
    pourcentageMention(e119, len(infoEtudiantSTAPS1))


    UEStats = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12]
    UEstats_mention = [e111, e112, e113, e114, e115a, e115g, e115j, e115f, e116, e117, e118, e119] #e115b , e115l

    semestre1MDS = [filiere, listeMatrice, staps1Moyenne, moy, session , creditS1STAPS1, UEStats, UEstats_mention, UeNomCode, listeMatriceS2epsR,  listeMatriceS2EpsSynthese ]

    return render(request, 'bulletin/releveCommun/releveCommun2.html', {'semestre1MDS': semestre1MDS} )

##########################################################################################################################################################################################################################################################################


#PV MDS1 SEMESTRE1
def resultatCommunmds(request):

    infoEtudiantMDS =list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("coefficient", "intitule_UE"))
    coefS1MDS1 = epurationCoef(coefS1MDS1)

    creditS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="GESTION").values("nombre_credit"))
    creditS1MDS1 = epurationCre(creditS1MDS1)

########################################################### S1 STATS VAL     ############################################################################################################################
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

########################################################### PV SEMESTRE 1    ############################################################################################################################

    MDS111 =list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='EXAMEN').values('note_Examen'))
    MDS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='EXAMEN').values('note_cc'))
    MDS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='EXAMEN').values('note_sn'))
    sort111 = epurationTriCroissant(MDS111)

    MDS111b =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='EXAMEN').values('note_Examen'))
    MDS111bcc =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='EXAMEN').values('note_cc'))
    MDS111bsn =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='EXAMEN').values('note_sn'))
    sort111b = epurationTriCroissant(MDS111b)

    MDS112 =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='EXAMEN').values('note_Examen'))
    MDS112cc =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='EXAMEN').values('note_cc'))
    MDS112sn =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='EXAMEN').values('note_sn'))
    sort112 = epurationTriCroissant(MDS112)

    MDS112b =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='EXAMEN').values('note_Examen'))
    MDS112bcc =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='EXAMEN').values('note_cc'))
    MDS112bsn =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='EXAMEN').values('note_sn'))
    sort112b = epurationTriCroissant(MDS112b)

    MDS113 =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='EXAMEN').values('note_Examen'))
    MDS113cc =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='EXAMEN').values('note_cc'))
    MDS113sn =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='EXAMEN').values('note_sn'))
    sort113 = epurationTriCroissant(MDS113)

    MDS114 =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='EXAMEN').values('note_Examen'))
    MDS114cc =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='EXAMEN').values('note_cc'))
    MDS114sn =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='EXAMEN').values('note_sn'))
    sort114 = epurationTriCroissant(MDS114)

    MDS115 =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='EXAMEN').values('note_Examen'))
    MDS115cc =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='EXAMEN').values('note_cc'))
    MDS115sn =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='EXAMEN').values('note_sn'))
    sort115 = epurationTriCroissant(MDS115)

    MDS116 =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='EXAMEN').values('note_Examen'))
    MDS116cc =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='EXAMEN').values('note_cc'))
    MDS116sn =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='EXAMEN').values('note_sn'))
    sort116 = epurationTriCroissant(MDS116)

    MDS117 =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='EXAMEN').values('note_Examen'))
    MDS117cc =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='EXAMEN').values('note_cc'))
    MDS117sn =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='EXAMEN').values('note_sn'))
    sort117 = epurationTriCroissant(MDS117)

    MDS117b =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='EXAMEN').values('note_Examen'))
    MDS117bcc =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='EXAMEN').values('note_cc'))
    MDS117bsn =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='EXAMEN').values('note_sn'))
    sort117b = epurationTriCroissant(MDS117b)

    listeMatrice = []
    mds1Moyenne = []

    for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

        matrice = [
                infoEtudiantMDS[j],

                [
                    MDS111[j]
                    , coefS1MDS1[0]
                    , MDS111[j]*coefS1MDS1[0]
                    , round( ((MDS111[j]*coefS1MDS1[0]) + (MDS111b[j]*coefS1MDS1[1]) + ( MDS112[j]*coefS1MDS1[2]) + (MDS112b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2)
                    , sort111.index(MDS111[j])+1
                    , (MDS111[j]>=10)
                    , creditS1MDS1[0]
                    , creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0
                    , MDS111cc[j]['note_cc']
                    , MDS111sn[j]['note_sn']
                ],

                [ MDS111b[j], coefS1MDS1[1], MDS111b[j]*coefS1MDS1[1], "MOYENNE", sort111b.index(MDS111b[j])+1,(MDS111b[j]>=10), creditS1MDS1[1], creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0, MDS111bcc[j]['note_cc'], MDS111bsn[j]['note_sn'] ],

                [ MDS112[j], coefS1MDS1[2], MDS112[j]*coefS1MDS1[2], "MOYENNE", sort112.index(MDS112[j])+1,(MDS112[j]>=10), creditS1MDS1[2], creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0 ,MDS112cc[j]['note_cc'], MDS112sn[j]['note_sn']],

                [ MDS112b[j], coefS1MDS1[3], MDS112b[j]*coefS1MDS1[3], "MOYENNE", sort112b.index(MDS112b[j])+1,(MDS112b[j]>=10), creditS1MDS1[3], creditS1MDS1[3] if((MDS112[j]+MDS112b[j])>=20) else 0, MDS112cc[j]['note_cc'], MDS112sn[j]['note_sn'] ],


                [
                    MDS113[j]
                    , coefS1MDS1[4]
                    , MDS113[j]*coefS1MDS1[4]
                    , round( ((MDS113[j]*coefS1MDS1[4]) + (MDS114[j]*coefS1MDS1[5]) + MDS115[j]*coefS1MDS1[6] + MDS116[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2)
                    , sort113.index(MDS113[j])+1
                    , (MDS113[j]>=10)
                    , creditS1MDS1[4]
                    , creditS1MDS1[4] if (MDS113[j]>=10) else 0
                    , MDS113cc[j]['note_cc']
                    , MDS113sn[j]['note_sn']
                ],

                [ MDS114[j], coefS1MDS1[5], MDS114[j]*coefS1MDS1[5], "MOYENNE", sort114.index(MDS114[j])+1,(MDS114[j]>=10), creditS1MDS1[5], creditS1MDS1[5] if (MDS114[j]>=10) else 0, MDS114cc[j]['note_cc'], MDS114sn[j]['note_sn'] ],

                [ MDS115[j], coefS1MDS1[6], MDS115[j]*coefS1MDS1[6], "MOYENNE", sort115.index(MDS115[j])+1,(MDS115[j]>=10), creditS1MDS1[6], creditS1MDS1[6] if (MDS115[j]>=10) else 0, MDS115cc[j]['note_cc'], MDS115sn[j]['note_sn'] ],

                [ MDS116[j], coefS1MDS1[7], MDS116[j]*coefS1MDS1[7], "MOYENNE", sort116.index(MDS116[j])+1,(MDS116[j]>=10), creditS1MDS1[7], creditS1MDS1[7] if (MDS116[j]>=10) else 0, MDS116cc[j]['note_cc'], MDS116sn[j]['note_sn'] ],


                [
                    MDS117[j]
                    , coefS1MDS1[8]
                    , MDS117[j]*coefS1MDS1[8]
                    , round(( MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2)
                    , sort117.index(MDS117[j])+1
                    , (MDS117[j]>=10)
                    , creditS1MDS1[8]
                    , creditS1MDS1[8] if (MDS117[j]>=10) else 0
                    , MDS117cc[j]['note_cc']
                    , MDS117sn[j]['note_sn']
                ],

                [ MDS117b[j], coefS1MDS1[9], MDS117b[j]*coefS1MDS1[9], "MOYENNE", sort117b.index(MDS117b[j])+1,(MDS117b[j]>=10), creditS1MDS1[9], creditS1MDS1[9] if ( (MDS117b[j]+MDS117[j]) >=20) else 0, MDS117bcc[j]['note_cc'], MDS117bsn[j]['note_sn'] ],

                [
                    ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),

                   round (MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] , 2),

                   round (( MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                ]

        ]
        #Decompte des crédits totaux PV semestre 1 Gestion
        MDSCreditCountPV(matrice)

        listeMatrice.append(matrice)
        mds1Moyenne.append(matrice[11][2])
        mds1Moyenne.sort(reverse=True)

        moy = stat.mean(mds1Moyenne)
        moy = round(moy, 2)
        session = 'Janvier 2023'

        filiere="GESTION"

########################################################### PV SEMESTRE 1  CC ###############################################################################
    listeMatrices1GesCC = []
    for j in range(len(infoEtudiantMDS)):

        matrices1GesCC = [

            infoEtudiantMDS[j],

            MDS111cc[j]['note_cc'],

            MDS111bcc[j]['note_cc'],

            MDS112cc[j]['note_cc'],

            MDS112bcc[j]['note_cc'],

            MDS113cc[j]['note_cc'],

            MDS114cc[j]['note_cc'],

            MDS115cc[j]['note_cc'],

            MDS116cc[j]['note_cc'],

            MDS117cc[j]['note_cc'],

            MDS117bcc[j]['note_cc'],

        ]
        listeMatrices1GesCC.append(matrices1GesCC)

########################################################### PV SEMESTRE 1 RATTRAPAGE ############################################################################################################################
    MDS111R =list(Evaluation.objects.filter(uniteEnseignement_id=40, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort111R = epurationRattrapage(MDS111R)

    MDS111bR =list(Evaluation.objects.filter(uniteEnseignement_id=41, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort111bR = epurationRattrapage(MDS111bR)

    MDS112R =list(Evaluation.objects.filter(uniteEnseignement_id=42, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort112R = epurationRattrapage(MDS112R)

    MDS112bR =list(Evaluation.objects.filter(uniteEnseignement_id=43, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort112bR = epurationRattrapage(MDS112bR)

    MDS113R =list(Evaluation.objects.filter(uniteEnseignement_id=44, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort113R = epurationRattrapage(MDS113R)

    MDS114R =list(Evaluation.objects.filter(uniteEnseignement_id=45, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort114R = epurationRattrapage(MDS114R)

    MDS115R =list(Evaluation.objects.filter(uniteEnseignement_id=46, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort115R = epurationRattrapage(MDS115R)

    MDS116R =list(Evaluation.objects.filter(uniteEnseignement_id=47, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort116R = epurationRattrapage(MDS116R)

    MDS117R =list(Evaluation.objects.filter(uniteEnseignement_id=48, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort117R = epurationRattrapage(MDS117R)

    MDS117bR =list(Evaluation.objects.filter(uniteEnseignement_id=49, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort117b = epurationRattrapage(MDS117bR)

    listeMatriceS1GesR = []
    matriceS1mdsR = []
    
    for j in range( len(infoEtudiantMDS) ):
        matriceS1mdsR = [
                infoEtudiantMDS[j],

                MDS111R[j],

                MDS111bR[j],

                MDS112R[j],

                MDS112bR[j],

                MDS113R[j],

                MDS114R[j],

                MDS115R[j],

                MDS116R[j],

                MDS117R[j],

                MDS117bR[j],
        ]
        listeMatriceS1GesR.append(matriceS1mdsR)

########################################################### PV SEMESTRE 1 SYNTHESE   ############################################################################################################################
    ##MATRICE SYNTHESE AVEC FONCTION
    listeMatricemdsS1Synthese, listeMoyenne = matriceSynthesemds1(listeMatrice, listeMatriceS1GesR, listeMatrice, listeMatrices1GesCC )
    #MDSCreditCount(listeMatricemdsS1Synthese)

    listeMatriceSynthese = []
    mds1MoyenneSyn = []

    for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

        matrice = [
                infoEtudiantMDS[j],

                [
                    ( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] )
                    , coefS1MDS1[0]
                    , (round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] ) * coefS1MDS1[0]
                    #, round( ((MDS111[j]*coefS1MDS1[0]) + (MDS111b[j]*coefS1MDS1[1]) + ( MDS112[j]*coefS1MDS1[2]) + (MDS112b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2)
                    , round( (( (round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] )*coefS1MDS1[0] ) + ( ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1]) + ( ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] )*coefS1MDS1[2]) + (( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] )*coefS1MDS1[3])) / (coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2)
                    #, sort111.index(MDS111[j])+1
                    , "RANG"#sort111.index( round(listeMatrices2GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][1]> 0) else MDS111[j] )+1
                    #, (MDS111[j]>=10)
                    , "RAS" #( ( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if ( listeMatriceS1GesR[j][1]> 0) else MDS111[j] ) >= 10 ) 
                    , creditS1MDS1[0]
                    #, creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0
                    , creditS1MDS1[1] if ((( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] ) + ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] ) )>=20) else 0 
                    , MDS111cc[j]['note_cc']
                    , MDS111sn[j]['note_sn']
                ],

                [
                    ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] )
                    , coefS1MDS1[1]
                    , ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1]
                    , "MOYENNE"
                    ,sort111b.index((round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j]))+1
                    , 'RAS'#((round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j])>=10)
                    , creditS1MDS1[1]
                    , creditS1MDS1[1] if ((( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j]) + (round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j]))>=20) else 0
                    , MDS111bcc[j]['note_cc']
                    , MDS111bsn[j]['note_sn']
                ],

                [
                    #MDS112[j]
                    ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] )
                    , coefS1MDS1[2]
                    #, MDS112[j]*coefS1MDS1[2]
                    ,( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] )*coefS1MDS1[2]
                    , "MOYENNE"
                    ,"RANG"#, sort112.index(MDS112[j])+1
                    #,(MDS112[j]>=10)
                    , ( ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] ) >= 10 )
                    , creditS1MDS1[2]
                    #, creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0 
                    , creditS1MDS1[1] if (( ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] ) + ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS112b[j] ) )>=20) else 0 
                    , MDS112cc[j]['note_cc']
                    , MDS112sn[j]['note_sn']
                ],

                [
                    #MDS112b[j]
                    ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] )
                    , coefS1MDS1[3]
                    #, MDS112b[j]*coefS1MDS1[3]
                    , ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] )*coefS1MDS1[3]
                    , "MOYENNE"

                    ,"RANG" # sort112b.index(MDS112b[j])+1
                    #,(MDS112b[j]>=10)
                    , (( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] )>=10)
                    , creditS1MDS1[3]
                    #, creditS1MDS1[3] if((MDS112[j]+MDS112b[j])>=20) else 0
                    , creditS1MDS1[3] if((( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] ) + ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] ))>=20) else 0
                    , MDS112cc[j]['note_cc']
                    , MDS112sn[j]['note_sn'] 
                ],


                [ 
                    #MDS113[j]
                    ( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] )
                    , coefS1MDS1[4]
                    #, MDS113[j]*coefS1MDS1[4] 
                    , ( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] )*coefS1MDS1[4]
                    #,round( ((MDS113[j]*coefS1MDS1[4]) + (MDS114[j]*coefS1MDS1[5]) + MDS115[j]*coefS1MDS1[6] + MDS116[j]*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2)
                    , round( ((( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] )*coefS1MDS1[4]) + (( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] )*coefS1MDS1[5]) + ( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] )*coefS1MDS1[6] + ( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] )*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2)
                    ,"RANG" #sort113.index(MDS113[j])+1
                    #,(MDS113[j]>=10)
                    , (( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] )>=10) 
                    ,creditS1MDS1[4]
                    #,creditS1MDS1[4] if (MDS113[j]>=10) else 0
                    , creditS1MDS1[4] if (( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] )>=10) else 0
                    ,MDS113cc[j]['note_cc']
                    ,MDS113sn[j]['note_sn']
                ],

                [ 
                    #MDS114[j]
                    ( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] )
                
                    , coefS1MDS1[5]
                    #, MDS114[j]*coefS1MDS1[5]
                    , ( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] )*coefS1MDS1[5]
                    , "MOYENNE"
                    #, sort114.index(MDS114[j])+1
                    , sort114.index(( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] ))+1
                    #, (MDS114[j]>=10)
                    , (( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] )>=10)
                    , creditS1MDS1[5]
                    #, creditS1MDS1[5] if (MDS114[j]>=10) else 0
                    , creditS1MDS1[5] if (( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] )>=10) else 0
                    , MDS114cc[j]['note_cc']
                    , MDS114sn[j]['note_sn'] 
                ],

                [ 
                    #MDS115[j]
                    ( round(listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j])
                    , coefS1MDS1[6]
                    #, MDS115[j]*coefS1MDS1[6]
                    ,( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] )*coefS1MDS1[6]
                    , "MOYENNE"
                    , "RANG" #sort115.index(MDS115[j])+1
                    #,(MDS115[j]>=10)
                    , ( ( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] )>=10 )
                    , creditS1MDS1[6]
                    #, creditS1MDS1[6] if (MDS115[j]>=10) else 0
                    , creditS1MDS1[6] if (( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] )>=10) else 0
                    , MDS115cc[j]['note_cc']
                    , MDS115sn[j]['note_sn'] 
                ],

                [ 
                    #MDS116[j]
                    ( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] )
                    , coefS1MDS1[7]

                    #, MDS116[j]*coefS1MDS1[7]
                    , ( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] )*coefS1MDS1[7]
                    , "MOYENNE"

                    ,"RANG" #sort116.index(MDS116[j])+1
                    #,(MDS116[j]>=10)
                    , (( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] )>=10)
                    , creditS1MDS1[7]
                    #, creditS1MDS1[7] if (MDS116[j]>=10) else 0
                    , creditS1MDS1[7] if (( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] )>=10) else 0
                    , MDS116cc[j]['note_cc']
                    , MDS116sn[j]['note_sn'] 
                ],

                [ 
                    #MDS117[j]
                    ( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )
                    , coefS1MDS1[8]
                    #, MDS117[j]*coefS1MDS1[8]
                    ,( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )*coefS1MDS1[8]
                    #, round(( MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2) 
                    , round(( ( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )*coefS1MDS1[8] + ( ( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] ) )*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2)
                    #,sort117.index(MDS117[j])+1
                    , sort117.index(( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] ))+1
                    #,(MDS117[j]>=10)
                    , (( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )>=10)
                    ,creditS1MDS1[8]
                    #,creditS1MDS1[8] if (MDS117[j]>=10) else 0
                    , creditS1MDS1[8] if (( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )>=10) else 0
                    ,MDS117cc[j]['note_cc']
                    ,MDS117sn[j]['note_sn']
                ],

                [ 
                    #MDS117b[j]
                    ( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] )
                    , coefS1MDS1[9]
                    #, MDS117b[j]*coefS1MDS1[9]
                    , ( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] )*coefS1MDS1[9]
                    , "MOYENNE"
                    , "RANG"#, sort117b.index(MDS117b[j])+1,(MDS117b[j]>=10)
                    , (( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] )>=10)
                    , creditS1MDS1[9]
                    #, creditS1MDS1[9] if ( (MDS117b[j]+MDS117[j]) >=20) else 0
                    , creditS1MDS1[9] if ( (( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] )+( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] )) >=20) else 0
                    , MDS117bcc[j]['note_cc']
                    , MDS117bsn[j]['note_sn'] 
                ],

                [
                    ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),

                   #round (MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] , 2),

                   #round (( MDS111[j]*coefS1MDS1[0]+MDS111b[j]*coefS1MDS1[1]+MDS112[j]*coefS1MDS1[2]+MDS112b[j]*coefS1MDS1[3]+MDS113[j]*coefS1MDS1[4]+MDS114[j]*coefS1MDS1[5]+MDS115[j]*coefS1MDS1[6]+MDS116[j]*coefS1MDS1[7]+ MDS117[j]*coefS1MDS1[8]+MDS117b[j]*coefS1MDS1[9] )/( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                   round ( ( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] ) *coefS1MDS1[0] + ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1] + ( ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] ) )*coefS1MDS1[2] + ( ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] ) )*coefS1MDS1[3] + ( ( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] ) )*coefS1MDS1[4] + ( ( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] ) )*coefS1MDS1[5] + ( ( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] ) )*coefS1MDS1[6] + ( ( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] ) )*coefS1MDS1[7] + ( ( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] ) )*coefS1MDS1[8] + ( ( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] ) )*coefS1MDS1[9] , 2),

                   round (( ( round(listeMatriceS1GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][1]> 0) else MDS111[j] ) *coefS1MDS1[0] + ( round( listeMatriceS1GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1] + ( ( round(listeMatriceS1GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][3]> 0) else MDS112[j] ) )*coefS1MDS1[2] + ( ( round(listeMatriceS1GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][4]> 0) else MDS112b[j] ) )*coefS1MDS1[3] + ( ( round(listeMatriceS1GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][5]> 0) else MDS113[j] ) )*coefS1MDS1[4] + ( ( round(listeMatriceS1GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][6]> 0) else MDS114[j] ) )*coefS1MDS1[5] + ( ( round( listeMatriceS1GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][7]> 0) else MDS115[j] ) )*coefS1MDS1[6] + ( ( round(listeMatriceS1GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][8]> 0) else MDS116[j] ) )*coefS1MDS1[7] + ( ( round(listeMatriceS1GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][9]> 0) else MDS117[j] ))*coefS1MDS1[8] + ( ( round(listeMatriceS1GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatriceS1GesR[j][10]> 0) else MDS117b[j] ) )*coefS1MDS1[9] ) / ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                ]
        ]
        #Decompte des crédits totaux PV semestre 1 Gestion
        MDSCreditCountPV(matrice)

        listeMatriceSynthese.append(matrice)
        mds1MoyenneSyn.append(matrice[11][2])

    #DECOMPTE DE CREDITS
    #MDSCreditCount()

########################################################### STATS VALIDATION ####################################################################################################################################
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

########################################################### STAT MENTION ###############################################################################################################################################
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


    semestre1MDS = [filiere, listeMatrice, mds1Moyenne, moy, session, creditS1MDS1, UEStats, UEstats_mention, listeMatriceS1GesR, listeMatriceSynthese, listeMatricemdsS1Synthese ] #filiere, listeMatrice, staps1Moyenne, moy, session

    return render(request, 'bulletin/releveCommun/releveCommunmds.html', {'semestre1MDS': semestre1MDS})


#PV MDS1 SEMESTRE2
def resultatCommuns2mds(request):
########################################################### S2 STATS VAL     ############################################################################################################################

    UeNomCode = list( UniteEnseignement.objects.filter(semestre_id = 2, filiere="GESTION").values("code_UE","intitule_UE", "semestre_id", "nombre_credit") )

    infoEtudiantMDS =list(Etudiant.objects.filter(filiere="GESTION", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="GESTION").values("coefficient", "intitule_UE"))
    coefS1MDS1 = epurationCoef(coefS1MDS1)

    creditS1MDS1 = list(UniteEnseignement.objects.filter(semestre_id=2,filiere="GESTION").values("nombre_credit"))
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

########################################################### PV SEMESTRE 2  ############################################################################################################################        
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

                [
                    MDS111[j]
                    , coefS1MDS1[0]
                    , MDS111[j]*coefS1MDS1[0]
                    , round( ((MDS111[j]*coefS1MDS1[0]) + (MDS111b[j]*coefS1MDS1[1]) + ( MDS112[j]*coefS1MDS1[2]) + (MDS112b[j]*coefS1MDS1[3]))/(coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2)
                    , sort111.index(MDS111[j])+1,(MDS111[j]>=10)
                    , creditS1MDS1[0]
                    , creditS1MDS1[1] if ((MDS111[j]+MDS111b[j])>=20) else 0
                    , MDS111cc[j]['note_cc']
                    , MDS111sn[j]['note_sn']
                ],

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
        #Decompte des crédits totaux PV semestre 1 Gestion
        MDSCreditCountPV(matrice)

        listeMatrice.append(matrice)
        mds1Moyenne.append(matrice[11][2])
        mds1Moyenne.sort(reverse=True)

        moy = stat.mean(mds1Moyenne)
        moy = round(moy, 2)
        session = 'Janvier 2023'

        filiere="GESTION"

########################################################### MATRICE RATTRAPAGE ###########################################################
    MDS121R =list(Evaluation.objects.filter(uniteEnseignement_id=88, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort121R = epurationRattrapage(MDS121R)

    MDS121bR =list(Evaluation.objects.filter(uniteEnseignement_id=89, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort121bR = epurationRattrapage(MDS121bR)

    MDS122R =list(Evaluation.objects.filter(uniteEnseignement_id=90, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort122R = epurationRattrapage(MDS122R)

    MDS122bR =list(Evaluation.objects.filter(uniteEnseignement_id=91, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort122bR = epurationRattrapage(MDS122bR)

    MDS123R =list(Evaluation.objects.filter(uniteEnseignement_id=92, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort123R = epurationRattrapage(MDS123R)

    MDS124R =list(Evaluation.objects.filter(uniteEnseignement_id=93, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort124R = epurationRattrapage(MDS124R)

    MDS125R =list(Evaluation.objects.filter(uniteEnseignement_id=95, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort125R = epurationRattrapage(MDS125R)

    MDS126R =list(Evaluation.objects.filter(uniteEnseignement_id=96, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort126R = epurationRattrapage(MDS126R)

    MDS127R =list(Evaluation.objects.filter(uniteEnseignement_id=97, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort127R = epurationRattrapage(MDS127R)

    MDS127bR =list(Evaluation.objects.filter(uniteEnseignement_id=98, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort127bR = epurationRattrapage(MDS127bR)

    listeMatrices2GesR = []

    for j in range( len(infoEtudiantMDS) ):

        matrices2mdsR = [

            infoEtudiantMDS[j],

            MDS121R[j],

            MDS121bR[j],

            MDS122R[j],

            MDS122bR[j],

            MDS123R[j],

            MDS124R[j],

            MDS125R[j],

            MDS126R[j],

            MDS127R[j],

            MDS127bR[j]
        ]
        listeMatrices2GesR.append(matrices2mdsR)

########################################################### MATRICE SYNTHESE #############################################################
    listeMatriceS = []
    for j in range( len(infoEtudiantMDS) ): #len(infoEtudiantMDS)

        matrice = [
                infoEtudiantMDS[j],

                [  ( round(listeMatrices2GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][1]> 0) else MDS111[j] )

                    , coefS1MDS1[0]
                    
                    , (round(listeMatrices2GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][1]> 0) else MDS111[j] ) * coefS1MDS1[0]
                    
                    , round( (( (round(listeMatrices2GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][1]> 0) else MDS111[j] )*coefS1MDS1[0] ) + ( ( round( listeMatrices2GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1]) + ( ( round(listeMatrices2GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][3]> 0) else MDS112[j] )*coefS1MDS1[2]) + (( round(listeMatrices2GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][4]> 0) else MDS112b[j] )*coefS1MDS1[3])) / (coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]), 2)
                    
                    , "RANG"#sort111.index( round(listeMatrices2GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][1]> 0) else MDS111[j] )+1
                    
                    , ( ( round(listeMatrices2GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if ( listeMatrices2GesR[j][1]> 0) else MDS111[j] ) >= 10 ) 
                    
                    , creditS1MDS1[0]

                    , creditS1MDS1[1] if ((( round(listeMatrices2GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][1]> 0) else MDS111[j] ) + ( round( listeMatrices2GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][2]> 0) else MDS111b[j] ) )>=20) else 0 
                    
                    , MDS111cc[j]['note_cc']

                    , MDS111sn[j]['note_sn']  
                ],

                
                [ ( round( listeMatrices2GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][2]> 0) else MDS111b[j] )

                    , coefS1MDS1[1]
                    
                    , ( round( listeMatrices2GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1]
                    
                    , "MOYENNE"
                    
                    , sort111b.index((round( listeMatrices2GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][2]> 0) else MDS111b[j]))+1
                    
                    , ((round( listeMatrices2GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][2]> 0) else MDS111b[j])>=10)
                    
                    , creditS1MDS1[1]
                    
                    , creditS1MDS1[1] if ((( round(listeMatrices2GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][1]> 0) else MDS111[j]) + (round( listeMatrices2GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][2]> 0) else MDS111b[j]))>=20) else 0
                    
                    , MDS111bcc[j]['note_cc']
                    
                    , MDS111bsn[j]['note_sn'] 
                ],

                
                [ ( round(listeMatrices2GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][3]> 0) else MDS112[j] )

                    , coefS1MDS1[2]
                    
                    , ( round(listeMatrices2GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][3]> 0) else MDS112[j] )*coefS1MDS1[2]
                    
                    , "MOYENNE"
                    
                    , 'RANG'#sort112.index( ( round(listeMatrices2GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][3]> 0) else MDS112[j] ) )+1
                    
                    , ( ( round(listeMatrices2GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][3]> 0) else MDS112[j] ) >= 10 ) 
                    
                    , creditS1MDS1[2]
                    
                    , creditS1MDS1[1] if (( ( round(listeMatrices2GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][3]> 0) else MDS112[j] ) + ( round(listeMatrices2GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][2]> 0) else MDS112b[j] ) )>=20) else 0 
                    
                    , MDS112cc[j]['note_cc']
                    
                    , MDS112sn[j]['note_sn']
                ],

                
                [ ( round(listeMatrices2GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][4]> 0) else MDS112b[j] )
                
                    , coefS1MDS1[3]
                    
                    , ( round(listeMatrices2GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][4]> 0) else MDS112b[j] )*coefS1MDS1[3]
                    
                    , "MOYENNE"
                    
                    , 'RANG'#sort112b.index(( round(listeMatrices2GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][4]> 0) else MDS112b[j] ))+1
                    
                    , (( round(listeMatrices2GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][4]> 0) else MDS112b[j] )>=10)
                    
                    , creditS1MDS1[3]
                    
                    , creditS1MDS1[3] if((( round(listeMatrices2GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][3]> 0) else MDS112[j] ) + ( round(listeMatrices2GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][4]> 0) else MDS112b[j] ))>=20) else 0
                    
                    , MDS112cc[j]['note_cc']
                    
                    , MDS112sn[j]['note_sn'] 
                ],


                [ ( round(listeMatrices2GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][5]> 0) else MDS113[j] )
                
                    , coefS1MDS1[4]
                    
                    , ( round(listeMatrices2GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][5]> 0) else MDS113[j] )*coefS1MDS1[4]

                    , round( ((( round(listeMatrices2GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][5]> 0) else MDS113[j] )*coefS1MDS1[4]) + (( round(listeMatrices2GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][6]> 0) else MDS114[j] )*coefS1MDS1[5]) + ( round( listeMatrices2GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][7]> 0) else MDS115[j] )*coefS1MDS1[6] + ( round(listeMatrices2GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][8]> 0) else MDS116[j] )*coefS1MDS1[7])/(coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]), 2)
                    
                    , "RANG"#sort113.index(( round(listeMatrices2GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][5]> 0) else MDS113[j] ))+1
                    
                    , (( round(listeMatrices2GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][5]> 0) else MDS113[j] )>=10) 

                    , creditS1MDS1[4]

                    , creditS1MDS1[4] if (( round(listeMatrices2GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][5]> 0) else MDS113[j] )>=10) else 0

                    , MDS113cc[j]['note_cc']

                    , MDS113sn[j]['note_sn']

                ],


                [ ( round(listeMatrices2GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][6]> 0) else MDS114[j] )
                
                    , coefS1MDS1[5]
                    
                    , ( round(listeMatrices2GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][6]> 0) else MDS114[j] )*coefS1MDS1[5]
                    
                    , "MOYENNE"
                    
                    , sort114.index(( round(listeMatrices2GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][6]> 0) else MDS114[j] ))+1
                    
                    , (( round(listeMatrices2GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][6]> 0) else MDS114[j] )>=10)
                    
                    , creditS1MDS1[5]
                    
                    , creditS1MDS1[5] if (( round(listeMatrices2GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][6]> 0) else MDS114[j] )>=10) else 0
                    
                    , MDS114cc[j]['note_cc']
                    
                    , MDS114sn[j]['note_sn'] 
                
                ],

                #7
                [ ( round(listeMatrices2GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][7]> 0) else MDS115[j])
                
                    , coefS1MDS1[6]
                    
                    ,( round( listeMatrices2GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][7]> 0) else MDS115[j] )*coefS1MDS1[6]
                    
                    , "MOYENNE"
                    
                    , "RANG"#sort115.index(( round( listeMatrices2GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][7]> 0) else MDS115[j] ))+1
                    
                    , ( ( round( listeMatrices2GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][7]> 0) else MDS115[j] )>=10 )
                    
                    , creditS1MDS1[6]
                    
                    , creditS1MDS1[6] if (( round( listeMatrices2GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][7]> 0) else MDS115[j] )>=10) else 0
                    
                    , MDS115cc[j]['note_cc']
                    
                    , MDS115sn[j]['note_sn'] 
                
                ],

                
                [ ( round(listeMatrices2GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][8]> 0) else MDS116[j] )
                
                    , coefS1MDS1[7]
                    
                    , ( round(listeMatrices2GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][8]> 0) else MDS116[j] )*coefS1MDS1[7]
                    
                    , "MOYENNE"
                    
                    , "RANG"#sort116.index(( round(listeMatrices2GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][8]> 0) else MDS116[j] ))+1
                    
                    , (( round(listeMatrices2GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][8]> 0) else MDS116[j] )>=10)
                    
                    , creditS1MDS1[7]
                    
                    , creditS1MDS1[7] if (( round(listeMatrices2GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][8]> 0) else MDS116[j] )>=10) else 0
                    
                    , MDS116cc[j]['note_cc']
                    
                    , MDS116sn[j]['note_sn'] 
                ],


                [ ( round(listeMatrices2GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][9]> 0) else MDS117[j] )
                
                    , coefS1MDS1[8]
                    
                    ,( round(listeMatrices2GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][9]> 0) else MDS117[j] )*coefS1MDS1[8]
                    
                    , round(( ( round(listeMatrices2GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][9]> 0) else MDS117[j] )*coefS1MDS1[8] + ( ( round(listeMatrices2GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][10]> 0) else MDS117b[j] ) )*coefS1MDS1[9] )/(coefS1MDS1[8]+coefS1MDS1[9]),2)
                    
                    , sort117.index(( round(listeMatrices2GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][9]> 0) else MDS117[j] ))+1
                    
                    , (( round(listeMatrices2GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][9]> 0) else MDS117[j] )>=10)

                    , creditS1MDS1[8]

                    , creditS1MDS1[8] if (( round(listeMatrices2GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][9]> 0) else MDS117[j] )>=10) else 0

                    , MDS117cc[j]['note_cc']

                    , MDS117sn[j]['note_sn']
                ],


                [ ( round(listeMatrices2GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][10]> 0) else MDS117b[j] )
                    
                    , coefS1MDS1[9]
                    
                    , ( round(listeMatrices2GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][10]> 0) else MDS117b[j] )*coefS1MDS1[9]
                    
                    , "MOYENNE"
                    
                    , "RANG"#sort117b.index(( round(listeMatrices2GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][10]> 0) else MDS117b[j] ))+1
                    
                    , (( round(listeMatrices2GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][10]> 0) else MDS117b[j] )>=10)
                    
                    , creditS1MDS1[9]
                    
                    , creditS1MDS1[9] if ( (( round(listeMatrices2GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][10]> 0) else MDS117b[j] )+( round(listeMatrices2GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][9]> 0) else MDS117[j] )) >=20) else 0
                    
                    , MDS117bcc[j]['note_cc']
                    
                    , MDS117bsn[j]['note_sn'] 
                ],

                [
                    ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),

                   round ( ( round(listeMatrices2GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][1]> 0) else MDS111[j] ) *coefS1MDS1[0] + ( round( listeMatrices2GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1] + ( ( round(listeMatrices2GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][3]> 0) else MDS112[j] ) )*coefS1MDS1[2] + ( ( round(listeMatrices2GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][4]> 0) else MDS112b[j] ) )*coefS1MDS1[3] + ( ( round(listeMatrices2GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][5]> 0) else MDS113[j] ) )*coefS1MDS1[4] + ( ( round(listeMatrices2GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][6]> 0) else MDS114[j] ) )*coefS1MDS1[5] + ( ( round( listeMatrices2GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][7]> 0) else MDS115[j] ) )*coefS1MDS1[6] + ( ( round(listeMatrices2GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][8]> 0) else MDS116[j] ) )*coefS1MDS1[7] + ( ( round(listeMatrices2GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][9]> 0) else MDS117[j] ) )*coefS1MDS1[8] + ( ( round(listeMatrices2GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][10]> 0) else MDS117b[j] ) )*coefS1MDS1[9] , 2),

                   round (( ( round(listeMatrices2GesR[j][1]*0.7 + MDS111cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][1]> 0) else MDS111[j] ) *coefS1MDS1[0] + ( round( listeMatrices2GesR[j][2]*0.7 + MDS111bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][2]> 0) else MDS111b[j] )*coefS1MDS1[1] + ( ( round(listeMatrices2GesR[j][3]*0.7 + MDS112cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][3]> 0) else MDS112[j] ) )*coefS1MDS1[2] + ( ( round(listeMatrices2GesR[j][4]*0.7 + MDS112bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][4]> 0) else MDS112b[j] ) )*coefS1MDS1[3] + ( ( round(listeMatrices2GesR[j][5]*0.7 + MDS113cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][5]> 0) else MDS113[j] ) )*coefS1MDS1[4] + ( ( round(listeMatrices2GesR[j][6]*0.7 + MDS114cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][6]> 0) else MDS114[j] ) )*coefS1MDS1[5] + ( ( round( listeMatrices2GesR[j][7]*0.7 + MDS115cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][7]> 0) else MDS115[j] ) )*coefS1MDS1[6] + ( ( round(listeMatrices2GesR[j][8]*0.7 + MDS116cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][8]> 0) else MDS116[j] ) )*coefS1MDS1[7] + ( ( round(listeMatrices2GesR[j][9]*0.7 + MDS117cc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][9]> 0) else MDS117[j] ))*coefS1MDS1[8] + ( ( round(listeMatrices2GesR[j][10]*0.7 + MDS117bcc[j]['note_cc']*0.3, 2) if (listeMatrices2GesR[j][10]> 0) else MDS117b[j] ) )*coefS1MDS1[9] ) / ( coefS1MDS1[0]+coefS1MDS1[1]+coefS1MDS1[2]+coefS1MDS1[3]+coefS1MDS1[4]+coefS1MDS1[5]+coefS1MDS1[6]+coefS1MDS1[7]+coefS1MDS1[8]+coefS1MDS1[9] ),2)
                ]

        ]
        #Decompte des crédits totaux PV semestre 1 Gestion
        MDSCreditCountPV(matrice)

        listeMatriceS.append(matrice)

########################################################### STATS VALIDATION ####################################################################################################################################
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


    semestre1MDS = [filiere, listeMatrice, mds1Moyenne, moy, session, creditS1MDS1, UEStats, UEstats_mention, UeNomCode, listeMatrices2GesR, listeMatriceS] #filiere, listeMatrice, staps1Moyenne, moy, session

    return render(request, 'bulletin/releveCommun/releveCommuns2mds.html', {'semestre1MDS': semestre1MDS})






#PV EPS2 SEMESTRE3
def resultatCommunstaps2(request):
########################################################################################### PV SEMESTRE 3 ##################################################################

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

                    [
                        EPS111[j]
                        , coefS1STAPS1[0]
                        , EPS111[j]*coefS1STAPS1[0]
                        , round( ((EPS111[j]*coefS1STAPS1[0]) + (EPS112[j]*coefS1STAPS1[1])) / (coefS1STAPS1[0]+coefS1STAPS1[1]), 2 )
                        , sort111.index(EPS111[j])+1
                        , (EPS111[j]>=10)
                        , creditS1STAPS1[0]
                        , creditS1STAPS1[0] if (EPS111[j]>=10) else 0
                        , EPS111cc[j]['note_cc']
                        , EPS111sn[j]['note_sn']
                    ],

                    [ EPS112[j], coefS1STAPS1[1], EPS112[j]*coefS1STAPS1[1], "MOYENNE", sort112.index(EPS112[j])+1,(EPS112[j]>=10), creditS1STAPS1[1], creditS1STAPS1[1] if (EPS112[j]>=10) else 0 , EPS112cc[j]['note_cc'], EPS112sn[j]['note_sn'] ],

                    [
                        EPS113[j]
                        , coefS1STAPS1[2]
                        , EPS113[j]*coefS1STAPS1[2]
                        , round(  ( (EPS113[j]*coefS1STAPS1[2]) + (EPS114[j]*coefS1STAPS1[3]) + (EPS115a[j]*coefS1STAPS1[4]) + (EPS115b[j]*coefS1STAPS1[5]) + (EPS115f[j]*coefS1STAPS1[6]) + (EPS115g[j]*coefS1STAPS1[7]) + (EPS115j[j]*coefS1STAPS1[8]) + (EPS115l[j]*coefS1STAPS1[9]) + (EPS116[j]*coefS1STAPS1[10]) ) / (coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]), 2 )
                        , sort113.index(EPS113[j])+1
                        , (EPS113[j] >=10)
                        , creditS1STAPS1[2]
                        , creditS1STAPS1[2] if (EPS113[j] >=10) else 0
                        , EPS113cc[j]['note_cc']
                        , EPS113sn[j]['note_sn']
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

                        #4,

                        #5
                    ]
            ]

            listeMatrice.append(matrice)
            

            staps1Moyenne.append(matrice[15][2])
            staps1Moyenne.sort(reverse=True)

            moy = stat.mean(staps1Moyenne)
            moy = round(moy, 2)
            session = 'Janvier 2023'

    EPS2CreditCountS3PV(listeMatrice)

########################################################################################### MATRICE RATTRAPAGE ##################################################################
    EPS111R = list(Evaluation.objects.filter(uniteEnseignement_id=62, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=62).values('note_cc'))
    #EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=62).values('note_sn'))
    sort111R = epurationRattrapage(EPS111R)

    EPS112R = list(Evaluation.objects.filter(uniteEnseignement_id=63, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=63).values('note_cc'))
    #EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=63).values('note_sn'))
    sort112R = epurationRattrapage(EPS112R)

    EPS113R = list(Evaluation.objects.filter(uniteEnseignement_id=64, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=64).values('note_cc'))
    #EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=64).values('note_sn'))
    sort113R = epurationRattrapage(EPS113R)

    EPS114R = list(Evaluation.objects.filter(uniteEnseignement_id=65, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=65).values('note_cc'))
    #EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=65).values('note_sn'))
    sort114 = epurationRattrapage(EPS114R)

    EPS115aR = list(Evaluation.objects.filter(uniteEnseignement_id=66, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=66).values('note_cc'))
    #EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=66).values('note_sn'))
    sort115aR = epurationRattrapage(EPS115aR)

    EPS115bR = list(Evaluation.objects.filter(uniteEnseignement_id=67, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS115bcc = list(Evaluation.objects.filter(uniteEnseignement_id=67).values('note_cc'))
    #EPS115bsn = list(Evaluation.objects.filter(uniteEnseignement_id=67).values('note_sn'))
    sort115bR = epurationRattrapage(EPS115bR) 

    EPS115fR = list(Evaluation.objects.filter(uniteEnseignement_id=68, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS115fcc = list(Evaluation.objects.filter(uniteEnseignement_id=68).values('note_cc'))
    #EPS115fsn = list(Evaluation.objects.filter(uniteEnseignement_id=68).values('note_sn'))
    sort115fR = epurationRattrapage(EPS115fR)

    EPS115gR = list(Evaluation.objects.filter(uniteEnseignement_id=69, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS115gcc = list(Evaluation.objects.filter(uniteEnseignement_id=69).values('note_cc'))
    #EPS115gsn = list(Evaluation.objects.filter(uniteEnseignement_id=69).values('note_sn'))
    sort115gR = epurationRattrapage(EPS115gR)

    EPS115jR = list(Evaluation.objects.filter(uniteEnseignement_id=70, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=70).values('note_cc'))
    #EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=70).values('note_sn'))
    sort115jR = epurationRattrapage(EPS115jR)

    EPS115lR = list(Evaluation.objects.filter(uniteEnseignement_id=71, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=71).values('note_cc'))
    #EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=71).values('note_sn'))
    sort115lR = epurationRattrapage(EPS115lR)

    EPS116R = list(Evaluation.objects.filter(uniteEnseignement_id=72, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=72).values('note_cc'))
    #EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=72).values('note_sn'))
    sort116R = epurationRattrapage(EPS116R)

    EPS117R = list(Evaluation.objects.filter(uniteEnseignement_id=73, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=73).values('note_cc'))
    #EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=73).values('note_sn'))
    sort117R = epurationRattrapage(EPS117R)

    EPS118R = list(Evaluation.objects.filter(uniteEnseignement_id=74, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=74).values('note_cc'))
    #EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=74).values('note_sn'))
    sort118R = epurationRattrapage(EPS118R)

    EPS119R = list(Evaluation.objects.filter(uniteEnseignement_id=75, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    #EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=75).values('note_cc'))
    #EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=75).values('note_sn'))
    sort119R = epurationRattrapage(EPS119R)

    #listMatrices4EpsR = []
    listMatriceRs4eps = []

    for j in range( len(infoEtudiantSTAPS1) ):

        matriceRs4eps = [
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

        #matrice de Rattrapage
        #listMatrices4EpsR.append(matriceReps2S2)
        listMatriceRs4eps.append(matriceRs4eps)

########################################################################################### MATRICE CC ##################################################################
    listeMatriceEPS2s3CC = []

    for j in range( len(infoEtudiantSTAPS1) ):

        matriceS3Eps2CC = [
            infoEtudiantSTAPS1[j],

            EPS111cc[j]["note_cc"],

            EPS112cc[j]["note_cc"],

            EPS113cc[j]["note_cc"],

            EPS114cc[j]["note_cc"],

            EPS115acc[j]["note_cc"],

            EPS115bcc[j]["note_cc"],

            EPS115fcc[j]["note_cc"],

            EPS115gcc[j]["note_cc"],

            EPS115jcc[j]["note_cc"],

            EPS115lcc[j]["note_cc"],

            EPS116cc[j]["note_cc"],

            EPS117cc[j]["note_cc"],

            EPS118cc[j]["note_cc"],

            EPS119cc[j]["note_cc"],
        ]
        listeMatriceEPS2s3CC.append(matriceS3Eps2CC)

########################################################################################### MATRICE SYNTHESE ####################################################################
    #MAtrice Synthèse EPS2 Semestre 3

    listeMatriceSyntheseEPS2s3 = matriceSyntheseEPS2S3(listeMatrice, listMatriceRs4eps, listeMatriceEPS2s3CC)

    #Decompte de Crédits
    EPS2CreditCountS3PV(listeMatriceSyntheseEPS2s3[0])

########################################################################################### STATS VALIDATIONS ##################################################################
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

    semestre1MDS = [filiere , listeMatrice, staps1Moyenne, moy, session, creditS1STAPS1, UEStats, UEstats_mention, listMatriceRs4eps, listeMatriceSyntheseEPS2s3 ]


    return render(request, 'bulletin/releveCommun/releveCommunstaps2.html',{'semestre1MDS': semestre1MDS})



#PV EPS2 SEMESTRE4
def resultatCommuns4staps2(request):
########################################################################################### PV EPS2 SEMESTRE 4 ##################################################################

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
                    [
                        EPS111[j]
                        , coefS1STAPS1[0]
                        , EPS111[j]*coefS1STAPS1[0]
                        , "MOYENNE"
                        , sort111.index(EPS111[j])+1
                        , (EPS111[j]>=10)
                        , creditS1STAPS1[0]
                        , creditS1STAPS1[0] if (EPS111[j]>=10) else 0
                        , EPS111cc[j]['note_cc']
                        , EPS111sn[j]['note_sn']
                    ],

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
                        
                    ]
            ]
            
            listeMatrice.append(matrice)

            staps1Moyenne.append(matrice[13][2])
            staps1Moyenne.sort(reverse=True)

            moy = stat.mean(staps1Moyenne)
            moy = round(moy, 2)
            session = 'Mai 2023'

########################################################################################### MATRICE RATTRAPAGE ##################################################################
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

    listMatrices4EpsR = []
    listMatriceRs4eps = []

    for j in range( len(infoEtudiantSTAPS1) ):

        matriceReps2S2 = [
            infoEtudiantSTAPS1[j],

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

        matriceRs4eps = [

            infoEtudiantSTAPS1[j],

            round(EPS1112R[j]*0.7 + 0.3*EPS111cc[j]['note_cc'],2) if EPS1112R[j] > 0 else 0,

            round(EPS115a2R[j]*0.7 + 0.3*EPS115acc[j]['note_cc'],2) if EPS115a2R[j] >0 else 0 ,

            round(EPS115f2R[j]*0.7 + 0.3*EPS115fcc[j]['note_cc'],2) if EPS115f2R[j]>0 else 0,

            round(EPS115j2R[j]*0.7 + 0.3*EPS115jcc[j]['note_cc'],2) if EPS115j2R[j]>0 else 0,

            round(EPS115g2R[j]*0.7 + 0.3*EPS115gcc[j]['note_cc'],2) if EPS115g2R[j]>0 else 0,

            round(EPS1122R[j]*0.7 + 0.3*EPS112cc[j]['note_cc'],2) if EPS1122R[j]>0 else 0,

            round(EPS1133R[j]*0.7 + 0.3*EPS113cc[j]['note_cc'],2) if EPS1133R[j]>0 else 0,

            round(EPS1144R[j]*0.7 + 0.3*EPS114cc[j]['note_cc'],2) if EPS1144R[j]>0 else 0,

            round(EPS1166R[j]*0.7 + 0.3*EPS116cc[j]['note_cc'],2) if EPS1166R[j]>0 else 0,

            round(EPS1177R[j]*0.7 + 0.3*EPS117cc[j]['note_cc'],2) if EPS1177R[j]>0 else 0,

            round(EPS1188R[j]*0.7 + 0.3*EPS118cc[j]['note_cc'],2) if EPS1188R[j]>0 else 0,

            round(EPS1199R[j]*0.7 + 0.3*EPS119cc[j]['note_cc'],2) if EPS1199R[j]>0 else 0 
        ]

        #matrice de Rattrapage
        listMatrices4EpsR.append(matriceReps2S2)
        listMatriceRs4eps.append(matriceRs4eps)

########################################################################################### MATRICE SYNTHESE   ##################################################################
    listeMatriceSeps2S2 = []
    EVEMoyenne2 = []

    for j in range( len(infoEtudiantSTAPS1) ):


        matriceSeps2s2 = [
                    infoEtudiantSTAPS1[j],

                    #STAGE-PROFESSIONNEL
                    [ 
                        ( round(listMatrices4EpsR[j][1]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][1]> 0) else EPS111[j] )
                        
                        , coefS1STAPS1[0]
                        
                        , ( round(listMatrices4EpsR[j][1]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][1]> 0) else EPS111[j] )*coefS1STAPS1[0]
                        
                        , "MOYENNE"
                        
                        , sort111.index(( round(listMatrices4EpsR[j][1]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][1]> 0) else EPS111[j] ))+1
                        
                        , (( round(listMatrices4EpsR[j][1]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][1]> 0) else EPS111[j] )>=10)
                        
                        , creditS1STAPS1[0]
                        
                        , creditS1STAPS1[0] if (( round(listMatrices4EpsR[j][1]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][1]> 0) else EPS111[j] )>=10) else 0
                        
                        , EPS111cc[j]['note_cc']
                        
                        , EPS111sn[j]['note_sn'] 
                    ],

                    #DIDACTIQUE DES APS
                    [ 
                        ( round(listMatrices4EpsR[j][2]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][2]> 0) else EPS115a[j] )
                        
                        , coefS1STAPS1[1]
                        
                        , ( round(listMatrices4EpsR[j][2]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][2]> 0) else EPS115a[j] )*coefS1STAPS1[1]
                        
                        , "MOYENNE"
                        
                        , sort115a.index(( round(listMatrices4EpsR[j][2]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][2]> 0) else EPS115a[j] ))+1
                        
                        , (( round(listMatrices4EpsR[j][2]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][2]> 0) else EPS115a[j] ) >=10)
                        
                        , creditS1STAPS1[1]
                        
                        , creditS1STAPS1[1] if (( round(listMatrices4EpsR[j][2]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][2]> 0) else EPS115a[j] ) >=10) else 0
                        
                        , EPS115acc[j]['note_cc'], EPS115asn[j]['note_sn'] 
                    ], 

                    #3
                    [ 
                        ( round(listMatrices4EpsR[j][3]*0.7 + EPS115fcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][3]> 0) else EPS115f[j] )
                    
                        , coefS1STAPS1[2]
                        
                        , ( round(listMatrices4EpsR[j][3]*0.7 + EPS115fcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][3]> 0) else EPS115f[j] )*coefS1STAPS1[2]
                        
                        , "MOYENNE"
                        
                        , 'RANG'#sort115f.index(( round(listMatrices4EpsR[j][3]*0.7 + EPS115fcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][3]> 0) else EPS115f[j] ))+1
                        
                        , (( round(listMatrices4EpsR[j][3]*0.7 + EPS115fcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][3]> 0) else EPS115f[j] ) >=10)
                        
                        , creditS1STAPS1[2]
                        
                        , creditS1STAPS1[2] if (( round(listMatrices4EpsR[j][3]*0.7 + EPS115fcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][3]> 0) else EPS115f[j] ) >=10) else 0
                        
                        , EPS115fcc[j]['note_cc']
                        
                        , EPS115fsn[j]['note_sn'] 

                    ],

                    [ 
                        ( round(listMatrices4EpsR[j][4]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][4]> 0) else EPS115j[j] )
                        
                        , coefS1STAPS1[3]
                        
                        , ( round(listMatrices4EpsR[j][4]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][4]> 0) else EPS115j[j] )*coefS1STAPS1[3]
                        
                        , "MOYENNE"
                        
                        , "RANG" #sort115j.index(( round(listMatrices4EpsR[j][4]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][4]> 0) else EPS115j[j] ))+1
                        
                        , (( round(listMatrices4EpsR[j][4]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][4]> 0) else EPS115j[j] ) >=10)
                        
                        , creditS1STAPS1[3]
                        
                        , creditS1STAPS1[3] if (( round(listMatrices4EpsR[j][4]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][4]> 0) else EPS115j[j] ) >=10) else 0
                        
                        , EPS115jcc[j]['note_cc']
                        
                        , EPS115jsn[j]['note_sn'] 
                    ],

                    [ 
                        ( round(listMatrices4EpsR[j][5]*0.7 + EPS115gcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][5]> 0) else EPS115g[j] ) 
                        
                        , coefS1STAPS1[4]
                        
                        , ( round(listMatrices4EpsR[j][5]*0.7 + EPS115gcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][5]> 0) else EPS115g[j] )*coefS1STAPS1[4]

                        , round( (( round(listMatrices4EpsR[j][2]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][2]> 0) else EPS115a[j] )*coefS1STAPS1[1]+( round(listMatrices4EpsR[j][3]*0.7 + EPS115fcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][3]> 0) else EPS115f[j] )*coefS1STAPS1[2]+( round(listMatrices4EpsR[j][4]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][4]> 0) else EPS115j[j] )*coefS1STAPS1[3]+( round(listMatrices4EpsR[j][5]*0.7 + EPS115gcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][5]> 0) else EPS115g[j] )*coefS1STAPS1[4])/(coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]), 2 )
                    
                        , "RANG" #sort115g.index(( round(listMatrices4EpsR[j][5]*0.7 + EPS115gcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][5]> 0) else EPS115g[j] ))+1
                    
                        , (( round(listMatrices4EpsR[j][5]*0.7 + EPS115gcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][5]> 0) else EPS115g[j] ) >=10)
                        
                        , creditS1STAPS1[4]
                        
                        , creditS1STAPS1[4] if ( (( round(listMatrices4EpsR[j][2]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][2]> 0) else EPS115a[j] )+( round(listMatrices4EpsR[j][3]*0.7 + EPS115fcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][3]> 0) else EPS115f[j] )+EPS115j[j]+( round(listMatrices4EpsR[j][5]*0.7 + EPS115gcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][5]> 0) else EPS115g[j] )) >=40) else 0
                        
                        , EPS115gcc[j]['note_cc']
                        
                        , EPS115gsn[j]['note_sn'] 

                    ],

                    #ANATOMIE
                    [ 
                        ( round(listMatrices4EpsR[j][6]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][6]> 0) else EPS112[j] ) 
                        
                        , coefS1STAPS1[5]
                        
                        , ( round(listMatrices4EpsR[j][6]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][6]> 0) else EPS112[j] )*coefS1STAPS1[5]
                        
                        , "MOYENNE"
                        
                        , "RANG" #sort112.index(( round(listMatrices4EpsR[j][6]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][6]> 0) else EPS112[j] ))+1
                        
                        , (( round(listMatrices4EpsR[j][6]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][6]> 0) else EPS112[j] )>=10)
                        
                        , creditS1STAPS1[5]
                        
                        , creditS1STAPS1[5] if (( round(listMatrices4EpsR[j][6]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][6]> 0) else EPS112[j] )>=10) else 0 
                        
                        , EPS112cc[j]['note_cc']
                        
                        , EPS112sn[j]['note_sn'] 
                    ],

                    #PHYSIOLOGIE
                    [ 
                        ( round(listMatrices4EpsR[j][7]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][7]> 0) else EPS113[j] )
                        
                        , coefS1STAPS1[6]
                        
                        , ( round(listMatrices4EpsR[j][7]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][7]> 0) else EPS113[j] )*coefS1STAPS1[6]
                        
                        , "MOYENNE"
                        
                        , "RANG"#sort113.index(( round(listMatrices4EpsR[j][7]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][7]> 0) else EPS113[j] ))+1
                        
                        , (( round(listMatrices4EpsR[j][7]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][7]> 0) else EPS113[j] ) >=10)
                        
                        , creditS1STAPS1[6]
                        
                        , creditS1STAPS1[6] if (( round(listMatrices4EpsR[j][7]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][7]> 0) else EPS113[j] ) >=10) else 0
                        
                        , EPS113cc[j]['note_cc']
                        
                        , EPS113sn[j]['note_sn'] 
                    ],

                    #EDUCATION PHYSIQUE : LOISIRS II
                    [ 
                        ( round(listMatrices4EpsR[j][8]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][8]> 0) else EPS114[j] )
                        
                        , coefS1STAPS1[7]
                        
                        , ( round(listMatrices4EpsR[j][8]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][8]> 0) else EPS114[j] )*coefS1STAPS1[7]
                        
                        , "MOYENNE"
                        
                        , "RANG"#sort114.index(( round(listMatrices4EpsR[j][8]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][8]> 0) else EPS114[j] ))+1
                        
                        , (( round(listMatrices4EpsR[j][8]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][8]> 0) else EPS114[j] ) >=10)
                        
                        , creditS1STAPS1[7]
                        
                        , creditS1STAPS1[7] if (( round(listMatrices4EpsR[j][8]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][8]> 0) else EPS114[j] ) >=10) else 0
                        
                        , EPS114cc[j]['note_cc'], EPS114sn[j]['note_sn'] 
                    ],

                    #TRAUMATOLOGIE - PREMIERS SECOURS
                    [ 
                        ( round(listMatrices4EpsR[j][9]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][9]> 0) else EPS116[j] )
                        
                        , coefS1STAPS1[8]
                        
                        , ( round(listMatrices4EpsR[j][9]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][9]> 0) else EPS116[j] )*coefS1STAPS1[8]
                        
                        , "MOYENNE"
                        
                        , "RANG" #sort116.index(( round(listMatrices4EpsR[j][9]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][9]> 0) else EPS116[j] ))+1
                        
                        , (( round(listMatrices4EpsR[j][9]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][9]> 0) else EPS116[j] ) >=10)
                        
                        , creditS1STAPS1[8]
                        
                        , creditS1STAPS1[8] if (( round(listMatrices4EpsR[j][9]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][9]> 0) else EPS116[j] ) >=10) else 0
                        
                        , EPS116cc[j]['note_cc']
                        
                        , EPS116sn[j]['note_sn'] 
                    ],

                    #PEDAGOGIE PRATIQUE III
                    [ 
                        ( round(listMatrices4EpsR[j][10]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][10]> 0) else EPS117[j] )
                    
                        , coefS1STAPS1[9]
                        
                        , ( round(listMatrices4EpsR[j][10]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][10]> 0) else EPS117[j] )*coefS1STAPS1[9] 

                        , round( (( round(listMatrices4EpsR[j][1]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][1]> 0) else EPS111[j] )*coefS1STAPS1[0]+( round(listMatrices4EpsR[j][2]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][2]> 0) else EPS115a[j] )*coefS1STAPS1[1]+( round(listMatrices4EpsR[j][3]*0.7 + EPS115fcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][3]> 0) else EPS115f[j] )*coefS1STAPS1[2]+( round(listMatrices4EpsR[j][4]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][4]> 0) else EPS115j[j] )*coefS1STAPS1[3]+EPS115g[j]*coefS1STAPS1[4]+( round(listMatrices4EpsR[j][6]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][6]> 0) else EPS112[j] )*coefS1STAPS1[5]+( round(listMatrices4EpsR[j][7]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][7]> 0) else EPS113[j] )*coefS1STAPS1[6]+( round(listMatrices4EpsR[j][8]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][8]> 0) else EPS114[j] )*coefS1STAPS1[7]+( round(listMatrices4EpsR[j][9]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][9]> 0) else EPS116[j] )*coefS1STAPS1[8]+( round(listMatrices4EpsR[j][10]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][10]> 0) else EPS117[j] )*coefS1STAPS1[9]) / (coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]), 2)
                            
                        , "RANG"#sort117.index(( round(listMatrices4EpsR[j][10]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][10]> 0) else EPS117[j] ))+1

                        , (( round(listMatrices4EpsR[j][10]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][10]> 0) else EPS117[j] ) >=10)

                        , creditS1STAPS1[9]

                        , creditS1STAPS1[9] if (( round(listMatrices4EpsR[j][10]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][10]> 0) else EPS117[j] ) >=10) else 0

                        , EPS117cc[j]['note_cc']

                        , EPS117sn[j]['note_sn'] 

                    ],

                    #ECONOMIE  
                    [ 
                        ( round(listMatrices4EpsR[j][11]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][11]> 0) else EPS118[j] )
                    
                        , coefS1STAPS1[10]
                    
                        , ( round(listMatrices4EpsR[j][11]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][11]> 0) else EPS118[j] )*coefS1STAPS1[10]

                        , "MOYENNE"

                        , "RANG"#sort118.index(( round(listMatrices4EpsR[j][11]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][11]> 0) else EPS118[j] ))+1 

                        , (( round(listMatrices4EpsR[j][11]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][11]> 0) else EPS118[j] ) >=10)

                        , creditS1STAPS1[10]

                        , creditS1STAPS1[10] if (( round(listMatrices4EpsR[j][11]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][11]> 0) else EPS118[j] ) >=10) else 0 

                        , EPS118cc[j]['note_cc'] 

                        , EPS118sn[j]['note_sn'] 
                    ],

                    #FRANCAIS
                    [ 
                        ( round(listMatrices4EpsR[j][12]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][12]> 0) else EPS119[j] )
                        
                        , coefS1STAPS1[11]
                        
                        , ( round(listMatrices4EpsR[j][12]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][12]> 0) else EPS119[j] )*coefS1STAPS1[11]

                        , round( (( round(listMatrices4EpsR[j][11]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][11]> 0) else EPS118[j] )*coefS1STAPS1[10]+( round(listMatrices4EpsR[j][12]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][12]> 0) else EPS119[j] )*coefS1STAPS1[11]) / (coefS1STAPS1[10]+coefS1STAPS1[11]) ,2)
                        
                        , #"MOYENNE",

                        "RANG" #sort119.index(( round(listMatrices4EpsR[j][12]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][12]> 0) else EPS119[j] ))+1

                        , (( round(listMatrices4EpsR[j][12]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][12]> 0) else EPS119[j] ) >=10)

                        , creditS1STAPS1[11], creditS1STAPS1[11] if (( round(listMatrices4EpsR[j][12]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][12]> 0) else EPS119[j] ) >=10) else 0 

                        , EPS119cc[j]['note_cc']

                        , EPS119sn[j]['note_sn'] 
                    ],

                    
                    #SOMME
                    [ 
                        ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 
                    
                    round( ( round(listMatrices4EpsR[j][1]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][1]> 0) else EPS111[j] )*coefS1STAPS1[0]+( round(listMatrices4EpsR[j][2]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][2]> 0) else EPS115a[j] )*coefS1STAPS1[1]+( round(listMatrices4EpsR[j][3]*0.7 + EPS115fcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][3]> 0) else EPS115f[j] )*coefS1STAPS1[2]+( round(listMatrices4EpsR[j][4]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][4]> 0) else EPS115j[j] )*coefS1STAPS1[3]+( round(listMatrices4EpsR[j][5]*0.7 + EPS115gcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][5]> 0) else EPS115g[j] )*coefS1STAPS1[4]+( round(listMatrices4EpsR[j][6]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][6]> 0) else EPS112[j] )*coefS1STAPS1[5]+( round(listMatrices4EpsR[j][7]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][7]> 0) else EPS113[j] )*coefS1STAPS1[6]+( round(listMatrices4EpsR[j][8]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][8]> 0) else EPS114[j] )*coefS1STAPS1[7]+( round(listMatrices4EpsR[j][9]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][9]> 0) else EPS116[j] )*coefS1STAPS1[8]+( round(listMatrices4EpsR[j][10]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][10]> 0) else EPS117[j] )*coefS1STAPS1[9]+( round(listMatrices4EpsR[j][11]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][11]> 0) else EPS118[j] )*coefS1STAPS1[10]+( round(listMatrices4EpsR[j][12]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][12]> 0) else EPS119[j] )*coefS1STAPS1[11] ,2), 

                    round(( ( round(listMatrices4EpsR[j][1]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][1]> 0) else EPS111[j] )*coefS1STAPS1[0]+( round(listMatrices4EpsR[j][2]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][2]> 0) else EPS115a[j] )*coefS1STAPS1[1]+( round(listMatrices4EpsR[j][3]*0.7 + EPS115fcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][3]> 0) else EPS115f[j] )*coefS1STAPS1[2]+( round(listMatrices4EpsR[j][4]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][4]> 0) else EPS115j[j] )*coefS1STAPS1[3]+( round(listMatrices4EpsR[j][5]*0.7 + EPS115gcc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][5]> 0) else EPS115g[j] )*coefS1STAPS1[4]+( round(listMatrices4EpsR[j][6]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][6]> 0) else EPS112[j] )*coefS1STAPS1[5]+( round(listMatrices4EpsR[j][7]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][7]> 0) else EPS113[j] )*coefS1STAPS1[6]+( round(listMatrices4EpsR[j][8]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][8]> 0) else EPS114[j] )*coefS1STAPS1[7]+( round(listMatrices4EpsR[j][9]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][9]> 0) else EPS116[j] )*coefS1STAPS1[8]+( round(listMatrices4EpsR[j][10]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][10]> 0) else EPS117[j] )*coefS1STAPS1[9]+( round(listMatrices4EpsR[j][11]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][11]> 0) else EPS118[j] )*coefS1STAPS1[10]+( round(listMatrices4EpsR[j][12]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (listMatrices4EpsR[j][12]> 0) else EPS119[j] )*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2), #moyenne
                        
                    ]
            ]

        listeMatriceSeps2S2.append(matriceSeps2s2)

        EVEMoyenne2.append(matriceSeps2s2[13][2])
        EVEMoyenne2.sort(reverse=True)

        moy2 = stat.mean(EVEMoyenne2)
        moy2 = round(moy2, 2)


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

    semestre1MDS = [filiere , listeMatrice, staps1Moyenne, moy, session, creditS1STAPS1, UEStats, UEstats_mention, code_UE, intitule_UE, listMatriceRs4eps, listeMatriceSeps2S2, EVEMoyenne2]


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
##################################################### S5 STATS VAL #########################################################################################################################################################################
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

##################################################### PV SEMESTRE 5 #####################################################################################################################################
    MAS315 = list(Evaluation.objects.filter(uniteEnseignement_id=76, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS315cc = list(Evaluation.objects.filter(uniteEnseignement_id=76, natureEvaluation='EXAMEN').values('note_cc'))
    MAS315sn = list(Evaluation.objects.filter(uniteEnseignement_id=76, natureEvaluation='EXAMEN').values('note_sn'))
    sort315 = epurationTriCroissant(MAS315)

    MAS325 = list(Evaluation.objects.filter(uniteEnseignement_id=77, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS325cc = list(Evaluation.objects.filter(uniteEnseignement_id=77, natureEvaluation='EXAMEN').values('note_cc'))
    MAS325sn = list(Evaluation.objects.filter(uniteEnseignement_id=77, natureEvaluation='EXAMEN').values('note_sn'))
    sort325 = epurationTriCroissant(MAS325)

    MAS335 = list(Evaluation.objects.filter(uniteEnseignement_id=78, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS335cc = list(Evaluation.objects.filter(uniteEnseignement_id=78, natureEvaluation='EXAMEN').values('note_cc'))
    MAS335sn = list(Evaluation.objects.filter(uniteEnseignement_id=78, natureEvaluation='EXAMEN').values('note_sn'))
    sort335 = epurationTriCroissant(MAS335)

    MAS345 = list(Evaluation.objects.filter(uniteEnseignement_id=79, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS345cc = list(Evaluation.objects.filter(uniteEnseignement_id=79, natureEvaluation='EXAMEN').values('note_cc'))
    MAS345sn = list(Evaluation.objects.filter(uniteEnseignement_id=79, natureEvaluation='EXAMEN').values('note_sn'))
    sort345 = epurationTriCroissant(MAS345)

    EVE355 = list(Evaluation.objects.filter(uniteEnseignement_id=80, natureEvaluation='EXAMEN').values('note_Examen'))
    EVE355cc = list(Evaluation.objects.filter(uniteEnseignement_id=80, natureEvaluation='EXAMEN').values('note_cc'))
    EVE355sn = list(Evaluation.objects.filter(uniteEnseignement_id=80, natureEvaluation='EXAMEN').values('note_sn'))
    sort355 = epurationTriCroissant(EVE355)

    EVE365 = list(Evaluation.objects.filter(uniteEnseignement_id=81, natureEvaluation='EXAMEN').values('note_Examen'))
    EVE365cc = list(Evaluation.objects.filter(uniteEnseignement_id=81, natureEvaluation='EXAMEN').values('note_cc'))
    EVE365sn = list(Evaluation.objects.filter(uniteEnseignement_id=81, natureEvaluation='EXAMEN').values('note_sn'))
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

                creditS5EVE[0],

                MAS315cc[j]['note_cc'],
                MAS315sn[j]['note_sn'],

            ],
            
            [ MAS325[j], coefS5EVE[1], round(MAS325[j]*coefS5EVE[1], 2), 'MOYENNE', sort325.index(MAS325[j])+1, (MAS325[j]>=10) ,creditS5EVE[1], MAS325cc[j]['note_cc'],
                MAS325sn[j]['note_sn'], ],
            
            [ MAS335[j], coefS5EVE[2], round(MAS335[j]*coefS5EVE[2], 2), 'MOYENNE', sort335.index(MAS335[j])+1, (MAS335[j]>=10), creditS5EVE[2], MAS335cc[j]['note_cc'],
                MAS335sn[j]['note_sn'] ],
            
            [ MAS345[j], coefS5EVE[3], round(MAS345[j]*coefS5EVE[3], 2), 'MOYENNE', sort345.index(MAS345[j])+1, (MAS345[j]>=10), creditS5EVE[3], MAS345cc[j]['note_cc'],
                MAS345sn[j]['note_sn'] ],
            
            [ EVE355[j], coefS5EVE[4], round(EVE355[j]*coefS5EVE[4], 2), 

                round((EVE355[j]*coefS5EVE[4] + EVE365[j]*coefS5EVE[5] )/(coefS5EVE[4]+coefS5EVE[5]), 2), #

                sort355.index(EVE355[j])+1, 

                (EVE355[j]>=10),

                creditS5EVE[4],

                EVE355cc[j]['note_cc'],

                EVE355sn[j]['note_sn'],
            ],
            
            [ EVE365[j], coefS5EVE[5], round(EVE365[j]*coefS5EVE[5], 2), 'MOYENNE', sort365.index(EVE365[j])+1, (EVE365[j]>=10), creditS5EVE[5], EVE365cc[j]['note_cc'],

                EVE365sn[j]['note_sn'], ],
        
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
        session = 'Janvier 2023'

##################################################### PV SEMESTRE 5 RATTRAPAGE ####################################################################################################################################
    MAS315R = list(Evaluation.objects.filter(uniteEnseignement_id=76, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))  
    sort316 = epurationRattrapage(MAS315R)

    MAS325R = list(Evaluation.objects.filter(uniteEnseignement_id=77, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort326 = epurationRattrapage(MAS325R)

    MAS335R = list(Evaluation.objects.filter(uniteEnseignement_id=78, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort336 = epurationRattrapage(MAS335R)

    MAS345R = list(Evaluation.objects.filter(uniteEnseignement_id=79, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort346 = epurationRattrapage(MAS345R)

    EVE355R = list(Evaluation.objects.filter(uniteEnseignement_id=80, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort356 = epurationRattrapage(EVE355R)

    EVE365R = list(Evaluation.objects.filter(uniteEnseignement_id=81, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort366 = epurationRattrapage(EVE365R)

    listeMatriceRs5EVE = []
    listeMatriceRs5EVEex = []
    

    for j in range (len(infoEtudiantEVE)):
        matriceRs5EVE = [

            infoEtudiantEVE[j],
            
            MAS315R[j],

            MAS325R[j],
            
            MAS335R[j],
            
            MAS345R[j],
            
            EVE355R[j],
            
            EVE365R[j],
        ]

        matriceRs5EVEex = [

            infoEtudiantEVE[j],
            
            ( round( MAS315R[j]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (MAS315R[j] > 0) else MAS315R[j] ) ,

            ( round( MAS325R[j]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (MAS325R[j] > 0) else MAS325R[j] ) ,
            
            ( round( MAS335R[j]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (MAS335R[j] > 0) else MAS335R[j] ) ,
            
            ( round( MAS345R[j]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (MAS345R[j] > 0) else MAS345R[j] ) ,
            
            ( round( EVE355R[j]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (EVE355R[j] > 0) else EVE355R[j] ) ,
            
            ( round( EVE365R[j]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (EVE365R[j] > 0) else EVE365R[j] ) ,
        ]
        listeMatriceRs5EVE.append(matriceRs5EVE)
        listeMatriceRs5EVEex.append(matriceRs5EVEex)

##################################################### PV SEMESTRE 5 EVE SYNTHESE   ###################################################################################################
    listeMatriceS5 =  []
    EVEMoyennes5 = []

    for j in range( len(infoEtudiantEVE) ):

        matricesS5EVE = [
            
            infoEtudiantEVE[j],

            [ 
                ( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) 
                
                , coefS5EVE[0]
                
                , round(( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0], 2)

                , round( ((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0]) + ( ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] )*coefS5EVE[1]) + (( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] )*coefS5EVE[2])  + (( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3]) ) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]), 2)  # (MAS335[j]*coefS5EVE[2]) ,  (MAS345[j]*coefS5EVE[3])
                
                #, round( ((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0]) + ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) + ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) + ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] ) ) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]), 2)

                #, sort315.index(( MAS315[j] ) )+1 #round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else

                , (( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] )  >=10)

                , creditS5EVE[0]

                , creditS5EVE[0] if((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] )  >=10)) else 0

                , MAS315cc[j]['note_cc']
                
                , MAS315sn[j]['note_sn'],
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) 
                
                , coefS5EVE[1]
                
                , round(( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) *coefS5EVE[1], 2)
                
                , 'MOYENNE'
                
                #, sort325.index((  MAS325[j] ) )+1 #round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else
                
                , (( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) >=10)

                , creditS5EVE[1]
                
                , creditS5EVE[1] if (( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) >=10) else 0

                , MAS325cc[j]['note_cc']
                
                , MAS325sn[j]['note_sn'],  
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) 
                
                , coefS5EVE[2]
                
                , round(( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) *coefS5EVE[2], 2)
                
                , 'MOYENNE'
                
                #, sort335.index((  MAS335[j] ) )+1 #round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else
                
                , (( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) >=10)
                
                , creditS5EVE[2]
                
                , creditS5EVE[2] if (( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) >=10) else 0

                , MAS335cc[j]['note_cc']
                
                , MAS335sn[j]['note_sn'] 
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )
                
                , coefS5EVE[3]
                
                , round(( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3], 2)
                
                , 'MOYENNE'
                
                #, sort345.index((  MAS345[j] ))+1 #round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else
                 
                , (( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )>=10)
                
                , creditS5EVE[3]
                
                , creditS5EVE[3] if (( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )>=10) else 0

                , MAS345cc[j]['note_cc']
                
                , MAS345sn[j]['note_sn']
                
                #, [ ( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) , ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) , ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) , ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )], MAS345R[j] 
                
                ],
            
            #MODULE 2
            [ 
                ( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )
                
                , coefS5EVE[4]
                
                , round(( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4], 2)

                , round((( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4] + ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] ) *coefS5EVE[5] )/(coefS5EVE[4]+coefS5EVE[5]), 2)

                #, sort355.index((  EVE355[j] ))+1 #round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else

                , (( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )>=10)

                , creditS5EVE[4]

                , creditS5EVE[4] if((( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )>=10)) else 0

                , EVE355cc[j]['note_cc']
                
                , EVE355sn[j]['note_sn']

                #, EVE355R[j]['note_rattrapage']
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] ) 
                
                , coefS5EVE[5]
                
                , round(( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )*coefS5EVE[5], 2)
                
                , 'MOYENNE'
                
                #, sort365.index((  EVE365[j] ))+1 #round(listeMatriceRs5EVE[j][6]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else
                
                , (( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )>=10)
                
                , creditS5EVE[5]
                
                , creditS5EVE[5] if (( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )>=10) else 0

                , EVE365cc[j]['note_cc']
                
                , EVE365sn[j]['note_sn']
                
                #, [ ( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] ), ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] ) ], EVE365R[j] 
            ],

            [ 
                (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),
    
                round( (( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0] + ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) *coefS5EVE[1] + ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) *coefS5EVE[2] + ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3]+( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4] + ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )*coefS5EVE[5] ), 2),

                round((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0] + MAS325[j]*coefS5EVE[1] + ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) *coefS5EVE[2] + ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3] + ( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4] + ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )*coefS5EVE[5])/(coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]), 2)
            ],
        ]

        listeMatriceS5.append(matricesS5EVE)
        EVEMoyennes5.append(matricesS5EVE[7][2])
    
    EVEMoyennes5.sort(reverse=True)

    moys5 = stat.mean(EVEMoyennes5)
    moys5 = round(moys5, 2)
    sessions5 = 'Janvier 2023'

    #semestre1MDS = [filiere, listeMatriceS5, EVEMoyennes5, moy, sessions5] #listeMatriceS5 , EVEMoyennes5,  sessions5

##################################################### STATS VALIDATION ############################################################################################################################
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

##################################################### STAT MENTION ###############################################################################################################################################
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



    semestre1MDS = [filiere, listeMatrice, EVEMoyenne, moy, session, creditS5EVE, UEStats, UEstats_mention, listeMatriceRs5EVE, listeMatriceS5, EVEMoyennes5] #listeMatriceS5

    return render(request, 'bulletin/releveCommun/releveCommunEve.html', {'semestre1MDS': semestre1MDS})





#PV EVE SEMESTRE6
def resultatCommuns6Eve(request):

    filiere = 'EVE'

    UeNomCode = list( UniteEnseignement.objects.filter(semestre_id = 6, filiere="MAS").values("code_UE","intitule_UE", "semestre_id", "nombre_credit") )

    infoEtudiantEVE = list( Etudiant.objects.filter(filiere="MAS", niveau=3, Specialite="EVENEMENTIEL").values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance','id', 'sexe'))
    
    coefS5EVE = list( UniteEnseignement.objects.filter(semestre_id=6,filiere="MAS").values("coefficient", "intitule_UE"))
    coefS5EVE = epurationCoef(coefS5EVE)

    creditS5EVE = list(UniteEnseignement.objects.filter(semestre_id=6,filiere="MAS").values("nombre_credit"))
    creditS5EVE = epurationCre(creditS5EVE)

    moyCredit = list(Etudiant.objects.filter(niveau=3).values('moyS1','crS1','moyS2','crS2','moyS3','crS3','moyS4','crS4','moyS5','crS5','moyS6','crS6'))

##################################################### PV SEMESTRE 5 #####################################################################################################################################
    MAS315 = list(Evaluation.objects.filter(uniteEnseignement_id=76, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS315cc = list(Evaluation.objects.filter(uniteEnseignement_id=76, natureEvaluation='EXAMEN').values('note_cc'))
    MAS315sn = list(Evaluation.objects.filter(uniteEnseignement_id=76, natureEvaluation='EXAMEN').values('note_sn'))
    sort315 = epurationTriCroissant(MAS315)

    MAS325 = list(Evaluation.objects.filter(uniteEnseignement_id=77, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS325cc = list(Evaluation.objects.filter(uniteEnseignement_id=77, natureEvaluation='EXAMEN').values('note_cc'))
    MAS325sn = list(Evaluation.objects.filter(uniteEnseignement_id=77, natureEvaluation='EXAMEN').values('note_sn'))
    sort325 = epurationTriCroissant(MAS325)

    MAS335 = list(Evaluation.objects.filter(uniteEnseignement_id=78, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS335cc = list(Evaluation.objects.filter(uniteEnseignement_id=78, natureEvaluation='EXAMEN').values('note_cc'))
    MAS335sn = list(Evaluation.objects.filter(uniteEnseignement_id=78, natureEvaluation='EXAMEN').values('note_sn'))
    sort335 = epurationTriCroissant(MAS335)

    MAS345 = list(Evaluation.objects.filter(uniteEnseignement_id=79, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS345cc = list(Evaluation.objects.filter(uniteEnseignement_id=79, natureEvaluation='EXAMEN').values('note_cc'))
    MAS345sn = list(Evaluation.objects.filter(uniteEnseignement_id=79, natureEvaluation='EXAMEN').values('note_sn'))
    sort345 = epurationTriCroissant(MAS345)

    EVE355 = list(Evaluation.objects.filter(uniteEnseignement_id=80, natureEvaluation='EXAMEN').values('note_Examen'))
    EVE355cc = list(Evaluation.objects.filter(uniteEnseignement_id=80, natureEvaluation='EXAMEN').values('note_cc'))
    EVE355sn = list(Evaluation.objects.filter(uniteEnseignement_id=80, natureEvaluation='EXAMEN').values('note_sn'))
    sort355 = epurationTriCroissant(EVE355)

    EVE365 = list(Evaluation.objects.filter(uniteEnseignement_id=81, natureEvaluation='EXAMEN').values('note_Examen'))
    EVE365cc = list(Evaluation.objects.filter(uniteEnseignement_id=81, natureEvaluation='EXAMEN').values('note_cc'))
    EVE365sn = list(Evaluation.objects.filter(uniteEnseignement_id=81, natureEvaluation='EXAMEN').values('note_sn'))
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
        session = 'Janvier 2023'

##################################################### PV SEMESTRE 5 RATTRAPAGE ####################################################################################################################################
    MAS315R = list(Evaluation.objects.filter(uniteEnseignement_id=76, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))  
    sort316 = epurationRattrapage(MAS315R)

    MAS325R = list(Evaluation.objects.filter(uniteEnseignement_id=77, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort326 = epurationRattrapage(MAS325R)

    MAS335R = list(Evaluation.objects.filter(uniteEnseignement_id=78, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort336 = epurationRattrapage(MAS335R)

    MAS345R = list(Evaluation.objects.filter(uniteEnseignement_id=79, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort346 = epurationRattrapage(MAS345R)

    EVE355R = list(Evaluation.objects.filter(uniteEnseignement_id=80, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort356 = epurationRattrapage(EVE355R)

    EVE365R = list(Evaluation.objects.filter(uniteEnseignement_id=81, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort366 = epurationRattrapage(EVE365R)

    listeMatriceRs5EVE = []
    listeMatriceRs5EVEex = []
    

    for j in range (len(infoEtudiantEVE)):
        matriceRs5EVE = [

            infoEtudiantEVE[j],
            
            MAS315R[j],

            MAS325R[j],
            
            MAS335R[j],
            
            MAS345R[j],
            
            EVE355R[j],
            
            EVE365R[j],
        ]

        matriceRs5EVEex = [

            infoEtudiantEVE[j],
            
            ( round( MAS315R[j]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (MAS315R[j] > 0) else MAS315R[j] ) ,

            ( round( MAS325R[j]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (MAS325R[j] > 0) else MAS325R[j] ) ,
            
            ( round( MAS335R[j]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (MAS335R[j] > 0) else MAS335R[j] ) ,
            
            ( round( MAS345R[j]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (MAS345R[j] > 0) else MAS345R[j] ) ,
            
            ( round( EVE355R[j]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (EVE355R[j] > 0) else EVE355R[j] ) ,
            
            ( round( EVE365R[j]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (EVE365R[j] > 0) else EVE365R[j] ) ,
        ]
        listeMatriceRs5EVE.append(matriceRs5EVE)
        listeMatriceRs5EVEex.append(matriceRs5EVEex)

##################################################### PV SEMESTRE 5 EVE SYNTHESE   ###################################################################################################
    listeMatriceS5 =  []
    EVEMoyennes5 = []

    for j in range( len(infoEtudiantEVE) ):

        matricesS5EVE = [
            
            infoEtudiantEVE[j],

            [ 
                ( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) 
                
                , coefS5EVE[0]
                
                , round(( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0], 2)

                , round( ((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0]) + ( ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] )*coefS5EVE[1]) + (( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] )*coefS5EVE[2])  + (( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3]) ) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]), 2)

                #, round( ((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0]) + (MAS325[j]*coefS5EVE[1]) + (MAS335[j]*coefS5EVE[2]) + (MAS345[j]*coefS5EVE[3])) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]), 2)
                
                #, sort315.index(( MAS315[j] ) )+1 #round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else

                , (( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] )  >=10)

                , creditS5EVE[0]

                , creditS5EVE[0] if((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] )  >=10)) else 0

                , MAS315cc[j]['note_cc']
                
                , MAS315sn[j]['note_sn'],
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) 
                
                , coefS5EVE[1]
                
                , round(( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) *coefS5EVE[1], 2)
                
                , 'MOYENNE'
                
                #, sort325.index((  MAS325[j] ) )+1 #round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else
                
                , (( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) >=10)

                , creditS5EVE[1]
                
                , creditS5EVE[1] if (( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) >=10) else 0

                , MAS325cc[j]['note_cc']
                
                , MAS325sn[j]['note_sn'],  
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) 
                
                , coefS5EVE[2]
                
                , round(( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) *coefS5EVE[2], 2)
                
                , 'MOYENNE'
                
                #, sort335.index((  MAS335[j] ) )+1 #round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else
                
                , (( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) >=10)
                
                , creditS5EVE[2]
                
                , creditS5EVE[2] if (( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) >=10) else 0

                , MAS335cc[j]['note_cc']
                
                , MAS335sn[j]['note_sn'] 
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )
                
                , coefS5EVE[3]
                
                , round(( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3], 2)
                
                , 'MOYENNE'
                
                #, sort345.index((  MAS345[j] ))+1 #round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else
                 
                , (( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )>=10)
                
                , creditS5EVE[3]
                
                , creditS5EVE[3] if (( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )>=10) else 0

                , MAS345cc[j]['note_cc']
                
                , MAS345sn[j]['note_sn']
                
                #, [ ( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) , ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) , ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) , ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )], MAS345R[j] 
                
                ],
            
            #MODULE 2
            [ 
                ( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )
                
                , coefS5EVE[4]
                
                , round(( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4], 2)

                , round((( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4] + ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] ) *coefS5EVE[5] )/(coefS5EVE[4]+coefS5EVE[5]), 2)

                #, sort355.index((  EVE355[j] ))+1 #round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else

                , (( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )>=10)

                , creditS5EVE[4]

                , creditS5EVE[4] if((( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )>=10)) else 0

                , EVE355cc[j]['note_cc']
                
                , EVE355sn[j]['note_sn']

                #, EVE355R[j]['note_rattrapage']
            ],
            
            [ 
                ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] ) 
                
                , coefS5EVE[5]
                
                , round(( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )*coefS5EVE[5], 2)
                
                , 'MOYENNE'
                
                #, sort365.index((  EVE365[j] ))+1 #round(listeMatriceRs5EVE[j][6]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else
                
                , (( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )>=10)
                
                , creditS5EVE[5]
                
                , creditS5EVE[5] if (( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )>=10) else 0

                , EVE365cc[j]['note_cc']
                
                , EVE365sn[j]['note_sn']
                
                #, [ ( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] ), ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] ) ], EVE365R[j] 
            ],

            [ 
                (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),
    
                round( (( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0] + ( round(listeMatriceRs5EVE[j][2]*0.7 + MAS325cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][2]> 0 ) else MAS325[j] ) *coefS5EVE[1] + ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) *coefS5EVE[2] + ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3]+( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4] + ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )*coefS5EVE[5] ), 2),

                round((( round(listeMatriceRs5EVE[j][1]*0.7 + MAS315cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][1]> 0 ) else MAS315[j] ) *coefS5EVE[0] + MAS325[j]*coefS5EVE[1] + ( round(listeMatriceRs5EVE[j][3]*0.7 + MAS335cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][3]> 0 ) else MAS335[j] ) *coefS5EVE[2] + ( round(listeMatriceRs5EVE[j][4]*0.7 + MAS345cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][4]> 0 ) else MAS345[j] )*coefS5EVE[3] + ( round(listeMatriceRs5EVE[j][5]*0.7 + EVE355cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][5]> 0 ) else EVE355[j] )*coefS5EVE[4] + ( round(listeMatriceRs5EVE[j][6]*0.7 + EVE365cc[j]['note_cc']*0.3, 2) if (listeMatriceRs5EVE[j][6]> 0 ) else EVE365[j] )*coefS5EVE[5])/(coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]), 2)
            ],
        ]

        listeMatriceS5.append(matricesS5EVE)
        EVEMoyennes5.append(matricesS5EVE[7][2])
    
    EVEMoyennes5.sort(reverse=True)

    moys5 = stat.mean(EVEMoyennes5)
    moys5 = round(moys5, 2)
    sessions5 = 'Janvier 2023'

    #semestre1MDS = [filiere, listeMatriceS5, EVEMoyennes5, moy, sessions5] #listeMatriceS5 , EVEMoyennes5,  sessions5

#################################################### S6 STATS VAL ############################################################################################################################
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

#################################################### PV SEMESTRE 6 ###########################################################################################################################
    MAS316 = list(Evaluation.objects.filter(uniteEnseignement_id=82, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS316cc = list(Evaluation.objects.filter(uniteEnseignement_id=82, natureEvaluation='EXAMEN').values('note_cc'))
    MAS316sn = list(Evaluation.objects.filter(uniteEnseignement_id=82, natureEvaluation='EXAMEN').values('note_sn'))
    sort315 = epurationTriCroissant(MAS316)

    MAS326 = list(Evaluation.objects.filter(uniteEnseignement_id=83, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS326cc = list(Evaluation.objects.filter(uniteEnseignement_id=83, natureEvaluation='EXAMEN').values('note_cc'))
    MAS326sn = list(Evaluation.objects.filter(uniteEnseignement_id=83, natureEvaluation='EXAMEN').values('note_sn'))
    sort325 = epurationTriCroissant(MAS326)

    MAS336 = list(Evaluation.objects.filter(uniteEnseignement_id=84, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS336cc = list(Evaluation.objects.filter(uniteEnseignement_id=84, natureEvaluation='EXAMEN').values('note_cc'))
    MAS336sn = list(Evaluation.objects.filter(uniteEnseignement_id=84, natureEvaluation='EXAMEN').values('note_sn'))
    sort335 = epurationTriCroissant(MAS336)

    MAS346 = list(Evaluation.objects.filter(uniteEnseignement_id=85, natureEvaluation='EXAMEN').values('note_Examen'))
    MAS346cc = list(Evaluation.objects.filter(uniteEnseignement_id=85, natureEvaluation='EXAMEN').values('note_cc'))
    MAS346sn = list(Evaluation.objects.filter(uniteEnseignement_id=85, natureEvaluation='EXAMEN').values('note_sn'))
    sort345 = epurationTriCroissant(MAS346)

    EVE356 = list(Evaluation.objects.filter(uniteEnseignement_id=86, natureEvaluation='EXAMEN').values('note_Examen'))
    EVE356cc = list(Evaluation.objects.filter(uniteEnseignement_id=86, natureEvaluation='EXAMEN').values('note_cc'))
    EVE356sn = list(Evaluation.objects.filter(uniteEnseignement_id=86, natureEvaluation='EXAMEN').values('note_sn'))
    sort355 = epurationTriCroissant(EVE356)

    EVE366 = list(Evaluation.objects.filter(uniteEnseignement_id=87, natureEvaluation='EXAMEN').values('note_Examen'))
    EVE366cc = list(Evaluation.objects.filter(uniteEnseignement_id=87, natureEvaluation='EXAMEN').values('note_cc'))
    EVE366sn = list(Evaluation.objects.filter(uniteEnseignement_id=87, natureEvaluation='EXAMEN').values('note_sn'))
    sort365 = epurationTriCroissant(EVE366)

    listeMatrice = []
    EVEMoyenne = []

    for j in range( len(infoEtudiantEVE) ):

        matrice = [
            
            infoEtudiantEVE[j],

            [ 
                MAS316[j]
                
                , coefS5EVE[0]
                
                , round(MAS316[j]*coefS5EVE[0], 2)

                , round( ((MAS316[j]*coefS5EVE[0]) + (MAS326[j]*coefS5EVE[1]) + (MAS336[j]*coefS5EVE[2]) + (MAS346[j]*coefS5EVE[3])) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]), 2)
                
                , sort315.index(MAS316[j])+1

                , (MAS316[j] >=10)

                , creditS5EVE[0]

                , creditS5EVE[0] if((MAS316[j] >=10)) else 0
                
                ,#crédit obtenu

                  MAS316cc[j]['note_cc']
                
                , MAS316sn[j]['note_sn'],

                #RATTRAPAGE
                #MAS316R[j]['note_rattrapage']
            ],
            
            [ 
                MAS326[j]
                
                , coefS5EVE[1]
                
                , round(MAS326[j]*coefS5EVE[1], 2)
                
                , 'MOYENNE'
                
                , sort325.index(MAS326[j])+1
                
                , (MAS326[j]>=10)

                , creditS5EVE[1]
                
                , creditS5EVE[1] if (MAS326[j]>=10) else 0
                
                , MAS326cc[j]['note_cc']
                
                , MAS326sn[j]['note_sn'],  
            ],
            
            [ 
                MAS336[j]
                
                , coefS5EVE[2]
                
                , round(MAS336[j]*coefS5EVE[2], 2)
                
                , 'MOYENNE'
                
                , sort335.index(MAS336[j])+1
                
                , (MAS336[j]>=10)
                
                , creditS5EVE[2]
                
                , creditS5EVE[2] if (MAS336[j]>=10) else 0
                
                , MAS336cc[j]['note_cc']
                
                , MAS336sn[j]['note_sn'] 
            ],
            
            [ 
                MAS346[j]
                
                , coefS5EVE[3]
                
                , round(MAS346[j]*coefS5EVE[3], 2)
                
                , 'MOYENNE'
                
                , sort345.index(MAS346[j])+1
                
                , (MAS346[j]>=10)
                
                , creditS5EVE[3]
                
                , creditS5EVE[3] if (MAS346[j]>=10) else 0
                
                , MAS346cc[j]['note_cc']
                
                , MAS346sn[j]['note_sn']
                
                #, [ MAS316[j], MAS326[j], MAS336[j], MAS346[j]], MAS346R[j] 
                
                ],
            
            #MODULE 2
            [ 
                EVE356[j]
                
                , coefS5EVE[4]
                
                , round(EVE356[j]*coefS5EVE[4], 2)

                , round((EVE356[j]*coefS5EVE[4] + EVE366[j]*coefS5EVE[5] )/(coefS5EVE[4]+coefS5EVE[5]), 2)

                , sort355.index(EVE356[j])+1

                , (EVE356[j]>=10)

                , creditS5EVE[4]

                , creditS5EVE[4] if((EVE356[j]>=10)) else 0

                , EVE356cc[j]['note_cc']
                
                , EVE356sn[j]['note_sn']

                #, EVE356R[j]['note_rattrapage']
            ],
            
            [ 
                EVE366[j]
                
                , coefS5EVE[5]
                
                , round(EVE366[j]*coefS5EVE[5], 2)
                
                , 'MOYENNE', sort365.index(EVE366[j])+1
                
                , (EVE366[j]>=10)
                
                , creditS5EVE[5]
                
                , creditS5EVE[5] if (EVE366[j]>=10) else 0
                
                , EVE366cc[j]['note_cc']
                
                , EVE366sn[j]['note_sn']
                
                #, [ EVE356[j], EVE366[j] ], EVE366R[j] 
            ],

            [ 
                (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),
    
                round( ( MAS316[j]*coefS5EVE[0] + MAS326[j]*coefS5EVE[1] + MAS336[j]*coefS5EVE[2] + MAS346[j]*coefS5EVE[3]+EVE356[j]*coefS5EVE[4] + EVE366[j]*coefS5EVE[5] ), 2),

                round((MAS316[j]*coefS5EVE[0] + MAS326[j]*coefS5EVE[1] + MAS336[j]*coefS5EVE[2] + MAS346[j]*coefS5EVE[3]+EVE356[j]*coefS5EVE[4] + EVE366[j]*coefS5EVE[5])/(coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]), 2)
            ],
        ]

        creditObtenus = 0
        listeCredit = []

        listeMatrice.append(matrice)
        EVEMoyenne.append(matrice[7][2])
        EVEMoyenne.sort(reverse=True)

        moy = stat.mean(EVEMoyenne)
        moy = round(moy, 2)
        session = ''

#################################################### PV SEMESTRE 6 RATTRAPAGE #################################################################################################################
    infoMAS316R = ""
    MAS316R = list(Evaluation.objects.filter(uniteEnseignement_id=82, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort316R = epurationRattrapage(MAS316R)

    infoMAS326R = ""
    MAS326R = list(Evaluation.objects.filter(uniteEnseignement_id=83, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort325 = epurationRattrapage(MAS326R)

    infoMAS336R =""
    MAS336R = list(Evaluation.objects.filter(uniteEnseignement_id=84, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort335 = epurationRattrapage(MAS336R)

    infoMAS346R =""
    MAS346R = list(Evaluation.objects.filter(uniteEnseignement_id=85, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort345 = epurationRattrapage(MAS346R)

    infoEVE356R = ""
    EVE356R = list(Evaluation.objects.filter(uniteEnseignement_id=86, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort355 = epurationRattrapage(EVE356R)

    infoEVE366R = ""
    EVE366R = list(Evaluation.objects.filter(uniteEnseignement_id=87, note_Examen=0, natureEvaluation='RATTRAPAGE').values('note_rattrapage'))
    sort365 = epurationRattrapage(EVE366R)

    listeMatriceRs6EVE = []
    listeMatriceRs6EVEex = []

    for j in range (len(infoEtudiantEVE)):
        matriceRs6EVE = [

            infoEtudiantEVE[j],
            
            MAS316R[j],

            MAS326R[j],
            
            MAS336R[j],
            
            MAS346R[j],
            
            EVE356R[j],
            
            EVE366R[j],
        ]

        matriceRs6EVEex = [

            infoEtudiantEVE[j],
            
            ( round( MAS316R[j]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (MAS316R[j] > 0) else MAS316R[j] ) ,

            ( round( MAS326R[j]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (MAS326R[j] > 0) else MAS326R[j] ) ,
            
            ( round( MAS336R[j]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (MAS336R[j] > 0) else MAS336R[j] ) ,
            
            ( round( MAS346R[j]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (MAS346R[j] > 0) else MAS346R[j] ) ,
            
            ( round( EVE356R[j]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (EVE356R[j] > 0) else EVE356R[j] ) ,
            
            ( round( EVE366R[j]*0.7 + EVE366cc[j]['note_cc']*0.3, 2) if (EVE366R[j] > 0) else EVE366R[j] ) ,
        ]
        listeMatriceRs6EVE.append(matriceRs6EVE)
        listeMatriceRs6EVEex.append(matriceRs6EVEex)

#################################################### PV SEMESTRE 6 SYNTHESE   ######################################################################################################################
    listeMatriceS =  []
    EVEMoyennes6 = []

    EVEMoyes5s6 = []

    for j in range( len(infoEtudiantEVE) ):

        matricesS6EVE = [
            
            infoEtudiantEVE[j],

            [ 
                ( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) 
                
                , coefS5EVE[0]
                
                , round(( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) *coefS5EVE[0], 2)

                , round( ((( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) *coefS5EVE[0]) + (MAS326[j]*coefS5EVE[1]) + (MAS336[j]*coefS5EVE[2]) + (MAS346[j]*coefS5EVE[3])) / (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]), 2)
                
                #, sort315.index(( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) )+1

                , (( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] )  >=10)

                , creditS5EVE[0]

                , creditS5EVE[0] if((( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] )  >=10)) else 0
                
                , MAS316cc[j]['note_cc']
                
                , MAS316sn[j]['note_sn'],
            ],
            
            [ 
                ( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) 
                
                , coefS5EVE[1]
                
                , round(( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) *coefS5EVE[1], 2)
                
                , 'MOYENNE'
                
                #, sort325.index(( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) )+1
                
                , (( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) >=10)

                , creditS5EVE[1]
                
                , creditS5EVE[1] if (( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) >=10) else 0
                
                , MAS326cc[j]['note_cc']
                
                , MAS326sn[j]['note_sn'],  
            ],
            
            [ 
                ( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) 
                
                , coefS5EVE[2]
                
                , round(( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) *coefS5EVE[2], 2)
                
                , 'MOYENNE'
                
                #, sort335.index(( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) )+1
                
                , (( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) >=10)
                
                , creditS5EVE[2]
                
                , creditS5EVE[2] if (( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) >=10) else 0
                
                , MAS336cc[j]['note_cc']
                
                , MAS336sn[j]['note_sn'] 
            ],
            
            [ 
                ( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )
                
                , coefS5EVE[3]
                
                , round(( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )*coefS5EVE[3], 2)
                
                , 'MOYENNE'
                
                #, sort345.index(( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] ))+1
                
                , (( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )>=10)
                
                , creditS5EVE[3]
                
                , creditS5EVE[3] if (( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )>=10) else 0
                
                , MAS346cc[j]['note_cc']
                
                , MAS346sn[j]['note_sn']
                
                #, [ ( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) , ( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) , ( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) , ( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )], MAS346R[j] 
                
                ],
            
            #MODULE 2
            [ 
                ( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )
                
                , coefS5EVE[4]
                
                , round(( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )*coefS5EVE[4], 2)

                , round((( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )*coefS5EVE[4] + EVE366[j]*coefS5EVE[5] )/(coefS5EVE[4]+coefS5EVE[5]), 2)

                #, sort355.index(( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] ))+1

                , (( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )>=10)

                , creditS5EVE[4]

                , creditS5EVE[4] if((( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )>=10)) else 0

                , EVE356cc[j]['note_cc']
                
                , EVE356sn[j]['note_sn']

                #, EVE356R[j]['note_rattrapage']
            ],
            
            [ 
                ( round(listeMatriceRs6EVE[j][6]*0.7 + MAS356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] ) 
                
                , coefS5EVE[5]
                
                , round(( round(listeMatriceRs6EVE[j][6]*0.7 + MAS356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] )*coefS5EVE[5], 2)
                
                , 'MOYENNE'
                
                #, sort365.index(( round(listeMatriceRs6EVE[j][6]*0.7 + MAS356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] ))+1
                
                , (( round(listeMatriceRs6EVE[j][6]*0.7 + MAS356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] )>=10)
                
                , creditS5EVE[5]
                
                , creditS5EVE[5] if (( round(listeMatriceRs6EVE[j][6]*0.7 + MAS356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] )>=10) else 0
                
                , EVE366cc[j]['note_cc']
                
                , EVE366sn[j]['note_sn']
                
                #, [ ( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] ), ( round(listeMatriceRs6EVE[j][6]*0.7 + MAS356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] ) ], EVE366R[j] 
            ],

            [ 
                (coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]),
    
                round( (( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) *coefS5EVE[0] + ( round(listeMatriceRs6EVE[j][2]*0.7 + MAS326cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][2]> 0 ) else MAS326[j] ) *coefS5EVE[1] + ( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) *coefS5EVE[2] + ( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )*coefS5EVE[3]+( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )*coefS5EVE[4] + ( round(listeMatriceRs6EVE[j][6]*0.7 + MAS356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] )*coefS5EVE[5] ), 2),

                round((( round(listeMatriceRs6EVE[j][1]*0.7 + MAS316cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][1]> 0 ) else MAS316[j] ) *coefS5EVE[0] + MAS326[j]*coefS5EVE[1] + ( round(listeMatriceRs6EVE[j][3]*0.7 + MAS336cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][3]> 0 ) else MAS336[j] ) *coefS5EVE[2] + ( round(listeMatriceRs6EVE[j][4]*0.7 + MAS346cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][4]> 0 ) else MAS346[j] )*coefS5EVE[3] + ( round(listeMatriceRs6EVE[j][5]*0.7 + EVE356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][5]> 0 ) else EVE356[j] )*coefS5EVE[4] + ( round(listeMatriceRs6EVE[j][6]*0.7 + MAS356cc[j]['note_cc']*0.3, 2) if (listeMatriceRs6EVE[j][6]> 0 ) else EVE366[j] )*coefS5EVE[5])/(coefS5EVE[0]+coefS5EVE[1]+coefS5EVE[2]+coefS5EVE[3]+coefS5EVE[4]+coefS5EVE[5]), 2),

                moyCredit[j]
            ],

            #moyenne et Crédit par Semestre
            #[moyCredit[j]]
        ]

        listeMatriceS.append(matricesS6EVE)

        EVEMoyes5s6.append( round( (listeMatriceS5[j][7][2]  + matricesS6EVE[7][2])/2, 2) )

        EVEMoyennes6.append(matricesS6EVE[7][2])
        EVEMoyennes6.sort(reverse=True)

        moy2 = stat.mean(EVEMoyennes6)
        moy2 = round(moy2, 2)
        session2 = ''

#################################################### STATS VALIDATION #########################################################################################################################
    for i in range (len(MAS316)):
        if MAS316[i] >= 10:
            val1['nombre']+=1
    val1['pourcentage']= round(((val1['nombre']/ len(infoEtudiantEVE))*100), 2) #round(2,(val1['nombre']/ len(infoEtudiantEVE))*100)
    for i in range (len(MAS326)):
        if MAS326[i] >= 10:
            val2['nombre']+=1
    val2['pourcentage']= round(((val2['nombre']/ len(infoEtudiantEVE))*100),2)
    for i in range (len(MAS336)):
        if MAS336[i] >= 10:
            val3['nombre']+=1
    val3['pourcentage']= round(((val3['nombre']/ len(infoEtudiantEVE))*100),2)
    for i in range (len(MAS346)):
        if MAS346[i] >= 10:
            val4['nombre']+=1
    val4['pourcentage']= round(((val4['nombre']/ len(infoEtudiantEVE))*100),2)
    for i in range (len(EVE356)):
        if EVE356[i] >= 10:
            val5['nombre']+=1
    val5['pourcentage']= round(((val5['nombre']/ len(infoEtudiantEVE))*100),2)
    for i in range (len(EVE366)):
        if EVE366[i] >= 10:
            val6['nombre']+=1
    val6['pourcentage']= round(((val6['nombre']/ len(infoEtudiantEVE))*100),2)

#################################################### STAT MENTION ################################################################################################################################
    statMention(MAS316,m315)
    pourcentageMention(m315, len(infoEtudiantEVE))

    statMention(MAS326,m325)
    pourcentageMention(m325, len(infoEtudiantEVE))

    statMention(MAS336,m335)
    pourcentageMention(m335, len(infoEtudiantEVE))

    statMention(MAS346,m345)
    pourcentageMention(m345, len(infoEtudiantEVE))

    statMention(EVE356,e355)
    pourcentageMention(e355, len(infoEtudiantEVE))

    statMention(EVE366,e365)
    pourcentageMention(e365, len(infoEtudiantEVE))

    UEStats = [val1, val2, val3, val4, val5, val6]
    UEstats_mention = [m315, m325, m335, m345, e355, e365]



    semestre1MDS = [filiere, listeMatrice, EVEMoyenne, moy, session, creditS5EVE, UEStats, UEstats_mention, listeMatriceS, UeNomCode, EVEMoyennes6, listeMatriceRs6EVEex, listeMatriceS5, EVEMoyes5s6]

    return render(request, 'bulletin/releveCommun/releveCommuns6Eve.html', {'semestre1MDS': semestre1MDS}) #, {'semestre1MDS': semestre1MDS}






#####################################################################################################################################################################################################################
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

## MDS1 DECOMPTE CREDIT
def MDSCreditCount(matrice):
    """
        Fonction permettant de compter le nombre de crédit total par semestre en MDS1

    """
    #ligne 1 & 2
    ##UE Fondamentales
    note1_2 = round( ((matrice[1][0]+matrice[2][0])/2), 2)
    if (((note1_2) >=7 and note1_2 < 10) and  matrice[1][3] >=10 ) or (note1_2 >= 10):
        matrice[1][5] = matrice[1][6]
    else:
        matrice[1][5] = 0
    #ligne3 & 4
    note3_4 = round(((matrice[3][0]+matrice[4][0])/2), 2)
    if (((note3_4) >=7 and note3_4 < 10) and  matrice[1][3] >=10 ) or (note3_4 >= 10):
        matrice[3][5] = matrice[3][6]
    else:
        matrice[3][5] = 0

    #ligne 5
    ##UE Pro
    if ((matrice[5][0] >=7 and matrice[5][0] < 10) and  matrice[5][3] >=10 ) or (matrice[5][0] >= 10):
        matrice[5][5] = matrice[5][6]
    else:
        matrice[5][5] = 0

    #ligne 6
    if ((matrice[6][0] >=7 and matrice[6][0] < 10) and  matrice[5][3] >=10 ) or (matrice[6][0] >= 10):
        matrice[6][5] = matrice[6][6]
    else:
        matrice[6][5] = 0

    #ligne 7
    if ((matrice[7][0] >=7 and matrice[7][0] < 10) and  matrice[5][3] >=10 ) or (matrice[7][0] >= 10):
        matrice[7][5] = matrice[7][6]
    else:
        matrice[7][5] = 0

    #ligne 8
    if ((matrice[8][0] >=7 and matrice[8][0] < 10) and  matrice[5][3] >=10 ) or (matrice[8][0] >= 10):
        matrice[8][5] = matrice[8][6]
    else:
        matrice[8][5] = 0

    ##UE Transversales
    #ligne 9
    if ((matrice[9][0] >=7 and matrice[9][0] < 10) and  matrice[9][3] >=10 ) or (matrice[9][0] >= 10):
        matrice[9][5] = matrice[9][6]
    else:
        matrice[9][5] = 0

    #ligne 10
    if ((matrice[10][0] >=7 and matrice[10][0] < 10) and  matrice[9][3] >=10 ) or (matrice[10][0] >= 10):
        matrice[10][5] = matrice[10][6]
    else:
        matrice[10][5] = 0

    ##Ajout total crédit à MAT 11
    matrice[11].append(matrice[1][5]+matrice[3][5]+matrice[5][5]+matrice[6][5]+matrice[7][5]+matrice[8][5]+matrice[9][5]+matrice[10][5])


## MDS1 DECOMPTE CREDIT
def MDSCreditCountPV(matrice):
    """
        Fonction permettant de compter le nombre de crédit total par semestre en MDS1

    """
    #ligne 1 & 2
    ##UE Fondamentales
    note1_2 = round( ((matrice[1][0]+matrice[2][0])/2), 2)
    if (((note1_2) >=7 and note1_2 < 10) and  matrice[1][3] >=10 ) or (note1_2 >= 10):
        matrice[1][5] = matrice[1][6]
    else:
        matrice[1][5] = 0
    #ligne3 & 4
    note3_4 = round(((matrice[3][0]+matrice[4][0])/2), 2)
    if (((note3_4) >=7 and note3_4 < 10) and  matrice[1][3] >=10 ) or (note3_4 >= 10):
        matrice[3][5] = matrice[3][6]
    else:
        matrice[3][5] = 0

    #ligne 5
    ##UE Pro
    if ((matrice[5][0] >=7 and matrice[5][0] < 10) and  matrice[5][3] >=10 ) or (matrice[5][0] >= 10):
        matrice[5][5] = matrice[5][6]
    else:
        matrice[5][5] = 0

    #ligne 6
    if ((matrice[6][0] >=7 and matrice[6][0] < 10) and  matrice[5][3] >=10 ) or (matrice[6][0] >= 10):
        matrice[6][5] = matrice[6][6]
    else:
        matrice[6][5] = 0

    #ligne 7
    if ((matrice[7][0] >=7 and matrice[7][0] < 10) and  matrice[5][3] >=10 ) or (matrice[7][0] >= 10):
        matrice[7][5] = matrice[7][6]
    else:
        matrice[7][5] = 0

    #ligne 8
    if ((matrice[8][0] >=7 and matrice[8][0] < 10) and  matrice[5][3] >=10 ) or (matrice[8][0] >= 10):
        matrice[8][5] = matrice[8][6]
    else:
        matrice[8][5] = 0

    ##UE Transversales
    #ligne 9
    if ((matrice[9][0] >=7 and matrice[9][0] < 10) and  matrice[9][3] >=10 ) or (matrice[9][0] >= 10):
        matrice[9][5] = matrice[9][6]
    else:
        matrice[9][5] = 0

    #ligne 10
    if ((matrice[10][0] >=7 and matrice[10][0] < 10) and  matrice[9][3] >=10 ) or (matrice[10][0] >= 10):
        matrice[10][5] = matrice[10][6]
    else:
        matrice[10][5] = 0

    ##Ajout total crédit à MAT 11
    matrice[11].append(matrice[1][5]+matrice[3][5]+matrice[5][5]+matrice[6][5]+matrice[7][5]+matrice[8][5]+matrice[9][5]+matrice[10][5])


def MDSCreditCountS2(matrice):
    """
        Fonction permettant de compter le nombre de crédit total par semestre en MDS
        Et décision  si Admis ou pas
    """
    for j in range(len(matrice[0])):

        mat = matrice[0][j]
        print(mat)

        note1_2 = round( ((mat[1][0]+mat[2][0])/2), 2)
        if (((note1_2) >=7 and note1_2 < 10) and  mat[1][3] >=10 ) or (note1_2 >= 10):
            mat[1][5] = mat[1][6]
        else:
            mat[1][5] = 0
        #ligne3 & 4
        note3_4 = round(((mat[3][0]+mat[4][0])/2), 2)
        if (((note3_4) >=7 and note3_4 < 10) and  mat[1][3] >=10 ) or (note3_4 >= 10):
            mat[3][5] = mat[3][6]
        else:
            mat[3][5] = 0

        #ligne 5 
        ##UE Pro
        if ((mat[5][0] >=7 and mat[5][0] < 10) and  mat[5][3] >=10 ) or (mat[5][0] >= 10):
            mat[5][5] = mat[5][6]
        else:
            mat[5][5] = 0

        #ligne 6
        if ((mat[6][0] >=7 and mat[6][0] < 10) and  mat[5][3] >=10 ) or (mat[6][0] >= 10):
            mat[6][5] = mat[6][6]
        else:
            mat[6][5] = 0

        #ligne 7
        if ((mat[7][0] >=7 and mat[7][0] < 10) and  mat[5][3] >=10 ) or (mat[7][0] >= 10):
            mat[7][5] = mat[7][6]
        else:
            mat[7][5] = 0

        #ligne 8
        if ((mat[8][0] >=7 and mat[8][0] < 10) and  mat[5][3] >=10 ) or (mat[8][0] >= 10):
            mat[8][5] = mat[8][6]
        else:
            mat[8][5] = 0

        ##UE Transversales
        #ligne 9
        if ((mat[9][0] >=7 and mat[9][0] < 10) and  mat[9][3] >=10 ) or (mat[9][0] >= 10):
            mat[9][5] = mat[9][6]
        else:
            mat[9][5] = 0

        #ligne 10
        if ((mat[10][0] >=7 and mat[10][0] < 10) and  mat[9][3] >=10 ) or (mat[10][0] >= 10):
            mat[10][5] = mat[10][6]
        else:
            mat[10][5] = 0

        ##Ajout total crédit à MAT 11
        mat[11].append(mat[1][5]+mat[3][5]+mat[5][5]+mat[6][5]+mat[7][5]+mat[8][5]+mat[9][5]+mat[10][5]) #

        #Enregistrement de la moyenne et crédits semestre 3
        e_matri = mat[0]["matricule"]
        student = Etudiant.objects.get(matricule = e_matri)
        student.moyS2 = mat[11][2]
        student.crS2  = mat[11][3]
        student.save()

        #Test d'admission


################################################ MODULE SYNTHESE ET DECOMPTE DE CREDITS ##########################################################
## EPS1 DECOMPTE CREDIT SEMESTRE 1
def EPSCreditCount(matrice):
    """
        Fonction permettant de compter le nombre de crédit total par semestre en EPS1
    """
    #print(len(matrice))
    ##UE Fondamentales
    #ligne 1
    if (((matrice[1][0]) >=7 and matrice[1][0] < 10) and  matrice[1][3] >=10 ) or (matrice[1][0] >= 10):
        matrice[1][7] = matrice[1][6]
    else:
        matrice[1][7] = 0
    #ligne 2
    if (((matrice[2][0]) >=7 and matrice[2][0] < 10) and  matrice[1][3] >=10 ) or (matrice[2][0] >= 10):
        matrice[2][7] = matrice[2][6]
    else:
        matrice[2][7] = 0

    ##UE Pro
    #ligne 3
    if (((matrice[3][0]) >=7 and matrice[3][0] < 10) and  matrice[3][3] >=10 ) or (matrice[3][0] >= 10):
        matrice[3][7] = matrice[3][6]
    else:
        matrice[3][7] = 0
    #ligne 4
    if (((matrice[4][0]) >=7 and matrice[4][0] < 10) and  matrice[3][3] >=10 ) or (matrice[4][0] >= 10):
        matrice[4][7] = matrice[4][6]
    else:
        matrice[4][7] = 0
    #ligne 5-8
    note5678 = round((matrice[5][0]+matrice[6][0]+matrice[7][0]+matrice[8][0])/4, 2)

    if ( (((matrice[5][0] >= 7 and matrice[5][0] < 10 ) and matrice[3][3] >=10) or matrice[5][0] >= 10) and (((matrice[6][0] >= 7 and matrice[6][0] < 10 ) and matrice[3][3] >=10) or matrice[6][0] >= 10) and (((matrice[7][0] >= 7 and matrice[7][0] < 10 ) and matrice[3][3] >=10) or matrice[7][0] >= 10) and (((matrice[8][0] >= 7 and matrice[8][0] < 10 ) and matrice[3][3] >=10) or matrice[8][0] >= 10) ):
        matrice[5][7] = matrice[5][6]
    else:
        matrice[5][7] = 0
    #ligne 9
    if (((matrice[9][0]) >=7 and matrice[9][0] < 10) and  matrice[3][3] >=10 ) or (matrice[9][0] >= 10):
        matrice[9][7] = matrice[9][6]
    else:
        matrice[9][7] = 0
    ##UE Transversales
    #ligne 10
    if (((matrice[10][0]) >=7 and matrice[10][0] < 10) and  matrice[10][3] >=10 ) or (matrice[10][0] >= 10):
        matrice[10][7] = matrice[10][6]
    else:
        matrice[10][7] = 0
    #ligne 11
    if (((matrice[11][0]) >=7 and matrice[11][0] < 10) and  matrice[10][3] >=10 ) or (matrice[11][0] >= 10):
        matrice[11][7] = matrice[11][6]
    else:
        matrice[11][7] = 0
    #ligne 12
    if (((matrice[12][0]) >=7 and matrice[12][0] < 10) and  matrice[10][3] >=10 ) or (matrice[12][0] >= 10):
        matrice[12][7] = matrice[12][6]
    else:
        matrice[12][7] = 0

    ##Ajout total crédit à MAT 13
    matrice[13].append(matrice[1][7]+matrice[2][7]+matrice[3][7]+matrice[4][7]+matrice[5][7]+matrice[9][7]+matrice[10][7]+matrice[11][7]+matrice[12][7])

## EPS1 DECOMPTE CREDIT SEMESTRE 2
def EPSCreditCount2(matrice):
    """
        Fonction permettant de compter le nombre de crédit total semestre2 en EPS1 

        Plus l'ajout de la moyenne et des crédits sur chaque étudiant
    """
    print(matrice)
    matlen = matrice[0]

    print(matlen)

    for j in range(len(matlen)):


        mat = matlen[j]


        ##UE Fondamentales
        #ligne 1
        if (((mat[1][0]) >=7 and mat[1][0] < 10) and  mat[1][3] >=10 ) or (mat[1][0] >= 10):
            #mat[1][7] = mat[1][6]
            mat[1].append(mat[1][5])
        else:
            #mat[1][7] = 0
            mat[1].append(0)
        #ligne 2
        if (((mat[2][0]) >=7 and mat[2][0] < 10) and  mat[1][3] >=10 ) or (mat[2][0] >= 10):
            #mat[2][7] = mat[2][6]
            mat[2].append(mat[2][5])
        else:
            #mat[2][7] = 0
            mat[2].append(0)
        ##UE Pro
        #ligne 3
        if (((mat[3][0]) >=7 and mat[3][0] < 10) and  mat[3][3] >=10 ) or (mat[3][0] >= 10):
            #mat[3][7] = mat[3][6]
            mat[3].append(mat[3][5])
        else:
            #mat[3][7] = 0
            mat[3].append(0)
        #ligne 4
        if (((mat[4][0]) >=7 and mat[4][0] < 10) and  mat[3][3] >=10 ) or (mat[4][0] >= 10):
            #mat[4][7] = mat[4][6]
            mat[4].append(mat[4][5])
        else:
            #mat[4][7] = 0
            mat[4].append(0)
        #ligne 5-8
        note5678 = round((mat[5][0]+mat[6][0]+mat[7][0]+mat[8][0])/4, 2)
        if (((note5678 >= 7 and note5678 < 10 ) and mat[3][3] >=10) or note5678 >= 10):
            #mat[5][7] = mat[5][6]
            mat[5].append(mat[5][5])
        else:
            #mat[5][7] = 0
            mat[5].append(0)
        #ligne 9
        if (((mat[9][0]) >=7 and mat[9][0] < 10) and  mat[3][3] >=10 ) or (mat[9][0] >= 10):
            #mat[9][7] = mat[9][6]
            mat[9].append(mat[9][5])
        else:
            #mat[9][7] = 0
            mat[9].append(0)
        ##UE Transversales
        #ligne 10
        if (((mat[10][0]) >=7 and mat[10][0] < 10) and  mat[10][3] >=10 ) or (mat[10][0] >= 10):
            #mat[10][7] = mat[10][6]

            mat[10].append(mat[10][5])
        else:
            #mat[10][7] = 0
            mat[10].append(0)

        #ligne 11
        if (((mat[11][0]) >=7 and mat[11][0] < 10) and  mat[10][3] >=10 ) or (mat[11][0] >= 10):
            #mat[11][7] = mat[11][6]
            #print(mat[11])
            mat[11].append(mat[11][5])
        else:
            #mat[11][7] = 0
            mat[11].append(0)

        #ligne 12
        if (((mat[12][0]) >=7 and mat[12][0] < 10) and  mat[10][3] >=10 ) or (mat[12][0] >= 10):
            #mat[12][7] = mat[12][6]
            mat[12].append(mat[12][5])
        else:
            mat[12].append(0)

        ##Ajout total crédit à MAT 13
        mat[13].append(mat[1][7]+mat[2][7]+mat[3][7]+mat[4][7]+mat[5][7]+mat[9][7]+mat[10][7]+mat[11][7]+mat[12][7])


        #Enregistrement des notes et crédits de Semestre1 en MDS1
        e_matri = mat[0]['matricule']
        #print(e_matri)
        studenteps = Etudiant.objects.get(matricule = e_matri)
        studenteps.moyS2 = mat[13][2]
        studenteps.crS2 = mat[13][3]
        studenteps.save()

## EPS1 DECOMPTE CREDIT
def EPSCreditCount22(matrice):
    """
        Fonction permettant de compter le nombre de crédit total par semestre en EPS1
    """
    #print(matrice)
    matlen = matrice[0]

    for j in range(len(matlen)):


        mat = matlen[j]

        ##UE Fondamentales
        #ligne 1
        if (((mat[1][0]) >=7 and mat[1][0] < 10) and  mat[1][3] >=10 ) or (mat[1][0] >= 10):
            #mat[1][7] = mat[1][6]
            mat[1].append(mat[1][6])
        else:
            #mat[1][7] = 0
            mat[1].append(0)
        #ligne 2
        if (((mat[2][0]) >=7 and mat[2][0] < 10) and  mat[1][3] >=10 ) or (mat[2][0] >= 10):
            #mat[2][7] = mat[2][6]
            mat[2].append(mat[2][6])
        else:
            #mat[2][7] = 0
            mat[2].append(0)
        ##UE Pro
        #ligne 3
        if (((mat[3][0]) >=7 and mat[3][0] < 10) and  mat[3][3] >=10 ) or (mat[3][0] >= 10):
            #mat[3][7] = mat[3][6]
            mat[3].append(mat[3][6])
        else:
            #mat[3][7] = 0
            mat[3].append(0)
        #ligne 4
        if (((mat[4][0]) >=7 and mat[4][0] < 10) and  mat[3][3] >=10 ) or (mat[4][0] >= 10):
            #mat[4][7] = mat[4][6]
            mat[4].append(mat[4][6])
        else:
            #mat[4][7] = 0
            mat[4].append(0)
        #ligne 5-8
        note5678 = round((mat[5][0]+mat[6][0]+mat[7][0]+mat[8][0])/4, 2)
        if (((note5678 >= 7 and note5678 < 10 ) and mat[3][3] >=10) or note5678 >= 10):
            #mat[5][7] = mat[5][6]
            mat[5].append(mat[5][6])
        else:
            #mat[5][7] = 0
            mat[5].append(0)
        #ligne 9
        if (((mat[9][0]) >=7 and mat[9][0] < 10) and  mat[3][3] >=10 ) or (mat[9][0] >= 10):
            #mat[9][7] = mat[9][6]
            mat[9].append(mat[9][6])
        else:
            #mat[9][7] = 0
            mat[9].append(0)
        ##UE Transversales
        #ligne 10
        if (((mat[10][0]) >=7 and mat[10][0] < 10) and  mat[10][3] >=10 ) or (mat[10][0] >= 10):
            #mat[10][7] = mat[10][6]
            mat[10].append(mat[10][6])
        else:
            #mat[10][7] = 0
            mat[10].append(0)

        #ligne 11
        if (((mat[11][0]) >=7 and mat[11][0] < 10) and  mat[10][3] >=10 ) or (mat[11][0] >= 10):
            #mat[11][7] = mat[11][6]
            mat[11].append(mat[11][6])
        else:
            #mat[11][7] = 0
            mat[11].append(0)

        #ligne 12
        if (((mat[12][0]) >=7 and mat[12][0] < 10) and  mat[10][3] >=10 ) or (mat[12][0] >= 10):
            #mat[12][7] = mat[12][6]
            mat[12].append(mat[12][6])
        else:
            mat[12].append(0)

        ##Ajout total crédit à MAT 13
        mat[13].append(mat[1][10]+mat[2][10]+mat[3][10]+mat[4][10]+mat[5][10]+mat[9][10]+mat[10][10]+mat[11][10]+mat[12][10])

## EPS2 DECOMPTE CREDIT S3
def EPS2CreditCountS3(matrice):
    """
        Fonction permettant de compter le nombre de crédit total par semestre en EPS2
    """

    for j in range(len(matrice)):
        mat = matrice[j]

        if ( ( (mat[1][0]) >=7 and mat[1][0] < 10) and  mat[1][3] >=10 ) or (mat[1][0] >= 10):
            mat[1].append( mat[1][6])
        else:
            mat[1].append(0)
        #ligne 2
        if (((mat[2][0]) >=7 and mat[2][0] < 10) and  mat[1][3] >=10 ) or (mat[2][0] >= 10):
            mat[2].append( mat[2][6])
        else:
            mat[2].append(0)
        #ligne 3
        if (((mat[3][0]) >=7 and mat[3][0] < 10) and  mat[3][3] >=10 ) or (mat[3][0] >= 10):
            mat[3].append( mat[3][6])
        else:
            mat[3].append(0)
        #ligne 4
        if (((mat[4][0]) >=7 and mat[4][0] < 10) and  mat[3][3] >=10 ) or (mat[4][0] >= 10):
            mat[4].append( mat[4][6])
        else:
            mat[4].append(0)
        #ligne 5-10
        note5678910 = round((mat[5][0]+mat[6][0]+mat[7][0]+mat[8][0]+mat[9][0]+mat[10][0])/6, 2)
        if (((note5678910 >= 7 and note5678910 < 10 ) and mat[3][3] >=10) or note5678910 >= 10):
            mat[5].append( mat[5][6])
        else:
            mat[5].append(0)
        #ligne 11
        if (((mat[11][0]) >=7 and mat[11][0] < 10) and  mat[3][3] >=10 ) or (mat[11][0] >= 10):
            mat[11].append( mat[11][6])
        else:
            mat[11].append(0)
        ##UE Transversales
        #ligne 12
        if (((mat[12][0]) >=7 and mat[12][0] < 10) and  mat[12][3] >=10 ) or (mat[12][0] >= 10):
            mat[12].append( mat[12][6])
        else:
            mat[12].append(0)
        #ligne 13
        if (((mat[13][0]) >=7 and mat[13][0] < 10) and  mat[12][3] >=10 ) or (mat[13][0] >= 10):
            mat[13].append( mat[13][6])
        else:
            mat[13].append(0)
        #ligne 14
        if (((mat[14][0]) >=7 and mat[14][0] < 10) and  mat[12][3] >=10 ) or (mat[14][0] >= 10):
            mat[14].append( mat[14][6])
        else:
            mat[14].append(0)

        ##Ajout total crédit à MAT 13
        mat[15].append(mat[1][7]+mat[2][7]+mat[3][7]+mat[4][7]+mat[5][7]+mat[11][7]+mat[12][7]+mat[13][7]+mat[14][7])

        #Enregistrement de la moyenne et crédits semestre 2
        e_matri = mat[0]["matricule"]
        studenteps2 = Etudiant.objects.get(matricule = e_matri)
        studenteps2.moyS3 = mat[15][2]
        studenteps2.crS3 = mat[15][3]
        studenteps2.save()

def EPS2CreditCountS3PV(matrice):
    """
        Fonction permettant de compter le nombre de crédit total par semestre en EPS2
    """

    for j in range(len(matrice)):
        mat = matrice[j]

        if ( ( (mat[1][0]) >=7 and mat[1][0] < 10) and  mat[1][3] >=10 ) or (mat[1][0] >= 10):
            #mat[1].append( mat[1][6])
            mat[1][7] =  mat[1][6]
        else:
            mat[1][7] =  0
        #ligne 2
        if (((mat[2][0]) >=7 and mat[2][0] < 10) and  mat[1][3] >=10 ) or (mat[2][0] >= 10):
            mat[2][7] =  mat[2][6]
        else:
            mat[2][7] =  0
        #ligne 3
        if (((mat[3][0]) >=7 and mat[3][0] < 10) and  mat[3][3] >=10 ) or (mat[3][0] >= 10):
            mat[3][7] =  mat[3][6]
        else:
            mat[3][7] =  0
        #ligne 4
        if (((mat[4][0]) >=7 and mat[4][0] < 10) and  mat[3][3] >=10 ) or (mat[4][0] >= 10):
            mat[4][7] =  mat[4][6]
        else:
            mat[1][7] =  0
        #ligne 5-10
        note5678910 = round((mat[5][0]+mat[6][0]+mat[7][0]+mat[8][0]+mat[9][0]+mat[10][0])/6, 2)
        if ( (((note5678910 >= 7 and note5678910 < 10 ) and mat[3][3] >=10) or note5678910 >= 10)  ):
            #mat[5].append( mat[5][6])
            mat[5][7] =  mat[5][6]
        else:
            mat[5][7] =  0
        #ligne 11
        if (((mat[11][0]) >=7 and mat[11][0] < 10) and  mat[3][3] >=10 ) or (mat[11][0] >= 10):
            mat[11][7] =  mat[11][6]
        else:
            mat[11][7] =  0
        ##UE Transversales
        #ligne 12
        if (((mat[12][0]) >=7 and mat[12][0] < 10) and  mat[12][3] >=10 ) or (mat[12][0] >= 10):
            mat[12][7] =  mat[12][6]
        else:
            mat[12][7] =  0
        #ligne 13
        if (((mat[13][0]) >=7 and mat[13][0] < 10) and  mat[12][3] >=10 ) or (mat[13][0] >= 10):
            mat[13][7] =  mat[13][6]
        else:
            mat[13][7] =  0
        #ligne 14
        if (((mat[14][0]) >=7 and mat[14][0] < 10) and  mat[12][3] >=10 ) or (mat[14][0] >= 10):
            mat[14][7] =  mat[14][6]
        else:
            mat[14][7] =  0

        #print(mat[1][7], mat[2][7],mat[3][7],mat[4][7],mat[5][7],mat[11][7],mat[12][7],mat[13][7],mat[14][7])

        ##Ajout total crédit à MAT 13
        mat[15].append(mat[1][7]+mat[2][7]+mat[3][7]+mat[4][7]+mat[5][7]+mat[11][7]+mat[12][7]+mat[13][7]+mat[14][7])

        #Enregistrement de la moyenne et crédits semestre 2
        #e_matri = mat[0]["matricule"]
        #studenteps2 = Etudiant.objects.get(matricule = e_matri)
        #studenteps2.moyS3 = mat[15][2]
        #studenteps2.crS3 = mat[15][3]
        #studenteps2.save()

## EPS2 DECOMPTE CREDIT S4
def EPS2CreditCountS4(matrice):
    """
        Fonction permettant de compter le nombre de crédit total en semestre 4 en EPS2
    """
    for j in range(len(matrice)):
        mat = matrice[j]

        #ligne 1
        #ligne 2

        #ligne 3
        if ( ( (mat[1][0]) >=7 and mat[1][0] < 10) and  mat[1][3] >=10 ) or (mat[1][0] >= 10):
            #mat[1].append( mat[1][6])
            mat[1][7] = ( mat[1][6] )
        else:
            #mat[1].append(0)
            mat[1][7] = 0
        #ligne 4-7
        note4567 = round((mat[2][0]+mat[3][0]+mat[4][0]+mat[5][0])/4, 2)
        if (((note4567 >= 7 and note4567 < 10 ) and mat[1][3] >=10) or note4567 >= 10):
            #mat[5].append( mat[5][6])
            mat[5][7] = ( mat[5][6] )
        else:
            #mat[5].append(0)
            mat[5][7] = 0
        #if (((mat[2][0]) >=7 and mat[2][0] < 10) and  mat[1][3] >=10 ) or (mat[2][0] >= 10):
        #    mat[2].append( mat[2][6])
        #else:
        #    mat[2].append(0)
        #ligne 8
        #if (((mat[3][0]) >=7 and mat[3][0] < 10) and  mat[3][3] >=10 ) or (mat[3][0] >= 10):
        #    mat[3].append( mat[3][6])
        #else:
        #    mat[3].append(0)
        #ligne 9
        #if (((mat[4][0]) >=7 and mat[4][0] < 10) and  mat[3][3] >=10 ) or (mat[4][0] >= 10):
        #    mat[4].append( mat[4][6])
        #else:
        #    mat[4].append(0)
        #ligne 5-10
        #note5678910 = round((mat[5][0]+mat[6][0]+mat[7][0]+mat[8][0]+mat[9][0]+mat[10][0])/6, 2)
        #if (((note5678910 >= 7 and note5678910 < 10 ) and mat[3][3] >=10) or note5678910 >= 10):
        #    mat[5].append( mat[5][6])
        #else:
        #    mat[5].append(0)

        #ligne 8
        if (((mat[6][0]) >=7 and mat[3][0] < 10) and  mat[1][3] >=10 ) or (mat[6][0] >= 10):
            mat[6][7] = ( mat[6][6] )
        else:
            mat[6][7] = 0
        #ligne 9
        if (((mat[7][0]) >=7 and mat[7][0] < 10) and  mat[1][3] >=10 ) or (mat[7][0] >= 10):
            #mat[7].append( mat[7][6])
            mat[7][7] = ( mat[6][6] )
        else:
            #mat[7].append(0)
            mat[7][7] = 0
        #ligne 10
        if ( ( (mat[8][0]) >=7 and mat[8][0] < 10 ) and  mat[1][3] >=10 ) or ( mat[8][0] >= 10 ):
            #mat[8].append( mat[8][6])
            mat[8][7] = ( mat[8][6] )
        else:
            #mat[8].append(0)
            mat[8][7] = 0
        #ligne 11
        if (((mat[9][0]) >=7 and mat[9][0] < 10) and  mat[1][3] >=10 ) or (mat[9][0] >= 10):
            #mat[9].append( mat[9][6])
            mat[9][7] = ( mat[9][6] )
        else:
            #mat[9].append(0)
            mat[9][7] = 0
        ##UE Transversales
        #ligne 12
        if (((mat[10][0]) >=7 and mat[10][0] < 10) and  mat[1][3] >=10 ) or (mat[10][0] >= 10):
            #mat[10].append( mat[10][6])
            mat[10][7] = ( mat[10][6])
            #mat[10][7] = ( len(mat[10]) )
        else:
            #mat[10].append(0)
            mat[10][7] = 0
        #ligne 13
        #if (((mat[13][0]) >=7 and mat[13][0] < 10) and  mat[12][3] >=10 ) or (mat[13][0] >= 10):
        #    mat[13].append( mat[13][6])
        #else:
        #    mat[13].append(0)

        #ligne 13
        if (((mat[11][0]) >=7 and mat[11][0] < 10) and  mat[12][3] >=10 ) or (mat[11][0] >= 10):
            #mat[11].append( mat[11][6])
            mat[11][7] = ( mat[11][6] )
        else:
            #mat[11].append(0)
            mat[11][7] = 0
        #ligne 14
        #if (((mat[14][0]) >=7 and mat[14][0] < 10) and  mat[12][3] >=10 ) or (mat[14][0] >= 10):
        #    mat[14].append( mat[14][6])
        #else:
        #    mat[14].append(0)

        #ligne 14
        if (((mat[12][0]) >=7 and mat[12][0] < 10) and  mat[12][3] >=10 ) or (mat[12][0] >= 10):
            #mat[12].append( mat[12][6])
            mat[12][7] = ( mat[12][6] )
        else:
            #mat[12].append(0)
            mat[12][7] = ( mat[12][6] )
        ##Ajout total crédit à MAT 13
        #mat[15].append(mat[1][7]+mat[2][7]+mat[3][7]+mat[4][7]+mat[5][7]+mat[11][7]+mat[12][7]+mat[13][7]+mat[14][7])
        #print(mat[2][7],mat[6][7],mat[7][7],mat[8][7],mat[9][7])
        mat[13].append(mat[1][7]+mat[2][7]+mat[6][7]+mat[7][7]+mat[8][7]+mat[9][7]+mat[10][7]+mat[11][7]+mat[12][7])

        #Enregistrement de la moyenne et crédits semestre 4
        e_matri = mat[0]["matricule"]
        student = Etudiant.objects.get(matricule = e_matri)
        student.moyS4 = mat[13][2]
        student.crS4  = mat[13][3]
        student.save()

#MATRICE DE SYNTHESE EPS2
#Il faut ajouter la matrice de CC
def matriceSyntheseEPS2S3(matI, matRa, matcc):
    listeMoyenne = []
    listeTotalMoyenne = []

    matS = copy.deepcopy(matI)

    #print(matRa)

    #i compteur de candidats
    for i in range(len(matI)):
        matR = matRa[i]

        #j compteur de matière
        for j in range(1, len(matR)):

            #print(matR[j])

            if (matR[j] > 0):
                #Les variantes de chaque ligne
                #0 nouvelle note
                matS[i][j][0] = round(matR[j]*0.7 + matcc[i][j]*0.3, 2)

                #2 noteCoefficiée
                matS[i][j][2] = matS[i][j][0] * matS[i][j][1]

                #6 Credit
                matS[i][j][6] = ( matS[i][j][6] if matS[i][j][0] >= 10 else 0 )

                #Au niveau des sommes
                #Ligne1 moyenne
                matS[i][1][3] = round (( matS[i][1][0]*matS[i][1][1] + matS[i][2][0]*matS[i][2][1] )/( matS[i][1][1] + matS[i][2][1] ), 2)

                #Ligne 3 moyenne
                matS[i][3][3] = round (( matS[i][3][0]*matS[i][3][1] + matS[i][4][0]*matS[i][4][1] + matS[i][5][0]*matS[i][5][1] + matS[i][6][0]*matS[i][6][1] + matS[i][7][0]*matS[i][7][1] + matS[i][8][0]*matS[i][8][1] + matS[i][9][0]*matS[i][9][1] + matS[i][10][0]*matS[i][10][1] + matS[i][11][0]*matS[i][11][1] )/( matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]+matS[i][10][1]+matS[i][11][1] ), 2)
                #matS[i][1][3] = 

                #Ligne 12 moyenne
                matS[i][12][3] = round(( matS[i][12][0]*matS[i][12][1] + matS[i][13][0]*matS[i][13][1] + matS[i][14][0]*matS[i][14][1] )/( matS[i][12][1] + matS[i][13][1] + matS[i][14][1] ), 2)

                #Ligne 15 Moyenne Total
                matS[i][15][0] = ( matS[i][1][1]+matS[i][2][1]+matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]+matS[i][10][1]+matS[i][11][1]+matS[i][12][1]+matS[i][13][1]+matS[i][14][1] )

                matS[i][15][1] = round( matS[i][1][0]*matS[i][1][1]+matS[i][2][0]*matS[i][2][1]+matS[i][3][0]*matS[i][3][1]+ matS[i][4][0]*matS[i][4][1]+ matS[i][5][0]*matS[i][5][1]+matS[i][6][0]*matS[i][6][1]+matS[i][7][0]*matS[i][7][1]+ matS[i][8][0]*matS[i][8][1]+ matS[i][9][0]*matS[i][9][1]+ matS[i][10][0]*matS[i][10][1]+matS[i][11][0]*matS[i][11][1]+matS[i][12][0]*matS[i][12][1]+matS[i][13][0]*matS[i][13][1]+matS[i][14][0]*matS[i][14][1] , 2)

                matS[i][15][2] = round ( matS[i][15][1] / matS[i][15][0] , 2)

                matS[i][j].append('Rattrapage')

        #Tableau contenant les nouvelles moyennes
        listeMoyenne.append(matS[i][15][2])
        listeMoyenne.sort(reverse=True)

    #listeMoyenne.sort(reverse=True)
    return matS , listeMoyenne

def matriceSyntheseEPS2S4(matI, matRa, matcc, mats3):
    listeMoyenne = []
    listeTotalMoyenne = []

    matS = copy.deepcopy(matI)

    #i compteur de candidats
    for i in range(len(matI)):
        matR = matRa[i]

        #j compteur de matière
        for j in range(1, len(matR)):
            if (matR[j] > 0):
                #Les variantes de chaque ligne
                #0 nouvelle note
                matS[i][j][0] = round(matR[j]*0.7 + matcc[i][j]*0.3, 2)

                #2 noteCoefficiée
                matS[i][j][2] = matS[i][j][0] * matS[i][j][1]

                #6 Credit
                matS[i][j][6] = ( matS[i][j][6] if matS[i][j][0] >= 10 else 0 )

                #Au niveau des sommes
                #Ligne1 moyenne
                #matS[i][1][3] = round (( matS[i][1][0]*matS[i][1][1] + matS[i][2][0]*matS[i][2][1] )/( matS[i][1][1] + matS[i][2][1] ), 2)

                #Ligne 3 moyenne
                #matS[i][3][3] = round (( matS[i][3][0]*matS[i][3][1] + matS[i][4][0]*matS[i][4][1] + matS[i][5][0]*matS[i][5][1] + matS[i][6][0]*matS[i][6][1] + matS[i][7][0]*matS[i][7][1] + matS[i][8][0]*matS[i][8][1] + matS[i][9][0]*matS[i][9][1] + matS[i][10][0]*matS[i][10][1] + matS[i][11][0]*matS[i][11][1] )/( matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]+matS[i][10][1]+matS[i][11][1] ), 2)
                matS[i][1][3] = round (( matS[i][1][0]*matS[i][1][1] + matS[i][2][0]*matS[i][2][1] + matS[i][3][0]*matS[i][3][1] + matS[i][4][0]*matS[i][4][1] + matS[i][5][0]*matS[i][5][1] + matS[i][6][0]*matS[i][6][1] + matS[i][7][0]*matS[i][7][1] + matS[i][8][0]*matS[i][8][1] + matS[i][9][0]*matS[i][9][1] + matS[i][10][0]*matS[i][10][1] )/( matS[i][1][1]+matS[i][2][1]+ matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]+matS[i][10][1] ), 2)

                #Ligne 12 moyenne
                #matS[i][12][3] = round(( matS[i][12][0]*matS[i][12][1] + matS[i][13][0]*matS[i][13][1] + matS[i][14][0]*matS[i][14][1] )/( matS[i][12][1] + matS[i][13][1] + matS[i][14][1] ), 2)

                #Ligne 13 moyenne
                matS[i][11][3] = round(( matS[i][12][0]*matS[i][12][1] + matS[i][11][0]*matS[i][11][1]  )/( matS[i][12][1] + matS[i][11][1] ), 2)

                #Ligne 15 Moyenne Total
                matS[i][13][0] = ( matS[i][1][1]+matS[i][2][1]+matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]+matS[i][10][1]+matS[i][11][1]+matS[i][12][1])

                matS[i][13][1] = round( matS[i][1][0]*matS[i][1][1]+matS[i][2][0]*matS[i][2][1]+matS[i][3][0]*matS[i][3][1]+ matS[i][4][0]*matS[i][4][1]+ matS[i][5][0]*matS[i][5][1]+matS[i][6][0]*matS[i][6][1]+matS[i][7][0]*matS[i][7][1]+ matS[i][8][0]*matS[i][8][1]+ matS[i][9][0]*matS[i][9][1]+ matS[i][10][0]*matS[i][10][1]+matS[i][11][0]*matS[i][11][1]+matS[i][12][0]*matS[i][12][1] , 2)

                matS[i][13][2] = round ( matS[i][13][1] / matS[i][13][0] , 2)

                matS[i][j].append('Rattrapage')

        #Tableau contenant les nouvelles moyennes
        listeMoyenne.append(matS[i][13][2])
        listeMoyenne.sort(reverse=True)

        listeTotalMoyenne.append( round(((matS[i][13][1] + mats3[i][15][1]) ), 2) ) #/(matS[i][13][0]+mats3[i][15][0])) )
        listeTotalMoyenne.sort(reverse=True)

    #listeMoyenne.sort(reverse=True)
    return matS , listeMoyenne, listeTotalMoyenne

def matriceSynthese(matI, matR, mats3):

    listeMoyenne = []
    listeTotaleMoyenne = []

    #matS = np.array(matI)
    matS = copy.deepcopy(matI)

    #i compteur de candidats
    for i in range(len(matI)):

        #j compteur de matière
        for j in range(1,len(matR[0])):
            #print(matR[i][j])
            if (matR[i][j] > 0):
                #0 nouvelle Note
                matS[i][j][0] = matR[i][j]
                #2 noteCoefficiée
                matS[i][j][2] = matS[i][j][0] * matS[i][j][1]

                #5
                matS[i][j][5] = (matS[i][j][0] >= 10)

                #7
                #matS[i][j][7] = (matS[i][j][6] if matS[i][j][0]>=10 else 0)

                #Au niveau des sommes
                #Ligne 5 moyenne
                matS[i][5][3] =  round( ( matS[i][2][0]*matS[i][2][1]+ matS[i][3][0]*matS[i][3][1]+ matS[i][4][0]*matS[i][4][1]+ matS[i][5][0]*matS[i][5][1])/(matS[i][2][1]+matS[i][3][1]+matS[i][4][1]+matS[i][5][1]), 2 )

                #Ligne 10 moyenne
                matS[i][10][3] = round( ( matS[i][1][0]*matS[i][1][1]+ matS[i][2][0]*matS[i][2][1]+ matS[i][3][0]*matS[i][3][1]+ matS[i][4][0]*matS[i][4][1]+ matS[i][5][0]*matS[i][5][1] +matS[i][6][0]*matS[i][6][1]+matS[i][7][0]*matS[i][7][1]+ matS[i][8][0]*matS[i][8][1]+ matS[i][9][0]*matS[i][9][1]+ matS[i][10][0]*matS[i][10][1] )/( matS[i][1][1]+matS[i][2][1]+matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]+matS[i][10][1] ), 2)

                #Ligne 12 moyenne
                matS[i][12][3] = round( ( matS[i][11][0]*matS[i][11][1]+matS[i][12][0]*matS[i][12][1] ) / ( matS[i][11][1]+matS[i][12][1] ) ,2)


                #Ligne 13 MOYENNE TOTAL
                matS[i][13][0]  = ( matS[i][1][1]+matS[i][2][1]+matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]+matS[i][10][1]+matS[i][11][1]+matS[i][12][1] )

                matS[i][13][1] =  round ( matS[i][1][0]*matS[i][1][1]+ matS[i][2][0]*matS[i][2][1]+ matS[i][3][0]*matS[i][3][1]+ matS[i][4][0]*matS[i][4][1]+ matS[i][5][0]*matS[i][5][1] +matS[i][6][0]*matS[i][6][1]+matS[i][7][0]*matS[i][7][1]+ matS[i][8][0]*matS[i][8][1]+ matS[i][9][0]*matS[i][9][1]+ matS[i][10][0]*matS[i][10][1]+matS[i][11][0]*matS[i][11][1]+matS[i][12][0]*matS[i][12][1] ,2)

                matS[i][13][2] = round (  (matS[i][13][1] / matS[i][13][0]) , 2)

                matS[i][j].append('Rattrapage')

        #tableau contenant les nouvelles moyennes
        listeMoyenne.append(matS[i][13][2])

        #val =
        listeTotaleMoyenne.append( round(((matS[i][13][1] + mats3[i][15][1]) ), 2) ) #/(matS[i][13][0]+mats3[i][15][0])) )
        listeTotaleMoyenne.sort(reverse=True)

        #listeTotaleMoyenne.append(matS[i][13][1])

    listeMoyenne.sort(reverse=True)

    return matS, listeMoyenne, listeTotaleMoyenne


#MATRICE DE SYNTHESE MDS1
#MDS1 S1
def matriceSynthesemds(matI, matR, matSi, matcc): #

    listeMoyenne = []
    listeTotaleMoyenne = []

    totalCredits = 0

    matS = matI

    #i compteur de candidats
    for i in range(len(matI)):

        #j compteur de matiere
        for j in range(1,len(matR[0])):

            #print(matR[i][j])
            if (matR[i][j] > 0):

                #0 nouvelle Note
                matS[i][j][0] = round(matR[i][j]*0.7 + matcc[i][j]*0.3, 2) #matR[i][j] 

                #2 noteCoefficiée
                matS[i][j][2] = matS[i][j][0] * matS[i][j][1]

                #5
                matS[i][j][5] = (matS[i][j][0] >= 10)

                #7
                matS[i][j][7] = (matS[i][j][6] if matS[i][j][0]>=10 else 0)

                #Au niveau des sommes
                #Ligne 1 moyenne
                matS[i][1][3] = round ( ( matS[i][1][0]*matS[i][1][1] + matS[i][2][0]*matS[i][2][1] + matS[i][3][0]*matS[i][3][1] + matS[i][4][0]*matS[i][4][1] )/(  matS[i][1][1]+matS[i][2][1]+matS[i][3][1]+matS[i][4][1] ) , 2 )

                #Ligne 5 moyenne
                matS[i][5][3] = round ( ( matS[i][5][0]*matS[i][5][1] + matS[i][6][0]*matS[i][6][1] + matS[i][7][0]*matS[i][7][1] + matS[i][8][0]*matS[i][8][1] )/(  matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1] ) , 2)

                #Ligne 9 Moyenne
                matS[i][9][3] = round ( ( matS[i][9][0]*matS[i][9][1] + matS[i][10][0]*matS[i][10][1] )/( matS[i][9][1] + matS[i][10][1] ) , 2) 

                #SOMME SOMME TOTALE TOTALE
                matS[i][11][0] =   ( matS[i][1][1]+matS[i][2][1]+matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1] + matS[i][10][1] ) 

                matS[i][11][1] =  round( (matS[i][1][0]*matS[i][1][1] + matS[i][2][0]*matS[i][2][1] + matS[i][3][0]*matS[i][3][1] + matS[i][4][0]*matS[i][4][1]+matS[i][5][0]*matS[i][5][1] + matS[i][6][0]*matS[i][6][1] + matS[i][7][0]*matS[i][7][1] + matS[i][8][0]*matS[i][8][1]+matS[i][9][0]*matS[i][9][1] + matS[i][10][0]*matS[i][10][1]) , 2 )

                matS[i][11][2] =  round( ( matS[i][11][1] / matS[i][11][0] ) , 2)
                
                #Credits Total obtenus
                #totalCredits += matS[i][j][7]

                matS[i][j].append('Rattrapage')

        #Total Crédits Obtenus       
        #matS[i][11].append(totalCredits)

        ##tableau contenant les nouvelles moyennes
        listeMoyenne.append(matS[i][11][2])

        #val = 
        listeTotaleMoyenne.append( round(((matS[i][11][1] + matSi[i][11][1]) ), 2) ) #/(matS[i][13][0]+mats3[i][15][0])) ) 
        listeTotaleMoyenne.sort(reverse=True)
    

    listeMoyenne.sort(reverse=True)


    return matS, listeMoyenne, listeTotaleMoyenne

#MDS1 S2
def matriceSynthesemds1(matI, matR, matSi, matcc): #

    listeMoyenne = []
    listeTotaleMoyenne = []

    totalCredits = 0

    matS = matI

    #i compteur de candidats
    for i in range(len(matI)):

        #j compteur de matiere
        for j in range(1,len(matR[0])):

            #print(matR[i][j])
            if (matR[i][j] > 0):

                #0 nouvelle Note
                #print(matcc[i][j])
                matS[i][j][0] = round(matR[i][j]*0.7 + matcc[i][j]*0.3, 2) #matR[i][j] 

                #2 noteCoefficiée
                matS[i][j][2] = matS[i][j][0] * matS[i][j][1]

                #5
                matS[i][j][5] = (matS[i][j][0] >= 10)

                #7
                matS[i][j][7] = (matS[i][j][6] if matS[i][j][0]>=10 else 0)

                #Au niveau des sommes
                #Ligne 1 moyenne
                matS[i][1][3] = round ( ( matS[i][1][0]*matS[i][1][1] + matS[i][2][0]*matS[i][2][1] + matS[i][3][0]*matS[i][3][1] + matS[i][4][0]*matS[i][4][1] )/(  matS[i][1][1]+matS[i][2][1]+matS[i][3][1]+matS[i][4][1] ) , 2 )

                #Ligne 5 moyenne
                matS[i][5][3] = round ( ( matS[i][5][0]*matS[i][5][1] + matS[i][6][0]*matS[i][6][1] + matS[i][7][0]*matS[i][7][1] + matS[i][8][0]*matS[i][8][1] )/(  matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1] ) , 2)

                #Ligne 9 Moyenne
                matS[i][9][3] = round ( ( matS[i][9][0]*matS[i][9][1] + matS[i][10][0]*matS[i][10][1] )/( matS[i][9][1] + matS[i][10][1] ) , 2) 

                #SOMME SOMME TOTALE TOTALE
                matS[i][11][0] =   ( matS[i][1][1]+matS[i][2][1]+matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1] + matS[i][10][1] ) 

                matS[i][11][1] =  round( (matS[i][1][0]*matS[i][1][1] + matS[i][2][0]*matS[i][2][1] + matS[i][3][0]*matS[i][3][1] + matS[i][4][0]*matS[i][4][1]+matS[i][5][0]*matS[i][5][1] + matS[i][6][0]*matS[i][6][1] + matS[i][7][0]*matS[i][7][1] + matS[i][8][0]*matS[i][8][1]+matS[i][9][0]*matS[i][9][1] + matS[i][10][0]*matS[i][10][1]) , 2 )

                matS[i][11][2] =  round( ( matS[i][11][1] / matS[i][11][0] ) , 2)
                
                #Credits Total obtenus
                #totalCredits += matS[i][j][7]

                matS[i][j].append('Rattrapage')

        #Total Crédits Obtenus       
        #matS[i][11].append(totalCredits)

        ##tableau contenant les nouvelles moyennes
        listeMoyenne.append(matS[i][11][2])

        #val = 
        #listeTotaleMoyenne.append( round(((matS[i][11][1] + matSi[i][11][1]) ), 2) ) #/(matS[i][13][0]+mats3[i][15][0])) ) 
        #listeTotaleMoyenne.sort(reverse=True)
    

    listeMoyenne.sort(reverse=True)


    return matS, listeMoyenne #, listeTotaleMoyenne

#MATRICE DE SYNTHESE EPS1
def matriceSyntheseEPS1(matI, matRa, mats1, matcc):

    listeMoyenne = []
    listeTotalMoyenne = []

    matS = copy.deepcopy(matI)

    #print(matRa)


    #i compteur de candidats
    for i in range(len(matI)):
        matR = matRa[i]

        #j compteur de matière
        for j in range(1, len(matR)):
            #print(matR)
            #print(matR[i][j])
            if (matR[j] > 0):
                #0 nouvelle note
                matS[i][j][0] = round(matR[j]*0.7 + matcc[i][j]*0.3, 2)

                #2 noteCoefficiée
                matS[i][j][2] = matS[i][j][0] * matS[i][j][1]

                #6
                #credit_count = ( matS[i][j][6] if matS[i][j][0] >= 10 else 0 )
                matS[i][j][6] = ( matS[i][j][6] if matS[i][j][0] >= 10 else 0 )
                #matS[i][j].append(credit_count)

                #Au niveau des sommes
                #Ligne 1 moyenne
                matS[i][1][3] = round (( matS[i][1][0]*matS[i][1][1] + matS[i][2][0]*matS[i][2][1] )/( matS[i][1][1] + matS[i][2][1] ), 2)

                #Ligne 3 moyenne
                matS[i][3][3] = round( ( matS[i][3][0]*matS[i][3][1] + matS[i][4][0]*matS[i][4][1] + matS[i][5][0]*matS[i][5][1] + matS[i][6][0]*matS[i][6][1] + matS[i][7][0]*matS[i][7][1] + matS[i][8][0]*matS[i][8][1] + matS[i][9][0]*matS[i][9][1] )/( matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]), 2)

                #Ligne 10 moyenne
                matS[i][10][3] = round( ( matS[i][10][0]*matS[i][10][1] + matS[i][11][0]*matS[i][11][1] + matS[i][12][0]*matS[i][12][1] )/( matS[i][10][1] + matS[i][11][1] + matS[i][12][1] ), 2)


                #Ligne 13 Moyenne TOTAL
                matS[i][13][0] = ( matS[i][1][1]+matS[i][2][1]+matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]+matS[i][10][1]+matS[i][11][1]+matS[i][12][1] )

                matS[i][13][1] = round( matS[i][1][0]*matS[i][1][1]+matS[i][2][0]*matS[i][2][1]+matS[i][3][0]*matS[i][3][1]+ matS[i][4][0]*matS[i][4][1]+ matS[i][5][0]*matS[i][5][1]+matS[i][6][0]*matS[i][6][1]+matS[i][7][0]*matS[i][7][1]+ matS[i][8][0]*matS[i][8][1]+ matS[i][9][0]*matS[i][9][1]+ matS[i][10][0]*matS[i][10][1]+matS[i][11][0]*matS[i][11][1]+matS[i][12][0]*matS[i][12][1] , 2)

                matS[i][13][2] = round (  (matS[i][13][1] / matS[i][13][0]) , 2)

                matS[i][j].append('Rattrapage')

        #tableau contenant les nouvelles moyennes
        listeMoyenne.append(matS[i][13][2])

        listeTotalMoyenne.append( round( (matS[i][13][1] + mats1[i][13][1]) , 2) )
        listeTotalMoyenne.sort(reverse=True)


    #listeMoyenne.sort(reverse=True)
    return matS , listeMoyenne, listeTotalMoyenne

#MATRICE DE SYNTHESE EPS1
def matriceSyntheseEPS1PV(matI, matRa, matcc):

    listeMoyenne = []
    listeTotalMoyenne = []

    matS = copy.deepcopy(matI)

    #print(matRa[0])
        #print(matRa[1])
        #print(matRa[2])

    #i compteur de candidats
    for i in range(len(matI)):
        matR = matRa[i]

        #j compteur de matière
        for j in range(1, len(matR)):
            #print(matR)
            #print(matR[i][j])
            if (matR[j] > 0):
                #0 nouvelle note
                matS[i][j][0] = round(matR[j]*0.7 + matcc[i][j]*0.3, 2)

                #2 noteCoefficiée
                matS[i][j][2] = matS[i][j][0] * matS[i][j][1]

                #6
                #credit_count = ( matS[i][j][6] if matS[i][j][0] >= 10 else 0 )
                matS[i][j][6] = ( matS[i][j][6] if matS[i][j][0] >= 10 else 0 )
                #matS[i][j].append(credit_count)

                #Au niveau des sommes
                #Ligne 1 moyenne
                matS[i][1][3] = round (( matS[i][1][0]*matS[i][1][1] + matS[i][2][0]*matS[i][2][1] )/( matS[i][1][1] + matS[i][2][1] ), 2)

                #Ligne 3 moyenne
                matS[i][3][3] = round( ( matS[i][3][0]*matS[i][3][1] + matS[i][4][0]*matS[i][4][1] + matS[i][5][0]*matS[i][5][1] + matS[i][6][0]*matS[i][6][1] + matS[i][7][0]*matS[i][7][1] + matS[i][8][0]*matS[i][8][1] + matS[i][9][0]*matS[i][9][1] )/( matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]), 2)

                #Ligne 10 moyenne
                matS[i][10][3] = round( ( matS[i][10][0]*matS[i][10][1] + matS[i][11][0]*matS[i][11][1] + matS[i][12][0]*matS[i][12][1] )/( matS[i][10][1] + matS[i][11][1] + matS[i][12][1] ), 2)


                #Ligne 13 Moyenne TOTAL
                matS[i][13][0] = ( matS[i][1][1]+matS[i][2][1]+matS[i][3][1]+matS[i][4][1]+matS[i][5][1]+matS[i][6][1]+matS[i][7][1]+matS[i][8][1]+matS[i][9][1]+matS[i][10][1]+matS[i][11][1]+matS[i][12][1] )

                matS[i][13][1] = round( matS[i][1][0]*matS[i][1][1]+matS[i][2][0]*matS[i][2][1]+matS[i][3][0]*matS[i][3][1]+ matS[i][4][0]*matS[i][4][1]+ matS[i][5][0]*matS[i][5][1]+matS[i][6][0]*matS[i][6][1]+matS[i][7][0]*matS[i][7][1]+ matS[i][8][0]*matS[i][8][1]+ matS[i][9][0]*matS[i][9][1]+ matS[i][10][0]*matS[i][10][1]+matS[i][11][0]*matS[i][11][1]+matS[i][12][0]*matS[i][12][1] , 2)

                matS[i][13][2] = round (  (matS[i][13][1] / matS[i][13][0]) , 2)

                matS[i][j].append('Rattrapage')

        #tableau contenant les nouvelles moyennes
        listeMoyenne.append(matS[i][13][2])

        #listeTotalMoyenne.append( round( (matS[i][13][1] + mats1[i][13][1]) , 2) )
        #listeTotalMoyenne.sort(reverse=True)


    #listeMoyenne.sort(reverse=True)
    return matS , listeMoyenne, listeTotalMoyenne









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

def epurationCC(b):
    for i in range(len(b)):
        tmp = b[i]["note_cc"]
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


def deliberation(request):

    #EPS1
    infoStaps1 = list(Etudiant.objects.filter(niveau=1, filiere="STAPS").values('matricule','nom','prenom','moyS1', 'crS1', 'moyS2', 'crS2', 'niveau'))

    #MDS1
    infoMds1 = list(Etudiant.objects.filter(niveau=1, filiere="GESTION").values('matricule','nom','prenom','moyS1', 'crS1', 'moyS2', 'crS2', 'niveau'))


    #EPS2
    infoStaps2 = list(Etudiant.objects.filter(niveau=2, filiere="STAPS").values('matricule','nom','prenom','moyS1', 'crS1', 'moyS2', 'crS2', 'niveau'))


    #MDS2

    #MDS3

    #STAPS3



    template = loader.get_template('bulletin/home.html')
    return HttpResponse(template.render({}, request))

