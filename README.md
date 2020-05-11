# Pi-con-el-metodo-montecarlo
Obtención aproximada del número pi con el uso del método montecarlo usando python


'''Partimos de un cuadrado de lado 1 y una semicircunferencia inscrita en el de radio 1.'''

<img src="https://github.com/chema-hg/Pi-con-el-metodo-montecarlo/blob/master/cuadrado_semicirculo.png">

Imaginemos que lanzamos un dardo aleatorio dentro de este cuadrante. Básicamente con el "metodo montecarlo" se 
trata de calcular las veces que este dardo aleatorio cae dentro de este semicirculo en relación al número de 
dardos en total lanzados.

La probabilidad de tal evento es, el número de casos posibles o veces que caen los dados dentro del semicirculo 
inscrito, dividido entre el número de casos totales que es el area del cuadrado.

Por geometría, el area de un circulo es pi*r**2, pero en este caso no es un circulo entero sino 1/4 del mismo.
Ya que estamos utilizando solo un cuadrante para lanzar nuestro dardo. Por ello, al ser el radio de la circufenrecia
igual a 1 el area del semicirculo inscrito en ese cuadrante es de pi/4. Este es el número de casos posibles.

El numero de casos totales es el área del cuadrado, lo que es más fácil de ver porque el area del cuadrado es 1.
Al ser el lado del cuadrado igual a 1, el área del cuadrado es ladoxlado, es decir 1 (area=lado*lado).

Por tanto la probabilidad de que un lanzamiento caiga dentro del semicirculo es igual al area_semicirculo/area_cuadrado.

Esto es probabilidad del suceso. Sustituyendo vemos que esto es igual a (pi/4)/1 o lo que es lo mismo la  probabilidad 
de que nuestro dardo caiga dentro del semicirculo es de pi/4. (pero de momento no sabemos cuando vale pi, que es lo que 
queremos obtener)

Aqui es donde entra en juego el script de Python. Se va a encargar de lanzar el dado por nosotros, 16.000.000 millones de veces
(aunque si en vuestro equipo tarda mucho tiempo lo podeis bajar a una cantidad menor, como 1.000.000 por ejemplo)
Cada vez que lanza el dardo mira si está dentro del semicirculo y si es así, lo va a guardar en la variable cont. Al final 
compara esta variable con el número de veces que hemos lanzado el dardo virtual y nos da una probabilidad.

Por ejemplo, 0.7852835625. (esta número variará ligeramente en cada ejecución del programa, ya que no lanzamos siempre
los dardos igual, pero será muy aproximado, por probabilidad.)

Si esto lo ponemos en relación con lo que sabemos de antes, tenemos la siguiente igualdad.

                              pi/4 = 0.7852835625 y despejando pi = 4 * 0.7852835625
                              Con lo que pi = 3.14113425 (Una aproximación bastante buena con un error 
                              de solo 0.00046)


El mismo sistema se puede utilizar para calcular el area que desconocemos de un poligono irregular dentro de un cuadrado.
En la práctica,se puede utilizar para calcular en un mapa de google maps, cual es el area de una finca que nos interese medir
utilizando la probabilidad.
