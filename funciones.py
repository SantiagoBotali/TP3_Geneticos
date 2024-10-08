import numpy as np

# Función para calcular la distancia euclidiana entre dos puntos
def distancia(p1, p2):
    lat_diff = (p1[0] - p2[0]) * 111  # Convertir latitud a km (Distancia Euclidiana)
    lon_diff = (p1[1] - p2[1]) * 85    # Convertir longitud a km (promedio)
    return np.sqrt(lat_diff**2 + lon_diff**2)

# Implementación de un algoritmo tipo KNN
def tsp_knn(ciudad_inicio, capitales, distancias, nombres):
    n = len(capitales)
    inicio = nombres.index(ciudad_inicio)  # Obtener el índice de la ciudad inicial
    visitadas = [inicio]  # Lista de ciudades visitadas
    distancia_total = 0

    while len(visitadas) < len(capitales):
        ciudad_actual = visitadas[-1]
        # Encontrar la ciudad más cercana que no fue visitada
        distancias_restantes = [(i, distancias[ciudad_actual, i]) for i in range(n) if i not in visitadas]
        proxima_ciudad = min(distancias_restantes, key=lambda x: x[1])[0]
        visitadas.append(proxima_ciudad)
        distancia_total += distancias[ciudad_actual, proxima_ciudad]

    # Volver a la ciudad inicial
    distancia_total += distancias[visitadas[-1], inicio]
    visitadas.append(inicio)

    return visitadas, distancia_total