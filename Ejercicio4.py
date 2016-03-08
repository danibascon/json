#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import sys
from pprint import pprint

fichero_perros = open('/home/dani/Documentos/perros.json','r')
perro = json.load(fichero_perros)


print "Ejercicio 4. Mostrar raza y barrio del siguiente codigo postal"


filas = len(perro["animales"]["animal"])
#312
lista_CP=[]
for i in xrange(1,filas):
	CP = perro["animales"]["animal"][i]["codigo_postal"]
	if not CP in lista_CP:
		lista_CP.append(CP)

for x in lista_CP:
	print x

buscar_CP = raw_input("Dime un codigo postal de la lista anterior para buscar: ")

lista_ej4=[]
for x in perro["animales"]["animal"]:
	CP_2 = x["codigo_postal"]

	if CP_2 == buscar_CP:
		lista_ej4.append(CP_2)
		print "raza:",x["descripcion"],"barrio:",x["barrio"]


contar_ej4 = len(lista_ej4)	
if contar_ej4 == 0: 	
	print "ese codigo postal no existe"

