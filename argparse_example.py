#!/usr/bin/python3

import argparse

# Declaro el objeto ArgumentParser
parser = argparse.ArgumentParser()

parser.add_argument(
    'posicion',
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

# Accedo fácilmente los argumentos mediante atributos del objeto args
# Si el argumento no fue dado por el usuario se convierte en None
print(
    'posicion: {}\n'
    'tiempo: {}\n'
    'completa: {}\n'.format(
        args.posicion,
        args.tiempo,
        args.completa
    )
)


def mi_funcion():
    pass


while True:

    import pdb
    a = input('Digite un número a: ')
    b = input('Digite un número b: ')

    try:
        pdb.set_trace()
        c = (b/a)
    except ZeroDivisionError:
        pdb.set_trace()
        print('Intentó dividir por 0, reinténtelo...')

    if (
        input('Digite SALIR para salir, otra cosa para continuar') == 'SALIR'
    ):
        break
