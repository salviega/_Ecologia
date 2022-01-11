# Descarga automática de imágenes landsat8 - 


## Importante

El programa se ejecuta unicamente corrinedo el script _main_. Lo más probale es que tenga que descargar algunas librerías, en la sección de instrucciones me encargo de eso. 

## Instrucciones

1. Lo primero que hay que hacer es descargar Python 3. En este vídeo le explican como descargarlo, instalarlo y comprobarlo: https://www.youtube.com/watch?v=BNcpRwxH8So

2. Luego, deben descargar el repositorio, pero para nuestros fines será suficiente la descarga de la carpeta landsat8; puede ser mediante el controlador de versiones GIT o undiendo el botón descargar como se presenta abajo. 

![Screen Shot 2022-01-11 at 05 14 23](https://user-images.githubusercontent.com/90350943/148924682-6f156e4f-0eb0-4156-95ce-8a136dbe7e35.png)

Cuando haya descomprimido el archivo .zip abra una ventana de comando, como vió en el vídeo del paso 1., e ingrese a la carpeta. En mi caso esta será la ruta que uso para llegar a los archivos. "cd" es un instrucción que entiende el compu para moverse entre carpetas.

```
cd Downloads/_Ecologia-main/Python/sensores_remotos/landsat8
```

3. Estando en la carpeta «landsat8» instale los paquetes respectivos con la siguiente linea de código.

```
pip install -r requirements.txt
```

4. En este punto, y por comodidad, abriremos el archivo «main.py» por algún editor de código, puede ser Pycharm o Visual Studio Code, por ejemplo, hay millones de editores de código fuente. Aquí le explicará como instalar Python en ambos editores. Yo usaré Visual Studio.

Pycharm: https://www.youtube.com/watch?v=EhN8BaHLCfY

Visual Studio Code: https://www.youtube.com/watch?v=-IyA_Yvs8IQ

luego de eso se encontrará con este código, lo único que tendrá que hacer es reemplazar las xxx que se encuentran dentro de las comillas y ya.

![Screen Shot 2022-01-11 at 05 50 22](https://user-images.githubusercontent.com/90350943/148929828-fb292c75-9412-40f3-8e50-6d3ca88e08d4.png)

Pero vamos por partes.

5. En la linea 4 «# Site's coord (EPSG:4326)» tendrá que escribir las coordenadass del lugar de interés, en este ejemplo tomaré la ciudad de Bogotá, Bogotá urbana. En internet está todo, busque por ahí las coordenadas. Después de reemplazar los valores «000» de latitud y longitud, mire el «screenshot», ingrese a esta página https://geojson.io/ para que genere el área de estudio y descarge el archivo .JSON. La página es contraintuitiva por lo que no explicaré como usarla, y además quiere sabe que es JSON le dejo un vídeo que se lo explica. Lo que sí debe saber es que en el archivo que descargará se encuentran las coordenasdas en el formato que el programa entiende. 

¿Qué es JSON?:  https://www.youtube.com/watch?v=FnW_WeBlCMk

![Screen Shot 2022-01-11 at 06 13 06](https://user-images.githubusercontent.com/90350943/148932669-fa31acf9-8778-4637-b90b-947d62e8f290.pn



## Bibliografía

## Construido

* [Python 3] (https://www.python.org/) - lenguaje usado

## Autor

* **Santiago Viana** - *Trabajo Inicial y documentación* - [salviega](https://github.com/salviega)