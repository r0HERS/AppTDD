from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Alunos,Professores,Materias,Cursos,Alunos_materia,Cursos_materia,Professores_materia

# Create your views here.

def index(request):
    materias=Materias.objects.all()
    alunos=Alunos.objects.all()
    cursos=Cursos.objects.all()
    return render(request,'index.html',{
        'alunos':alunos,
        'materias':materias,
        'cursos':cursos
    })

def add(request):
    if request.method == "POST":
        nome=request.POST["nome"]
        RP=request.POST['RP']
        novo_professor=Professores(nome=nome,RP=RP)
        novo_professor.save()
        if request.POST['prof_mat'] != '':
             materia=Materias.objects.get(id=request.POST['prof_mat'])

             novo_prof=Professores_materia(professor=novo_professor,materia=materia)
             novo_prof.save()
             
    return HttpResponseRedirect(reverse("index"))

def dele(request,m_id):
    p = Materias.objects.get(id=m_id)
    p.delete()

    return HttpResponseRedirect(reverse("index"))

def search(request):
    a = Alunos.objects.get(nome=request.POST["RA"]) 
    c=Cursos.objects.get(id=a.curso_id)
    materias = Alunos_materia.objects.filter(aluno=a.id)
    professores =[]
    for m in materias:
         professores.append(Professores_materia.objects.filter(materia=m.materia.id))

    mat_prof=list(zip(materias,professores))

    return render(request,'aluno.html',{
        'aluno':a,
        'curso':c,
        'mat_prof':mat_prof,
    })


def edit(request,c_id):
    c = Cursos.objects.get(id=c_id)
   
    
    if request.method == "POST":
            nome=request.POST["nome"]
            campus=request.POST['campus']
            c.nome=nome
            c.campus=campus
            materia=request.POST["materias"]
            if materia != "":
                tirar_materia=Cursos_materia.objects.get(curso=c_id,materia=materia)
                
                tirar_materia.delete()


            c.save()
            return HttpResponseRedirect(reverse('edit',args=[c_id]))
    else:
        
        materias = Cursos_materia.objects.filter(curso=c_id)
        
        return render(request,'curso.html',{
            'curso':c,
            'materias':materias
        })






