#Autor: Diego Cadena
#Fecha: 14/4/21
#Version: 1.0
#Nombre: Ejercicio
#Correo: Dobleaduo@gmail.com

texto=input("Ingrese el texto: ")
print ("El primer caracter es: ",texto[0])
caracter=len(texto)
print ("Ingrese un valor dentro del rango (0 hasta",caracter,")")
indice=int(input("Ingrese el valor dentro del rango: "))
print("El valor del indice es: ",indice)
print("El caracter en esa posicion: ",texto[indice])