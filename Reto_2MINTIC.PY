def bd_objetos():

    objetos = {

        'Mark I': {
            'color': 'Gris',
            'material': 'metal',
            'peso kg': 360,
            'sistema': 'MS-DOS',
            'disponible': False
        },
        'Mark II': {
            'color': 'Gris',
            'material': 'metal',
            'peso kg': 280,
            'sistema': 'JARVIS',
            'disponible': True
        },
        'Mark III': {
            'color': 'Rojo Y Oro',
            'material': 'oro y titanio',
            'peso kg': 280,
            'sistema': 'JARVIS',
            'disponible': True
        },
        'Mark VII': {
            'color': 'Rojo Y Oro',
            'material': 'oro y titanio',
            'peso kg': 200,
            'sistema': 'JARVIS',
            'disponible': False
        },
        'Veronica I': {
            'color': 'Rojo Y Oro',
            'material': 'acero, hierro y niquel',
            'peso kg': 975,
            'sistema': 'JARVIS',
            'disponible': True
        },
    }

    return objetos


def reto_2(nombre: str, color: str, material: str, peso: int, sistema: str, disponible: bool, bd_objetos: dict) -> dict:

    if type(nombre) is not type(str()):
        return f"Ingrese un id de tipo valido."
    
    datos = {}
    nombre = nombre.upper()
 

    datos[property] = {
        'color': color.title(), 
        'material': material.lower(),
        'peso kg': peso,
        'sistema': sistema.upper(),
        'disponible': disponible
    }

    nombre_split = nombre.split(" ")
    nombre = f"{nombre_split[0].capitalize()} {nombre_split[1].upper()}"
    if nombre in bd_objetos:
        if bd_objetos[nombre] != datos[property]:
            bd_objetos[nombre] = datos[property]

            return f"Objeto {nombre}, actualizado en la base de datos"

        return f"El objeto {nombre} Se encuentra en la base de datos"
    
    else:
        bd_objetos.update({nombre: datos[property]})
        return f"El objeto {nombre} se agregó a la base de datos."
        
objetos = bd_objetos()
print(reto_2('mark Vii', 'rojo y ORO', 'ORO Y TITANIO', 200, 'jarvis', True, objetos))
print(objetos.get('Mark VII', 'Objeto no se encuentra en BD.'))

objetos = bd_objetos()
print(reto_2('Mark II', 'Gris', 'TITANIO', 280, 'jarvis', True, objetos))
print(objetos.get('Mark II', 'Objeto no se encuentra en BD.'))

objetos = bd_objetos()
print(reto_2(117108116114111110, 'n/a', 'TITANIO', 280, 'ultron', False, objetos))
print(objetos.get(10101, 'Objeto no se encuentra en BD.'))

objetos = bd_objetos()
print(reto_2('ultron i', 'gris', 'TITANIO', 250, 'ultron', True, objetos))
print(objetos.get('Ultron I', 'Objeto no se encuentra en BD.'))