#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import sys
from pprint import pprint

fichero_perros = open('/home/dani/Documentos/perros.json','r')
perro = json.load(fichero_perros)

print "Ejercicio 1. Lista las distintas razas que hay"
print "Ejercicio 2. ¿Cuantos perros hay?"
print "Ejercicio 3. Mostrar raza y tamaño de la siguiente cadena"
print "Ejercicio 4. Mostrar raza y barrio del siguiente codigo postal"
print "Ejercicio 5. Las razas que tengan mas de un numero de perros"

pregunta = int(raw_input("Dime el numero del ejercicio que quieres ejecutar: "))
os.system("clear")

if pregunta == 1:

#1. Lista las distintas razas que hay.
	print "Ejercicio 1. Lista las distintas razas que hay"
	print "Estas son las distintas razas de perros que hay:"

	filas = len(perro["animales"]["animal"])
	#312
	lista_perro=[]
	for i in xrange(1,filas):
		raza = perro["animales"]["animal"][i]["descripcion"]
		if not raza in lista_perro:
			lista_perro.append(raza)

	for x in lista_perro:
		print x


if pregunta == 2:

#2. ¿Cuantos perros grandes hay?
	print "2. ¿Cuantos perros grandes hay?"


	dicc_tam=[]
	for x in perro["animales"]["animal"]:
		tam = (x["tamanyo"])
		dicc_tam.append(tam)
		contador_grande = 0
		for x in dicc_tam:
			if x == "Grande":
				contador_grande = contador_grande + 1


	print "Hay un total de",contador_grande,"perros grandes"
		
		

if pregunta == 3:

#3. Mostrar raza y tamaño de la cadena siguiente:
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




if pregunta == 4:

#4. Mostrar raza y barrio
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

if pregunta == 5:		

#5. Lista las razas que tengan más de XX númeno de perros
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
