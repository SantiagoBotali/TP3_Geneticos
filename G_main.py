import numpy as np

import G_funciones as f

# Datos de las capitales y sus coordenadas
capitales = [
    ("Ciudad Autónoma de Buenos Aires", -34.6033, -58.3817, 1),
    ("Córdoba", -31.4167, -64.1833, 2),
    ("Santiago del Estero", -27.7833, -64.2667, 3),
    ("San Juan", -31.5342, -68.5261, 4),
    ("Salta", -24.7833, -65.4167, 5),
    ("Santa Fe", -31.6333, -60.7000, 6),
    ("San Salvador de Jujuy", -24.1833, -65.3000, 7),
    ("Corrientes", -27.4833, -58.8167, 8),
    ("Resistencia", -27.4514, -58.9867, 9),
    ("Posadas", -27.3667, -55.9000, 10),
    ("Paraná", -31.7331, -60.5297, 11),
    ("Formosa", -26.1833, -58.1833, 12),
    ("Neuquén", -38.9525, -68.0642, 13),
    ("La Plata", -34.9211, -57.9544, 14),
    ("La Rioja", -29.4125, -66.8542, 15),
    ("San Luis", -33.3000, -66.3333, 16),
    ("Catamarca", -28.4667, -65.7833, 17),
    ("San Miguel", -26.8167, -65.2167, 18),
    ("Mendoza", -32.8833, -68.8167, 19),
    ("Ushuaia", -54.8019, -68.3031, 20),
    ("Viedma", -40.8, -63, 21),
    ("Río Gallegos", -51.6233, -69.2161, 22),
    ("Rawson", -43.3, -65.1, 23),
    ("Santa Rosa", -36.6167, -64.2833, 24)
]

# Extraer las coordenadas y capitales por separado
nombres, latitudes, longitudes, indices = zip(*capitales)

# Matriz de distancias entre las ciudades
n = len(capitales)
distancias = np.zeros((n, n))

for i in range(n):
    for j in range(i + 1, n):
        distancias[i, j] = distancias[j, i] = f.distancia(
            (latitudes[i], longitudes[i]), (latitudes[j], longitudes[j])
        )


# Cromosomas de la poblacion
N = 50
# Cantidad de ciclos
ciclos = 200
# Probabilidad de mutacion
Pm = 0.05
# Probabilidad de cruce
Pc = 0.7

metodo = int(input("Ingrese el metodo de seleccion: 1. Ruleta 2. Torneo: "))
while (metodo != 1 and metodo != 2):
    metodo = int(input("Ingrese el metodo de seleccion: 1. Ruleta 2. Torneo: "))

print("Capitales disponibles:")
for i, nombre in enumerate(nombres):
    print(f"{i + 1}. {nombre}")

ciudad_inicio = int(input("Ingrese la ciudad de inicio: "))
while ciudad_inicio <0 or ciudad_inicio>=len(nombres):
    ciudad_inicio = int(input("Ingrese la ciudad de inicio: "))

# Crear la poblacion inicial
poblacion = f.llenarPoblacion(N, ciudad_inicio)
print(poblacion)

for c in range(ciclos):
    # arreglo de fitness
    fitness = [f.fitness(cromosoma, distancias) for cromosoma in poblacion] 
    # Seleccion de padres
    if metodo == 1:
        padres = f.seleccionRuleta(poblacion, fitness)
    else:
        padres = f.seleccionTorneo(poblacion, fitness)

    hijos = []
    for i in range(0, len(padres)-1, 2):
        hijo1, hijo2 = (f.cruce(padres[i], padres[i+1], Pc))
        hijos.append(hijo1)
        hijos.append(hijo2)
    
    for cromosoma in hijos:
        print("cromosoma", cromosoma)
        cromosoma = f.mutacion(cromosoma, Pm)
    
    poblacion = hijos

    poblacion.sort(key=lambda x: f.fitness(x, distancias))

    mejor_ruta = poblacion[0]
    print(f"Mejor ruta, ciclo {c+1}: {mejor_ruta}")
    print(f"Distancia: {f.fitness(mejor_ruta, distancias)}")
