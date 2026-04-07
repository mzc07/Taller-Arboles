# Taller-Arboles
Taller en clase implementando árboles con POO

## 1. Elaborar un árbol en Python
[[arboles_POO.py]]

## 2. Ejemplo de implementación

### Librería Bigtree
BigTree es una librería de Python que nos facilita la vida a la hora de trabajar estructuras de datos jerárquicas como árboles y grafos acíclicos no dirigidos (DAG). Se caracteriza por ser altamente extensible. Nos permite construir estas estructuras a partir de listas, diccionarios, DataFrames, etc; Realizar recorridos de preorden, postorden y por niveles; Buscar y filtrar nodos y exportar a multiples formatos como JSON, dict y gráficos. Todo esto sin restringir el número de hijos por lo que permite implementar arboles no binarios de forma natural


### Ejemplo de implementación de un árbol no binario usando bigtree
```
from bigtree import Tree
path_list = ["a/b/d", "a/b/e/g", "a/b/e/h", "a/c/f"]
tree = Tree.from_list(path_list)
tree.plot("-ok")
<Figure size 1280x960 with 1 Axes>
```
## 3.
