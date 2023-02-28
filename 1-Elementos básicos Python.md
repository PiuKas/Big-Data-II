## 0- Elementos básicos
Se pueden definir con "" o ''
```Python
"Això és una cadena"
"Això és 'una cadena'  "
```
### 0.1-Comandos
python main.py  --> para llamar al archivo a que se ejecute en la consola de Pycharm
ctrl + L limpia la terminal
ctrl + C mata proceso


## 1- Variables
Se asigna un valor (el que sea) a una variable que creemos
```Python
var=10 #el valor de var será el número 10
var="10" #el valor de var será el string 10
```
En python la variables se sobreescriben
```Python
variable_1=1  
variable_2= 4  
suma= variable_1+ variable_2  #aquí suma=5
print(suma)  
variable_3=5  
suma=variable_1+variable_2+variable_3  #aquí sum =10
print(suma)
```


## 2- Listas 
### 2.1- Definir listas
*lista=[lemento 1, elemento 2]*
```Python
noms= ["Santi", "Abril", "Matias"]  
cognoms = ["Pérez", "López", "Vázquez"]  
print(noms)
#imprimira: Santi, Abril, Matias
```
### 2.2- Anidar listas
Creando una lista que contenga otras
```Python
noms= ["Santi", "Abril", "Matias"]  
cognoms = ["Pérez", "López", "Vázquez"]  
print(noms) #imprimirá ['Santi', 'Abril', 'Matias']
llista = [noms,cognoms]  
print(llista) #imprimirá [['Santi', 'Abril', 'Matias'], ["Pérez", "López", "Vázquez"]]
```
### 2.3-Funciones de las listas
#### 2.3.1- append()
Añade un elemento al final de una lista
*lista.append(elemento)*
```Python
frutas=["platano", "manzana", "pera"]  
frutas.append("higo")  
print(frutas) 
#["platano", "manzana", "pera". "higo"] 
```
#### 2.3.2- extend()
Itera sobe cada uno de los elementos para añadirlos uno a uno en una lista
*lista.append(lista)*
```Python
escuderia=["aston martin", "redbull", "mclaren"]  
piloto=["Fernando Alonso", "Max Verstappen", "Lando Norris"]  
escuderia.extend(piloto)  
print(escuderia)
#['aston martin', 'redbull', 'mclaren', 'Fernando Alonso', 'Max Verstappen', 'Lando Norris']
```


## 3- Iteraciones
### 3.1-For
#### Recorrer una lista e imprimirla
*Ejemplo 1*
```Python 
llista_noms= ["Santi", "Abril", "Matias"]  
for nom in llista_noms: #nom es una variable que yo nombro como quiero, la que recorre  
    print(nom)
#Santi
#Abril
#Matias
```
*Ejemplo 2*
```Python
llista_noms= ["Santi", "Abril", "Matias"]  
for nom in llista_noms:   
    print(f"El {nom} es alto")
#El Santi es alto
#El Abril es alto
#El Matias es alto
```
*Ejemplo 3: sumar a una variable*
```Python
nota=[9, 8, 5, 4]  
plus=0.5  
  
for nota_final in nota: #nota_final=variable que itera  
    resultado=(nota_final+plus) #resultado será la variable que va alternando + plus  
    print(resultado)
```


## 4- Condicionales
If, else y elif
Operadores posibles:  == || <= || >= || < || >
*Ejemplo 1: si hay una Carla en la lista dímelo*
```Python
lista=["Marcos", "Diana", "Xurxo", "Carla", "Marc"]  
#primero tenemos que recorrer la lista con un for  
for nombre in lista:  
    if nombre =="Carla":  
        print("Hay una Carla")
#Hay una Carla
```
*Ejemplo 1.2: comprueba cada nombre y dime si es Carla*
```Python
lista=["Marcos", "Diana", "Xurxo", "Carla", "Marc"]  
#primero tenemos que recorrer la lista con un for  
for nombre in lista:  
    if nombre =="Carla":  
        print("¡Es ella!")  
    else:  
        print(nombre,"no es Carla")
#Marcos no es Carla
#Diana no es Carla
#Xurxo no es Carla
#¡Es ella!
#Marc no es Carla
```
Los condicionales se pueden anidar
*Ejemplo 2: El cálculo se ejecuta si el número es >= 5 y solo se imprimen aquellos resultados >17*
```Python
var=10  
numeros=[1,2,3,4,5,6,7,8,9,10]  
for numerito in numeros:  #siempre hay que recorrer primero 
    if numerito >=5:  
        calculo=numerito + var  
        if calculo >17:  
            print(calculo)
```

## 5- Funciones nativas de python
https://docs.python.org/3/library/functions.html

### 5.0- Básicas
#### Función print()
```Python
def normal (): ##definimos la funcion normal
	print("cosa")
normal() #imprimirá cosa
```
Se puede imprimir más sencillo 
OPCIÓ 1
```Python
seguidors="566"  
print("Aquest usuaris té", seguidors, "seguidors" )
```
OPCIÓ AMB F 
*print(f"frase {variable} frase")*
```python
seguidors="566"
print(f"Aquest usuari té {seguidors} seguidors")
```

#### Convertir número en string
*str(funcion)*
```Python
usuario= "Illo Juan""  
likes=100  
frase_final= ("El usuario" + usuario, "tiene", str(likes), "likes" )  
print(frase_final)
```

#### Convertir string en int
*variable=int(lista)*
```python
lista=["1","2"]
lista_num=int(lista)
```


### 5.1- index()
### 5.2- len()
### 5.3- set()
### 5.4 - count()

