import pandas as pd #importamos pandas

#GENERA UN NUEVO DATASET QUE CONTENTA(ÚNICAMENTE) LOS DATOS NECESARIOS PARA RESPONDER A LA PREGUNTA
df=pd.read_csv("feb_23_es_simple.csv", #Creamos el df leyendo el csv que nos dan
               sep="\t",#Indicamos al código que la inforomación está separada por tabulador
               usecols= ["captured_at","streamer_name","viewer_count","game_name"]) #Cogemos las variables necesarias para los ejercicios


#1-¿CUÁL HA SIDO LA EVOLUCIÓN DE LOS ESPECTADORES (CAPTURA A CAPTURA) DURANTE EL PERIODO?
df_ej1=df.groupby("captured_at")["viewer_count"].sum().reset_index() #Agrupamos la información por captured_at y sumamosel viewer count de cada captured_at --> groupby("segun qué agrupas")["lo que te suma")
df_ej1.to_csv("Ejercicio_1.csv") #Creamos el csv para trabajar con Tableau

#2-¿CUÁLES SON LAS CATEGORÍAS MÁS VISTAS Y EN LAS QUE MÁS HORAS DE DIRECTO SE HAN REALIZADO?
df.ej2=df.groupby("game_name")["viewer_count"].sum().reset_index() #Agrupamos para analizar las categorías más vistas
df.ej2_pt2=df["game_name"].value_counts().reset_index() #Usamos value_counts para mirar el número de captured_at de cada juego que utilizaremos para mirar las horas de directo
df.ej2_pt2.rename(columns = {'game_name':'capturas', 'index':'game_name'}, inplace = True) #Renombramos las columnas correctamente
#unimos los dos dataframes
ejercicio_2=pd.merge(df.ej2,df.ej2_pt2)
ejercicio_2.to_csv("Ejercicio2.csv") #Creamos el csv para trabajar con Tableau

#3-¿CÓMO HAN EVOLUCIONADO (captura a captura) ESTAS CATEGORIAS A LO LARGO DEL MES?
df.ej3=df.groupby(["captured_at","game_name"])["viewer_count"].sum().reset_index() #Generamos un dataframe organizado por capturas, juegos y viewer_count. Cuántos viewers ha tenido cada juego en cada captura
df.ej3.to_csv("Ejercicio3.csv")

#4-¿CUÁL ES LA DISTRIBUCIÓN DE LOS STREAMERS SI LOS CLASIFICAMOS POR VOLÚMENES DE AUDIENCIA Y HORAS REALIZADAS?
df.ej4=df.groupby("streamer_name")["viewer_count"].sum().reset_index() #Agrupamos para analizar los streamers más vistos
df.ej4_pt2=df["streamer_name"].value_counts().reset_index() 
df.ej4_pt2.rename(columns = {'streamer_name':'capturas', 'index':'streamer_name'}, inplace = True) #Renombramos como queremos para trabajar con Tableau
#unimos los dos dataframes
ejercicio_4=pd.merge(df.ej4,df.ej4_pt2) 
ejercicio_4.to_csv("Ejercicio4.csv") #creamos el csv para trabajar con Tableau

#5¿CUÁL HA SIDO LA EVOLUCIÓN (captura a captura) DE LA DESVIACIÓN ESTÁNDAR EN EL VOLÚMEN DE ESPECTADORES?
df.ej5=df.groupby("captured_at")["viewer_count"].std().reset_index() #std() calcula la desviación estandar
df.ej5.rename(columns = {'viewer_count':'desviacion'}, inplace = True) #Renombramos la columna correctamente de "viewer_count" a "desviación"
df.ej5.to_csv("Ejercicio5.csv", decimal=",") #creamos el csv para trabajar con Tableau




