import datetime

class Perro:

   def __init__(self, nombre, raza):
       self.__nombre = nombre
       self.__raza = raza
  

   def asignar_raza(self, raza):
       self.__raza = raza

   def asignar_nombre(self, nombre):
       self.__nombre = nombre

   def dar_raza(self):
       return(self.__raza)

   def dar_nombre(self):
       return(self.__nombre)
