from django.db import models

# Create your models here.

class Alunos(models.Model):

    nome=models.CharField(max_length=30)
    RA=models.CharField(max_length=30)
    curso_id=models.IntegerField()

    class Meta:
        managed=False
        db_table='alunos'

class Materias(models.Model):

    nome=models.CharField(max_length=20)
    carga_horaria=models.CharField(max_length=20)
    prof_id=models.IntegerField()

    class Meta:
        managed=False
        db_table='materias'

class Professores(models.Model):

    nome=models.CharField(max_length=30)
    RP=models.CharField(max_length=20)


    class Meta:
        managed=False
        db_table='professores'



class Cursos(models.Model):


    nome=models.CharField(max_length=20)
    campus=models.CharField(max_length=20)


    class Meta:
        managed=False
        db_table='cursos'


class Alunos_materia(models.Model):


    aluno=models.ForeignKey(Alunos, on_delete=models.CASCADE,related_name='alunos')
    materia=models.ForeignKey(Materias,on_delete=models.CASCADE,related_name='materias')


    class Meta:
        managed=False
        db_table='alunos_materia'


class Cursos_materia(models.Model):

    curso=models.ForeignKey(Cursos, on_delete=models.CASCADE,related_name='cursos')
    materia=models.ForeignKey(Materias,on_delete=models.CASCADE,related_name='mat')


    class Meta:
        managed=False
        db_table='cursos_materia'