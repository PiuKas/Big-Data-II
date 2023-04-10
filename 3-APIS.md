## 1-Twitch
*Cuando ejecutemos aquí, hay que poner en el terminal:  python3 main.py*
```Python
from twitchAPI.twitch import Twitch #carga su propia libreria  
twitch = Twitch('352e2ul58dwnjz5aua1kxuhyi2cvpq', 'i55ygvu0l1ozkhq48l3p99dukx28ch')  #variable que contiene las credenciales
print(twitch.get_users(logins=['your_twitch_username'])) #imprime el resultado de una función
```
*Utilizamos funciones propias de la API*
	get_users
	get_streams
```Python
from twitchAPI.twitch import Twitch  
  
twitch = Twitch('352e2ul58dwnjz5aua1kxuhyi2cvpq', 'i55ygvu0l1ozkhq48l3p99dukx28ch')  
print(twitch.get_users(logins=['PiuKasss']))  
  
#FUNCION GET_STREAMS  
streams = twitch.get_streams(first=20, language="es")  #guardo los primeros 20 streams en español en la variable "streams"  
print(streams)  
  
data=streams["data"] #guardo en la variable data, la parte de data de la variable streamsç  
for d in data:  
    print(d)
```

Guardar en un documento json

```Python
from twitchAPI.twitch import Twitch
import json
  
twitch = Twitch('352e2ul58dwnjz5aua1kxuhyi2cvpq', 'i55ygvu0l1ozkhq48l3p99dukx28ch')  
print(twitch.get_users(logins=['PiuKasss']))  
  
#FUNCION GET_STREAMS  
streams = twitch.get_streams(first=20, language="es")  #guardo los primeros 20 streams en español en la variable "streams"  
  
#GUARDAMOS LA RESPUESTA EN UN DOCUMENTO JSON  
    with open("output_file.json", 'w', encoding='utf-8') as f:  
        json.dump(result, f, ensure_ascii=False, indent=4)
```

Función para saber hora actual
```Python
import datetime
now = datetime.datetime.now()
#tenemos la hora en la variable now
```

Creamos el dataframe con las variables que queremos
```Python
from twitchAPI.twitch import Twitch  
import json  
import pandas as pd  
import datetime  
now = datetime.datetime.now()  
print(now)  
  
twitch = Twitch('352e2ul58dwnjz5aua1kxuhyi2cvpq', 'i55ygvu0l1ozkhq48l3p99dukx28ch')  
print(twitch.get_users(logins=['PiuKasss']))  
  
#FUNCION GET_STREAMS  
streams = twitch.get_streams(first=1, language="es")  #guardo los primeros 20 streams en español en la variable "streams"  
  
dades=streams["data"] #es donde tenemos los datos  
  
#entramos uno a uno y extraemos elementos que guardamos en variables  
for dada in dades:  
    captured_at=now  
    user_id=dada["user_id"]  
    user_name=dada["user_name"]  
    game_id=dada["game_id"]  
    game_name=dada["game_name"]  
    title=dada["title"]  
    viewer_count=dada["viewer_count"] #accedemos al viewer count con la keyword del diccionadio dades  
    started_at=dada["started_at"]  
    is_mature=dada["is_mature"]  
  
    df=pd.DataFrame({ #creamos un dataframe para cada variable  
        "captured_at": captured_at,  
        "user_id" : user_id,  
        "user_name" : user_name,  
        "game_id": game_id,  
        "game_name" : game_name,  
        "title" : title,  
        "viewer_count" : viewer_count,  
        "started_at" : started_at,  
        "is_mature" : is_mature,  
  
    }, index=[0])  #para indicar a pandas  
  
    print(df) #variable   que contiene el dataframe
```

Ahora haremos lo mismo pero guardando 20 streams hacaiendo una lista de dataframes

```Python
from twitchAPI.twitch import Twitch  
import json  
import pandas as pd  
import datetime  
now = datetime.datetime.now()  
print(now)  
  
twitch = Twitch('352e2ul58dwnjz5aua1kxuhyi2cvpq', 'i55ygvu0l1ozkhq48l3p99dukx28ch')  
#print(twitch.get_users(logins=['PiuKasss']))  
  
#FUNCION GET_STREAMS  
streams = twitch.get_streams(first=20, language="es")  #guardo los primeros 20 streams en español en la variable "streams"  
  
dades=streams["data"] #es donde tenemos los datos  
llista_dataframes=[]  
#entramos uno a uno y extraemos elementos que guardamos en variables  
for dada in dades:  
    captured_at=now  
    user_id=dada["user_id"]  
    user_name=dada["user_name"]  
    game_id=dada["game_id"]  
    game_name=dada["game_name"]  
    title=dada["title"]  
    viewer_count=dada["viewer_count"] #accedemos al viewer count con la keyword del diccionadio dades  
    started_at=dada["started_at"]  
    is_mature=dada["is_mature"]  
  
    df=pd.DataFrame({ #creamos un dataframe para cada variable  
        "captured_at": captured_at,  
        "user_id" : user_id,  
        "user_name" : user_name,  
        "game_id": game_id,  
        "game_name" : game_name,  
        "title" : title,  
        "viewer_count" : viewer_count,  
        "started_at" : started_at,  
        "is_mature" : is_mature,  
  
    }, index=[0])  #para indicar a pandas  
    
    llista_dataframes.append(df)  
    print(llista_dataframes)
```

Concatenamos y creamos el dataframe final

```Python
#ponemos esto al final del código
final_dataframe=pd.concat(llista_dataframes)  
print(final_dataframe)
```

Exportamos en csv
```Python
final_dataframe=pd.concat(llista_dataframes)  
final_dataframe.to_csv("export.csv",index=False)
```

Esta API solo permite imprimir un número determinado de streamers, pero podemos posicionar la selección en otro punto y coger otros.
*Cuando recibe la respuesta, coje todos los datos que tieene ahora, una vez hecho eso, mira si tiene las variables "paginacion" o "cursor", si no las ha encontrado vuelve a iterar*
```Python
from twitchAPI.twitch import Twitch
import json
import datetime
import pandas as pd
import time

twitch = Twitch('fpob8mnea92timwors9okz586udkqo', '0ly66c08kcjrd8dashw88ynx4i6d3c')
now = datetime.datetime.now()
llista_streams = []
cursor_dummy = None
def crida(cursor):

    streams = twitch.get_streams(first=20, language="ca", after=cursor)

    dades = streams["data"]
    for dada in dades:
        captured_at = now
        user_id = dada["user_id"]
        user_name = dada["user_name"]
        game_id = dada["user_id"]
        game_name = dada["game_name"]
        title = dada["title"]
        viewers = dada["viewer_count"]
        started_at = dada["started_at"]
        is_mature = dada["is_mature"]

        df = pd.DataFrame({
            "captured_at":captured_at,
            "user_id": user_id,
            "user_name": user_name,
            "game_id": game_id,
            "game_name": game_name,
            "title" : title,
            "viewer_count": viewers,
            "started_at": started_at,
            "mature": is_mature
        },index=[0])
        llista_streams.append(df)

    print(len(llista_streams))
    try:
        cursor = streams["pagination"]["cursor"]
        print(f"Fent una nova consulta. Portem {len(llista_streams)} streams")
        time.sleep(1)
        crida(cursor)
    except KeyError:
        print(f"Ultima pagina. {len(llista_streams)} streams capturats")
        pass


crida(cursor_dummy)

final_dataframe = pd.concat(llista_streams)
final_dataframe.to_csv("twitch.csv", index=False)
```
## APIS Y FUNCIONES
```Python 




```

