# Autor: Esteban Francisco Janiot River cod:2191593
# Autor: Santiago Andrés Moreno cod:2221879

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, valor, padre=None, lado="izquierda"):
        nuevo_nodo = Nodo(valor)
        if padre is None:
            if self.raiz is None:
                self.raiz = nuevo_nodo
                print(f"Raíz creada: {nuevo_nodo.valor}")
            else:
                print("El árbol ya tiene una raíz.")
        else:
            if lado == "izquierda":
                if padre.izquierda is None:
                    padre.izquierda = nuevo_nodo
                    print(f"Nodo '{nuevo_nodo.valor}' agregado como hijo izquierdo de '{padre.valor}'")
                else:
                    print(f"El nodo '{padre.valor}' ya tiene un hijo izquierdo.")
            elif lado == "derecha":
                if padre.derecha is None:
                    padre.derecha = nuevo_nodo
                    print(f"Nodo '{nuevo_nodo.valor}' agregado como hijo derecho de '{padre.valor}'")
                else:
                    print(f"El nodo '{padre.valor}' ya tiene un hijo derecho.")
        return nuevo_nodo

    def peso(self):
        def _peso(nodo):
            if nodo is None:
                return 0
            return 1 + _peso(nodo.izquierda) + _peso(nodo.derecha)
        return _peso(self.raiz)

    def orden(self):
        def _orden(nodo):
            if nodo is None:
                return 0
            hijos = 0
            if nodo.izquierda: hijos += 1
            if nodo.derecha: hijos += 1
            return max(hijos, _orden(nodo.izquierda), _orden(nodo.derecha))
        return _orden(self.raiz)

    def altura(self):
        def _altura(nodo):
            if nodo is None:
                return 0
            return 1 + max(_altura(nodo.izquierda), _altura(nodo.derecha))
        return _altura(self.raiz)

if __name__ == "__main__":
    arbol = Arbol()
    print("Creando el árbol...")
    raiz = arbol.agregar_nodo("Raíz")
    nodo1 = arbol.agregar_nodo("Hijo 1", raiz, "izquierda")
    nodo2 = arbol.agregar_nodo("Hijo 2", raiz, "derecha")
    arbol.agregar_nodo("Hijo 1.1", nodo1, "izquierda")
    arbol.agregar_nodo("Hijo 1.2", nodo1, "derecha")
    arbol.agregar_nodo("Hijo 2.1", nodo2, "izquierda")

    print("\n--- Estadísticas del árbol ---")
    print("Peso del árbol:", arbol.peso())
    print("Orden del árbol:", arbol.orden())
    print("Altura del árbol:", arbol.altura())
