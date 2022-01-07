import landsat
from landsat import landsatAPI

# Site's coord (EPSG:4326)
latitude = 5.48333
longitude = -75.0667
geojson = "/Users/santiagoviana/Desktop/SIG/PNNSFL/Imagenes satelitales/map.geojson" # https://geojson.io/
footprint = landsat.Footprint(latitude, longitude, geojson)

# USGS website
username = 'salviega6'
password = '6y2w4r3e3e1q9o'

# Download folder
donwload_folder = "/Users/santiagoviana/Downloads"

# Download imagen Landsat 8 
api = landsatAPI(username, password)
api.query(footprint, ("01/01/2017", "07/31/2017"), donwload_folder) # date start & date end