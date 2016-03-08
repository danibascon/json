#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import sys
from pprint import pprint

fichero_perros = open('/home/dani/Documentos/perros.json','r')
perro = json.load(fichero_perros)
dicc_tam=[]
for x in perro["animales"]["animal"]:
	tam = (x["tamanyo"])
	dicc_tam.append(tam)
	contador_grande = 0
	for x in dicc_tam:
		if x == "Grande":
			contador_grande = contador_grande + 1


print "Hay un total de",contador_grande,"perros grandes"