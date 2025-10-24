from series_tv import *
from datetime import date

def crea_series():
    series_tv = [
        SerieTV(
            titulo="Viaje en el Tiempo",
            episodios=[
                '1x01-El Portal',
                '1x02-El Experimento',
                '2x01-El Cambio',
                '2x02-El Dilema Temporal',
                '2x03-El Confrontamiento Final'
            ],
            generos={"Ciencia Ficción", "Aventura"},
            valoracion=4.5,
            fecha_lanzamiento=date(2023, 2, 10),
            num_temporadas=2,
            finalizada=False
        ),
        SerieTV(
            titulo="Aventuras en el Espacio",
            episodios=[
                '1x01-El Descubrimiento',
                '1x02-El Encuentro Alienígena',
                '2x01-La Batalla Final',
                '2x02-La Gran Revelación'
            ],
            generos={"Ciencia Ficción", "Aventura"},
            valoracion=4.6,
            fecha_lanzamiento=date(2022, 11, 30),
            num_temporadas=2,
            finalizada=True
        ),
        SerieTV(
            titulo="Intriga en la Ciudad",
            episodios=[
                '1x01-El Complot',
                '1x02-El Secreto Oscuro',
                '1x03-El Doble Juego',
                '2x01-El Punto de No Retorno',
                '2x02-El Confrontamiento Final',
                '3x01-La Venganza',
                '3x02-El Destino Final'
            ],
            generos={"Drama", "Misterio"},
            valoracion=4.2,
            fecha_lanzamiento=date(2023, 1, 20),
            num_temporadas=3,
            finalizada=False
        ),
        SerieTV(
            titulo="Romance en París",
            episodios=[
                '1x01-El Encuentro',
                '1x02-El Baile de Máscaras',
                '1x03-La Confesión',
                '2x01-El Desafío del Amor',
                '2x02-La Búsqueda de la Felicidad',
                '3x01-El Gran Final'
            ],
            generos={"Romance", "Drama"},
            valoracion=4.7,
            fecha_lanzamiento=date(2022, 8, 5),
            num_temporadas=3,
            finalizada=True
        ),
        SerieTV(
            titulo="El Misterio del Pasado",
            episodios=[
                '1x01-El Descubrimiento',
                '1x02-La Conspiración',
                '1x03-El Enigma del Antiguo Manuscrito',
                '2x01-La Verdad Oculta',
                '2x02-El Último Capítulo',
                '3x01-El Destino Final'
            ],
            generos={"Misterio", "Aventura"},
            valoracion=4.4,
            fecha_lanzamiento=date(2023, 3, 15),
            num_temporadas=3,
            finalizada=False
        ),
        SerieTV(
            titulo="Risas en la Oficina",
            episodios=[
                '1x01-El Nuevo Jefe',
                '1x02-La Fiesta de Cumpleaños',
                '1x03-El Desafío de la Integración',
                '2x01-El Día de la Presentación',
                '2x02-El Concurso de Talento',
                '3x01-La Gran Final'
            ],
            generos={"Comedia", "Drama"},
            valoracion=4.5,
            fecha_lanzamiento=date(2022, 7, 20),
            num_temporadas=3,
            finalizada=True
        ),
        SerieTV(
            titulo="Amistad en la Universidad",
            episodios=[
                '1x01-El Primer Encuentro',
                '1x02-La Prueba de Lealtad',
                '1x03-La Gran Fiesta',
                '2x01-La Competencia Académica',
                '2x02-El Desafío del Amor',
                '3x01-El Camino a la Graduación'
            ],
            generos={"Drama", "Comedia"},
            valoracion=4.3,
            fecha_lanzamiento=date(2023, 1, 10),
            num_temporadas=3,
            finalizada=False
        ),
        SerieTV(
            titulo="Misterios en el Pueblo",
            episodios=[
                '1x01-El Descubrimiento',
                '1x02-La Desaparición',
                '1x03-El Enigma de la Mansión',
                '2x01-El Secreto de la Biblioteca',
                '2x02-El Misterio del Cementerio',
                '3x01-El Último Capítulo'
            ],
            generos={"Misterio", "Drama"},
            valoracion=4.1,
            fecha_lanzamiento=date(2022, 10, 5),
            num_temporadas=3,
            finalizada=True
        ),
        SerieTV(
            titulo="El Desafío del Espía",
            episodios=[
                '1x01-El Reclutamiento',
                '1x02-La Misión Imposible',
                '2x01-El Agente Doble',
                '2x02-La Trampa Mortal',
                '2x03-El Contraataque Final'
            ],
            generos={"Acción", "Aventura"},
            valoracion=4.6,
            fecha_lanzamiento=date(2023, 4, 8),
            num_temporadas=2,
            finalizada=False
        )  ]
    return series_tv

