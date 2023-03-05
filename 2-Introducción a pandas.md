## 0-Ejercicios
Tarea 1: Unificar los nombres y apellidos de los alumnos en una única cadena de texto
```Python
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]    
noms_complets=[] #creamos una lista vacia para meter los nombres  
for nom, cognom in zip(alumnes,cognoms):  
   nom_complet=f"{nom} {cognom}"  #así te junta nombre y apellido como uno  
   noms_complets.append(nom_complet)  
print(noms_complets)
```
Tarea 2: Crear una lista de "tuplas" que contengan los datos del alumno unificados, y la nota obtenida
*Manera 1*
```Python
for nota, nom_F in zip(notes,noms_complets): #itero sobre la lista de notas y la lista creada antes  
   print(nom_F, nota)
```
*Manera 2*
```Python
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  

lista_de_tuples=[] #creamos una lista vacia para meter los nombres    
for nom, cognom, nota in zip(alumnes,cognoms,notes): #podemos trabajar las 3 listas a la vez  
   nom_complet=f"{nom} {cognom}"  #así te junta nombre y apellido como uno  
   tupla= (nom_complet, nota) #cada nombre que se procesa va a una tupla  
   llista_de_tuples.append(tupla)  #creamos lista de tuplas  
print(llista_de_tuples)
```
**Tarea 3:** Sumar un punto a todas la notas, sin que puedan sobrepasar el 10
```Python
#ABRIENDO TUPLAS  
  
for persona in llista_de_tuples:  
   nota_nova=persona[1]+1 #la nota esta en la posición 2 de la tupla y así lo suma de cada vez  
   if nota_nova>10: #si al sumar 1 es >10, lo dejas en 10 porque no puede ser más  
      nota_nova=10  
   nova_persona= (persona[0],nota_nova)  
   print(nova_persona) #para imprimir notas actualizadas
```
**Tarea 4:** Añadir un tercer elemento a la tupla siguiendo este criterio:  
- Si la nota final es inferior a 5, añadir el texto "suspendido".  
- Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".  
- Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".  
- Si la nota es igual o superior a 7, añadir el texto "notable".  
- Si la nota supera el 9, añadir el texto "Excelente".  
- Si la nota equivale a un 10, añadir el texto "matrícula de honor".
```Python
notes = [1,6,8,9,10,6,5]  
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]  
cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]  
  
llista_de_tuples=[] #creamos una lista vacia para meter los nombres  
  
for nom, cognom, nota in zip(alumnes,cognoms,notes): #podemos trabajar las 3 listas a la vez  
   nom_complet=f"{nom} {cognom}"  #así te junta nombre y apellido como uno  
   tupla= (nom_complet, nota) #cada nombre que se procesa va a una tupla  
   llista_de_tuples.append(tupla)  #creamos lista de tuplas  
print(llista_de_tuples)  
  
  
for persona in llista_de_tuples:  
   nota_nova=persona[1]+1 #la nota esta en la posición 2 de la tupla y así lo suma de cada vez  
   if nota_nova>10: #si al sumar 1 es >10, lo dejas en 10 porque no puede ser más  
      nota_nova=10  
   if nota_nova<5: #- Si la nota final es inferior a 5, añadir el texto "suspendido".  
      quali="suspendido"  
   elif nota_nova >=5 and nota_nova <=6: #- Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".  
      quali="aprobado"  
   elif nota_nova>6 and nota_nova<7: # - Si la nota es superior a 6, e inferior a 7, añadir el texto "bien"  
      quali="bien"  
   elif nota_nova >=7 and nota_nova<9:#- Si la nota es igual o superior a 7, añadir el texto "notable".  
      quali="notable"  
   elif nota_nova >=9 and nota_nova<10: #- Si la nota supera el 9, añadir el texto "Excelente".  
      quali="excelente"  
   elif nota_nova==10: #- Si la nota equivale a un 10, añadir el texto "matrícula de honor".  
      quali="matricula d'honor"  
  
   nova_persona= (persona[0],nota_nova,quali) ##AÑADIMOS AQUÍ LA QUALI  
   print(nova_persona) #para imprimir notas actualizadas + nombres**
```
## 1-Importar en pandas
*Al principio del archivo hay que poner:* import pandas as pd
*En la consola:* pip install pandas 
### 1.1-Crear un dataframe
*Se crea una variable, normalmente df al final del documento*
```Python
df=pd.DataFrame({ #el pd de "import pandas as pd"
	"col1" : algo,
	"col2" :algo_1,
	"col3" : alguna_cosa,
	})
#estamos declarando una lista de tuplas

```
### 1.2-Crear un dataset 
```Python
df=pd.DataFrame(llista_definitiva, columns= ["nom","nota","quali"])
df.to_csv("dataset.csv") #al ejecutar el archivo python crea un dataset
```
### 1.3-Crear un excel
```Python
df=pd.DataFrame(llista_definitiva, columns= ["nom","nota","quali"])
df.to_excel("dataset.xlsx") #al ejecutar el archivo python crea un dataset
```
### 1.4- Pandas read de docs
https://pandas.pydata.org/docs/user_guide/index.html#user-guide
Sitio en el que consultar 

## 2-Importar un json
Un json es un archivo que contiene una lista de {"key" : "valor" }, es decir, diccionarios.
*Cargar el archivo*
```Python
import json #importamos esta libreria  
  
f=open("medidas.json") #CARGAR EL ARCHIVO
print(f)  
data=json.load(f) #TRANSFORMAR EN DICCIONARIOS
#si imprimimos eso, nos enseñará todos los datos
```
*Imprimir cada pareja*
```Python
import json #importamos esta libreria  
  
f=open("medidas.json")  
print(f)  
data=json.load(f) 
  
#bucle que me imprime cada cosa por separado  
for d in data:  
    print(d)  

```
*Queremos imprimir solo 1 valor*
```Python
import json 
f=open("medidas.json") 
print(f)  
data=json.load(f)  
  
for d in data:  
    print(d["temperatura"]) #accedemos a una variable
```
*Imprimos dos variables*
```Python
import json   
f=open("medidas.json") 
print(f)  
data=json.load(f)   
for d in data:  
    print(f'{d["fecha"]} {d["temperatura"]}')
```

## Ejercicios
¿Cuantas muestras ha capturado el sensor?
```Python
import json #importamos esta libreria  
  
f=open("medidas.json") #cargamos el archivo json  
print(f)  
data=json.load(f)  
  
print(len(data))
```
Transformar los datos a un formato .csv para poder manipularlos con Excel/8ableau y hacer las gráficas evolutivas
```Python
import json #importamos esta libreria  
import panda as pd  
  
f=open("medidas.json") #cargamos el archivo json  
print(f)  
data=json.load(f)  
  
llista_dades=[0]  
for d in data:  
    temp=d["temperatura"]  
    pres=d["presion"]  
    date=d["fecha"]  
    tupla=(temp,pres,date)  
    llista_dades.append(tupla)  
  
  
df=pd.DataFrame(llista_dades, columns=["temp","pres","data"])  #convertimos a dataframe
print(df)
df.to_csv(temperaturas.csv, index=False, decimal=",") #exportamos y creamos doc
```