from bulletin.models import *



#PV EPS1 SEMESTRE1
def PVEPS1s1():

    UeNomCode = list( UniteEnseignement.objects.filter(semestre_id = 1, filiere="STAPS").values("code_UE","intitule_UE", "semestre_id", "nombre_credit") )

    infoEtudiantSTAPS1 =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))

    coefS1STAPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("coefficient"))
    coefS1STAPS1 = bulletin.views.epurationCoef(coefS1STAPS1)

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
    val88 = {
        'nombre': 0,
        'pourcentage': 0,
    }
    val888 = {
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

    e115fo = {
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
    e115at = {
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
    EPS111 = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS111cc = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS111sn = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort111 = epurationTriCroissant(EPS111)

    EPS112 = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS112cc = list(Evaluation.objects.filter(uniteEnseignement_id=51,  natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS112sn = list(Evaluation.objects.filter(uniteEnseignement_id=51,  natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort112 = epurationTriCroissant(EPS112)

    EPS113 = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS113cc = list(Evaluation.objects.filter(uniteEnseignement_id=52,  natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS113sn = list(Evaluation.objects.filter(uniteEnseignement_id=52,  natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort113 = epurationTriCroissant(EPS113)

    EPS114 = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS114cc = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS114sn = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort114 = epurationTriCroissant(EPS114)

    EPS115a = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS115acc = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS115asn = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort115a = epurationTriCroissant(EPS115a)

    EPS115b = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS115bcc = list(Evaluation.objects.filter(uniteEnseignement_id=55,  natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS115bsn = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort115b = epurationTriCroissant(EPS115b)

    EPS115j = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS115jcc = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS115jsn = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort115j = epurationTriCroissant(EPS115j)

    EPS115l = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS115lcc = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS115lsn = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort115l = epurationTriCroissant(EPS115l)

    foot115 = list(Evaluation.objects.filter(uniteEnseignement_id=136, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    foot115cc = list(Evaluation.objects.filter(uniteEnseignement_id=136, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    foot115sn = list(Evaluation.objects.filter(uniteEnseignement_id=136, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sortfoot115 = epurationTriCroissant(foot115)

    athl115 = list(Evaluation.objects.filter(uniteEnseignement_id=137, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    athl115cc = list(Evaluation.objects.filter(uniteEnseignement_id=137, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    athl115sn = list(Evaluation.objects.filter(uniteEnseignement_id=137, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sortath115 = epurationTriCroissant(athl115)

    EPS116 = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS116cc = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS116sn = list(Evaluation.objects.filter(uniteEnseignement_id=58,  natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort116 = epurationTriCroissant(EPS116)

    EPS117 = list(Evaluation.objects.filter(uniteEnseignement_id=59,  natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS117cc = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS117sn = list(Evaluation.objects.filter(uniteEnseignement_id=59,  natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort117 = epurationTriCroissant(EPS117)

    EPS118 = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS118cc = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS118sn = list(Evaluation.objects.filter(uniteEnseignement_id=60,  natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort118 = epurationTriCroissant(EPS118)

    EPS119 = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_Examen'))
    EPS119cc = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_cc'))
    EPS119sn = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='EXAMEN', date_Examen=dateExamen[0]['date_SN']).values('note_sn'))
    sort119 = epurationTriCroissant(EPS119)


    staps1 = []
    staps1Moyenne = []
    listeMatrice = [ ]

    for j in range( len(infoEtudiantSTAPS1) ):

        matrice = [
            infoEtudiantSTAPS1[j],

            #1 EPS111
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

            #2 EPS112
            [ EPS112[j], coefS1STAPS1[1], EPS112[j]*coefS1STAPS1[1], "MOYENNE", sort112.index(EPS112[j])+1,(EPS112[j]>=10), creditS1STAPS1[1], creditS1STAPS1[1] if (EPS112[j]>=10) else 0, EPS112cc[j]['note_cc'], EPS112sn[j]['note_sn'] ],

            #3 EPS113
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

            #4 EPS114
            [ EPS114[j],  coefS1STAPS1[3], EPS114[j]*coefS1STAPS1[3], "MOYENNE", sort114.index(EPS114[j])+1, (EPS114[j] >=10), creditS1STAPS1[3], creditS1STAPS1[3] if (EPS114[j] >=10) else 0, EPS114cc[j]['note_cc'], EPS114sn[j]['note_sn']  ],

            #5 EPS115 Volley
            [ EPS115a[j], coefS1STAPS1[4], EPS115a[j]*coefS1STAPS1[4], "MOYENNE", sort115a.index(EPS115a[j])+1, (EPS115a[j] >=10), creditS1STAPS1[4], creditS1STAPS1[4] if (EPS115a[j] >=10) else 0, EPS115acc[j]['note_cc'], EPS115asn[j]['note_sn'] ], #crédits

            #6 EPS115 Danse
            [ EPS115b[j], coefS1STAPS1[5], EPS115b[j]*coefS1STAPS1[5], "MOYENNE", sort115b.index(EPS115b[j])+1, (EPS115b[j] >=10), creditS1STAPS1[5], creditS1STAPS1[5] if (EPS115b[j] >=10) else 0, EPS115bcc[j]['note_cc'], EPS115bsn[j]['note_sn'] ],
            
            #7 EPS115 GYMNASTIQUE
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

            #8 EPS115 LUTTE
            [ 
                EPS115l[j]
                , coefS1STAPS1[7]
                , EPS115l[j]*coefS1STAPS1[7]
                , "MOYENNE"
                , sort115l.index(EPS115l[j])+1
                , (EPS115l[j] >=10)
                , creditS1STAPS1[7]
                , creditS1STAPS1[7] if ((EPS115a[j]+EPS115b[j]+EPS115j[j]+EPS115l[j]) >=40) else 0
                , EPS115lcc[j]['note_cc']
                , EPS115lsn[j]['note_sn']
            ],

            #9 EPS115 FOOT
            [
                foot115[j]
                , coefS1STAPS1[7]
                , foot115[j]*coefS1STAPS1[7]
                , "MOYENNE"
                , sortfoot115.index(foot115[j])+1
                , (foot115[j] >=10)
                , creditS1STAPS1[7]
                , creditS1STAPS1[7] if ((EPS115a[j]+EPS115b[j]+EPS115j[j]+EPS115l[j]+foot115[j]+athl115[j]) >=60) else 0
                , foot115cc[j]['note_cc']
                , foot115sn[j]['note_sn']
            ],

            #10 EPS115 ATHLETISME
            [
                athl115[j]
                , coefS1STAPS1[7]
                , athl115[j]*coefS1STAPS1[7]
                , "MOYENNE"
                , sortath115.index(athl115[j])+1
                , (athl115[j] >=10)
                , creditS1STAPS1[7]
                , creditS1STAPS1[7] if ((EPS115a[j]+EPS115b[j]+EPS115j[j]+EPS115l[j]+foot115[j]+athl115[j]) >=60) else 0
                , athl115cc[j]['note_cc']
                , athl115sn[j]['note_sn']
            ],

            #11 EPS116 
            [ EPS116[j],  coefS1STAPS1[8], EPS116[j]*coefS1STAPS1[8], "MOYENNE", sort116.index(EPS116[j])+1, (EPS116[j] >=10), creditS1STAPS1[8], creditS1STAPS1[8] if (EPS116[j] >=10) else 0, EPS116cc[j]['note_cc'], EPS116sn[j]['note_sn'] ],
            
            #12 EPS117 
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

            #13 EPS118
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

            #14 EPS119
            [ EPS119[j], coefS1STAPS1[11], EPS119[j]*coefS1STAPS1[11], "MOYENNE", sort119.index(EPS119[j])+1, (EPS119[j] >=10), creditS1STAPS1[11], creditS1STAPS1[11] if (EPS119[j] >=10) else 0, EPS119cc[j]['note_cc'], EPS119sn[j]['note_sn'] ],

            #15 RESULTAT
            [
                ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+  coefS1STAPS1[7]+coefS1STAPS1[7]  +coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ), #coefsomme

                round( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115j[j]*coefS1STAPS1[6]+EPS115l[j]*coefS1STAPS1[7]+ foot115[j]*coefS1STAPS1[7]+athl115[j]*coefS1STAPS1[7]  +EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11], 2),

                round(( EPS111[j]*coefS1STAPS1[0]+EPS112[j]*coefS1STAPS1[1]+EPS113[j]*coefS1STAPS1[2]+EPS114[j]*coefS1STAPS1[3]+EPS115a[j]*coefS1STAPS1[4]+EPS115b[j]*coefS1STAPS1[5]+EPS115j[j]*coefS1STAPS1[6]+EPS115l[j]*coefS1STAPS1[7]+ foot115[j]*coefS1STAPS1[7]+athl115[j]*coefS1STAPS1[7]  +EPS116[j]*coefS1STAPS1[8]+EPS117[j]*coefS1STAPS1[9]+EPS118[j]*coefS1STAPS1[10]+EPS119[j]*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+ coefS1STAPS1[7]+coefS1STAPS1[7] +coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2 ),
            ]
        ]

        staps1Moyenne.append(matrice[15][2])#(matrice[13][2])

        #EPSCreditCount(matrice)
        listeMatrice.append(matrice)

        #ESPACE INFOS LISTE DES ETUDIANTS ALLANT AU RATTRAPAGE
        

        staps1Moyenne.sort(reverse=True)
        moy = stat.mean(staps1Moyenne)
        moy = round(moy, 2)
        session = dateExamen[0]['date_SN'] #session = 'Janvier 2023'

        filiere = 'STAPS'

    #EPS2CreditCountS3(listeMatrice)
    EPS2CreditCountS3PV(listeMatrice)

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


                foot115cc[j]["note_cc"],

                athl115cc[j]["note_cc"],


                EPS116cc[j]["note_cc"],

                EPS117cc[j]["note_cc"],

                EPS118cc[j]["note_cc"],

                EPS119cc[j]["note_cc"],
            ]
            listeMatriceS1EpsCC.append(matriceS1EpsCC)

########################################################### PV SEMESTRE 1 EPS RATTRAPAGE ############################################################################################################################
    EPS111R = list(Evaluation.objects.filter(uniteEnseignement_id=50, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort111R = epurationRattrapage(EPS111R)

    EPS112R = list(Evaluation.objects.filter(uniteEnseignement_id=51, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort112R = epurationRattrapage(EPS112R)

    EPS113R = list(Evaluation.objects.filter(uniteEnseignement_id=52, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort113R = epurationRattrapage(EPS113R)

    EPS114R = list(Evaluation.objects.filter(uniteEnseignement_id=53, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort114R = epurationRattrapage(EPS114R)

    EPS115aR = list(Evaluation.objects.filter(uniteEnseignement_id=54, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort115aR = epurationRattrapage(EPS115aR)

    EPS115bR = list(Evaluation.objects.filter(uniteEnseignement_id=55, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort115bR = epurationRattrapage(EPS115bR) 

    EPS115jR = list(Evaluation.objects.filter(uniteEnseignement_id=56, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort115jR = epurationRattrapage(EPS115jR)

    EPS115lR = list(Evaluation.objects.filter(uniteEnseignement_id=57, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort115lR = epurationRattrapage(EPS115lR)

    foot115R = list(Evaluation.objects.filter(uniteEnseignement_id=136, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    foot115R = epurationRattrapage(foot115R)
    
    athl115R = list(Evaluation.objects.filter(uniteEnseignement_id=137, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    athl115R = epurationRattrapage(athl115R)

    EPS116R = list(Evaluation.objects.filter(uniteEnseignement_id=58, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort116R = epurationRattrapage(EPS116R)

    EPS117R = list(Evaluation.objects.filter(uniteEnseignement_id=59, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort117R = epurationRattrapage(EPS117R)

    EPS118R = list(Evaluation.objects.filter(uniteEnseignement_id=60, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
    sort118R = epurationRattrapage(EPS118R)

    EPS119R = list(Evaluation.objects.filter(uniteEnseignement_id=61, natureEvaluation='RATTRAPAGE', date_Rattrapage=dateExamen[0]['date_RT']).values('note_rattrapage'))
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


            foot115R[j],

            athl115R[j],


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


            ( round( foot115R[j]*0.7 + foot115cc[j]['note_cc']*0.3, 2) if (foot115R[j] > 0) else foot115[j] ) ,

            ( round( athl115R[j]*0.7 + athl115cc[j]['note_cc']*0.3, 2) if (athl115R[j] > 0) else athl115[j] ) ,


            ( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] ) ,

            ( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] ) ,

            ( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] ) ,

            ( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] ) ,

        ]
        listeMatriceRs1EPS1.append(matriceRs1EPS1)
        listeMatriceRs1EPS1ex.append(matriceRs1EPS1ex)

########################################################### PV SEMESTRE 1 EPS SYNTHESE   ############################################################################################################################

    listeMatrices1eps = []
    staps1Moyenne = []

    for j in range( len(infoEtudiantSTAPS1) ):

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
                    , "RATTRAPAGE" if (EPS111R[j] > 0) else None
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
                    ,"RATTRAPAGE" if (EPS112R[j] > 0) else None
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
                    ,"RATTRAPAGE" if (EPS113R[j] > 0) else None
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
                    ,"RATTRAPAGE" if (EPS114R[j] > 0) else None
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
                    ,"RATTRAPAGE" if (EPS115aR[j] > 0) else None
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
                    ,"RATTRAPAGE" if (EPS115bR[j] > 0) else None
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
                    ,"RATTRAPAGE" if (EPS115jR[j] > 0) else None
                ],

                [ 
                    ( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )
                    , coefS1STAPS1[7]
                    , ( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]
                    , "MOYENNE"
                    #, sort115l.index(EPS115l[j])+1
                    , (( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] ) >=10)
                    , creditS1STAPS1[7]
                    #, creditS1STAPS1[7] if ((( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )+( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )) >=40) else 0
                    ,creditS1STAPS1[7] if ( ( ( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )+( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )+( round( foot115R[j]*0.7 + foot115cc[j]['note_cc']*0.3, 2) if (foot115R[j] > 0) else foot115[j] )+( round( athl115R[j]*0.7 + athl115cc[j]['note_cc']*0.3, 2) if (athl115R[j] > 0) else athl115[j] )) >=40) else 0
                    , EPS115lcc[j]['note_cc']
                    , EPS115lsn[j]['note_sn'] 
                    ,"RATTRAPAGE" if (EPS115lR[j] > 0) else None
                ],

                ##Foot
                [ 
                    ( round( foot115[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (foot115[j] > 0) else EPS115l[j] )
                    , coefS1STAPS1[7]
                    , ( round( foot115[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (foot115[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]
                    , "MOYENNE"
                    #, sort115l.index(EPS115l[j])+1
                    , (( round( foot115[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (foot115[j] > 0) else EPS115l[j] ) >=10)
                    , creditS1STAPS1[7]
                    , creditS1STAPS1[7] if ( ( ( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )+( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )+( round( foot115R[j]*0.7 + foot115cc[j]['note_cc']*0.3, 2) if (foot115R[j] > 0) else foot115[j] )+( round( athl115R[j]*0.7 + athl115cc[j]['note_cc']*0.3, 2) if (athl115R[j] > 0) else athl115[j] )) >=40) else 0
                    , foot115cc[j]['note_cc']
                    , foot115sn[j]['note_sn'] 
                    ,"RATTRAPAGE" if (foot115R[j] > 0) else None
                ],

                ##Athl
                [ 
                    ( round( athl115R[j]*0.7 + athl115cc[j]['note_cc']*0.3, 2) if (athl115R[j] > 0) else athl115[j] )
                    ,  coefS1STAPS1[7]
                    , ( round( athl115R[j]*0.7 + athl115cc[j]['note_cc']*0.3, 2) if (athl115R[j] > 0) else athl115[j] )*coefS1STAPS1[7]
                    , "MOYENNE"
                    #, sort116.index(athl115[j])+1
                    , (( round( athl115R[j]*0.7 + athl115cc[j]['note_cc']*0.3, 2) if (athl115R[j] > 0) else athl115[j] ) >=10)
                    , creditS1STAPS1[7]
                    , creditS1STAPS1[7] if (( round( athl115R[j]*0.7 + athl115cc[j]['note_cc']*0.3, 2) if (athl115R[j] > 0) else athl115[j] ) >=10) else 0
                    , athl115cc[j]['note_cc']
                    , athl115sn[j]['note_sn'] 
                    ,"RATTRAPAGE" if (athl115R[j] > 0) else None
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
                    ,"RATTRAPAGE" if (EPS116R[j] > 0) else None
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
                    ,"RATTRAPAGE" if (EPS117R[j] > 0) else None
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
                    ,"RATTRAPAGE" if (EPS118R[j] > 0) else None
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
                    ,"RATTRAPAGE" if (EPS119R[j] > 0) else None
                ],

                [ 
                    ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[7]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11] ), #coefsomme

                    round( ( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )*coefS1STAPS1[0]+( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )*coefS1STAPS1[1]+( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] ) *coefS1STAPS1[2]+( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )*coefS1STAPS1[3]+( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )*coefS1STAPS1[4]+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )*coefS1STAPS1[5]+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )*coefS1STAPS1[6]+ ( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7] + ((( round( foot115R[j]*0.7 + foot115cc[j]['note_cc']*0.3, 2) if (foot115R[j] > 0) else foot115[j] )*coefS1STAPS1[1] + round( athl115R[j]*0.7 + athl115cc[j]['note_cc']*0.3, 2) if (athl115R[j] > 0) else athl115[j] )*coefS1STAPS1[1] )  +  ( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )*coefS1STAPS1[8]+( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] )*coefS1STAPS1[9]+( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )*coefS1STAPS1[10]+( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )*coefS1STAPS1[11], 2),

                    round(( ( round( EPS111R[j]*0.7 + EPS111cc[j]['note_cc']*0.3, 2) if (EPS111R[j] > 0) else EPS111[j] )*coefS1STAPS1[0]+( round( EPS112R[j]*0.7 + EPS112cc[j]['note_cc']*0.3, 2) if (EPS112R[j] > 0) else EPS112[j] )*coefS1STAPS1[1]+( round( EPS113R[j]*0.7 + EPS113cc[j]['note_cc']*0.3, 2) if (EPS113R[j] > 0) else EPS113[j] ) *coefS1STAPS1[2]+( round( EPS114R[j]*0.7 + EPS114cc[j]['note_cc']*0.3, 2) if (EPS114R[j] > 0) else EPS114[j] )*coefS1STAPS1[3]+( round( EPS115aR[j]*0.7 + EPS115acc[j]['note_cc']*0.3, 2) if (EPS115aR[j] > 0) else EPS115a[j] )*coefS1STAPS1[4]+( round( EPS115bR[j]*0.7 + EPS115bcc[j]['note_cc']*0.3, 2) if (EPS115bR[j] > 0) else EPS115b[j] )*coefS1STAPS1[5]+( round( EPS115jR[j]*0.7 + EPS115jcc[j]['note_cc']*0.3, 2) if (EPS115jR[j] > 0) else EPS115j[j] )*coefS1STAPS1[6] + ((( round( foot115R[j]*0.7 + foot115cc[j]['note_cc']*0.3, 2) if (foot115R[j] > 0) else foot115[j] )*coefS1STAPS1[1] + round( athl115R[j]*0.7 + athl115cc[j]['note_cc']*0.3, 2) if (athl115R[j] > 0) else athl115[j] )*coefS1STAPS1[1] ) + ( round( EPS115lR[j]*0.7 + EPS115lcc[j]['note_cc']*0.3, 2) if (EPS115lR[j] > 0) else EPS115l[j] )*coefS1STAPS1[7]+( round( EPS116R[j]*0.7 + EPS116cc[j]['note_cc']*0.3, 2) if (EPS116R[j] > 0) else EPS116[j] )*coefS1STAPS1[8]+( round( EPS117R[j]*0.7 + EPS117cc[j]['note_cc']*0.3, 2) if (EPS117R[j] > 0) else EPS117[j] )*coefS1STAPS1[9]+( round( EPS118R[j]*0.7 + EPS118cc[j]['note_cc']*0.3, 2) if (EPS118R[j] > 0) else EPS118[j] )*coefS1STAPS1[10]+( round( EPS119R[j]*0.7 + EPS119cc[j]['note_cc']*0.3, 2) if (EPS119R[j] > 0) else EPS119[j] )*coefS1STAPS1[11] ) / ( coefS1STAPS1[0]+coefS1STAPS1[1]+coefS1STAPS1[2]+coefS1STAPS1[3]+coefS1STAPS1[4]+coefS1STAPS1[5]+coefS1STAPS1[6]+coefS1STAPS1[7]+coefS1STAPS1[7]+coefS1STAPS1[7]+coefS1STAPS1[8]+coefS1STAPS1[9]+coefS1STAPS1[10]+coefS1STAPS1[11]), 2 ),
                ]
        ]
                
        staps1Moyenne.append(matriceS1EPS[15][2])

        #DECOMPTE CREDITS
        EPSCreditCount(matriceS1EPS)

        listeMatrices1eps.append(matriceS1EPS)
    

    #Décompte de crédit
    #EPSCreditCount22(listeMatriceS1EpsSynthese)
    #EPSCreditCount(listeMatrices1eps)
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

    val88['pourcentage']= round(((val88['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(foot115)):
        if foot115[i] >= 10:
            val88['nombre']+=1

    val888['pourcentage']= round(((val888['nombre']/ len(infoEtudiantSTAPS1))*100), 2)
    for i in range (len(athl115)):
        if athl115[i] >= 10:
            val888['nombre']+=1


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

    statMention(foot115,e115fo)
    pourcentageMention(e115fo, len(infoEtudiantSTAPS1))

    statMention(athl115,e115at)
    pourcentageMention(e115at, len(infoEtudiantSTAPS1))

    statMention(EPS116,e116)
    pourcentageMention(e116, len(infoEtudiantSTAPS1))

    statMention(EPS117,e117)
    pourcentageMention(e117, len(infoEtudiantSTAPS1))

    statMention(EPS118,e118)
    pourcentageMention(e118, len(infoEtudiantSTAPS1))

    statMention(EPS119,e119)
    pourcentageMention(e119, len(infoEtudiantSTAPS1))


    UEStats = [val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12 , val88, val888]
    UEstats_mention = [e111, e112, e113, e114, e115a, e115b, e115j, e115l, e116, e117, e118, e119, e115fo, e115at ]

    #La liste de matrice qui contient les décomptes de crédit(listeMatriceS1EpsSynthese[0])          

    lundi,mardi,mercredi = ([], [], [])
    semestre1MDS = [filiere, listeMatrice, staps1Moyenne, moy, session , creditS1STAPS1, UEStats, UEstats_mention, listeMatriceRs1EPS1 ,listeMatrices1eps , mercredi, dateExamen, UeNomCode]#, listeMatriceRs1EPS1, listeMatriceS1EpsSynthese[0],  listeMatriceS1EpsSynthese ] #, listeMatrices1eps

    return (semestre1MDS)

