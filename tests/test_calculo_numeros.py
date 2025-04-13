import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
    SalirDelPrograma
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):


#tests para numeros positivos


    @patch(  'builtins.input',return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='1')
    def test_numero_positivo_minimo(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 1)

    @patch('builtins.input', return_value='999')
    def test_numero_positivo_grande(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 999)

    @patch('builtins.input', return_value='0')
    def test_cero_es_valido(self, mock_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 0)


#tests para numeros negativos


    @patch('builtins.input',return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-1')
    def test_numero_negativo_minimo(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='-999')
    def test_numero_negativo_grande(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='  -5  ')
    def test_numero_negativo_con_espacios(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()


#tests para texto no numérico


    @patch('builtins.input',return_value='AAA')
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='hola')
    def test_texto_simple(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='123abc')
    def test_texto_mezclado_con_numeros(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='!!@@##')
    def test_simbolos(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='   ')
    def test_espacios_vacios(self, mock_input):
        with self.assertRaises(ValueError):
            ingrese_numero()


#tests para la excepción SalirDelPrograma


    @patch('builtins.input', return_value='salir')
    def test_salir_del_programa(self, mock_input):
        with self.assertRaises(SalirDelPrograma):
            ingrese_numero()

    @patch('builtins.input', return_value='SALIR')
    def test_salir_del_programa_mayúsculas(self, mock_input):
        with self.assertRaises(SalirDelPrograma):
            ingrese_numero()

    @patch('builtins.input', return_value='Salir')
    def test_salir_del_programa_con_mayúsculas(self, mock_input):
        with self.assertRaises(SalirDelPrograma):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main() 