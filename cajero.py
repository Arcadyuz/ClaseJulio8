#Autor: Diego Cadena
#Fecha: 24/4/21
#Version: 1.0
#Nombre: Ejercicio de cajero
#Correo: Dobleaduo@gmail.com

usuario = "neo"
clave = "123456"
saldo = 1000

def validaUsuario (u,c):
    if u == usuario and c == clave:
        return True
    return False

def login():
    usuario = input ("digite usuario: ")
    clave = input("digite clave: ")
    return validaUsuario(usuario,clave)

def retirar(valor):
    if valor > saldo:
        return False, saldo 

    return True, saldo - valor

def consignar (valor):
    return True, saldo + valor

def accion(opcion):
    if opcion == 1:
        valor = int(input("Digite el valor a consignar: "))
        return consignar(valor)
    if opcion == 2:
        valor = int(input("Digite valor a retirar: "))
        return retirar(valor)
    
    return False, saldo

def ejecutar():
    if not login():
        print("Usuario o clave invalido")
        return

    print("Que desea hacer?")
    opcion = int(input("1. Consignar o 2. Retirar: "))

    ok, saldo = accion(opcion)
    if not ok:
        print("No se realizo la accion, saldo: ", saldo)
    else:
        print("accion realizada correctamente, saldo: ", saldo)

ejecutar( )