import datetime

class Perro:

   def __init__(self, nombre, raza, propietario):
       self.__nombre = nombre
       self.__raza = raza
       self.__propietario = propietario
  

   def asignar_raza(self, raza):
       self.__raza = raza

   def asignar_nombre(self, nombre):
       self.__nombre = nombre
       
   def asignar_propietario(self, propietario):
       self.__propietario = propietario

   def dar_raza(self):
       return(self.__raza)

   def dar_nombre(self):
       return(self.__nombre)
   
   def dar_propietario(self):
       return self.__propietario
