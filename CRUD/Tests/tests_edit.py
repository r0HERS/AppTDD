from django.test import TestCase, Client
from ..models import Alunos, Materias, Professores, Cursos, Alunos_materia, Cursos_materia
from django.db import IntegrityError
from django.urls import reverse
from django.core.exceptions import ValidationError

class ModelTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        self.aluno1 = Alunos.objects.create(nome='João', RA='12345', curso_id=1)
        self.aluno2 = Alunos.objects.create(nome='Maria', RA='54321', curso_id=2)

        self.professor1 = Professores.objects.create(nome='Dr. Silva', RP='9876')
        self.professor2 = Professores.objects.create(nome='Profa. Oliveira', RP='5432')

        self.curso1 = Cursos.objects.create(nome='Engenharia', campus='Campus A')
        self.curso2 = Cursos.objects.create(nome='Administração', campus='Campus B')

        self.materia1 = Materias.objects.create(nome='Matemática', carga_horaria='60 horas', prof_id=1)
        self.materia2 = Materias.objects.create(nome='Economia', carga_horaria='45 horas', prof_id=2)

        self.aluno_materia1 = Alunos_materia.objects.create(aluno=self.aluno1, materia=self.materia1)
        self.aluno_materia2 = Alunos_materia.objects.create(aluno=self.aluno2, materia=self.materia2)

        self.curso_materia1 = Cursos_materia.objects.create(curso=self.curso1, materia=self.materia1)
        self.curso_materia2 = Cursos_materia.objects.create(curso=self.curso2, materia=self.materia2)

    def test_curso_edit(self):
        client = Client()
        novo_nome = 'Engenharia Civil'
        novo_campus = 'Campus C'
        c_id = 2  
        url = reverse('edit', args=[c_id])
        response = client.post(url, {'nome': novo_nome, 'campus': novo_campus, "materias": 1})
        self.assertEqual(response.status_code, 302)
        curso_atualizado = Cursos.objects.get(id=c_id)
        self.assertEqual(curso_atualizado.nome, novo_nome)
        self.assertEqual(curso_atualizado.campus, novo_campus)
        

        