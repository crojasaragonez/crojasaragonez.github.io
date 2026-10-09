---
title: "Los datos de criminalidad en Costa Rica cuentan dos historias"
description: "Exploré once años de las estadísticas policiales abiertas del Poder Judicial. La mayoría de los delitos registrados bajó, mientras los homicidios subieron, impulsados por los casos de ajuste de cuentas."
pubDate: 2026-10-09
lang: es
draft: true
---

Cuando en Costa Rica hablamos de criminalidad, solemos hablar de una sola cosa que va empeorando. Quise ver si los datos públicos respaldan esa idea, así que descargué todos los archivos anuales de las estadísticas policiales abiertas del Poder Judicial, de 2015 a septiembre de 2026, y los analicé juntos.

Son unos 577.000 registros. Cada uno trae el delito, la modalidad, la fecha y la provincia, el cantón y el distrito donde se registró. Los archivos están publicados en el [portal de datos abiertos del Poder Judicial](https://datosabiertospj.poder-judicial.go.cr/dataset/estadisticas-policiales) con licencia Creative Commons Atribución.

Lo que encontré son dos historias que van en direcciones opuestas.

## Qué contienen los datos

Los archivos tienen seis categorías de delito:

| Categoría | Qué incluye | Registros en 2025 |
|---|---|---|
| Homicidio | Muerte intencional de una persona | 997 |
| Asalto | Robo a una persona con violencia o amenaza | 9.425 |
| Robo | Robo con fuerza sobre las cosas, como un boquete o una puerta forzada | 6.876 |
| Hurto | Robo sin fuerza ni violencia, como un carterista | 12.591 |
| Robo de vehículo | Robo del vehículo completo | 5.151 |
| Tacha de vehículo | Robo de objetos dentro de un vehículo | 4.345 |

Dos limitaciones marcan todo lo que sigue. **Son delitos registrados, no la criminalidad real.** Un asalto que nadie denuncia nunca entra al archivo, así que una cifra que baja puede significar menos asaltos o menos denuncias. Además, el archivo de 2026 llega hasta el 30 de septiembre. Por eso, cada vez que comparo 2026 con años anteriores, comparo los mismos nueve meses de cada año.

## Dos líneas que van en direcciones opuestas

Para poner categorías de tamaños muy distintos en una misma escala, dividí la cifra de cada año entre la de 2015 de la misma categoría. Un valor de 100 significa lo mismo que en 2015.

<!-- chart:index:start -->
<figure class="fig chart-figure">
<img src="/images/blog/costa-rica-crime/index.svg" alt="Índice de registros de enero a septiembre, 2015 = 100, valor en 2026: Homicidio 146; Robo de vehículo 130; Asalto 58; Robo 57; Hurto 56; Tacha de vehículo 86." loading="lazy" />
<figcaption><strong>Figura 1.</strong> Cada línea compara los registros de una categoría con su propio nivel de 2015, para que categorías de tamaños muy distintos compartan una escala.</figcaption>
</figure>
<!-- chart:index:end -->

De enero a septiembre, los asaltos pasaron de 10.859 registros en 2015 a 6.248 en 2026. Los robos pasaron de 8.864 a 5.020 y los hurtos de 14.313 a 7.959. **Las tres categorías más comunes bajaron más de 40%.**

Los homicidios fueron en sentido contrario: 429 registros en los primeros nueve meses de 2015 y 751 en los mismos meses de 2025. El robo de vehículos es la otra excepción: está 30% por encima de su nivel de 2015.

La pandemia se ve claramente en 2020, cuando casi todas las categorías cayeron. La mayoría de los delitos contra la propiedad nunca volvió a sus niveles anteriores. Un detalle me sorprendió: los asaltos con arma de fuego pasaron de 10.337 registros en 2018 a 3.614 en 2025, una caída de 65%. Se registran menos asaltos a mano armada y, al mismo tiempo, más asesinatos.

## La mayor parte del aumento viene de un solo móvil

El archivo registra un móvil para cada homicidio. Separar el total por móvil explica la mayor parte del cambio.

<!-- chart:homicide-motives:start -->
<figure class="fig chart-figure">
<img src="/images/blog/costa-rica-crime/homicide-motives.svg" alt="Registros de homicidio por móvil, 2015 a 2025. Ajuste de cuentas o venganza: 232 en 2015, 708 en 2025. Indeterminado: 138 en 2015, 35 en 2025. Totales: 575 en 2015, 997 en 2025." loading="lazy" />
<figcaption><strong>Figura 2.</strong> Solo años completos. «Indeterminado» agrupa tres etiquetas que el archivo usa para un móvil desconocido.</figcaption>
</figure>
<!-- chart:homicide-motives:end -->

Los homicidios registrados como ajuste de cuentas o venganza pasaron de 232 en 2015 a 708 en 2025. Todos los demás móviles juntos se mantuvieron entre unos 250 y 440 registros por año, con tendencia a la baja. **El ajuste de cuentas pasó de explicar cerca de cuatro de cada diez homicidios a siete de cada diez.**

Eso coincide con lo que ha dicho públicamente el OIJ. En un [artículo del Poder Judicial sobre la evolución de los homicidios en los últimos diez años](https://pjenlinea3.poder-judicial.go.cr/biblioteca/uploads/Archivos/Articulo/Evolucion%20de%20los%20homicidios%20en%20Costa%20Rica%20en%20los%20ultimos.pdf), el director interino del OIJ señaló que el principal móvil en 2022 fue el ajuste de cuentas por narcotráfico. También dijo que la mayoría de las víctimas tenía antecedentes criminales y que las autoridades las relacionan con grupos que se disputan territorios.

Una advertencia sobre este gráfico. Los casos con móvil indeterminado también bajaron, de 138 registros en 2015 a 35 en 2025. Parte del crecimiento del ajuste de cuentas podría venir de que los investigadores ahora clasifican más casos, y no de nuevos asesinatos. Eso no explica la mayor parte, eso sí: los casos indeterminados bajaron unos 100 registros y el ajuste de cuentas creció casi 500.

## Dónde ocurren los homicidios

<!-- chart:homicide-provinces:start -->
<figure class="fig chart-figure">
<img src="/images/blog/costa-rica-crime/homicide-provinces.svg" alt="Registros de homicidio por provincia, 2015 a 2025: San José de 263 a 340; Limón de 101 a 206; Puntarenas de 52 a 140; Alajuela de 56 a 115; Guanacaste de 24 a 86; Cartago de 40 a 71; Heredia de 39 a 39." loading="lazy" />
<figcaption><strong>Figura 3.</strong> Solo años completos. Los círculos vacíos son 2015 y los llenos, 2025.</figcaption>
</figure>
<!-- chart:homicide-provinces:end -->

Limón se duplicó, de 101 a 206 registros. Puntarenas pasó de 52 a 140 y Guanacaste de 24 a 86. Heredia terminó 2025 exactamente donde empezó, en 39. San José es el caso particular: bajó a 129 registros en 2022 y luego subió a 340 en 2025, la cifra más alta del país.

El desglose por provincia también explica lo que va de 2026.

<!-- chart:homicides-monthly:start -->
<figure class="fig chart-figure">
<img src="/images/blog/costa-rica-crime/homicides-monthly.svg" alt="Registros mensuales de homicidio, enero 2015 a septiembre 2026. El promedio de 12 meses es 73 en septiembre de 2026, frente a 84 en septiembre de 2024. Máximo: 121 en febrero de 2024." loading="lazy" />
<figcaption><strong>Figura 4.</strong> Cada barra es un mes. La línea suaviza la variación de un mes a otro.</figcaption>
</figure>
<!-- chart:homicides-monthly:end -->

El peor mes de la serie fue febrero de 2024, con 121 registros. De enero a septiembre de 2026 hubo 625 registros de homicidio, 17% menos que en los mismos meses de 2025. **La mayor parte de esa baja es San José**, que pasó de 254 a 159. Limón fue en sentido contrario, de 159 a 175. Una baja nacional puede esconder una provincia donde la situación empeora.

## La cifra que no coincidió

Antes de escribir esto, comparé el dataset con los totales de homicidios que el OIJ anuncia cada año. No coinciden.

| Año | Anunciado por el OIJ | Registros en los datos abiertos | Diferencia |
|---|---|---|---|
| 2019 | 564 | 623 | +10% |
| 2020 | 570 | 625 | +10% |
| 2021 | 588 | 650 | +11% |
| 2022 | 656 | 732 | +12% |
| 2023 | 905 | 1.008 | +11% |
| 2024 | 876 | 1.013 | +16% |
| 2025 | 873 | 997 | +14% |

Las cifras de 2019 a 2022 vienen del [artículo del Poder Judicial](https://pjenlinea3.poder-judicial.go.cr/biblioteca/uploads/Archivos/Articulo/Evolucion%20de%20los%20homicidios%20en%20Costa%20Rica%20en%20los%20ultimos.pdf) citado arriba. Las de 2023 a 2025 vienen del [cierre de 2025 del OIJ, según Delfino](https://delfino.cr/2026/01/costa-rica-registro-873-homicidios-en-2025-el-tercer-ano-mas-violento-de-la-historia), que también reporta una tasa de 16,7 homicidios por cada 100.000 habitantes en 2025.

Los datos abiertos están entre 10% y 16% por encima de los totales anunciados todos los años. En 2025 el OIJ también publicó totales por provincia, y los datos abiertos son más altos en las siete.

No pude encontrar la razón en los archivos. No tienen un identificador de caso, así que no puedo saber si hay filas duplicadas, si el dataset cuenta algo que el total oficial excluye, o si revisiones posteriores explican la diferencia. En los últimos años, cerca de una de cada ocho filas de homicidio es idéntica a otra. Puede ser una segunda víctima del mismo ataque o un duplicado.

La tendencia se sostiene a pesar de la diferencia. Según el conteo del propio OIJ, los homicidios subieron 55% de 2019 a 2025; los datos abiertos muestran 60%. Por eso aquí uso los datos abiertos para la forma (qué móviles, qué provincias, qué meses) y las cifras oficiales para cuántas personas murieron.

La lección que me llevo no es exclusiva de Costa Rica: **un dataset abierto es un punto de partida, y compararlo con una sola cifra independiente es la prueba más barata que existe.** Sin ella, habría publicado cifras de homicidios equivocadas.

## Lo que estos datos no pueden decir

Algunas preguntas necesitan otras fuentes:

- **Si los delitos contra la propiedad realmente bajaron.** Menos registros pueden significar menos delitos o menos denuncias. Las encuestas de victimización, que les preguntan directamente a los hogares, son la forma de distinguir una cosa de la otra.
- **Las tasas.** Todo lo anterior son conteos. La población de Costa Rica creció en estos años, así que las tasas por cada 100.000 habitantes harían el aumento de los homicidios algo menor y la caída de los delitos contra la propiedad algo mayor. No las incluí porque no pude acceder a las estimaciones de población por cantón del INEC cuando hice este análisis.
- **Nada sobre el sexo de las víctimas.** Esa columna viene vacía en todos los años de los archivos.

## Lo que me deja este ejercicio

Esperaba una sola historia: la criminalidad en aumento. Los datos muestran un país donde la mayoría de los delitos cotidianos registrados bajó cerca de 40% desde 2015, mientras los homicidios subieron a niveles cercanos al récord, concentrados en un móvil y en algunas provincias.

Son dos problemas distintos y necesitan respuestas distintas. Una política que trate la "criminalidad" como una sola cosa no va a resolver ninguno de los dos.
