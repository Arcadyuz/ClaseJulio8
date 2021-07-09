def reto_1(nombre: str, apellido: str, id: int, tiempo1: float, tiempo2: float, tiempo3: float) -> str: 
 codigo = f"{nombre[0]}{apellido[0]}{id}"
 promedio = round((tiempo1+tiempo2+tiempo3)/3,2)
 mejor_tiempo = min(tiempo1, tiempo2, tiempo3)
 mejor_velocidad = round(100/mejor_tiempo,2)
 return f"Participante {codigo}: \nTiempo promedio: {promedio}s\nMejor_Tiempo: {mejor_tiempo}s\nVel Max: {mejor_velocidad}m/s"


#print(reto_1("Usain", "Bolt", 246810, 9.58, 9.63, 9.72)) 

#print(reto_1("Tayson", "Gray", 135790, 9.69, 9.88, 10.0))

#print(reto_1("Yohan", "Blake", 102365, 9.69, 9.75, 9.76))

print(reto_1("Lizzeth", "Yela", 201423, 30, 25, 5.566)) 