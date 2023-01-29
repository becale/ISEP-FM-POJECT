from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse

# Create your views here.

def home(request):
    
    template = loader.get_template('bulletin/home.html')
    return HttpResponse(template.render({}, request))

def bulletin(request):
    template = loader.get_template('bulletin/bulletin.html')
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
        #data = list(data.items())
    
    key, values = extract(data)
    
    saveData(key,values)
    text = "<html><body> %s </body></html>" % values
    return HttpResponse(text)
    #return JsonResponse(keyValue, safe=False)


def test(request):
    return render(request, 'bulletin/BulletinTemplate/bulletin1.html')

"""
    Requête Bulletin
"""
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
        
        for i in range(1,len(key)):
            setKey = key[i]
            if(setKey[0]=="CC"):
                natureEvaluation_ = 'Contrôle_Continue'
            elif(setKey[0]=="SN"):
                natureEvaluation_ = 'Session_Normale'
            matricule = setKey[1]
            codeUe = setKey[2]
            note_ = values[i]

            etudiant_Query = Etudiant.objects.filter(matricule=matricule)#.values('nom')
            etudiant = etudiant_Query[0]

            ue_Query = UniteEnseignement.objects.filter(code_UE=codeUe)#.values('id')
            ue = ue_Query[0]

            evaluation = Evaluation(natureEvaluation=natureEvaluation_, note=note_, etudiant=etudiant, uniteEnseignement=ue)
            evaluation.save()

def extract(a):
    key = list(a.keys())
    value = list(a.values())
    
    for i in range(len(key)):
        k = key[i]
        key[i] = k.split()
        
        """val = value[i]
        val1 = val[0]
        value[i] = val1"""
        
    return (key, value)

"""
def saveData(key, values):
    if (len(key) == len(values)):
        
        for i in range(1,len(key)):
            setKey = key[i]
            if(setKey[0]=="CC"):
                natureEvaluation = 'Contrôle_Continue'
            elif(setKey[0]=="SN"):
                natureEvaluation = 'Session_Normale'
            matricule = setKey[1]
            codeUe = setKey[2]
            note = int(values[i])

"""

"""
def extract(dicto):
    couple = ()
    big = ()
    for key,value in dicto.items():
        couple_list = list(couple)
        couple_list.append(key)
        couple_list.append(value)
        couple = tuple(couple_list)
        big_list = list(big)
        big_list.append(couple)
        big = tuple(big_list)
        couple = ()
    return big

def splitVar(a):
    big = ()
    i=1
    for i in range(len(a)):
        key , val = a[i]
        b = key.split()
        c = val
        
        a_list = list(a[i])
        a_list[0] =b
        a_list[1] = c
        
        big_list = list(big)
        big_list.append(a_list)
        big = tuple(big_list)
    return big
"""

#Génération de bulletin
def GenerateBulletin (request):
    bulletin = {
        'etudiant' : {
            'id': "",
            'filiere':"",
            'specialite':"",
            'nom': "",
            'prenom':"",
            'Nationalité':"",
            'grade':"",
            'annee_academique':"",
            'lieu_naissance':"",
            'niveau':"",
        },

        'matiere':{
            'groupe1':{
                "intitulé":"",
                "ue":{}

            },
            'groupe2':{

            },
            'groupe3':{

            }
        }
    }


