*Procesar los datos obtenidos de la API de Twitter y realizar un análisis de la conversación social sobre los candidatos a la alcaldía de Barcelona en las elecciones Municipales del 2023. Los tweets estan publicados entre el 1/04/2023 y el 16/04/2023 en cualquier idioma. Es decir, se han recopilado todos los tweets que contienen alguna de las combinaciones indicadas
Los candidatos son: Basha Change, Xavier Trias, Anna Grau, Eva Parera, Daniel Sirera, Ernest Maragall y Jaume Collboni.*

## Análisis de interacción en Twitter
*La primera (A) se centrará en crear un archivo .csv que sea analizable con Tableau.*
### A. Extracción de dataset y Tableau
##### 1.  Analizar el archivo .json y comprender cuál es su estructura.
Un archivo .json tiene una estructura que consta de una lista ordenada de valores. Suelen estar emparejados en forma de {"nombre" : "valor"}.

##### 2.  Entender qué datos tenemos disponibles.
Tenemos disponibles una serie de datos relacionados con el tweet que van desde el id del autor/a, hasta el número de respuestas pasando por si el tweet tiene contenido esplícito, es sensible o el idioma en el que está.

##### 3.  Procesar los archivos en serie y generar un dataset .csv

##### 4.  Plantear preguntas de investigación que podemos responder con Tableau.
Realizar un análisis de la conversación social tiene como objetivo saber cómo se siente la gente respecto a sus candidatos.

###### 4.1.  ¿Cuál es el candidato más mencionado?
El candidato o la candidata, en este caso, es la actual alcaldesa de Barcelona Ada Colau. Como nos indica el gráfico que se ve a continuación, la diferencia con la segunda más mencionada es gigantesca (casi 7 veces más).
![ej1.png](https://github.com/PiuKas/Big-Data-II/blob/main/Ex_json/ej1.png)
Esto es debido a las grandes polémicas que la señora Colau carga siempre a sus espaldas. Aun así, es sorprendente estas métricas de menciones, puesto que la alcaldesa decidió cesar su actividad en Twitter hace ya más de dos años. Por lo tanto, se puede afirmar que a pesar de no estar siquiera presente en la plataforma, es un actor fundamental en la conversación sobre las elecciones de la ciudad condal.

###### 4.2.  ¿Qué usuarios son más activos?
Entre los 10 usuarios y usuarias más activos y activas de la conversación, encontramos tres medios de comunicación: naciodigital (2o puesto), elnacionalcat (6o puesto) y btv (10o puesto). Todos ellos son medios catalanes que se encargan de cubrir la actualidad autonómica y es comprensible que, por eso, se encuentren tan presentes en la conversación.
![ej2.png](https://github.com/PiuKas/Big-Data-II/blob/main/Ex_json/ej2.png)
Si analizamos los 3 primeros perfiles que no son medios podemos observar que:
- ander_the_table: perfil con casi 5k de seguidores que prácticamente no pública pero interactúa muchísimo con posts relacionados con política y urbanismo.
- LauraMartiBCN: trabajadora del Periódico que pública y habla constantemente de notícias y artículos de este medio. No es pro Ada Colau.
- DespertaFerro11: perfil completamente político y a favor de Junts per Catalunya.
Así mismo, se puede confirmar que son perfiles que participan e interactúan con la conversación social desde un punto de vista político.

###### 4.3.  ¿Cuál es la actividad de cada candidato en sus cuentas oficiales?
La candidata más activa es Eva Parera, candidata por Valents (un nuevo partido político). Este dato es comprensible, ya que al ser una nueva formación debe hacer mucha más campaña y hacerse oír. Lo mismo pasa con el otro partido de derechas (PP) y su representate Daniel Sirera, son partidos que necesitan hacer una gran publicidad y aprovechar para desprestigiar mediante ella. Finalmente tenemos a Basha Change de la CUP porque twittea mucho sobre temas sociales de interés y denúncia de injusticias.
![ej3.png](https://github.com/PiuKas/Big-Data-II/blob/main/Ex_json/ej3.png)

###### 4.4.  ¿Qué temas destacan?
Entre los 10 temas más destacados, podemos destacar ULTIMAHORA, que es el que usa el medio 3/24 para anunciar sus noticias. Así mismo, podemos ver 2 referencias a Barcelona (Barcelona y BCN) que utiliza la gente para distintos temas. Por otra parte, vemos que POLONIATV3 es recurrente, puesto que es un programa de humor de TV3 que menciona constantemente a políticos y recientemente tuvo polémica por un gag sobre Andalucía y su cultura del cual opinaron muchas figuras importantes.
![ej4.png](https://github.com/PiuKas/Big-Data-II/blob/main/Ex_json/ej4.png)

###### 4.5.  ¿Qué temas despiertan más interés entre los usuarios?
Los temas que despiertan más interés están relacionados con el tema de los okupas, que está siendo bastante presente en la conversación social general en España actualmente. Además, la alcaldesa Ada Colau y su partido, no se muerden la lengua a la hora de tratar este tema y eso genera mucha controversia entre sus adversarios políticos.
![ej5.png](https://github.com/PiuKas/Big-Data-II/blob/main/Ex_json/ej5.png)

Por último, relacionado con el partido que gobierna la ciudad se encuentra el tema YolandaPresidenta. Esto es así, porque en el último mes la candidata de SUMAR ha estado haciendo visitas y campaña por Barcelona de la mano de Ada Colau y lo han compartido y comentado mucho en redes.



### B. Combinado de datos y Gephi
*La segunda (B), la dedicaremos a analizar con mayor profundidad las relaciones existentes en el dataset para generar redes de interacción o relaciones.*
Para esto, se ha creado un csv con las columnas "target" y "source" para que Gephy sea capaz de leerlas. En la siguiente representación de se pueden apriar los usuarios que más interactuan en la conversación social analizada. De hecho, "WillyTolerdo", "FroiLannister" y "capTercio" son los principales protagonistas de esta conversación.
![ej6.png](https://github.com/PiuKas/Big-Data-II/blob/main/Ex_json/ej6.png)