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
    etudiantEVE = list(Etudiant.objects.filter(Specialite="EVE", niveau=3).values())

    return JsonResponse(etudiantEVE, safe= False)

def UEAPI(request):
    mydata = list(UniteEnseignement.objects.all().values())

    return JsonResponse(mydata, safe=False)


############### API REQUETTES POST ###########################################################
def AddNoteEtudiant(request):
    if request.method == 'POST':
        data = request.POST
    
    dicto = extract(data)
    keyValue = splitVar(dicto)

    
    #return HttpResponse(success)
    return JsonResponse(keyValue, safe=False)



def test(request):
    return render(data, 'bulletin/test.html')


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

def saveData(a):
    for i in a:
        g = i[0]
        val = i[1]
        if(g[0]=="CC"):
            natureEvaluation = "Contrôle_Continue"
        else:
            natureEvaluation = "Session_Normale"
        matricule = g[1]
        codeUE = g[2]
        note = val
        print(natureEvaluation, matricule, note)