from django.test import TestCase

import unittest
import expendedora.views

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        # The index page loads properly
        response = self.client.get('http://127.0.0.1:8000/maquina/')
        self.assertEqual(response.status_code, 200)

class ExpendTestCase(unittest.TestCase):
    def test_saldo_rest(self):
        result = expendedora.views.saldo_rest(1, 4)
        comp_1 = 'El saldo restante es: 0\nGracias por la compra !!!'
        comp_2 = 'No tiene el monto para el producto seleccionado'
        self.assertEqual(result, comp_2)
