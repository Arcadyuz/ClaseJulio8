#Autor: Diego Cadena
#Fecha: 14/4/21
#Version: 1.0
#Nombre: Ejercicio
#Correo: Dobleaduo@gmail.com

money=int(input("Ingrese la cantidad de dinero: "))
precio=int(input("Valor total productos: "))
falta=precio-money
if money>=precio:
    print("Si alcanza")
elif money==0:
    print("No hay saldo")
else:
    print(f"No alcanza,le falta {falta}")