def copiar_texto(origen, destino):
    with open(origen, "r") as f1:
        contenido = f1.read()
    with open(destino, "w") as f2:
        f2.write(contenido)


def copiar_binario(origen, destino):
    with open(origen, "rb") as f1:
        data = f1.read()
    with open(destino, "wb") as f2:
        f2.write(data)


copiar_texto(
    r"C:\Users\aless\OneDrive\Desktop\Laboratorio21\alessandro_justo\laboratorio21\ejercicio07\origen.txt",
    r"C:\Users\aless\OneDrive\Desktop\Laboratorio21\alessandro_justo\laboratorio21\ejercicio07\destino.txt"
)

copiar_binario(
    r"C:\Users\aless\OneDrive\Desktop\Laboratorio21\alessandro_justo\laboratorio21\ejercicio07\imagen.jpg",
    r"C:\Users\aless\OneDrive\Desktop\Laboratorio21\alessandro_justo\laboratorio21\ejercicio07\imagen_copia.jpg"
)

print("Archivos copiados correctamente.")
