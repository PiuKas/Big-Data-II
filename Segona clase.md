# Ejercicios básicos
## Ejercicio 1
```python
cadena= "esto es un ejercicio"  
print(cadena)  
nota=9,75  
asig="analitica digital"  
nota=10  
frase=print(f"En la asignatura {asig} he tret un {nota}")
#esto es un ejercicio"
#En la asignatura analitica digital he tret un 10

```
## Ejercicio 2
```python
notas = ["5", "7", "6", "4", "8", "2"]  
alumnos = ["jaume", "carla", "pere", "adria", "rafael", "agnes"]  
# sumar 1 punto a cada nota  
for nota in notas:  
    nota_numerica = int(nota)  
    print(nota_numerica + 1)
```


# Ejercicios de obtención de datos
## Ejercicio 1
```python
#La UAB acaba de celebrar sus jornadas de puertas abiertas y los futuros estudiantes han acudido a las sesiones informativas. Cada vez que una persona entra en una sesión se anota su nombre. Alguien ha juntado todos los nombres en una sola lista... ¿Puedes sacar información útil de este listado?
llista = [  
    "david",  
    "dani",  
    "marta",  
    "jaume",  
    "adria",  
    "carla",  
    "joan",  
    "pere",  
    "carla",  
    "pere",  
    "adria",  
    "quico",  
    "pere",  
    "joan",  
    "agustí",  
    "adria",  
    "joan",  
    "adria",  
    "siscu",  
    "carles",  
    "dani",  
    "carla"  
    ]  
  
#CUANTAS PERSONAS HAN ASISTIDO A LAS JORNADAS DE PUERTAS ABIERTAS
asistentes=set(llista) #te immprimirá la lista de los asistentes sin repetir  
total_asistentes=(len(asistentes)) #te imprime el número de personas  
print(f"Han vingut {total_asistentes} asistents")  
  
#CUANTAS PERSONAS HAN ASISTIDO A MÁS DE DOS SESIONES
    #Se hará con un contadorllista_repetidos=[]
llista_repetidos=[]  
for nom in asistentes:  
    numero_veces=llista.count(nom) #seteamos contador  
    if numero_veces > 2:  
        llista_repetidos.append(nom)  
Num_repetidos=(len(llista_repetidos))  
print(f"{Num_repetidos} assistents han vingut a més de dos sesions")

#Han vingut 12 asistents
#4 assistents han vingut a més de dos sesions
#Ha habido un porcentaje de 33.33333333333333 de asistentes



#QUÉ PORCENTAJE DE LOS ASISTENTES ACCEDE A MÁS DE DOS SESIONES
```

  