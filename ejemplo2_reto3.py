
def reto_3(diccionario: dict) -> str:
    mayor = None
    key = None
    lista = []
    sep = ", "
    if diccionario:
        for k in diccionario:
            if mayor is None:
                mayor = diccionario[k]
                key = k
            elif diccionario[k] >= mayor:
                mayor = diccionario[k]
                key = k
                lista.append(key)
                cumplen = sep.join(lista)
        return cumplen
    return lista

vendedores = {'John': 16, 'Alex': 12, 'Bob': 8, 'Mike': 14, 'Molly': 14}
vendedor = reto_3(vendedores)
print("Best: {}".format(vendedor))
#Best:John


#vendedores = {'John': 12, 'Bob': 14, 'Mike': 16, 'Molly': 16, 'Adam': 10}
#vendedor = reto_3(vendedores)
#print("Best: {}".format(vendedor))
#Best: Mike,Molly


#vendedores = None
#vendedor = reto_3(vendedores)
#print("Best: {}".format(vendedor))
#Best:None

#asistencia = {'Cindy': 8, 'Fabian': 15, 'Juan': 17, 'Laura': 10, 'Diego': 6}
#print(mejor_valor(asistencia))