from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from itertools import islice

from django.views.generic import View
from .utils import render_to_pdf 


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

    key,values = extract(data)
    
    #Ajout de la fonction de couplage
    saveData(key,values)
    print(key, values)
    text = "<html><body> %s </body></html>" % data
    return JsonResponse(request.POST, safe=False)


def test(request):
    return render(request, 'bulletin/BulletinTemplate/bulletin1.html')

#################################REQUETES POUR BULLETIN#############################################################
def bulls1eps(request, filiere):

    infoEtudiantMDS =list(Etudiant.objects.filter(filiere="STAPS", niveau=1).values('matricule', 'nom', 'prenom', 'date_naissance','lieu_naissance'))
    coefS1EPS1 = list(UniteEnseignement.objects.filter(semestre_id=1,filiere="STAPS").values("coefficient"))
    EPS111 =list(Evaluation.objects.filter(uniteEnseignement_id=3).values('note_Examen'))
    EPS112 =list(Evaluation.objects.filter(uniteEnseignement_id=4).values('note_Examen'))
    EPS113 =list(Evaluation.objects.filter(uniteEnseignement_id=5).values('note_Examen'))
    EPS114 =list(Evaluation.objects.filter(uniteEnseignement_id=6).values('note_Examen'))
    EPS115 =list(Evaluation.objects.filter(uniteEnseignement_id=7).values('note_Examen'))
    EPS116 =list(Evaluation.objects.filter(uniteEnseignement_id=8).values('note_Examen'))
    EPS117 =list(Evaluation.objects.filter(uniteEnseignement_id=9).values('note_Examen'))
    EPS118 =list(Evaluation.objects.filter(uniteEnseignement_id=10).values('note_Examen'))
    EPS119 =list(Evaluation.objects.filter(uniteEnseignement_id=11).values('note_Examen'))

    semestre1MDS = [infoEtudiantMDS,EPS111, EPS112,EPS113,EPS114,EPS115,EPS116,EPS117,EPS118,EPS119]

    if filiere == "GESTION":
        fil = 'GESTION'
    else:
        fil = 'STAPS'
    

    return render(request,'bulletin/BulletinTemplate/bullS1eps.html', {'semestre1MDS': semestre1MDS, filiere:fil}) 

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
"""


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