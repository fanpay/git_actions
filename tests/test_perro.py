import unittest
from src.perro import Perro


class PersonaTestCase(unittest.TestCase):

   def setUp(self):
      self.perro1 = Perro(nombre='Berlín', raza="Border Collie", propietario="Fabián")
      self.perro2 = Perro(nombre='Titán', raza="American Bully", propietario="Nathy")
      self.perro3 = Perro(nombre='Donna', raza="Golden", propietario="Eli")
      self.perro4 = Perro(nombre='Aslan', raza="Husky", propietario="Laura")
      self.grupo = [self.perro1, self.perro2, self.perro3]

   def test_constructor(self):
      self.assertEqual(self.perro1.dar_nombre(), 'Berlín')  
      self.assertEqual(self.perro1.dar_raza(), 'Border Collie')
      self.assertEqual(self.perro1.dar_propietario(), 'Fabián')

   def test_asignacion(self):
      self.perro2.asignar_raza("Labrador")
      self.perro2.asignar_nombre("Violet")
      self.assertFalse(self.perro2.dar_nombre()=='Titán')
      self.assertFalse(self.perro2.dar_raza()=='American Bully')
      self.assertTrue(self.perro2.dar_nombre()=='Violet')
      self.assertTrue(self.perro2.dar_raza()=='Labrador')

   def test_objetos_iguales(self):
      perro_nuevo = self.perro1
      self.assertIsNot(self.perro1, self.perro3)
      self.assertIs(self.perro1, perro_nuevo)

   def test_elemento_en_conjunto(self):
      self.assertIn(self.perro3, self.grupo)
      self.assertNotIn(self.perro4, self.grupo)

   def test_instancia_clase(self):
      self.assertIsInstance(self.perro1, Perro)
      self.assertNotIsInstance(self.grupo, Perro)