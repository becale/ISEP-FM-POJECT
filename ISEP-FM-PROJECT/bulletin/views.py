from django.shortcuts import render
from django.http import HttpRequest
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse

# Create your views here.

def home(request):
    
    mydata = Etudiant.objects.all().values()

    context = {
        'Etudiants': mydata,
    }

    template = loader.get_template('bulletin/home.html')
    return HttpResponse(template.render(context, request))

def bulletin(request):
    template = loader.get_template('bulletin/bulletin.html')
    return HttpResponse(template.render({}, request))

def notes(request):
    #les données des etudiants, notes et matières doivent être chargées dans cette pages et receptionnées

    """mydata = list(Etudiant.objects.all().values())"""
    """context = {
     #   'Etudiants': mydata,
    }"""

    template = loader.get_template('bulletin/notes.html')
    return HttpResponse(template.render({}, request))


############### API ###########################################################
def EtudiantApi(request):
    mydata = list(Etudiant.objects.all().values())

    return JsonResponse(mydata, safe=False)

def EtudiantNiveau1Staps(request):
    etudiantStaps1 = list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values())
    
    return JsonResponse(etudiantStaps1, safe= False)

def UEAPI(request):
    mydata = list(UniteEnseignement.objects.all().values())

    return JsonResponse(mydata, safe=False)