#!/usr/bin/env python
#! _*_ coding: utf-8 -*_

__author__ = "cpina"

import os
import shutil
import time

fecha = time.strftime("%d/%m/%y")+'.txt'

class Monitor:
	"""Objeto monitor para la selección del personal"""
	"""
	variables:
	nombre 			identificador del monitor
	correo 			contacto del monitor
	telefono 		contacto del monitor
	oportunidad 	variable que soporta una (solo una) falla sin ir al final de la cola
	fallas 			cantidad de veces que el monitor ha fallado a los llamados
	bilingues 		variable que determina si puede realizar tour en ingles o no
	exitos 			cantidad de veces que ha aceptado los llamados al tour
	"""
	def __init__(self, fal, opo, nom, tel, cor):
		self.nombre = nom
		self.telefono = tel
		self.correo = cor
		self.fallas = int(fal)
		self.oportunidad = int(opo)
	
	def fallo(self):
		if self.oportunidad < 1:
		    self.oportunidad = 2
		else:
			self.oportunidad = 1

def llenar():
	nom = []
	archivo = open("nombres.txt", "r+")
	linea = archivo.readline()
	while linea != '':
		separado = linea.split(' ')
		monit = Monitor(separado[0], separado[1], separado[2], separado[3], separado[4])
		nom.append(monit)
		linea = archivo.readline()
	return nom

def respaldar():
	archi=open('respaldo.txt','w')
	shutil.copyfile('nombres.txt', 'respaldo.txt')
	archi.close()
#def volver():

#agregar el problema de los bilingues a la cuestione esta.
#agregar una variable para el indice de exitos en el trabajo.

if __name__ == '__main__':
	#shutil.copyfile('nombres.txt', fecha)
	nomina = llenar()
	respaldar()
	#casco = os.remove("cosa.txt")
	for x in range(len(nomina)):
		cosa = nomina.pop(0)	#quita el primer elemento de la estructura
		print cosa.nombre
		nomina.append(cosa)		#agrega al elemento en la última posición de la estructura
	#Datos del archivo en la lista de monitores
	# La prioridad es 0 y el último es n.
	cosa = nomina[0]
	print cosa.nombre
	print 5+cosa.fallas
	print "\nfin programa"


	#http://pythonya.appspot.com/detalleconcepto?deta=Creaci%C3%B3n,%20carga%20y%20lectura%20de%20archivos%20de%20texto
