#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import sys
from pprint import pprint

fichero_perros = open('/home/dani/Documentos/perros.json','r')
perro = json.load(fichero_perros)
print "Ejercicio 5. Las razas que tengan mas de un numero de perros"

filas = len(perro["animales"]["animal"])
#312
lista_perro=[]
for i in xrange(1,filas):
	raza = perro["animales"]["animal"][i]["descripcion"]
	if not raza in lista_perro:
		lista_perro.append(raza)

lista=[]
for x in perro["animales"]["animal"]:
	y =(x["descripcion"])
	lista.append(y)

numero = int(raw_input("Dime el numero como minimo: "))
print "las razas de perros que tiene,",numero,"de perros son:"

for x in lista_perro:
	if x in lista:
		contar = len(x)

		if contar >= numero:

			
			print "raza",x,"; hay un total de:",contar
			

	
		print "ninguna, pues no hay ninguna raza con",numero,"o mas perros"
		sys.exit()