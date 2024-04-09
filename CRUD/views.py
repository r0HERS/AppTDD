from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Alunos,Professores,Materias

# Create your views here.
materias=Materias.objects.all()
alunos=Alunos.objects.all()
def index(request):
    return render(request,'index.html',{
        'alunos':alunos,
        'materias':materias
    })

def add(request):
    if request.method == "POST":
        print("oal")
        nome=request.POST["nome"]
        RP=request.POST['RP']

        novo_aluno=Professores(nome=nome,RP=RP)
        novo_aluno.save()
    


    return render(request,'index.html',{
        'alunos':alunos,
        'materias':materias
    })