from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre="Lab Test", ciudad="Ciudad Test", pais="País Test")

    def test_laboratorio_data(self):
        laboratorio = Laboratorio.objects.get(id=1)
        self.assertEqual(laboratorio.nombre, "Lab Test")
        self.assertEqual(laboratorio.ciudad, "Ciudad Test")
        self.assertEqual(laboratorio.pais, "País Test")

class LaboratorioURLTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre="Lab Test", ciudad="Ciudad Test", pais="País Test")

    def test_url_list_status(self):
        response = self.client.get(reverse('laboratorio_list'))
        self.assertEqual(response.status_code, 200)
