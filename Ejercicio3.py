#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import sys
from pprint import pprint

fichero_perros = open('/home/dani/Documentos/perros.json','r')
perro = json.load(fichero_perros)

print "Ejercicio 3. Mostrar raza y tamaño de la siguiente cadena"	

cadena = raw_input("Introduce una cadena para buscar: ").capitalize()
lista_cadena = []
lista_cadena2 = []
lista_cadena3 = []
for x in perro["animales"]["animal"]:
	raza = x["descripcion"]
	tam = x["tamanyo"]
	barrio = x["barrio"]
	lista_cadena.append(barrio)
	lista_cadena.append(tam)
	lista_cadena.append(raza)

for y in lista_cadena:
	if y.startswith(cadena) is True:
		lista_cadena2.append(y)

conta = len (lista_cadena2)

if conta == 0:
	print "error, esa cadena no existe"
if conta != 0:
	print "La raza y el tamaño de los perros con la cadena que hemos hayado son:"
	for x in perro["animales"]["animal"]:
		raza = x["descripcion"]
		tam = x["tamanyo"]
		barrio = x["barrio"]
		lista_cadena.append(barrio)
		lista_cadena.append(tam)
		lista_cadena.append(raza)

	for y in lista_cadena:
		if y.startswith(cadena) is True:
			print "raza:",x["descripcion"],"; tamaño:",x["tamanyo"]
