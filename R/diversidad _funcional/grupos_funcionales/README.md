# Diversidad funcional - grupos funcionales

La diversidad funcional es un componente de la biodiversidad que se centra en el valor y variabilidad de las características de los organismos que influyen en el funcionamiento del ecosistema (Petchey & Gaston, 2006). El uso de grupos funcionales permite identificar los diferentes conjuntos de especies dentro de una comunidad que realizan un mismo proceso ecosistémico, debido a que comparten similitud en el consumo de recursos y/o características de hábitat (Blondel, 2003). El conocimientos de grupos funcionales es clave para conocer el nivel de estabilidad y resiliencia de la comunidad al disturbio y el mantenimiento de procesos ecosistémicos, mediante, por ejemplo, el vínculo con el tamaño de los grupos funcionales, el nivel de redundancia funcional (Biggs et al., 2020).

## Importante

La función «functionalGroups» será la encargada de retornar una tupla de dos elementos; 1. el dataframe inicial con una columna respectiva al grupo funcional que pertenece cada especie, y 2. el dendograma con el nivel de disimilaridad. 

La distancia euclidiana y el método ward.D2 son los escogidos como criterios de selección del par de clusters. Y la función sólo soportará la escogencia de 2 a 10 grupos funcionales, en el caso de incumplir esta condición la función no correrá, también recomiendo transformar los datos (no importa que escala de transformación use) esto mejorará la presentación visual. En el ejemplo práctico uso «scale» como método de transformación.

Los datos del ejemplo son de Flake et al (2021), ver bibliografía. 

## Bibliografía

Biggs, C. R., Yeager, L. A., Bolser, D. G., Bonsell, C., Dichiera, A. M., Hou, Z., Keyser, S. R., Khursigara, A. J., Lu, K., Muth, A. F., Negrete, B., & Erisman, B. E. (2020). Does functional redundancy affect ecological stability and resilience? A review and meta-analysis. Ecosphere, 11(7). https://doi.org/10.1002/ecs2.3184

Blondel, J. (2003). Guilds or functional groups: Does it matter? Oikos, 100(2), 223–231. https://doi.org/10.1034/j.1600-0706.2003.12152.x

Flake, S. W., Abreu, R. C. R., Durigan, G., & Hoffmann, W. A. (2021). Savannas are not old fields: Functional trajectories of forest expansion in a fire-suppressed Brazilian savanna are driven by habitat generalists. Functional Ecology, 35(8), 1797–1809. https://doi.org/10.1111/1365-2435.13818

Petchey, O. L., & Gaston, K. J. (2006). Functional diversity: Back to basics and looking forward. Ecology Letters, 9(6), 741–758. https://doi.org/10.1111/j.1461-0248.2006.00924.x

## Construido

* [R] (https://cran.r-project.org/) - lenguaje usado

## Autor

* **Santiago Viana** - *Trabajo Inicial y documentación* - [salviega](https://github.com/salviega)
 
