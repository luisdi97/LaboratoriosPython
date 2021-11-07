#!/usr/bin/python3
'''
Autor: Luis Diego Araya Campos.

Programa que define una clase para el manejo de matrices.

Este programa define la clase Matriz que permite crear matrices de dimensión
nxm inicializadas con elementos iguales a cero, donde la creación de un objeto
de esta clase se realiza con la sintaxis m = Matriz(n, m). Dentro de la clase
se define la representación como string. Para acceder al elemento (i, j) se
puede usar el método get(i, j) o mediante paréntesis cuadrados. Para definir el
elemento (i, j) con cierto valor se puede usar el método set(i, j, valor) o
mediante paréntesis cuadrados. Esta clase permite la suma y resta
de sus objetos mediante los operadores + y -. Finalmente, los elementos
permitidos en la matriz son números reales.
'''


class Vector():
    '''
    Esta clase define un vector de ceros de tamaño m
    '''
    def __init__(self, m):
        '''
        Esta función contruye un objeto de esta clase

        :param int m: tamaño del vector
        :return: objecto de la clase Vector
        '''
        self.m = int(m)
        # se crea una lista vacía
        list = []
        # se agregan m ceros a la lista
        for i in range(m):
            list.append(0)
        # se define esta lista como un atributo
        self.vec = list


class Matriz():
    '''
    Esta clase define matrices de tamaño nxm
    '''
    def __init__(self, n, m):
        '''
        Esta función contruye un objeto de esta clase

        :param int n: cantidad de filas
        :param int m: cantidad de columnas
        :return: objecto de la clase Matriz
        '''
        self.n = int(n)
        self.m = int(m)
        # se crea una lista vacía
        list = []
        # se añaden n objetos vector a la lista
        for i in range(n):
            list.append(Vector(m))
        # se define esta lista como un atributo
        self.filas = list

    def __str__(self):
        '''
        Esta función genera una representación del objeto de la clase Matriz
        como un string

        :return: string de la matriz
        '''
        filas = self.filas
        matriz = []
        # mediante el siguiente for se contruye una matriz como una lista
        for object in filas:
            matriz.append(object.vec)
        n = self.n
        m = self.m
        # defino un string vacío
        string = ''
        # añado todos los elementos de la matriz donde cada línea es una
        # fila de la matriz
        for a in range(n):
            for b in range(m):
                if b != m - 1:
                    string = string + str(matriz[a][b]) + ' '
                elif a != n-1:
                    string = string + str(matriz[a][b]) + '\n'
                else:
                    string = string + str(matriz[a][b])
        return string

    def get(self, n, m):
        '''
        Esta función permite obtener el valor del elemento de posición (n, m)
        de la matriz

        :param int n: índice de la fila del elemento por obtener
        :param int m: índice de la columna del elemento por obtener
        :return: elemento de la matriz
        '''
        if (not isinstance(n, int)):
            print('Error: La coordenada debe ser un entero')
            raise TypeError
        # de lo anterior se asegura que los índices son enteros, lo que puede
        # pasar es que estos índices estén fuera de rango, por eso se realiza
        # el siguiente manejo de error
        try:
            elemento = self.filas[n].vec[m]
        except IndexError:
            print('Error: La coordenada está fuera de rango')
        return elemento

    def set(self, n, m, valor):
        '''
        Esta función permite definir el valor del elemento de posición (n, m)
        de la matriz

        :param int n: índice de la fila del elemento por definir
        :param int m: índice de la columna del elemento por definir
        :param valor: un número para definir como el nuevo valor del elemento
                      de la matriz
        '''
        if (not isinstance(n, int)):
            print('Error: La coordenada debe ser un entero')
            raise TypeError
        if (not (isinstance(valor, int) or isinstance(valor, float))):
            print('Error: El valor debe ser un número')
            raise TypeError
        # de lo anterior se asegura que los índices son enteros y que el valor
        # es un entero o un flotante, lo que puede pasar es que estos índices
        # estén fuera de rango, por eso se realiza el siguiente manejo de error
        try:
            self.filas[n].vec[m] = valor
        except IndexError:
            print('Error: La coordenada está fuera de rango')

    def __add__(self, other):
        '''
        Esta función permite sumar matrices

        Para usar esta función se usa el operador +
        '''
        n = self.n
        m = self.m
        n_other = other.n
        m_other = other.m

        # El único manejo de error es revisar si las dimensiones de ambas
        # matrices son iguales
        if (n != n_other or m != m_other):
            print('Las matrices a sumar deben ser del mismo tamaño')
            raise Exception

        matriz_suma = Matriz(n, m)

        for a in range(n):
            for b in range(m):
                suma = self.get(a, b) + other.get(a, b)
                matriz_suma.set(a, b, suma)

        return matriz_suma

    def __sub__(self, other):
        '''
        Esta función permite restar matrices

        Para usar esta función se usa el operador -
        '''
        n = self.n
        m = self.m
        n_other = other.n
        m_other = other.m

        # El único manejo de error es revisar si las dimensiones de ambas
        # matrices son iguales
        if (n != n_other or m != m_other):
            print('Las matrices a restar deben ser del mismo tamaño')
            raise Exception

        matriz_resta = Matriz(n, m)

        for a in range(n):
            for b in range(m):
                resta = self.get(a, b) - other.get(a, b)
                matriz_resta.set(a, b, resta)

        return matriz_resta

    def __getitem__(self, index):
        '''
        Esta función permite acceder/definir los valores de la matriz mediante
        el uso de paréntesis cuadrados

        Ejemplos de uso:

        Aceeder valor: valor = matriz[1][2]
        Definir valor: matriz[1][2] = valor
        '''
        filas = self.filas
        matriz = []
        # se construye una matriz como una lista
        for object in filas:
            matriz.append(object.vec)
        # se ingresan los índices como una variable index que contiene ambos
        # índices
        return matriz[index]


if __name__ == '__main__':
    n = 3
    m = 3
    matriz_1 = Matriz(n, m)
    print('Una matriz 3x3 de ceros:')
    print(matriz_1)
    print('')

    elemento_1_2 = matriz_1.get(1, 2)
    print('El elemento (1,2) de la matriz con .get():')
    print(elemento_1_2)
    print('')

    matriz_1.set(1, 2, 4)
    print('El elemento (1,2) de la matriz con .get() luego de usar .set():')
    print(matriz_1.get(1, 2))
    print('')

    matriz_2 = Matriz(n, m)

    for a in range(n):
        for b in range(m):
            matriz_1.set(a, b, 1)
            matriz_2.set(a, b, 2)

    matriz_3 = matriz_1 + matriz_2
    print('La suma de una matriz de 1\'s y una matriz de 2\'s:')
    print(matriz_3)
    print('')

    matriz_4 = matriz_1 - matriz_2
    print('La resta de una matriz de 1\'s menos una matriz de 2\'s:')
    print(matriz_4)
    print('')

    matriz_4_1_1 = matriz_4[1][1]
    print('Acceso mediante paréntesis cuadrados al elemento (1,1):')
    print(matriz_4_1_1)
    print('')

    matriz_4[1][1] = 5
    print('Definición mediante paréntesis cuadrados del elemento (1,1):')
    print(matriz_4[1][1])
