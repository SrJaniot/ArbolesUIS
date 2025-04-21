# pip install bigtree

from bigtree import Node, print_tree

# Crear el nodo raíz
empresa = Node("Empresa")

# Crear ramas principales
gerencia = Node("Gerencia", parent=empresa)
tecnologia = Node("Tecnología", parent=empresa)

# Agregar hijos a Gerencia
finanzas = Node("Finanzas", parent=gerencia)
talento = Node("Talento Humano", parent=gerencia)

# Agregar hijos a Tecnología
desarrollo = Node("Desarrollo", parent=tecnologia)
soporte = Node("Soporte", parent=tecnologia)
seguridad = Node("Seguridad", parent=tecnologia)

# Imprimir estructura
print_tree(empresa)

