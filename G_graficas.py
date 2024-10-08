import matplotlib.pyplot as plt

# Imprimir la mejor ruta y su distancia
def imprimirRuta(ciudad_inicial, nombres, mejor_ruta, mejor_distancia, latitudes, longitudes):
    print(f"Mejor ruta comenzando desde {ciudad_inicial}:")
    # print([nombres[i] for i in mejor_ruta])
    print(f"Distancia total: {mejor_distancia:.2f} Km")

    # Graficar la ruta
    ruta_completa = mejor_ruta
    ruta_completa.append(mejor_ruta[0])
    plt.figure(figsize=(10, 15))
    plt.scatter(longitudes, latitudes, color='blue')

    # Dibujar la ruta
    for i in range(len(ruta_completa) - 1):
        plt.plot(
            [longitudes[ruta_completa[i]-1], longitudes[ruta_completa[i + 1]-1]],
            [latitudes[ruta_completa[i]-1], latitudes[ruta_completa[i + 1]-1]],
            color='red'
        )

    # Añadir nombres de las ciudades
    for i, nombre in enumerate(nombres):
        plt.text(longitudes[i], latitudes[i], nombre, fontsize=9, ha='right')

    # Configurar el gráfico
    plt.title(f"Ruta más corta entre capitales de Argentina comenzando en {ciudad_inicial} :" + f"{mejor_distancia:.2f} Km")
    plt.xlabel("Longitud")
    plt.ylabel("Latitud")
    plt.grid(True)
    plt.show()