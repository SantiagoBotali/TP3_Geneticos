import numpy as np
import random

def distancia(p1, p2):
    lat_diff = (p1[0] - p2[0]) * 111  # Convertir latitud a km (Distancia Euclidiana)
    lon_diff = (p1[1] - p2[1]) * 85    # Convertir longitud a km (promedio)
    return np.sqrt(lat_diff**2 + lon_diff**2)

def crearCromosoma(indice_inicio):
    rango = list(range(1, 25))  # Crear una lista con los índices de las ciudades
    rango.remove(indice_inicio)  # Eliminar el índice_inicio de la lista
    cromosoma = random.sample(rango, 23)  # Crear una muestra de 23 elementos
    cromosoma.insert(0, indice_inicio)  # Insertar el indice_inicio al principio del cromosoma
    return cromosoma

def llenarPoblacion(cantCromosomas, indice_inicio):
    poblacion = []
    for _ in range(cantCromosomas):
        poblacion.append(crearCromosoma(indice_inicio))
    return poblacion

# Calcular la aptitud (distancia total) de un cromosoma
def fitness(cromosoma, matriz_distancias):
    distancia = 0
    for i in range(len(cromosoma) - 1):
        distancia += matriz_distancias[cromosoma[i]-1][cromosoma[i + 1]-1]
    distancia += matriz_distancias[cromosoma[-1]-1][cromosoma[0]-1]  # Cerrar el ciclo
    return distancia


def seleccionTorneo(poblacion, fitness):
    padres = []
    n = len(poblacion)
    for _ in range(n):
        torneo = random.sample(list(enumerate(fitness)), 5)
        torneo.sort(key=lambda x: x[1])
        padres.append(poblacion[torneo[0][0]])
    return padres

# Crossover cíclico entre dos padres
def cruce(padre1, padre2, prob_cruce):
    if random.random() > prob_cruce:
        # Si no se cumple la probabilidad, se devuelven los padres tal cual
        return padre1[:], padre2[:]
    
    size = len(padre1)
    hijo1 = [-1] * size  # Inicializa el hijo 1 con -1
    hijo2 = [-1] * size  # Inicializa el hijo 2 con -1
    
    # Crear el primer ciclo para hijo1
    index = 0
    while hijo1[index] == -1:
        hijo1[index] = padre1[index]
        index = padre1.index(padre2[index])
    
    # Completar el hijo 1 con los elementos restantes del padre2
    for i in range(size):
        if hijo1[i] == -1:
            hijo1[i] = padre2[i]
    
    # Crear el primer ciclo para hijo2
    index = 0
    while hijo2[index] == -1:
        hijo2[index] = padre2[index]
        index = padre2.index(padre1[index])
    
    # Completar el hijo 2 con los elementos restantes del padre1
    for i in range(size):
        if hijo2[i] == -1:
            hijo2[i] = padre1[i]
    
    return hijo1, hijo2

def mutacion(cromosoma, Pm):
    if(random.random() < Pm):
        print("Mutacion!!!! MUTANTEEEEEEE  -O.O-")
        print("cromo antes de mutar", cromosoma)
        i = random.randint(1, len(cromosoma) - 1)
        j = random.randint(1, len(cromosoma) - 1)
        aux = cromosoma[i]
        cromosoma[i] = cromosoma[j]
        cromosoma[j] = aux
        print("cromo despues de mutar", cromosoma)

    # return cromosoma

