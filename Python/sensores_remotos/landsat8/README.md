# Descarga automática de imágenes landsat 8 -
 
 
## Importante
 
El programa se ejecuta únicamente corriendo el script _main_. Lo más probable es que tenga que descargar algunas librerías, en la sección de instrucciones me encargo de eso.
 
## Instrucciones
 
1. Lo primero que hay que hacer es descargar Python 3. En este vídeo le explican como descargarlo, instalarlo y comprobarlo: https://www.youtube.com/watch?v=BNcpRwxH8So
 
2. Luego, deben descargar el repositorio, pero para nuestros fines será suficiente la descarga de la carpeta landsat 8; puede ser mediante el controlador de versiones GIT o hundiendo el botón descargar como se presenta abajo.
 
![Screen Shot 2022-01-11 at 05 14 23](https://user-images.githubusercontent.com/90350943/148938919-1fc28175-21cf-45dd-ba90-2815c9f1f527.png)
 
Cuando haya descomprimido el archivo .zip abra una ventana de comando, como vió en el vídeo del paso 1., e ingrese a la carpeta. En mi caso esta será la ruta que uso para llegar a los archivos. "cd" es un instrucción que entiende el compu para moverse entre carpetas.
 
```
cd Downloads/_Ecologia-main/Python/sensores_remotos/landsat8
```
 
3. Estando en la carpeta «landsat 8» instale los paquetes respectivos con la siguiente linea de código.
 
```
pip install -r requirements.txt
```
 
4. En este punto, y por comodidad, abriremos el archivo «main.py» por algún editor de código, puede ser Pycharm o Visual Studio Code, por ejemplo, hay millones de editores de código fuente. Aquí le explicará cómo instalar Python en ambos editores. Yo usaré Visual Studio.
 
Pycharm: https://www.youtube.com/watch?v=EhN8BaHLCfY
 
Visual Studio Code: https://www.youtube.com/watch?v=-IyA_Yvs8IQ
 
Luego de eso se encontrará con este código, lo único que tendrá que hacer es reemplazar las xxx que se encuentran dentro de las comillas y ya está.
 
![Screen Shot 2022-01-11 at 05 50 22 2](https://user-images.githubusercontent.com/90350943/148939217-8be63bc9-d49f-4584-b06e-695c8adad752.png)
 
Pero vamos por partes.
 
5. En la línea 4 «# Site 's coord (EPSG:4326)» tendrá que escribir las coordenadas del lugar de interés en las líneas 5 y 6, en este ejemplo tomaré la ciudad de Bogotá, Bogotá urbana. En internet está todo, busque por ahí las coordenadas. Después de reemplazar los valores «000» de latitud y longitud, mire el «screenshot».
 
![Screen Shot 2022-01-11 at 06 22 31](https://user-images.githubusercontent.com/90350943/148939396-094e72b0-5b39-46c0-94a9-ea4723a7d33e.png)
 
Ingrese a esta página https://geojson.io/ para que genere el área de estudio y descarge el archivo .JSON. La página es contraintuitiva por lo que no explicaré como usarla, y si quiere sabe qué es JSON le dejo un vídeo que se lo explica. Lo que sí debe saber es que en el archivo contiene las coordenadas en el formato que el programa entiende.
 
¿Qué es JSON?:  https://www.youtube.com/watch?v=FnW_WeBlCMk
 
![Screen Shot 2022-01-11 at 06 13 06](https://user-images.githubusercontent.com/90350943/148939267-96517253-cbd6-4c8d-9d00-9420999a63d2.png)

 
para finalizar escriba la dirección donde se encuentra el archivo, mire otra vez el «screenshot» en la línea 7.
 
6. Ahora lo único que falta es cambiar las xxx de la línea 11 y 12 por el nombre de usuario y contraseña de su cuenta de USGS para la descarga de imágenes landsat8, aquí: https://earthexplorer.usgs.gov/
 
7. De nuevo, en la línea 15 tendrá que escribir la dirección donde se guardarán las imágenes, yo las guardaré en la carpeta de descargas, que es la misma ruta que usé para indicar la ubicación de las coordenadas. Mire el «screenshot» aquí abajo.
 
![Screen Shot 2022-01-11 at 06 33 36](https://user-images.githubusercontent.com/90350943/148939513-a45bda24-18b1-4eff-a7c3-16b5beb50e67.png)
 
8. Por último y para finalizar escriba en la línea 19, el rango de tiempo en fecha que le interesa, donde vaya primero el mes/día/año de inicio y luego la fecha mes/día/año final. Para el ejemplo usaré estas fechas; 01/01/2021 y 01/31/2021.
 
![Screen Shot 2022-01-11 at 06 37 34](https://user-images.githubusercontent.com/90350943/148939650-1a3a0d2a-c0b2-4f3e-9316-fc9ac216cb00.png) 

9. Ya puede hacer magia, corra el «script».
 
10. Si desea la descarga multitemporal, ya dependerá de su escala de trabajo, tendrá que modificar las fechas de la línea 19. Yo copiaría esa línea de código, digamos 5 veces, para realizar un estudio multitemporal de 5 años, de 2017 a 2021 en el mes de enero; mire el «screenshot», y corra el script.

![Screen Shot 2022-01-11 at 06 49 02](https://user-images.githubusercontent.com/90350943/148939746-8c8fe99a-94d8-46b9-bedb-f7ef0a9aaeb3.png)
 
## Construido
 
* [Python 3] (https://www.python.org/) - lenguaje usado
 
## Autor
 
* **Santiago Viana** - *Trabajo Inicial y documentación* - [salviega](https://github.com/salviega)