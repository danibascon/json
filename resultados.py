#!/usr/bin/python
# -+- coding: utf-8 .*.

import json
from pprint import pprint

with open('/home/dani/Documentos/nuevo/python/marcas/json/resultados_academicos.json') as f:
	a =json.load(f)



print "1. Listame los distintos label que hay."
print "2. La cantidad de label que hay."
print "3. Mostrar la tasa de exito donde apareza la siguiente cadena en su correspondiente label."
print "4. Pedir tasa de éxito y mostrar los  labels que tiene esa tasa o superior"
print "5. Pedir un numero minimo y maximo de taza de abandono del tercer curso y mostrar los label que esten entre esos dos datos."
print
print
lista_num=[1,2,3,4,5]
num=int(raw_input("Dime un ejercicio: "))
print
while num not in lista_num:
	num=int(raw_input("Dime un ejercicio entre el 1 y el 5: "))


print
print
if num==1:
	print "1. Listame los distintos label que hay."
	print
	for x in a["results"]["bindings"]:
	    print x["rdfs_label"]["value"]

 

if num==2:
	print "2. La cantidad de label que hay."
	print
	print "hay un total de ",len(a["results"]["bindings"]),"labels"




if num==3:
	print "3. Mostrar la tasa de exito donde apareza la siguiente cadena en su correspondiente label."
	print
	cadena=raw_input("Dime una cadena para buscar: ")

	for x in a["results"]["bindings"]:
		if len(x) >=8:
#el len es por que hay diccionarios que no tienen todas las tasas

	 	   if x["rdfs_label"]["value"].find(cadena) >0:
	 	   		print x["rdfs_label"]["value"],"--> tasa de exito:",x["ou_tasaExito"]["value"]


if num==4:
	print "4. Pedir tasa de éxito y mostrar los  labels que tiene esa tasa o superior"
	print

	tasa=float(raw_input("Dime una tasa para comparar: "))
	cont=0

	for x in a["results"]["bindings"]:
		if len(x) >=8:
#el len es por que hay diccionarios que no tienen todas las tasas

	 	   if tasa <= float(x["ou_tasaExito"]["value"]):
	 	   		cont=cont+1
	 	   		print x["rdfs_label"]["value"],"--> tasa de exito:",x["ou_tasaExito"]["value"]
	 	   		print
	print
	print "hay un total de",cont,"tasas"




if num==5:
	print "5. Pedir un numero minimo y maximo de taza de abandono del tercer curso y mostrar los label que esten entre esos dos datos."
	print

	nummin=float(raw_input("Dime una tasa minima para comparar: "))
	nummax=float(raw_input("Dime una tasa maxima para comparar: "))
	while nummax<nummin:
		nummax=float(raw_input("Dime una tasa maxima para comparar mayoy que la minima: "))


	cont=0

	for x in a["results"]["bindings"]:
		if len(x) >=13:
#el len es por que hay diccionarios que no tienen todas las tasas

	 	   if nummax >=float(x["ou_tasaAbandonoTercerCurso"]["value"]) >= nummin:
	 	   		cont=cont+1
	 	   		print x["rdfs_label"]["value"],"--> tasa de exito:",x["ou_tasaAbandonoTercerCurso"]["value"]
	 	   		print
	print
	print "hay un total de",cont,"tasas"


