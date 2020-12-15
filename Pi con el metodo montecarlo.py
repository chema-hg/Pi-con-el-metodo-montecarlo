#!/usr/bin/env python
# -*- cofing:utf-8 -*-

'''Aproximación al numero pi usando el método montecarlo'''

'''Dado un cuadrado de lado 1 y una semicircunferencia inscrita de radio 1.

Calculamos las veces que lanzando un dardo al azar este cae dentro del semicirculo inscrito.

La probabilidad de tal evento es el numero de casos posibles o veces que caen los dados dentro ((pi*r**2)/4)
del circulo inscrito, dividido entre el numero de casos totales que es el area del cuadrado.

Por geometria el area del circulo es pi*r**2, pero en este caso no es un circulo entero sino 1/4 del mismo.
Al ser el radio = 1 el area del semicirculo es de pi/4. Este es el numero de casos posibles.

El numero de casos totales es el area del cuadrado, lo que es más facil de ver porque el area es l*l. Al
ser el lado = 1 el área del cuadrado es de 1)

Por tanto la probabilidad de que un lanzamiento caiga dentro del circulo es area_semicirculo/area_cuadrado.

Esto es probabilidad=(pi/4)/1 o lo que es lo mismo probabilidad = pi/4. Si despejamos pi, que desconocemos
su valor y lo vamos a calcular por aproximación : pi = probabilidad * 4'''

# Importamos el modulo para escoger un numero aleatorio entre 0 y 1
from random import random
# Importamos el modulo para comparar el valor obtenido con el valor de pi
from math import pi

# Numero de veces que se repite el experimento 16.000.000 millones.
REPETICIONES=16_000_000

x,y = 0, 0 # Definimos las coordenadas del punto(x,y)
cont = 0 # Inicializamos a 0 el contador de las veces que el punto va a estar dentro del semicirculo.
        # Va a recoger el numero de veces que el lanzamiento esta dentro del semicirculo.
for i in range(REPETICIONES): # Lanzamos los dados el numero de veces que indiquemos en REPETICIONES
    x=random() # Coordenada x del punto
    y=random() # Coordenada y del punto.
    # Por el teorema de Pitagoras la hipotenusa, que es lo que necesitamos saber para ver si el punto está
    # dentro o fuera de la semicircunferencia h**2=x**2+y**2 por lo que despejando:
    p=(x**2+y**2)**0.5
    if p<=1: # Si el punto esta dentro aumentamos el contador en 1
        cont+=1
prob = cont/REPETICIONES        
print('Probabilidad=', prob)
print('El numero estimado de pi=', prob*4)
# Ese :.5f en la cadena de formato está especificando que se quiere representar un número en coma flotante
# con hasta cinco decimales, como mucho. f"{valor:.5f}". Esto para verlo por pantalla, si queremos redondear
# En los calculos habria que usar round(float, nº decimales).
# En los casos en que necesites números exactos, con precisión definida, usa en su lugar un módulo que te permita trabajar
# con números de aritmética decimal de coma fija, ej decimal
print(f'El error para {REPETICIONES} REPETICIONES es de {(pi-prob*4):.5f}')
    
