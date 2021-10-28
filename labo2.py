#!/usr/bin/python3
'''
Autor: Luis Diego Araya Campos.

Programa para darle formato correcto a los nombres.

Este programa toma nombres de 3 o 4 componentes cuyos caracteres pertenezcan al
alfabeto, es decir, no sean numeros ni caracteres especiales, y vuelve la
primer letra de cada componente en mayuscula y el resto en minuscula.
'''

nombres = []

while(True):
    BOOL_tam = True  # Defino dos booleanos como verdaderos
    BOOL_esp = True
    nombre = input('Escriba un nombre, o SALIR para salir: ')
    if(nombre == 'SALIR'):
        break
    lista = nombre.split(' ')
    length = len(lista)
    if(not(length == 3 or length == 4)):
        BOOL_tam = False  # Es falso si la cantidad de compontes esta mal
    for n in range(length):
        if(not lista[n].isalpha()):
            BOOL_esp = False  # Es falso si hay caracteres no alfabeticos
    if(not BOOL_tam and not BOOL_esp):  # Se presentan ambos errores
        print('ERROR 1: Debe ingresar nombres de 3 o 4 componentes')
        print('ERROR 2: Debe ingresar nombres sin numeros o caracteres '
              'especiales')
    elif(not BOOL_tam):  # Se presenta el error de cantidad de componentes
        print('ERROR: Debe ingresar nombres de 3 o 4 componentes')
    elif(not BOOL_esp):  # Se presenta el error de caracteres no alfabeticos
        print('ERROR: Debe ingresar nombres sin numeros o caracteres '
              'especiales')
    else:  # Si no hay errores le da el formato correcto al nombre
        for n in range(length):
            lista[n] = lista[n].capitalize()
        nombre = ' '.join(lista)
        nombres.append(nombre)  # Agrega el nombre a una lista

for name in nombres:  # Al SALIR imprime los nombres corregidos
    print(name)
