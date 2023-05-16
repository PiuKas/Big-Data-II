```python
import pandas as pd
import glob

#glob lo pone todo en una lista llamada "datasets"
datasets=glob.glob("datasets/twitch_*") 
#("nombre de los datasets") En este caso queremos todos los archivos que comiencen por twitch_ de la carpeta datasets.

llista_streamers=["auronplay","IlloJuan"]
for data in datasets:
	df=pd.read_csv(data, sep="\t")
	for streamer in llista
		#df.loc[df["column_name"] ==streamer
		df.loc[df["streamer_name"] == streamer#para filtrar por streamer
		llista.append(df)
df_final=pd.concat(llista)
df_final.to_csv(f"{streamer}-dataset.csv", index=False)
```

Datos trabajo final
Tamaño dashboard: 800x800
datos-->final dataset-->extraer
servidor--> tableau public---> publicar en tableau public
