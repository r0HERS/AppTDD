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
    professores=Professores.objects.all()
    return render(request,'index.html',{
        'alunos':alunos,
        'materias':materias,
        'cursos':cursos,
        'professores':professores
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

def search(request,al_id):
    if request.method == 'POST':
        a = Alunos.objects.get(nome=request.POST["RA"]) 
    else:
        a = Alunos.objects.get(id=al_id) 

    

    c=Cursos.objects.get(id=a.curso_id)
    
    materias = Cursos_materia.objects.filter(curso=a.curso_id)
    
    professores =[]
    for m in materias:
         professores.append(Professores_materia.objects.filter(materia=m.materia.id))

    
    mat_prof=list(zip(materias,professores))
    cursos=Cursos.objects.all
    return render(request,'aluno.html',{
        'aluno':a,
        'curso':c,
        'mat_prof':mat_prof,
        'cursos':cursos
    })


def edit_curso(request,c_id):
    c = Cursos.objects.get(id=c_id)
    
    if request.method == "POST":
            nome=request.POST["nome"]
            campus=request.POST['campus']
            c.nome=nome
            c.campus=campus
            if request.POST["ad_materias"]!='':
                add_materia=Materias.objects.get(id=request.POST["ad_materias"])
                Cursos_materia.objects.create(curso=c,materia=add_materia)

            elif request.POST["del_materias"]!='':
                materia=Materias.objects.get(id=request.POST["del_materias"])
                del_mat=Cursos_materia.objects.filter(materia=materia)
                del_mat.delete()


            c.save()
            return HttpResponseRedirect(reverse('edit',args=[c_id]))
    else:
        
        mat = Cursos_materia.objects.filter(curso=c_id)
        materias=[]
        for m in mat:
            materias.append(m.materia)

        todas_materias=Materias.objects.all()
        outras_materias=[]

        for todas in todas_materias:
            if todas not in materias:
                outras_materias.append(todas)
        
        return render(request,'curso.html',{
            'curso':c,
            'materias':materias,
            'outras_mat':outras_materias
        })


def add_al(request):
    if request.method == "POST":
        nome=request.POST["nome"]
        RA=request.POST['RA']
        curso=request.POST['al_curso']
        novo_aluno=Alunos(nome=nome,RA=RA,curso_id=curso)
        novo_aluno.save()
    return HttpResponseRedirect(reverse("index"))



def del_al(request,a_id):
    p = Alunos.objects.get(id=a_id)
    p.delete()

    return HttpResponseRedirect(reverse("index"))


def edit_al(request,al_id):

    al =Alunos.objects.get(id=al_id)
    if request.method == "POST":
        nome=request.POST["nome"]

        if request.POST["cursos"] == al.curso_id:
            curso = al.curso_id
        else:
            curso=request.POST["cursos"]
        
        al.curso_id=curso
        al.nome=nome

        al.save()
    return HttpResponseRedirect(reverse('search',args=[al.id]))

def search_curso(request):
    if request.method == 'POST':
        curso=Cursos.objects.get(nome=request.POST["nome"])

    
    return HttpResponseRedirect(reverse('edit',args=[curso.id]))
    

def add_curso(request):
    if request.method == 'POST':
        nome=request.POST['nome']
        campus=request.POST['campus']
        materias = request.POST.getlist("materias[]")
        curso=Cursos.objects.create(nome=nome,campus=campus)
        for m in materias:
            mat=Materias.objects.get(id=m)
            Cursos_materia.objects.create(materia=mat,curso=curso)
    
    return HttpResponseRedirect(reverse('edit',args=[curso.id]))

def del_curso(request,c_id):
    curso=Cursos.objects.get(id=c_id)
    curso.delete()
    
    return HttpResponseRedirect(reverse("index"))

def add_mat(request):
    if request.method == 'POST':
        nome=request.POST['nome']
        cg=request.POST['cg']
        professores = request.POST.getlist("professores[]")
        materia=Materias.objects.create(nome=nome,carga_horaria=cg,prof_id=0)
        for p in professores:
            prof=Professores.objects.get(id=p)
            Professores_materia.objects.create(materia=materia,professor=prof)

    return HttpResponseRedirect(reverse('edit_materia',args=[materia.id]))
    
def search_materia(request):
    if request.method == "POST":
        materia=Materias.objects.get(nome=request.POST["nome"])

    return HttpResponseRedirect(reverse('edit_materia',args=[materia.id]))

def edit_materia(request,mat_id):
    materia = Materias.objects.get(id=mat_id)
    todos_profs=Professores.objects.all()
    if request.method == 'POST':
        nome=request.POST['nome']
        cg=request.POST['carga_horaria']

        if request.POST['ad_professores']!='':
            prof=Professores.objects.get(id=request.POST['ad_professores'])
            Professores_materia.objects.create(professor=prof,materia=materia)

        elif request.POST['del_professores']!='':
            prof=Professores.objects.get(id=request.POST['del_professores'])
            del_prof=Professores_materia.objects.filter(professor=prof)
            del_prof.delete()

        materia.nome=nome
        materia.carga_horaria=cg
        materia.save()

        return HttpResponseRedirect(reverse('edit_materia',args=[materia.id]))
    else:
        profs=Professores_materia.objects.filter(materia=materia.id)
        professores=[]
        for p in profs:
            professores.append(Professores.objects.get(id=p.professor.id))

        outros_profs=[]
        for todos in todos_profs:
            if todos  not in professores:
                outros_profs.append(todos)


        return render(request,'materia.html',{
            'materia':materia,
            'professores':professores,
            'outros_profs':outros_profs
        })
    

def search_prof(request):
    a = Professores.objects.get(nome=request.POST["RA"]) 
    c = Professores_materia.objects.filter(professor=a.id)

    materias = [materia.materia for materia in c]
       

    return render(request,'professor.html',{
        'professor':a,
        'materias': materias,
    })

def cria_prof(request):
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

def del_prof(request,prof_id):
    professor=Professores.objects.get(id=prof_id)
    professor.delete()
    
    return HttpResponseRedirect(reverse("index"))

def edit_prof(request,prof_id):
    professor = Professores.objects.get(id=prof_id)

    c = Professores_materia.objects.filter(professor=professor.id)

    materias = [materia.materia for materia in c]

    
    
    if request.method == "POST":
            nome=request.POST["nome"]
            professor.nome=nome
            if request.POST["ad_materias"]!='':
                add_materia=Materias.objects.get(id=request.POST["ad_materias"])
                Professores_materia.objects.create(professor=professor,materia=add_materia)

            elif request.POST["del_materias"]!='':
                materia=Materias.objects.get(id=request.POST["del_materias"])
                del_mat=Professores_materia.objects.filter(materia=materia)
                del_mat.delete()


            professor.save()
            return HttpResponseRedirect(reverse('edit_prof',args=[professor.id]))
    else:
        
        todas_materias=Materias.objects.all()
        outras_materias=[]

        for todas in todas_materias:
            if todas not in materias:
                outras_materias.append(todas)
        
        return render(request,'professor.html',{
            'professor':professor,
            'materias':materias,
            'outras_mat':outras_materias
        })
