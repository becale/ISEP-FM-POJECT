from django.urls import path
from . import views
from .views import GeneratePdf

urlpatterns=[
    path('', views.home, name="home"),
    path('bulletin/', views.bulletin, name="bulletin"),
    path('bulletin-collectif/', views.bulletinCollectif, name="bulletin"),
    path('notes/', views.notes, name="notes"),
    path('kds/', views.EtudiantApi, name="etudiantAPI"),
    path('UeAPI/', views.UEAPI, name='UeAPI)'),

    path('etudiantStaps1/', views.EtudiantNiveau1Staps, name="etudiantstaps1"),
    path('etudiantMDS1/', views.EtudiantNiveau1MDS, name="etudiantmds1"),
    path('etudiantStaps2/', views.EtudiantNiveau2Staps, name="etudiantstaps2"),
    path('etudiantNiveau3/', views.EtudiantNiveau3, name="etudiantniveau3"),
    path('etudiantNiveau3MSO/', views.EtudiantNiveau3MSO, name="etudiantniveau3MSO"),
    path('etudiantNiveau3EVE/', views.EtudiantNiveau3EVE, name="etudiantniveau3EVE"),

    path('notes/ajoutNoteEtudiant/', views.AddNoteEtudiant,name="addNoteEtudiant"),
    path('notes/ajoutNoteEtudiantRattrapage/', views.AddNoteEtudiantRattrapage,name="addNoteEtudiantRattrapage"),

    path('BulletinUnique/',views.BulletinUnique, name="bulletinUnique"),
    path('BulletinSpecialite/',views.BulletinSpecialite, name="bulletinSpacialite"),
    path('BullS2EPS/', views.test, name="bull"),

    path('bulletin/Semestre1/<filiere>', views.bulls1epsmds, name="bullS1epsmds"),
    path('bulletin/Semestre2/<filiere>', views.bulls2epsmds, name="bullS2epsmds"),

    path('bulletin/Semestre3/<filiere>', views.bulls3eps2, name="bullS3eps"),
    path('bulletin/Semestre4/<filiere>', views.bulls4eps2, name="bullS4eps"),

    path('bulletin/Semestre5/<filiere>', views.bulls5msoeve, name="bullS5msoeve"),
    path('bulletin/Semestre6/<filiere>', views.bulls6msoeve, name="bullS6msoeve"),

    #PROCES VERBAUX
    #SEMESTRE 1
    path('bulletin-collectif/Semestre1/STAPS1', views.resultatCommunepsmds, name="resultCommun"),
    path('bulletin-collectif/Semestre1/GESTION', views.resultatCommunmds, name="resultCommunmds"),

    #SEMESTRE 2
    path('bulletin-collectif/Semestre2/GESTION', views.resultatCommuns2mds, name="resultCommuns2mds"),
    path('bulletin-collectif/Semestre2/STAPS1', views.resultatCommuns2staps, name="resultCommuns2staps"),

    #SEMESTRE 3 & 4
    path('bulletin-collectif/Semestre3/STAPS2', views.resultatCommunstaps2, name="resultCommunstaps2"),
    path('bulletin-collectif/Semestre4/STAPS2', views.resultatCommuns4staps2, name="resultCommuns4staps2"),

    #SEMESTRE 5 & 6
    path('bulletin-collectif/Semestre5/EVE', views.resultatCommunEve, name="resultCommunEve"),
    path('bulletin-collectif/Semestre6/EVE', views.resultatCommuns6Eve, name="resultCommuns6Eve"),


    
    #path('releveCommun/semestre1/<filiere>', views.resultatCommunepsmds, name="resultCommun"),


    path('pdf/', GeneratePdf.as_view(),name='pdf'), 
]


