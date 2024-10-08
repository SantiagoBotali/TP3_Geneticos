import numpy as np

import funciones as f

# Datos de las capitales y sus coordenadas
capitales = [
    ("Buenos Aires", -34.6033, -58.3817),
    ("Córdoba", -31.4167, -64.1833),
    ("Santiago del Estero", -27.7833, -64.2667),
    ("San Juan", -31.5342, -68.5261),
    ("Salta", -24.7833, -65.4167),
    ("Santa Fe", -31.6333, -60.7000),
    ("San Salvador de Jujuy", -24.1833, -65.3000),
    ("Corrientes", -27.4833, -58.8167),
    ("Resistencia", -27.4514, -58.9867),
    ("Posadas", -27.3667, -55.9000),
    ("Paraná", -31.7331, -60.5297),
    ("Formosa", -26.1833, -58.1833),
    ("Neuquén", -38.9525, -68.0642),
    ("La Plata", -34.9211, -57.9544),
    ("La Rioja", -29.4125, -66.8542),
    ("San Luis", -33.3000, -66.3333),
    ("Catamarca", -28.4667, -65.7833),
    ("San Miguel", -26.8167, -65.2167),
    ("Mendoza", -32.8833, -68.8167),
    ("Ushuaia", -54.8019, -68.3031),
    ("Viedma", -40.8, -63),
    ("Río Gallegos", -51.6233, -69.2161),
    ("Rawson", -43.3, -65.1),
    ("Santa Rosa", -36.6167, -64.2833)
]

# Extraer las coordenadas y capitales por separado
nombres, latitudes, longitudes = zip(*capitales)

# Matriz de distancias entre las ciudades
n = len(capitales)
distancias = np.zeros((n, n))

for i in range(n):
    for j in range(i + 1, n):
        distancias[i, j] = distancias[j, i] = f.distancia(
            (latitudes[i], longitudes[i]), (latitudes[j], longitudes[j])
        )


# Menú para seleccionar la ciudad de inicio
def mostrar_menu():
    print("Capitales disponibles:")
    for i, nombre in enumerate(nombres):
        print(f"{i + 1}. {nombre}")
    
    try:
        opcion = int(input("Seleccione el número de la ciudad de inicio: ")) - 1
        if opcion < 0 or opcion >= len(nombres):
            raise ValueError
        return nombres[opcion]
    except ValueError:
        print("Opción inválida. Intente nuevamente.")
        return mostrar_menu()

# Bucle principal iterativo
while True:
    ciudad_inicial = mostrar_menu()

    # Calculo KNN
    mejor_ruta, mejor_distancia = f.tsp_knn(ciudad_inicial, capitales, distancias, nombres)

    # Imprimir la mejor ruta y su distancia
    f.imprimirRuta(ciudad_inicial, nombres, mejor_ruta, mejor_distancia, latitudes, longitudes)

    # Preguntar al usuario si desea continuar
    continuar = input("¿Desea calcular otra ruta? (s/n): ").lower()
    if continuar != 's':
        break
