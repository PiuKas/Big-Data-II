
### Saber la posición de un elemento en una lista
lista.index(variable_iteradora)
```python
#COMPROBAR QUE UN ELEMENTO ESTÁ EN UNA LISTA I EN QUÉ POSICIÓN
llista=["adrian","carla","joan","pere","josep"]  
nom="josep"  
#check de si el joan está a la llista  
if nom in llista:  
    print("si")  
    position=llista.index(nom)  
    print(position)  
else:  
    print("no")
#si
#4
```
### Comprobar valores únicos de una lista
set(lista)
Te imprime los elementos únicos de una lista
```python
llista=["adrian","carla","carla","pere","josep"]  
valors_unics=set(llista)  
print(valors_unics)
#adrian
#pere
#josep
```
### Longitud lista
len(lista)
Te imprime el número de elementos que hay en una lista
```python
llista=["adrian","carla","carla","pere","josep"]  
longitud=len(llista)  
print(longitud)
#5
```
### Emparejar listas
La funcion zip permite ir iterando dos listas a la vez
```python
notas = ["5", "7", "6", "4", "8", "2"]  
alumnos = ["jaume", "carla", "pere", "adria", "rafael", "agnes"]  
  
for nota, nom in zip(notas,alumnos):  #nota i nom son les variables que iteren en notas i alumnos  
    nota_numerica = int(nota)  
# sumar 1 punto a cada nota  
    nota_final=nota_numerica+1  
#imprimir el resultado junto al nombre de cada alumno  
    print(nota_final,nom)
```
### Contador
llista.count(variable)
# Ejemplos
```python
notas = ["5", "7", "6", "4", "8", "2"]  
alumnos = ["jaume", "carla", "pere", "adria", "rafael", "agnes"]  
  
for nota, nom in zip(notas,alumnos):  #nota i nom son les variables que iteren en notas i alumnos  
    nota_numerica = int(nota)  
# sumar 1 punto a cada nota  
    nota_final=nota_numerica+1  
#imprimir el resultado junto al nombre de cada alumno  
    print(nota_final,nom)

```
## Ejemplos
Sumar +2 a una nota
```Python
numeros = [1,2,3,4,5,6,7,8,9,10]  
afegir=2  
for nota in numeros:  
    print(nota+afegir)

```