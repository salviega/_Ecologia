# Estadística Descriptiva - «Outliers»

En una colección de datos, se suele observar valores que sobrepasan los límites de la distribución de probabilidad de la variable o de las variables que se tomaron registro. Eso podría deberse a que la toma se realizó en una circunstancia excepcional donde las condiciones del registro permitiera esa clase de valor. Sin embargo, lo general o lo más común es que ese dato pertenezca a otra población, o quizá en la práctica; el daños, la falta de calibración de instrumentos de medición o simplemente por error humano en algún proceso de datificación genere esos valores atípicos. Esos valores son mayoritariamente conocidos como «outliers».
La importancia de detectar «outliers» en nuestros datos es importante ya que podría comprometer el cuerpo de nuestros modelos, lo que ocasiona mala interpretación de nuestros resultados.


Es por eso que se deben pasar nuestros datos por métodos de detección de «outliers» antes de pasarlos a pruebas o modelos estadísticos. Uno de esos métodos de detección es la puntuación de z o «_z score_». El cual genera un tasa de valor común del tamaño de la población mediante su media y desviación estándar. Los datos que se mantengan dentro de ese tamaño se alinean al patrón aleatorio natural de la población, los que no, los que punteen valores críticos de z, por fuera del tamaño propuesto, son considerados valores anómalos, que debaten la hipótesis nula de la puntuación. Para nuestro caso, esos valores son nuestros «outliers», vistos desde un punto ESTADÍSTICO.

El umbral de la puntuación de dispersión típica es "subjetiva" pero una extensa literatura considera (+3) desviaciones a la derecha y (-3) a la izquierda de la curva de dispersión típica cómo medición óptima para detectar «outliers».

## Importante

La función «removeOutliers» será la encargada de retornar el set de datos sin «outliers» pero se mostrará en consola los registros eliminados. 

La función tiene la ventaja de que el umbral de detección es móvil, el usuario tiene la potestad para escoger una puntuación de extensión de la curva de dispersión. Al igual que en el programa de grupos funcionales, realizó una práctica para mostrar cómo se deben pasar el set de datos por la función. 

Los datos del ejemplo son de mi tesis de pregrado "Diversidad funcional a lo largo de la cronosecuencia de pastura abandonada a bosque húmedo tropical en paisaje amazónico" pertenecientes al instituto SINCHI del proyecto: «Restauración de áreas disturbadas por implementación de sistemas productivos agropecuarios en el departamento de Caquetá».

## Bibliografía

Rousseeuw, P. J., & Hubert, M. (2011). Robust statistics for outlier detection. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 1(1), 73–79. https://doi.org/10.1002/widm.2

Viana V., S. A. (2020). Diversidad funcional a lo largo de la cronosecuencia de pastura abandonada a bosque húmedo tropical en paisaje amazónico [Pontificia Universidad Javeriana]. https://repository.javeriana.edu.co/handle/10554/53026

## Construido

* [R] (https://cran.r-project.org/) - lenguaje usado

## Autor

* **Santiago Viana** - *Trabajo Inicial y documentación* - [salviega](https://github.com/salviega)
 
