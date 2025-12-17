class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")
        else:
            print(f"Libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"Libro '{self.titulo}' devuelto.")

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({estado})"


class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamañoMB):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tamañoMB = tamañoMB

    def prestar(self):
        print(f"Libro digital '{self.titulo}' siempre disponible.")


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        for libro in self.libros:
            print(libro)

    def buscar_por_autor(self, autor):
        for libro in self.libros:
            if libro.autor == autor:
                print(libro)

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.prestar()
                return
        print("Libro no encontrado.")

biblio = Biblioteca()

l1 = Libro("Python Básico", "Ana Pérez", 2020)
l2 = Libro("Java Avanzado", "Juan Díaz", 2019)
l3 = Libro("Algoritmos", "Ana Pérez", 2018)

d1 = LibroDigital("IA Moderna", "Carlos Ruiz", 2022, "PDF", 5)
d2 = LibroDigital("Big Data", "Carlos Ruiz", 2021, "EPUB", 8)

biblio.agregar_libro(l1)
biblio.agregar_libro(l2)
biblio.agregar_libro(l3)
biblio.agregar_libro(d1)
biblio.agregar_libro(d2)

print("\n--- Listar libros ---")
biblio.listar_libros()

print("\n--- Prestar libro físico ---")
biblio.prestar_libro("Python Básico")

print("\n--- Prestar libro digital 5 veces ---")
for _ in range(5):
    biblio.prestar_libro("IA Moderna")

print("\n--- Intentar prestar libro ya prestado ---")
biblio.prestar_libro("Python Básico")

print("\n--- Buscar libros por autor ---")
biblio.buscar_por_autor("Ana Pérez")

