import pandas as pd
import json
import glob  # Para poder leer todos los archivos
import tqdm as tqdm  # Sirve para indicar el porcentaje que llevamos de datos recabados

files = glob.glob("archivos_json_ej/*")  # Le decimos que coja todos los de esa carpeta que sean .json

llista_dfs = []
for file in files:  #Para los datos en el dataset
    with open(file, encoding="utf-8") as jsonfile:  #Ir abriendo por compartimentos
        dades = json.load(jsonfile)
        tweets = dades["data"]  # Entremos en data, que es dónde están los datos que buscamos
        print(tweets)
        vacia = None  # Necesitamos crear una columna vacía para que cuadre (chapuza)
        for tweet in tweets:
            author_id = tweet["author_id"]  #Buscamos la variable author id
            users=dades["includes"]["users"]  # Tenemos que entrar a includes para coger los usuarios
            likes=tweet['public_metrics']['like_count']
            retweet=tweet['public_metrics']['retweet_count']
            reply=tweet['public_metrics']['reply_count']
            quote=tweet['public_metrics']['quote_count']

            if 'entities' in tweet:  # Queremos los hashtags, entramos a "entities" que los allberta
               entities = tweet['entities']
               if 'hashtags' in entities:
                  tags = entities['hashtags'] #Lo metemos en la variable tag
                  for hashtag in tags:
                     hashtags = hashtag['tag']
               else:
                  hashtags = None
            else:
               hashtags = None #Puede no haber hashtag en los tweets

            for user in users:
                if user["id"] == author_id:
                    user_name = user["username"]  #Buscamos la variable user_name
                    #print(user["id"], user["username"])
                    followers = user["public_metrics"]["followers_count"]  #Buscamos la métrica de followers
                    break
                else:
                    pass
            text = tweet["text"]  # Buscamos el texto
            text_minus = text.lower()  #Esta función pasa todos los texto a minúsculas y así eliminamos los problemas por case sensitive
            #Vamos a usar booleanos para comprobar la existencia o la "mención"
            if text_minus.find('ada') >= 0:
               Ada = True
            elif text_minus.find('colau') >= 0:
               Ada = True
            else:
               Ada = False
            if text_minus.find('basha') >= 0:
               Basha = True
            elif text_minus.find('changue') >= 0:
               Basha = True
            else:
               Basha = False
            if text_minus.find('ernest') >= 0:
               Ernest = True
            elif text_minus.find('maragall') >= 0:
               Ernest = True
            else:
               Ernest = False
            if text_minus.find('jaume') >= 0:
               Jaume = True
            elif text_minus.find('collboni') >= 0:
               Jaume = True
            else:
               Jaume = False
            if text_minus.find('xavier') >= 0:
               Xavier = True
            elif text_minus.find('trias') >= 0:
               Xavier = True
            else:
               Xavier = False
            if text_minus.find('anna') >= 0:
               Anna = True
            elif text_minus.find('grau') >= 0:
               Anna = True
            else:
               Anna = False
            if text_minus.find('eva') >= 0:
               Eva = True
            elif text_minus.find('parera') >= 0:
               Eva = True
            else:
               Eva = False
            if text_minus.find('daniel') >= 0:
               Daniel = True
            elif text_minus.find('sirera') >= 0:
               Daniel = True
            else:
               Daniel = False
            df = pd.DataFrame({  # Creamos un data frame en el que volcamos los datos que queremos
            #Variables que queremos
               "user_id": author_id,
               "user_name": user_name,
               "followers": followers,
               "text": text,
               "textNO" : vacia, #"Chapuza" para arreglar problemas
               "hashtags": hashtags,
               "like": likes,
               "retweet": retweet,
               "reply": reply,
               "quote": quote,
           #Metemos los nombres de los candidatos
               "Ada Colau": Ada,
               "Basha Changue": Basha,
               "Ernest Maragall": Ernest ,
               "Jaume Collboni": Jaume ,
               "Xavier Trias": Xavier,
               "Anna Grau": Anna ,
               "Eva Parera": Eva ,
               "Daniel Sirera": Daniel ,

            }, index=[0])  # Ponemos index 0 para que no nos haga una columna inutil
            #print(df)
            llista_dfs.append(df) #Salimos del bucle para guardar los datos en el dataframe
df_final = pd.concat(llista_dfs)
llista_dfs.to_csv("final.csv", index=False)

# Analizar el archivo .json y comprender cuál es su estructura.
# Entender qué datos tenemos disponibles.
# Procesar los archivos en serie y generar un dataset .csv
# Plantear preguntas de investigación que podemos responder con Tableau (por ejemplo):
