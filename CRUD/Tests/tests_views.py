from django.test import TestCase, Client
from ..models import Alunos, Materias, Professores, Cursos, Alunos_materia, Cursos_materia
from django.urls import reverse

class ModelTestCase(TestCase):
    def test_acesso_rota_index(self):
        client = Client()
        url = reverse('index')
        response = client.get(url)
        self.assertEqual(response.status_code, 200, 'ERROR')

    def test_acesso_rota_add(self):
        client = Client()
        url = reverse('add')
        response = client.get(url)
        self.assertEqual(response.status_code, 302, 'ERROR')

    def test_acesso_rota_search(self):
        client = Client()
        url = reverse('search') 
        response = client.get(url)
        self.assertEqual(response.status_code, 200, 'ERROR')

    def test_acesso_rota_dele(self):
        client = Client()
        m_id = "99999"  
        url = reverse('del', args=[m_id])
        response = client.get(url)
        self.assertEqual(response.status_code, 200, 'ERROR')


    def test_acesso_rota_edit(self):
        client = Client()
        c_id = "1"  
        url = reverse('edit', args=[c_id])
        response = client.get(url)
        self.assertEqual(response.status_code, 200, 'ERROR')