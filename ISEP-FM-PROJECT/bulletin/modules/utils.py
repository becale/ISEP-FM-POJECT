
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

def epurationSN(b):
    for i in range(len(b)):
        tmp = b[i]["note_sn"]
        b[i] = tmp

    #b = sorted(b, reverse=True)
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

    #EPS2
    infoStaps2 = list(Etudiant.objects.filter(niveau=2, filiere="STAPS").values('matricule','nom','prenom','moyS3', 'crS3', 'moyS4', 'crS4', 'niveau', 'redoublant'))
    for etudiant in infoStaps2:
        #print(etudiant)
        student = Etudiant.objects.get(matricule = etudiant["matricule"])

        if (etudiant["moyS3"] == None or  etudiant["moyS4"] == None):
            break

        if ( (((etudiant["moyS3"] + etudiant["moyS4"])/2) >= 10 ) and (etudiant["redoublant"] == 0 ) ):
            #etudiant["niveau"] = str(int(etudiant["niveau"]) + 1)
            student.niveau = str(int(3))
        else:
            #etudiant["redoublant"] = 1
            student.redoublant = 1

        student.save()

    #EPS1
    infoStaps1 = list(Etudiant.objects.filter(niveau=1, filiere="STAPS").values('matricule','nom','prenom','moyS1', 'crS1', 'moyS2', 'crS2', 'niveau'))
    for etudiant in infoStaps1:
        #student_matri = etudiant["matricule"]
        student = Etudiant.objects.get(matricule = etudiant["matricule"])

        if (etudiant["moyS1"] == None or  etudiant["moyS2"] == None):
            break

        if ( ((etudiant["moyS1"] + etudiant["moyS2"])/2) >= 10 ):
            student.niveau = str(2)

        else:
            #etudiant["redoublant"] = 1
            student.redoublant = 1

        student.save()

        print(student)



    #MDS1
    infoMds1 = list(Etudiant.objects.filter(niveau=1, filiere="GESTION").values('matricule','nom','prenom','moyS1', 'crS1', 'moyS2', 'crS2', 'niveau'))
    for etudiant in infoMds1:
        #student_matri = etudiant["matricule"]
        student = Etudiant.objects.get(matricule = etudiant["matricule"])

        if (etudiant["moyS1"] == None or  etudiant["moyS2"] == None):
            break

        if ( ((etudiant["moyS1"] + etudiant["moyS2"])/2) >= 10 ):
            #etudiant["niveau"] = str(int(etudiant["niveau"]) + 1)
            student.niveau = str(2)
        else:
            #etudiant["redoublant"] = 1
            student.redoublant = 1

        student.save()


    #MDS2

    #MDS3

    #STAPS3



    template = loader.get_template('bulletin/home.html')
    return HttpResponse(template.render({}, request))

