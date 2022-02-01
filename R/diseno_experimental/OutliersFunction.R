# Santiago Viana
# Enero 2022
# Version 1.0

# La función «installAndLoadPackages» descargará los paquetes respectivos para la ejecutción correcta del script y luego los importará al proyecto.
# Si el usuario descargó los paquetes con anterioridad la función sólo los importará.

installAndLoadPackages <- function(packages){
  new.packages <- packages[!(packages %in% installed.packages()[, "Package"])]
  
  if (length(new.packages)) {
    install.packages(new.packages, dependencies = TRUE)
    sapply(packages, require, character.only = TRUE)
  }else{
    sapply(packages, require, character.only = TRUE)
  }
}

# La función «removeOutliers» será la encargada de retornar el dataframe sin los datos «outliers», en la consola 
# se presentaran los datos, en este caso especies de cada parce. 

# IMPORTANTE:

# La selección de outliers se realiza mediante la puntuación de z, calculada mediante la desviación estandar y media de la población.
# Los valores superiores a esta medida son conciderados valores atípicos, poco corrientes, desde un punto de vista ESTADÍSTICO. 
# El umbral de distribución es "subjetivo" pero un gran número de literatura estadísitca consideran umbral de 3 cómo el más óptimo para su
# detección.

removeOutliers<-function(x, column, pos, umbral){
  
  posM<- strsplit(pos, split = ":")
  posM<-  posM[[1]]
  posList<- NULL
  for (i in posM)
  {
    posList<- append(posList,as.numeric(i))
  }
  sample<- (unique(x[,column]))
  sampleOutliersList<- NULL
  sampleFDList<-NULL
  i<- 1
  j<- 1
  k<- 1
  
  while (i<= length(sample)) {
    
    dfSample<- x %>% dplyr::filter (x[,column] == sample[i])
    dfM<- as.data.frame(dfSample[posList[1]:posList[2]])
    
    y<- NULL
    while(k <= ncol(dfM))
    {
      z<- (dfM[,k] - mean(dfM[,k]))/sd(dfM[,k])
      
      if(!length(which(z > umbral)) == 0){
        
        y<- c(y, which(z > umbral))
        
      }
      y
      k<- k+1
    }
    k<- 1
    
    if(!is.null(y)){
      
      y<- unique(y)
      y<- sort(y, decreasing = FALSE)
      
      dfSample$numberRow<- seq.int(nrow(dfSample))
      dfSampleOutliers<- dfSample[dfSample$numberRow %in% y,]
      sampleOutliersList[[j]]<- dfSampleOutliers
      dfSample<- dfSample[!dfSample$numberRow %in% y,]
      sampleClean<- dfSample
      j<- j+1
      
    }else{
      
      dfSample$numberRow<- seq.int(nrow(dfSample))
      sampleClean<- dfSample
    }
    
    sampleFDList[[i]]<- sampleClean
    sampleFDList
    
    if (i == length(sample)){
      xOutliers<- do.call(rbind, sampleFDList)
      xOutliers$ID<- seq.int(nrow(xOutliers))
      xOutliers<- subset(xOutliers, select = -c(numberRow))
      outliers<- do.call(rbind, sampleOutliersList)
      outliers$ID<- seq.int(nrow(outliers))
      outliers<- subset(outliers, select = -c(numberRow))
      writeLines(sprintf(" --------------------------------------------- Lista de outliers eliminadas: --------------------------------------------- "))
      writeLines(sprintf(" ------------------------------------------------------------------------------------------------------------------------- "))
      writeLines(sprintf("                                                                                                                           "))
      print(outliers)
      writeLines(sprintf("                                                                                                                           "))
      writeLines(sprintf("                                                                                                                           "))
      writeLines(sprintf(" ------------------------------------------------------------------------------------------------------------------------- "))
      writeLines(sprintf(" --------------------------------------------- Lista de outliers eliminadas: --------------------------------------------- "))
      return(xOutliers)
    }
    i<- i+1
  }
}

# La variable «packages» contiene los nombres de los paquetes que harán que «removeOutliers» funcione, y será el parámetro de «installAndLoadPackages».

packages <- c("dplyr","tibble")

installAndLoadPackages(packages)

# Ejemplo práctico

df<-read.csv("/Users/santiagoviana/Documents/Proyectos/1. DF en Caquetá/Datos/0.0_Base_de_datos.csv", sep = ",", header = TRUE)# df = x
head(df[5], n=5) # column = 5 ... en la columna 5 se encuentran las parcelas o sub-muestras dónde se reirará la función
head(df[,7:10]) # pos = "7:10 ... desde la columna 7 a la 10 se encuentran las mediciones
df<- removeOutliers(x = df, column = 5, pos = "7:10", umbral = 3) # umbral 3 es el escogido para el ejemplo. 
