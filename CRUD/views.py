from django.shortcuts import render
from django.shortcuts import HttpResponse,get_object_or_404, HttpResponseRedirect, render
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
    if request.method == "POST":
        m_id = request.POST.get('m_id')
        
        
        q=Materias.objects.filter(id=m_id)
        q.delete()
        
        return HttpResponseRedirect(reverse("index"))
    else:
         return HttpResponse("erro")

def search(request):
    if request.method == "POST":
        ra = request.POST.get("RA")
        aluno = Alunos.objects.get(nome=ra)
        curso = Cursos.objects.get(id=aluno.curso_id)
        materias = Alunos_materia.objects.filter(aluno=aluno.id)
        professores=[]
        for m in materias:
            professores.append(Professores_materia.objects.filter(materia=m.materia.id))
        mat_prof = list(zip(materias, professores))
        return render(request, 'aluno.html', {
            'aluno': aluno,
            'curso': curso,
            'mat_prof': mat_prof,
        })
        
    else:
            return HttpResponse(f"Erro ao buscar aluno")

        
    


def edit(request, c_id):
    curso = get_object_or_404(Cursos, id=c_id)
    
    if request.method == "POST":
        nome = request.POST.get("nome")
        campus = request.POST.get("campus")
        materias_ids = request.POST.getlist("materias")  
        
       
        curso.nome = nome
        curso.campus = campus
        curso.save()
        
        
        curso_materias = Cursos_materia.objects.filter(curso=curso)
        for curso_materia in curso_materias:
            if curso_materia.materia.id not in materias_ids:
                curso_materia.delete()
        
        return HttpResponseRedirect(reverse('edit', args=[c_id]))
    else:
        materias = Cursos_materia.objects.filter(curso=c_id)
        return render(request, 'curso.html', {'curso': curso, 'materias': materias})






