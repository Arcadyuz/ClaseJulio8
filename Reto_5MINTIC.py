import pandas as pd
import numpy as np

def reto_5(ruta_archivo: str) ->list:
    ruta_archivo = pd.read_csv(ruta_archivo)


   # Calcular Puntaje
    ruta_archivo['PUNTAJE'] = ruta_archivo['MATEMATICA'] + ruta_archivo['LENGUAJE'] + ruta_archivo['CIENCIAS'] + ruta_archivo['CIUDADANAS'] + ruta_archivo['IDIOMAS']


    by_puntaje = ruta_archivo.sort_values('PUNTAJE', ascending=False).head()
    by_puntaje = by_puntaje[['ESTUDIANTE', 'PUNTAJE']]
    puestos = [1, 2, 3, 4, 5]
    posiciones = by_puntaje.set_index(np.array(puestos))
    posiciones.index.name = 'PUESTO'
    promedio = pd.DataFrame(ruta_archivo.mean().round(2), columns = ["PROMEDIO"])
    promedio.index.name = 'PRUEBAS'

    
    return [posiciones, promedio]

top, promedio = reto_5('https://raw.githubusercontent.com/JParrales/mision-tic-2021 ciclo_python/master/G25/Reto%205/notas.csv')
print('Tabla 1:\n', top)
print('\nTabla 2:\n', promedio)	

top, promedio = reto_5('https://raw.githubusercontent.com/JParrales/mision-tic-2021-ciclo_python/master/G85/Reto%205/resultados.csv')
print('Tabla 1:\n', top)
print('\nTabla 2:\n', promedio)