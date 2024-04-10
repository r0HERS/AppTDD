from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Alunos,Professores,Materias,Cursos

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
    rota=request.path
    
    if request.method == "POST":
            nome=request.POST["nome"]
            campus=request.POST['campus']
            c.nome=nome
            c.campus=campus
            c.save()
            return HttpResponseRedirect(reverse('edit',args=[c_id]))
    else:

        return render(request,'curso.html',{
            'curso':c,
            'verifica':c_id,
            'rota':rota
        })






