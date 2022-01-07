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

# Por favor, pase al archivo README de la carpeta

functionalGroups<- function(df){
  
  summaryCluster <-NbClust(df, distance = "euclidean", min.nc=2, max.nc=10, method = "kmeans", index = "alllong")
  numberGroups <-as.numeric(readline(prompt="How many functional groups do you want to create? (min:2 max:10): "))
  if(2<=numberGroups && numberGroups<=10){
    colorGroup <-switch(numberGroups,
                        colorGroup <-NULL,                
                        colorGroup <-c("#1B9E77","#D95F02"),
                        colorGroup <-c("#1B9E77","#D95F02","#7570B3"),
                        colorGroup <-c("#1B9E77","#D95F02","#7570B3","red"),
                        colorGroup <-c("#1B9E77","#D95F02","#7570B3","red","yellow"),
                        colorGroup <-c("#1B9E77","#D95F02","#7570B3","red","yellow","#02ced9"),
                        colorGroup <-c("#1B9E77","#D95F02","#7570B3","red","yellow","#02ced9","#e39fe2"),
                        colorGroup <-c("#1B9E77","#D95F02","#7570B3","red","yellow","#02ced9","#e39fe2","black"),
                        colorGroup <-c("black","black","black","black","black","black","black","black","black"),
                        colorGroup <-c("black","black","black","black","black","black","black","black","black","black"))
    group <- hcut(df, k = numberGroups, hc_metric = "euclidean", hc_method = "ward.D2")
    dend <-fviz_dend(group, rect = TRUE, cex = 0.5,
                     horiz = FALSE, ylab = "Disimilary", xlab = "functional groups", main = "",
                     k_colors = colorGroup,color_labels_by_k = FALSE)
  }else{
    print("There was an error, The function ended")
  }
  kx <- kmeans(df, centers = numberGroups, nstart = 25)
  dfReturn <-df
  dfReturn <-as.data.frame(dfReturn)
  dfReturn$groups<-as.factor(kx$cluster)
  dfReturn <-dfReturn[order(dfReturn$groups),]
  result <-list(dfReturn,dend)
  return(result)
}

# La variable «packages» contiene los nombres de los paquetes que harán que «functionalGroups» funcione, y será el parámetro de «installAndLoadPackages».

packages <- c("factoextra","NbClust","tibble")

installAndLoadPackages(packages)

# Ejemplo: el objetivo de la práctica es mostrar como debe prepararse el dataframe para pasarlo en «functionalGroups»

example<- read.csv('/Users/santiagoviana/Desktop/clean_species2020-06-09.csv', header =  TRUE, sep = ',')
head(example, n = 10) # 
example<- example[complete.cases(example),]
head(example, n = 10)
example<- example[,-c(1,15,16)]
head(example, n = 10)
example<- as.data.frame(example)
row.names(example) <- NULL
head(example, n = 10)
example<- column_to_rownames(example, var = 'Code')
head(example, n = 10)
example<- scale(example)
head(example, n = 10)

functionalGroups(example)

