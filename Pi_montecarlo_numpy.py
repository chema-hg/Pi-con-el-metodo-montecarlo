#!/usr/bin/var python
# -*- coding:utf-8 -*-

# chema HG
# 1-05-2020

'''Aproximación al numero pi usando el método montecarlo la libreria numpy'''

'''Dado un cuadrado de lado 1 y una semicircunferencia inscrita de radio 1.

Calculamos las veces que lanzando un dardo al azar este cae dentro del circulo inscrito.

La probabilidad de tal evento es el numero de casos posibles o vences que caen los dados dentro ((pi*r**2)/4)
del circulo inscrito, dividido entre el numero de casos totales que es el area del cuadrado.

Por geometria el area del circulo es pi*r**2, pero en este caso no es un circulo entero sino 1/4 del mismo.
Al ser el radio = 1 el area del semicirculo es de pi/4. Este es el numero de casos posibles.

El numero de casos totales es el area del cuadrado, lo que es más facil de ver porque el area es l*l. Al
ser el lado = 1 el área del cuadrado es de 1)

Por tanto la probabilidad de que un lanzamiento caiga dentro del circulo es area_semicirculo/area_cuadrado.

Esto es probabilidad=(pi/4)/1 o lo que es lo mismo probabilidad = pi/4. Si despejamos pi, que desconocemos
su valor y lo vamos a calcular por aproximación : pi = probabilidad * 4'''

import numpy as np
from math import pi

# Numero de veces que se repite el experimento 16_000_000
REPETICIONES=16_000_000

# Por el teorema de Pitagoras la hipotenusa, que es lo que necesitamos saber para ver si el punto está
# dentro o fuera de la semicirculo, lo que es igual a h**2=x**2+y**2 por lo que despejando:
# h=(x**2+y**2)**0.5


# Creamos una matriz aleatoria con 2 filas y 16.000.000 de columnas: np.random.rand(2,REPETICIONES)
# La primera fila serán las coordenadas x del punto y la segunda fila las coordenadas y.
# Como necesitamos que x e y esten elevados al cuadrado segun la formula (x**2+y**2) elevamos el array
# de numpy al cuadrado con **2
punto=np.random.rand(2,REPETICIONES)**2

# como en la formula tenemos que sumar x**2+y**2 utilizamos .sum de numpy de esta forma:
# punto.sum(axis=0) es decir sumamos por columnas. Luego elevar un numero a 0.5 es en realidad
# hacer su raiz cuadrada de ahi el **5

rdo=punto.sum(axis=0)**0.5 #axis=0  suma por columnas, axis=1 suma por filas.

# Ahora tenemos un array final con una sola fila y 16.000.000 de columnas.
# Filtramos para ver cuantos de esos valores son menores o iguales que 1 y por tanto estan en el
#semicirculo
final=rdo[rdo<=1]

probabilidad=final.size/REPETICIONES #tamaño del array/numero total de lanzamientos

print("La probabilidad =", probabilidad)
print("El numero estimado de pi=", probabilidad*4)
print(f'El error para {REPETICIONES} de REPETICIONES es de {(pi-probabilidad*4):.5f}')


    
