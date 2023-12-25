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