def test_series_de_anyo(series, anyo):
    res = series_de_anyo(series, anyo)
    print(f"Series estrenadas en {anyo}:", res)


def test_episodios_de_temporada(serie, temporada):
    res = episodios_de_temporada(serie, temporada)
    print(f"Episodios de la temporada {temporada} de {serie.titulo}:", res)


def test_num_episodios_temporada(serie, temporada):
    res = num_episodios_temporada(serie, temporada)
    print(f"Número de episodios en la temporada {temporada} de {serie.titulo}:", res)


def test_num_series_lanzadas_en_anyo(series, anyo):
    res = num_series_lanzadas_en_anyo(series, anyo)
    print("Número de series lanzadas en {anyo}:", res)


def test_media_num_episodios_en_emision(series):
    res = media_num_episodios_en_emision(series)
    print("Media de episodios de series en emisión:", res)


def test_hay_serie_genero_valoracion_superior(series,genero, valoracion):
    res = hay_serie_genero_valoracion_superior(series, genero, valoracion)
    print(f"¿Hay serie de género {genero} con valoración >= {valoracion}?", res)


def test_tiene_todas_series_finalizadas_valoracion_superior(series,valoracion):
    res = tiene_todas_series_finalizadas_valoracion_superior(series, valoracion)
    print(f"¿Todas las series finalizadas tienen valoración > {valoracion}?", res)


def test_anyo_series_emision(series):
    res = anyo_series_emision(series)
    print("Años de estreno de las series:", res)


def test_serie_peor_valorada_de_genero(series, genero):
    res = serie_peor_valorada_de_genero(series, genero)
    print(f"Serie peor valorada del género {genero}:", res)


def test_serie_finalizada_mas_temporadas(series):
    res = serie_finalizada_mas_temporadas(series)
    print("Serie finalizada con más temporadas:", res.titulo if res else None)

def main():
    series = crea_series()

    print("Ejercicio 1", "="*50)
    test_series_de_anyo(series, 2022)
    print("Ejercicio 2", "="*50)
    test_episodios_de_temporada(series[0], 3)
    print("Ejercicio 3", "="*50)
    test_num_episodios_temporada(series[0], 3)
    print("Ejercicio 4", "="*50)
    test_num_series_lanzadas_en_anyo(series,2022)
    print("Ejercicio 5", "="*50)
    test_media_num_episodios_en_emision(series)
    print("Ejercicio 6", "="*50)
    test_hay_serie_genero_valoracion_superior(series,"Drama", 4.2)
    test_hay_serie_genero_valoracion_superior(series,"Comedia", 4.7)
    print("Ejercicio 7", "="*50)
    test_tiene_todas_series_finalizadas_valoracion_superior(series,3)
    test_tiene_todas_series_finalizadas_valoracion_superior(series,4.7)
    print("Ejercicio 8", "="*50)
    test_anyo_series_emision(series)
    print("Ejercicio 9", "="*50)
    test_serie_peor_valorada_de_genero(series, "Comedia")
    test_serie_peor_valorada_de_genero(series, "Thriller")
    print("Ejercicio 10", "="*50)
    test_serie_finalizada_mas_temporadas(series)

if __name__== "__main__":
    main()

    
