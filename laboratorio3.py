#!/usr/bin/python3
'''
Autor: Luis Diego Araya Campos.

Programa que calcula el enésimo número de la serie de Fibonacci.

Este programa toma el número N y regresa el elemento de la serie de Fibonacci
con ese índice. Si se utiliza la opción de --tiempo se regresa además el tiempo
de ejecución del programa, si se utiliza la opción de --completa se regresa
también todos los elementos de la serie de Fibonacci hasta el índice N.
'''

import argparse
from time import time


def fibonacci(n):
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

    if N < 0:
        print('Error: El número debe ser positivo o cero.')
    else:
        if c:
            print('Serie de Fibonacci hasta el índice {} es:'.format(N))
            for i in range(N+1):
                print(fibonacci(i))
        else:
            print('El número de Fibonacci del índice {} es:'.format(N))
            print(fibonacci(N))

        if t:
            print(
                'Tiempo total de ejecución: {} segundos'.format(time() - start)
                )
