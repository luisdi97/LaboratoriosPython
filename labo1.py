#!/usr/bin/python3

c = input('Ingrese un caracter, por favor:')
n = int(input('Ingrese un numero, por favor:'))

for a in range(n, 0, -1):
    for _ in range(a):
        print(c, end="")
    print('')
