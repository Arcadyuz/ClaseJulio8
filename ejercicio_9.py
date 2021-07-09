#Autor: Diego Cadena
#Fecha: 14/4/21
#Version: 1.0
#Nombre: Ejercicio
#Correo: Dobleaduo@gmail.com

name=input("Ingrese su nombre: ")
age=int(input("Ingrese su edad: "))
print(f"Hola, mi nombre es {name} y tengo {age} años: ")
if age > 18:
    print("Es mayor de edad:")
else: 
    print(f"{name}es menor de edad por que tiene {age}")
