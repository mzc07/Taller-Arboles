# Archivo: arboles_POO.py
# Autores: Martín Ariza (2251516) - Juliana Rueda (2251801) - Ivanna Alvarez (2251805)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijo = None
        self.hermano = None

class Arbol:
    def __init__(self, raiz):
        self.raiz = Nodo(raiz)

    def agregar_hijo(self, nodo, dato_hijo):
        nuevo = Nodo(dato_hijo)
        if nodo.hijo is None:
            nodo.hijo = nuevo
        else:
            actual = nodo.hijo
            while actual.hermano:
                actual = actual.hermano
            actual.hermano = nuevo

    def buscar(self, nodo, valor):
        if nodo is None:
            return None
        if nodo.dato == valor:
            return nodo
        encontrado = self.buscar(nodo.hijo, valor)
        if encontrado:
            return encontrado

        return self.buscar(nodo.hermano, valor)

    def peso(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.peso(nodo.hijo) + self.peso(nodo.hermano)

    def orden(self, nodo):
        if nodo is None:
            return 0
        count = 0
        actual = nodo.hijo

        while actual:
            count += 1
            actual = actual.hermano

        max_sub = max(self.orden(nodo.hijo), self.orden(nodo.hermano))

        return max(count, max_sub)

    def altura(self, nodo):
        if nodo is None:
            return 0

        max_altura_hijos = 0
        actual = nodo.hijo



        while actual:
            max_altura_hijos = max(max_altura_hijos, self.altura(actual))
            actual = actual.hermano

        return 1 + max_altura_hijos

raiz = input("Ingrese el valor de la raíz: ")
arbol = Arbol(raiz)

while True:
    padre = input("Ingrese el nodo padre (o 'salir'): ")
    if padre.lower() == "salir":
        break

    nodo_padre = arbol.buscar(arbol.raiz, padre)

    if nodo_padre:
        hijo = input("Ingrese el valor del hijo: ")
        arbol.agregar_hijo(nodo_padre, hijo)
    else:
        print("Nodo padre no encontrado")

print("\n--- RESULTADOS ---")
print("Peso del árbol:", arbol.peso(arbol.raiz))
print("Orden del árbol:", arbol.orden(arbol.raiz))
print("Altura del árbol:", arbol.altura(arbol.raiz))
