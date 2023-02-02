from django.urls import path
from . import views
from .views import GeneratePdf

urlpatterns=[
    path('', views.home, name="home"),
    path('bulletin/', views.bulletin, name="bulletin"),
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
    path('BulletinUnique/',views.BulletinUnique, name="bulletinUnique"),
    path('BulletinSpecialite/',views.BulletinSpecialite, name="bulletinSpacialite"),
    path('BullS2EPS/', views.test, name="bull"),
    path('bulletin/BullS1EPS/<filiere>/', views.bulls1eps, name="bullS1eps"),

    path('pdf/', GeneratePdf.as_view(),name='pdf'), 
]


