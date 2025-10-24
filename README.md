# T01.10 -TratamientosSecuenciales

Autora: Toñi Reina
Última modificación: 24/10/2025

El objetivo de este proyecto es trabajar los esquemas de los distintos tratamientos secuenciales vistos en la clase de teoría: existe, para todo, selección tanto a lista como a conjunto, contador, media , máximo/mínimo.
Para ello se proporcionan dos módulos `series_tv`y `series_tv_test`. En el módulo `series_tv` tienes la siguiente definición de tupla con nombre
```python
SerieTV = namedtuple('SerieTV', 
                    ['titulo', 'episodios', 'generos', 'valoracion', 'fecha_lanzamiento' , 'num_temporadas', 'finalizada'])
```
donde 
- titulo: `str`, es el título de la serie
- episodios: `list[str]`, con la lista de episodios de la serie. Cada episodio es una cadena que tiene el formato TxE-titulo, donde T es el número de la temporada y E el del episodio. Por ejemplo, "1x01-El Inicio" sería el título del primer episodio de la primera temporada.
- generos: `set[str]` con los géneros a los que pertenece la serie.
- valoracion: `float`, valoración que dan los usuarios a la serie.
- fecha_lanzamieto: `datetime.date`, con la fecha en la que se estrenó el primer capítulo de la serie.
- num_temporadas: `int`, número de temporadas de la serie.
- finalizada: `bool`, indica si la serie ha finalizado (True) o sigue en emisión (False)

En el módulo `series_tv_test` tienes implementadas las pruebas para las siguientes funciones, que debes implementar en el módulo `series_tv`:

1. `series_de_anyo`, que recibe una lista de tuplas de tipo `SerieTV` y un año, y devuelve una lista, ordenada alfabéticamente, con los títulos de las series que se estrenaron ese año.  

2.	`episodios_de_temporada`, que recibe una tupla de tipo `SerieTV` y y un número entero, correspondiente a un número de temporada y devuelve una lista ordenada alfabéticamente,  los episodios de la temparada dada como parámetro. Ayuda: Usa `startswith` para saber si una cadena comienza por una serie de caracteres. Por ejemplo, `cadena.startswith("11")` devuelve `True` si cadena empieza por la subcadena "11".
    
3. `num_episodios_temporada`, que recibe una tupla de tipo `SerieTV` y un número entero, correspondiente a un número de temporada y devuelve el número de capítulos de esa temporada. Ayuda: Usa startswith para saber si una cadena comienza por una serie de caracteres. Por ejemplo, `cadena.startswith("11")` devuelve `True` si cadena empieza por la subcadena "11". 

4. `num_series_lanzadas_en_anyo`, que recibe una lista de tuplas de tipo `SerieTV` y un número, correspondiente a un año, y devuelve el número de series que se lanzaron ese año.

5. `media_num_episodios_en_emision`, que recibe una lista de tuplas de tipo `SerieTV` y devuelve el número medio de episodios de las series que están en emisión (no han finalizado). Si no se puede calcular la media, devuelve `None`.

6. `hay_serie_genero_valoracion_superior`, que recibe una lista de tuplas de tipo `SerieTV`, un género y una valoración y devuelve `True` si hay alguna serie del género dado con una valoración superior o igual a la dada, O `.

7. `tiene_todas_series_finalizadas_valoracion_superior`, que recibe una lista de tuplas de tipo `SerieTV` y una valoración y devuelve `True` si todas las series finalizadas tienen una valoración superior a la dada como parámetro.

8. `anyo_series_emision`, que recibe una lista de tuplas de tipo `SerieTV` y devuelve los años en los que se estrenaron esas series (sin duplicados).

9. `serie_peor_valorada_de_genero`  que recibe una lista de tuplas de tipo `SerieTV` y un género, y devuelve el título de la serie mejor valorada de ese género. Si no se puede calcular, devuelve `None`.

10. `serie_finalizada_mas_temporadas` que recibe una lista de tuplas de tipo `SerieTV` y devuelve la serie finalizada con más temporadas. Si no se puede calcular, devuelve `None`.