from django.contrib import admin
from .models import Alunos,Alunos_materia,Cursos,Cursos_materia,Professores,Materias,Professores_materia
# Register your models here.
admin.site.register(Alunos)
admin.site.register(Cursos)

admin.site.register(Alunos_materia)
admin.site.register(Cursos_materia)
admin.site.register(Professores)
admin.site.register(Materias)
admin.site.register(Professores_materia)