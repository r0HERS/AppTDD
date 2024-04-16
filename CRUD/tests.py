from django.test import TestCase, Client
from .models import Alunos, Materias, Professores, Cursos, Alunos_materia, Cursos_materia
from django.db import IntegrityError
from django.urls import reverse
from django.core.exceptions import ValidationError

class ModelTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        # Criação de instâncias de exemplo para cada modelo
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

    def test_aluno_model(self):
        self.assertEqual(self.aluno1.nome, 'João')
        self.assertEqual(self.aluno2.RA, '54321')

    def test_professor_model(self):
        self.assertEqual(self.professor1.nome, 'Dr. Silva')
        self.assertEqual(self.professor2.RP, '5432')

    def test_curso_model(self):
        self.assertEqual(self.curso1.nome, 'Engenharia')
        self.assertEqual(self.curso2.campus, 'Campus B')

    def test_materia_model(self):
        self.assertEqual(self.materia1.nome, 'Matemática')
        self.assertEqual(self.materia2.carga_horaria, '45 horas')

    def test_aluno_materia_model(self):
        self.assertEqual(self.aluno_materia1.aluno, self.aluno1)
        self.assertEqual(self.aluno_materia2.materia, self.materia2)

    def test_curso_materia_model(self):
        self.assertEqual(self.curso_materia1.curso, self.curso1)
        self.assertEqual(self.curso_materia2.materia, self.materia2)
    def test_aluno_nome_string(self):
        self.assertIsInstance(self.aluno1.nome, str)
        self.assertTrue(self.aluno1.nome.isalpha())

    def test_professor_nome_string(self):
        self.assertIsInstance(self.professor1.nome, str)
        self.assertTrue(self.professor1.nome.isalpha())

    def test_curso_nome_string(self):
        self.assertIsInstance(self.curso1.nome, str)
        self.assertTrue(self.curso1.nome.isalpha())

    def test_materia_nome_string(self):
        self.assertIsInstance(self.materia1.nome, str)
        self.assertTrue(self.materia1.nome.isalpha())

    def test_aluno_RA_string_numerico(self):
        self.assertIsInstance(self.aluno1.RA, str)
        self.assertTrue(self.aluno1.RA.isdigit())

    def carga_horaria_formato(self):
        carga_horaria_formato_invalido = Materias.objects.create(nome='Física', carga_horaria='60h')
        self.assertRaises(ValidationError, carga_horaria_formato_invalido.full_clean)

    def test_acesso_rota_view(self):
        
        client = Client()

        
        url = reverse('index')

        
        response = client.get(url)

       
        self.assertEqual(response.status_code, 200, 'ERROR')



if __name__ == '__main__':
    ModelTestCase()
