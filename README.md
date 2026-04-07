# Taller-Arboles
Taller en clase implementando árboles con POO

## 1. Elaborar un árbol en Python
[arboles_POO.py](https://github.com/mzc07/Taller-Arboles/blob/main/arboles_POO.py)

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
## 3. Algoritmo de codificación de Huffman
La codificación Huffman es un algoritmo de compresión de datos sin pérdida.
-La idea consiste en asignar códigos de longitud variable a los caracteres de entrada, cuya longitud depende de la frecuencia de cada carácter. El método voraz consiste en asignar el código de menor longitud al carácter más frecuente.
-Los códigos de longitud variable asignados a los caracteres de entrada son códigos de prefijo, lo que significa que los códigos (secuencias de bits) se asignan de tal manera que el código asignado a un carácter no es el prefijo del código asignado a ningún otro carácter. Así es como la codificación Huffman garantiza que no haya ambigüedad al decodificar el flujo de bits generado.
***Cómo funciona:***
1. Cuenta con qué frecuencia aparece cada dato.
2. Construye un árbol binario , comenzando con los nodos con el recuento más bajo. El nuevo nodo padre tendrá el recuento combinado de sus nodos hijos.
3. La arista que parte de un nodo padre recibe un valor de '0' para el nodo hijo izquierdo y un valor de '1' para la arista que va al nodo hijo derecho.
4. En el árbol binario finalizado, siga las aristas desde el nodo raíz, agregando '0' o '1' a cada rama, para encontrar el nuevo código Huffman para cada dato.
5. Crea el código Huffman convirtiendo los datos, pieza por pieza, en un código binario utilizando el árbol binario.

La codificación Huffman utiliza una longitud variable de bits para representar cada dato, con una representación de bits más corta para los datos que aparecen con mayor frecuencia.
Además, la codificación Huffman garantiza que ningún código sea el prefijo de otro código, lo que facilita la decodificación de los datos comprimidos.

***La compresión de datos*** consiste en reducir el tamaño de los datos originales, pero conservando la mayor parte de la información. Por ejemplo, los archivos de sonido o música suelen almacenarse en formato comprimido, aproximadamente un 10 % del tamaño original, pero manteniendo la mayor parte de la información.
***Sin pérdida*** significa que, incluso después de comprimir los datos, toda la información permanece intacta. Esto implica que, por ejemplo, un texto comprimido conserva las mismas letras y caracteres que el original.
***La compresión con pérdida*** es otra variante de compresión de datos, donde se pierde o se sacrifica parte de la información original para poder comprimir aún más los datos. La música, las imágenes y los vídeos se suelen almacenar y transmitir con compresión con pérdida, como en los formatos mp3, jpeg y mp4.

### Descifrando el código Huffman
Al igual que con el código almacenado en UTF-8, que nuestros ordenadores ya pueden decodificar a las letras correctas, el ordenador necesita saber qué bits representan qué datos en el código Huffman.
Por lo tanto, junto con un código Huffman, también debe haber una tabla de conversión con información sobre cuál es el código binario Huffman para cada dato, de modo que pueda ser decodificado.

***Cómo funciona:***
1. Empiece por la izquierda en el código Huffman y busque cada secuencia de bits en la tabla.
2. Asocia cada código con la letra correspondiente.
3. Continúa hasta que se descifre todo el código Huffman.

La codificación Huffman se puede utilizar para la compresión sin pérdida de cualquier tipo de datos, no solo texto. También se utiliza como componente en otros algoritmos de compresión como zip, e incluso en compresiones con pérdida como jpeg y mp3.
