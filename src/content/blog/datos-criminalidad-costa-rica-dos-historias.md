---
title: "Los datos de criminalidad en Costa Rica cuentan dos historias"
description: "Analicé las estadísticas policiales abiertas de 2015 a septiembre de 2026: bajaron los registros de asaltos, robos y hurtos, mientras aumentaron los de homicidio."
pubDate: 2026-10-09
lang: es
draft: false
---

Cuando en Costa Rica hablamos de criminalidad, solemos hablar de una sola cosa que va empeorando. Quise ver si los datos públicos respaldan esa idea, así que descargué las estadísticas policiales abiertas del Poder Judicial: once años completos, de 2015 a 2025, y los primeros nueve meses de 2026.

Son unos 577.000 registros. Cada uno trae el delito, la modalidad, la fecha y la provincia, el cantón y el distrito donde se registró. Los archivos están publicados en el [portal de datos abiertos del Poder Judicial](https://datosabiertospj.poder-judicial.go.cr/dataset/estadisticas-policiales) con licencia Creative Commons Atribución.

Encontré dos historias que van en direcciones opuestas: bajaron los registros de asaltos, robos y hurtos, mientras aumentaron los de homicidio. También encontré una diferencia entre los datos abiertos y los totales oficiales que obliga a leer estas cifras con cuidado.

## Qué contienen los datos

Los archivos reúnen seis categorías de delito. No abarcan toda la criminalidad del país:

| Categoría | Qué incluye | Registros en 2025 |
|---|---|---|
| Homicidio | Muerte intencional de una persona | 997 |
| Asalto | Robo a una persona con violencia o amenaza | 9.425 |
| Robo | Robo con fuerza sobre las cosas, como un boquete o una puerta forzada | 6.876 |
| Hurto | Robo sin fuerza ni violencia, como un carterista | 12.591 |
| Robo de vehículo | Robo del vehículo completo | 5.151 |
| Tacha de vehículo | Robo de objetos dentro de un vehículo | 4.345 |

Dos limitaciones marcan todo lo que sigue. **Son registros policiales, no una medida de todos los delitos que ocurrieron.** Un asalto que nadie denuncia puede quedar fuera del archivo, así que una cifra que baja puede reflejar menos asaltos, menos denuncias o cambios en el registro. Además, 2026 está incompleto: excluí las 36 filas fechadas el 1 de octubre y fijé el corte en el 30 de septiembre. Cada comparación que incluye 2026 usa los mismos nueve meses de cada año.

**En homicidios, una fila tampoco equivale necesariamente a una víctima distinta.** Entre 2019 y 2025, los registros de los datos abiertos superan entre 10% y 16% los totales anunciados por el OIJ. Más adelante detallo esa diferencia; por ahora, los gráficos deben leerse como conteos de filas del archivo.

## Dos líneas que van en direcciones opuestas

Para poner categorías de tamaños muy distintos en una misma escala, dividí los registros de enero a septiembre de cada año entre los del mismo período de 2015 y multipliqué por 100. Un valor de 100 equivale al nivel de 2015; uno de 150 indica un aumento de 50%.

<!-- chart:index:start -->
<figure class="fig chart-figure">
<img src="/images/blog/costa-rica-crime/index.svg" alt="Índice de registros de enero a septiembre, 2015 = 100, valor en 2026: Homicidio 146; Robo de vehículo 130; Asalto 58; Robo 57; Hurto 56; Tacha de vehículo 86." loading="lazy" />
<figcaption><strong>Figura 1.</strong> Cada línea compara los registros de una categoría con su propio nivel de 2015, para que categorías de tamaños muy distintos compartan una escala.</figcaption>
</figure>
<!-- chart:index:end -->

De enero a septiembre, los asaltos pasaron de 10.859 registros en 2015 a 6.248 en 2026. Los robos pasaron de 8.864 a 5.020 y los hurtos de 14.313 a 7.959. **Las tres categorías más comunes bajaron más de 40%.**

Los registros de homicidio fueron en sentido contrario: pasaron de 429 en los primeros nueve meses de 2015 a 625 en los mismos meses de 2026, un aumento de 46%. En 2025 habían llegado a 751. El robo de vehículos es la otra excepción: en enero-septiembre de 2026 está 30% por encima de su nivel de 2015.

En 2020, el primer año de la pandemia, casi todas las categorías cayeron. La mayoría de los registros de delitos contra la propiedad no había recuperado sus niveles anteriores al cierre de este análisis. Un detalle me sorprendió: en años completos, los asaltos con arma de fuego pasaron de 10.337 registros en 2018 a 3.614 en 2025, una caída de 65%. La caída de esos registros coexistió con el aumento de los de homicidio.

## El aumento se concentra en ajuste de cuentas o venganza

El archivo clasifica los registros de homicidio por móvil, aunque en algunos casos lo deja indeterminado. Ese desglose permite ver en qué categoría se concentra el aumento; por sí solo no demuestra sus causas.

<!-- chart:homicide-motives:start -->
<figure class="fig chart-figure">
<img src="/images/blog/costa-rica-crime/homicide-motives.svg" alt="Registros de homicidio por móvil, 2015 a 2025. Ajuste de cuentas o venganza: 232 en 2015, 708 en 2025. Indeterminado: 138 en 2015, 35 en 2025. Totales: 575 en 2015, 997 en 2025." loading="lazy" />
<figcaption><strong>Figura 2.</strong> Solo años completos. «Indeterminado» agrupa las etiquetas «Desconocido», «No determinado» y «Otro o indeterminado».</figcaption>
</figure>
<!-- chart:homicide-motives:end -->

Los registros clasificados como ajuste de cuentas o venganza pasaron de 232 en 2015 a 708 en 2025. Todos los demás móviles juntos se mantuvieron entre unos 250 y 440 registros por año: fueron 343 en 2015 y 289 en 2025. **El ajuste de cuentas o venganza pasó de representar cerca de cuatro de cada diez registros de homicidio a siete de cada diez.**

Eso coincide con lo que ha dicho públicamente el OIJ. En un [artículo del Poder Judicial sobre la evolución de los homicidios en los últimos diez años](https://pjenlinea3.poder-judicial.go.cr/biblioteca/uploads/Archivos/Articulo/Evolucion%20de%20los%20homicidios%20en%20Costa%20Rica%20en%20los%20ultimos.pdf), el director interino del OIJ señaló que el principal móvil en 2022 fue el ajuste de cuentas por narcotráfico. También dijo que la mayoría de las víctimas tenía antecedentes criminales y que las autoridades las relacionan con grupos que se disputan territorios.

Hay otra cautela: las tres etiquetas agrupadas como «Indeterminado» bajaron de 138 registros en 2015 a 35 en 2025. Parte del aumento del ajuste de cuentas podría reflejar cambios en la clasificación. Esa reducción de 103 registros es menor que el aumento de 476 en ajuste de cuentas, pero el archivo no permite seguir reclasificaciones ni saber si cambiaron los criterios de registro.

## Dónde ocurren los homicidios

<!-- chart:homicide-provinces:start -->
<figure class="fig chart-figure">
<img src="/images/blog/costa-rica-crime/homicide-provinces.svg" alt="Registros de homicidio por provincia, 2015 a 2025: San José de 263 a 340; Limón de 101 a 206; Puntarenas de 52 a 140; Alajuela de 56 a 115; Guanacaste de 24 a 86; Cartago de 40 a 71; Heredia de 39 a 39." loading="lazy" />
<figcaption><strong>Figura 3.</strong> Solo años completos. Los círculos vacíos son 2015 y los llenos, 2025.</figcaption>
</figure>
<!-- chart:homicide-provinces:end -->

Entre 2015 y 2025, los registros de homicidio en Limón se duplicaron, de 101 a 206. Puntarenas pasó de 52 a 140 y Guanacaste de 24 a 86. Heredia terminó 2025 con la misma cifra que en 2015: 39. San José tuvo un recorrido distinto: bajó a 129 registros en 2022 y luego subió a 340 en 2025, el mayor conteo entre las provincias. Son cantidades absolutas; sin ajustar por población, no permiten comparar el riesgo entre provincias.

El desglose por provincia también explica lo que va de 2026.

<!-- chart:homicides-monthly:start -->
<figure class="fig chart-figure">
<img src="/images/blog/costa-rica-crime/homicides-monthly.svg" alt="Registros mensuales de homicidio, enero 2015 a septiembre 2026. El promedio de 12 meses es 73 en septiembre de 2026, frente a 84 en septiembre de 2024. Máximo: 121 en febrero de 2024." loading="lazy" />
<figcaption><strong>Figura 4.</strong> Cada barra muestra los registros de un mes. La línea es el promedio móvil de los últimos doce meses.</figcaption>
</figure>
<!-- chart:homicides-monthly:end -->

El mes con más registros de homicidio fue febrero de 2024, con 121. De enero a septiembre de 2026 hubo 625, un 17% menos que en los mismos meses de 2025. **San José concentra cerca de tres cuartas partes de esa baja nacional**: pasó de 254 a 159, una reducción de 95 registros frente a los 126 del país. Limón fue en sentido contrario, de 159 a 175. Una baja nacional puede coexistir con aumentos en algunas provincias.

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

En todos los años comparados, los datos abiertos están entre 10% y 16% por encima de los totales anunciados. Estos últimos corresponden a las publicaciones citadas y pueden cambiar con revisiones posteriores. En 2025 el OIJ también publicó totales por provincia, y los datos abiertos son más altos en las siete.

No pude encontrar la razón en los archivos. No tienen un identificador de caso, así que no puedo saber si hay filas duplicadas, si el dataset cuenta algo que el total oficial excluye, o si revisiones posteriores explican la diferencia. En los últimos años, cerca de una de cada ocho filas de homicidio es idéntica a otra. Puede ser una segunda víctima del mismo ataque o un duplicado.

Ambas fuentes muestran un aumento entre 2019 y 2025: según los totales anunciados por el OIJ, fue de 55%; en los datos abiertos, de 60%. Esa coincidencia respalda la dirección del cambio, pero no garantiza que las proporciones por móvil o provincia estén libres de sesgos. Uso los datos abiertos para explorar esos desgloses y los totales del OIJ para hablar del número de víctimas.

La lección que me llevo no es exclusiva de Costa Rica: **un conjunto de datos abierto necesita contraste con otras publicaciones y una definición clara de lo que cuenta.** Sin esa revisión, habría presentado filas del archivo como si fueran el número oficial de víctimas.

## Lo que estos datos no pueden decir

Algunas preguntas necesitan otras fuentes:

- **Si los delitos contra la propiedad realmente bajaron.** Menos registros pueden significar menos delitos o menos denuncias. Las encuestas de victimización, que les preguntan directamente a los hogares, son la forma de distinguir una cosa de la otra.
- **El riesgo por habitante.** Los gráficos muestran conteos e índices, no tasas por cada 100.000 habitantes. Para calcular tasas nacionales y provinciales hacen falta estimaciones de población para esos mismos años y territorios; las estimaciones por cantón serían necesarias para un análisis cantonal. Sin ese ajuste, una provincia con más registros no necesariamente tiene una tasa mayor.
- **Nada sobre el sexo de las víctimas.** Esa columna viene vacía en todos los años de los archivos.

## Lo que me deja este ejercicio

Esperaba una sola historia: la criminalidad en aumento. Encontré una caída de más de 40% en los registros de asaltos, robos y hurtos entre enero-septiembre de 2015 y el mismo período de 2026. Los registros de homicidio, en cambio, seguían 46% por encima de 2015, aunque bajaron respecto a 2025. En los años completos, el aumento se concentra en la categoría de ajuste de cuentas o venganza.

Eso cambia las preguntas que conviene hacer. Para los delitos contra la propiedad, falta saber cuánto de la caída refleja menos delitos y cuánto refleja cambios en la denuncia o el registro. Para los homicidios, hace falta entender el aumento y su distribución. Hablar de una sola cifra de «criminalidad» borra esas diferencias y dificulta evaluar las respuestas.
