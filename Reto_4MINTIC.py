import numpy as np
def reto_4(diccionario: dict) -> tuple:

#a,b,c,d,e = reto_4(Aviones) 
#a = resultados;
#b = Matriz;
#c = Promedio;
#d = Puntajes;
#e = seleccionados;

 aviones = [] #['Usain Bolt', 'Tayson Gray', 'Yohan Blake']

 for i in diccionario.keys():
     aviones.append(i)

 #print(participantes)

 prueba = [] #['100m', '200m', '4x100m']

 for i in diccionario[aviones[0]].keys():
     prueba.append(i)

 #print(pruebas)

 resultados = []
 # [[9.63, 19.52, 36.48], [9.73, 19.52, 37.23], [9.73, 22.52, 35.48]]


 for i in aviones:
         resultados_diccionario = []
         for x in prueba:
             resultados_diccionario.append(diccionario[i][x])
         resultados.append(resultados_diccionario)

 #print(resultados)

 normalizar = []

 for i in resultados:
     normalizados = list(map(lambda valor: 5 if valor < 5 else valor, i))
     normalizar.append(normalizados)

 #print(normalizar)

 matriz = np.array(normalizar)
 #print(matriz)
 #print()
 promedio = np.average(matriz, axis=0)
 promedio = np.around(promedio, decimals=1)
 #print(promedio)

 puntajes = np.sum(matriz, axis=1)
 #print(t_total)

 seleccionado = aviones[puntajes.argmax()]
 #print(seleccionado)

 return (normalizar, matriz, promedio, puntajes, seleccionado)

#aviones = {'Avion T1': {'prueba 1': 8, 'prueba 2': 7, 'prueba 3': 9}, 'Avion T2': { 
# 'prueba 1': 5, 'prueba 2': 7, 'prueba 3': 9}, 'Avion T3': {'prueba 1': 6, 'prueba 2': 7, 'prueba 3': 9}} 
#a, b, c, d, e = reto_4(aviones) 
#a = f"Resultados: {a}" 
#b = f"Matriz: \n{b}" 
#c = f"Promedio: {c}" 
#d = f"Puntajes: {d}" 
#e = f"Seleccionado: {e}"  
#print(a, b, c, d, e, sep='\n')

aviones = {'Avion j': {'prueba 1': 8, 'prueba 2': 7, 'prueba 3': 9}, 'Avion k': {
 'prueba 1': 8, 'prueba 2': 7, 'prueba 3': 9}, 'Avion l': {'prueba 1': 6, 'prueba 2': 7, 'prueba 3': 9}}
a, b, c, d, e = reto_4(aviones)
a = f"Resultados: {a}"
b = f"Matriz: \n{b}"
c = f"Promedio: {c}"
d = f"Puntajes: {d}"
e = f"Seleccionado: {e}"
print(a, b, c, d, e, sep='\n')

#aviones = {'Avion': {'prueba 1': 8, 'prueba 2': 7, 'prueba 3': 9}}
#a, b, c, d, e = reto_4(aviones)
#a = f"Resultados: {a}"
#b = f"Matriz: \n{b}"
#c = f"Promedio: {c}"
#d = f"Puntajes: {d}"
#e = f"Seleccionado: {e}"
#print(a, b, c, d, e, sep='\n')
