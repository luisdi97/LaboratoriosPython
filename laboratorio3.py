#!/usr/bin/python3
'''
Autor: Luis Diego Araya Campos.

Programa que calcula el enésimo número de la serie de Fibonacci.

Este programa toma el número N e imprime el elemento de la serie de Fibonacci
con ese índice. Si se utiliza la opción de --tiempo se imprime además el tiempo
de ejecución del programa, si se utiliza la opción de --completa se imprime
todos los elementos de la serie de Fibonacci hasta el índice N.
'''

import argparse
from time import time


def fibonacci(n):
    '''
    Función que devuelve el elemento de índice n de la serie de Fibonacci.

    :param int n: índice del elemento por calcular
    :return int: el elemento n de la serie de Fibonacci
    '''

    # El elemento de la serie de Fibonacci se calcula de forma recursiva
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':

    start = time()  # Mido el tiempo inicial

    # Declaro el objeto ArgumentParser
    parser = argparse.ArgumentParser()

    # Defino los argumentos que recibe el script
    parser.add_argument(
        'posicion',
        type=int,
        help='Posicion en la secuencia de Fibonacci que debe ser calculado.'
    )
    parser.add_argument(
        '--tiempo',
        '-t',
        action="store_true",
        help='Imprime el tiempo transcurrido para finalizar el cálculo.'
    )
    parser.add_argument(
        '--completa',
        '-c',
        action="store_true",
        help='Imprime la secuencia completa.'
    )

    # Obtengo los argumentos y los guardo en args
    args = parser.parse_args()
    N = args.posicion
    t = args.tiempo
    c = args.completa

    if N < 0:  # Si el número es un entero negativo da error
        print('Error: El número debe ser positivo o cero.')
    else:  # Si el número es un entero positivo o cero sigue el flujo
        if c:
            # Si se incluye el argumento c, se imprimen todos los elementos de
            # la serie de Fibonacci
            print('Serie de Fibonacci hasta el índice {} es:'.format(N))
            for i in range(N+1):
                print(fibonacci(i))
        else:
            # Si no se incluye el argumento c, solo se imprime el elemento n de
            # la serie de Fibonacci
            print('El número de Fibonacci del índice {} es:'.format(N))
            print(fibonacci(N))

        if t:
            # Si se incluye el argumento t, se imprime el tiempo de ejecución
            print(
                'Tiempo total de ejecución: {} segundos'.format(time() - start)
                )
