from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Alunos,Professores,Materias,Cursos,Cursos_materia

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
        print("oal")
        nome=request.POST["nome"]
        RP=request.POST['RP']

        novo_aluno=Professores(nome=nome,RP=RP)
        novo_aluno.save()
    

    return HttpResponseRedirect(reverse("index"))

def dele(request,m_id):
    p = Materias.objects.get(id=m_id)
    p.delete()

    return HttpResponseRedirect(reverse("index"))

def search(request):
    a = Alunos.objects.get(nome=request.POST["RA"])
 
    c=Cursos.objects.get(id=a.curso_id)
    
    return render(request,'aluno.html',{
        'aluno':a,
        'curso':c
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
                print(tirar_materia)
                tirar_materia.delete()


            c.save()
            return HttpResponseRedirect(reverse('edit',args=[c_id]))
    else:
        
        materias = Cursos_materia.objects.filter(curso=c_id)
        print(materias[0].materia.nome)
        return render(request,'curso.html',{
            'curso':c,
            'verifica':c_id,
            'materias':materias
        })






