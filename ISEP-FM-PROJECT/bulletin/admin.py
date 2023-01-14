from django.contrib import admin
from bulletin.models import Etudiant, Semestre, UniteEnseignement, Evaluation

# Register your models here.
admin.site.register(Etudiant)
admin.site.register(Semestre)
admin.site.register(UniteEnseignement)
admin.site.register(Evaluation)