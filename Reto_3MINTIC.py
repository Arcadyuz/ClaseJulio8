def reto_3(diccionario: dict) -> str:
    mayor = None
    key = None

#    if diccionario:

#        for k in diccionario:
#            if mayor is None:
#                mayor = diccionario[k]
#                key = k
#            elif diccionario[k]> mayor:
#                mayor = diccionario[k]
#                key = k
        
#        return key
    
#    return key

    if diccionario:

        valores = list(diccionario.values())
        mayor = max(valores)
        llaves = [k for k in diccionario if diccionario[k] == mayor]

    #for key, value in diccionario.items():
    #    if value == mayor:
    #        llaves.append(key)
        return ", ".join(llaves)

    #else:
    return "None"

vendedores = {'John': 16, 'Alex': 12, 'Bob': 8, 'Mike': 14, 'Molly': 14}
vendedor = reto_3(vendedores)
print("Best: {}".format(vendedor))
#Best:John


vendedores = {'John': 12, 'Bob': 14, 'Mike': 16, 'Molly': 16, 'Adam': 10}
vendedor = reto_3(vendedores)
print("Best: {}".format(vendedor))
#Best: Mike,Molly


vendedores = None
vendedor = reto_3(vendedores)
print("Best: {}".format(vendedor))
#Best:None