El enlace para consultar la información de cada año es el mismo, solo cambia el número final.
```python
import requests #modulo que permite consultar páginas web  
from bs4 import BeautifulSoup  
import pandas as pd  
import time  
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
  
llista_dataframes=[]  
  
anys=range(2000,2024,1) #año de inicio, año de fin y cada cuanto deb saltar  
  
for any in anys:  
    try:  
        resposta=requests.get(f"https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{any}")  
        soup = BeautifulSoup(resposta.text, "html.parser")  # pasamos el paseador para que trabaje como un html y no un txt  
        final = soup.find("span", id="Final")  #encuentra el span que se llama final  
        tabla = final.find_next("table")  
        df = pd.read_html(tabla.prettify())[0]  #para que me lo haga bonito  
        df["any"]=any #creamos una nueva columna para el año en el df  
        print(df)  
  
        df.columns.values[0]= "N. "  
        df.columns.values[5]= "Puntos"  
        df.columns.values[2] = "Cantante"  
  
  
  
        llista_dataframes.append(df)  
    except AttributeError:  
        print(f"error: {any}")  
  
final=pd.concat(llista_dataframes)  
final.to_excel("llista_final.xlsx", index=False)  
  
  
#PART SPOTIPY  
df=pd.read_excel("llista_final.xlsx")  
  
SPOTIPY_CLIENT_ID="6a2bcf4006234d71898260c66e148af9"  
SPOTIPY_CLIENT_SECRET="45a5e5b0d8bc4042a569d9257ab863cd"  
  
from spotipy.oauth2 import SpotifyClientCredentials  
  
auth_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)  
sp=spotipy.Spotify(auth_manager=auth_manager)  
  
for index, row in df.iterrows():  
    artista=row["Cantante"]  
    track = row["Canción"]  
    try:  
        p_track= track.split("«")[1].split("»")[0] #quitamos las comillas del titulo de las canciones  
    except IndexError:  
        p_track=track  
    print(artista, p_track)  
    q= f"{p_track}{artista} eurovision"    info=sp.search(q, limit=1, offset=0, type="track", market="None")  
    print(info)  
    time.sleep(0.5)
```