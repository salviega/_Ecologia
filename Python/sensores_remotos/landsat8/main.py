import landsat
from landsat import landsatAPI

# Site's coord (EPSG:4326)
latitude = 5.48333
longitude = -75.0667
geojson = "xxx" # https://geojson.io/
footprint = landsat.Footprint(latitude, longitude, geojson)

# USGS website
username = 'xxx'
password = 'xxx'

# Download folder
donwload_folder = "xxx"

# Download imagen Landsat 8 
api = landsatAPI(username, password)
api.query(footprint, ("xxx", "xxx"), donwload_folder) # date start & date end