# ArbolesUIS
# Esteban Francisco Janiot Rivera cod:2191593
# Santiago Andrés Moreno cod:2221879

#  Proyecto de Estructuras de Árboles en Python

Este proyecto contiene dos implementaciones de árboles en Python:

1.  Un **árbol binario** implementado desde cero sin librerías externas.
2.  Un **árbol no binario** utilizando la librería externa `BigTree`.

También incluye una breve investigación sobre los **Árboles de Huffman**, utilizados en compresión de datos.

---

##  Archivos incluidos

- `Arbol.py`: Implementación de un árbol binario con clases personalizadas.
- `arbol_con_libreria.py`: Implementación de un árbol no binario con `BigTree`.

---

##  1. Árbol Binario Personalizado (`Arbol.py`)

###  Descripción

Este archivo implementa un **árbol binario**, donde cada nodo puede tener como máximo dos hijos: izquierdo y derecho. Se puede usar para representar estructuras jerárquicas simples.

###  Clases y métodos

- `NodoArbol`:
  - Contiene un valor, un hijo izquierdo y uno derecho.
- `ArbolBinario`:
  - `crear_raiz(valor)`: Crea la raíz del árbol.
  - `insertar_izquierda(padre, valor)`: Inserta un nodo a la izquierda.
  - `insertar_derecha(padre, valor)`: Inserta un nodo a la derecha.
  - `buscar(valor)`: Busca un nodo en el árbol.
  - `peso(nodo)`: Calcula el número total de nodos en el árbol (peso).

###  Consideración importante

El método `peso()` se debe usar de forma recursiva asegurando que el nodo no sea `None`, para evitar errores como:

```
RecursionError: maximum recursion depth exceeded
```

Se recomienda utilizar una lógica como:

```python
def peso(self, nodo=None):
    if nodo is None:
        return 0
    return 1 + self.peso(nodo.izquierda) + self.peso(nodo.derecha)
```

---

##  2. Árbol No Binario con BigTree (`arbol_con_libreria.py`)

###  Descripción

Este script demuestra el uso de la librería `BigTree` para construir árboles **no binarios**, donde cada nodo puede tener múltiples hijos.

###  Instalación

```bash
pip install bigtree
```

###  Estructura del árbol

```plaintext
Empresa
├── Gerencia
│   ├── Finanzas
│   └── Talento Humano
└── Tecnología
    ├── Desarrollo
    ├── Soporte
    └── Seguridad
```

###  Funciones utilizadas

- `Node(nombre, parent=padre)`: Crea un nodo hijo con su nodo padre.
- `print_tree(raiz)`: Muestra el árbol en consola.

---

##  3. Investigación: Árboles de Huffman

###  ¿Qué son?

Un **Árbol de Huffman** es un tipo especial de árbol binario utilizado para **compresión de datos sin pérdida**, asignando códigos binarios más cortos a los símbolos más frecuentes.

###  ¿Cómo funciona?

1. Se listan todos los símbolos con sus frecuencias.
2. Se crean nodos hoja para cada símbolo.
3. Se combinan los dos nodos con menor frecuencia en un nuevo nodo.
4. Se repite hasta formar un solo árbol.
5. Los códigos se generan recorriendo el árbol:
   - Hijo izquierdo = 0
   - Hijo derecho = 1

###  Ejemplo

| Símbolo | Frecuencia | Código |
|---------|------------|--------|
| A       | 5          | 10     |
| B       | 9          | 11     |
| C       | 12         | 0      |

###  Ventajas

- Produce una codificación óptima.
- Muy usado en algoritmos como ZIP, GZIP, JPEG, MP3.
- Algoritmo determinístico y eficiente.

###  Aplicaciones

- Compresión de texto e imágenes.
- Transmisión eficiente de datos.
- Compiladores y estructuras de datos.

---

