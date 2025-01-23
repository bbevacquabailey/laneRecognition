import ee
import geemap as gmap

# Initialize the Earth Engine library
#ee.Initialize(project="ee-bevacquab7")

latitude = 27.96678402973752
longitude = -82.50553584388906

Map = gmap.Map()

# Define the area of interest
geometry = ee.Geometry.Point([longitude, latitude]).buffer(1000)  # 1000-meter radius

# Load a satellite image collection
image = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2") \
    .filterBounds(geometry) \
    .filterDate('2022-01-01', '2022-12-31') \
    .median()

# Export the image
task = ee.batch.Export.image.toDrive(
    image=image,
    description='Satellite_Image',
    scale=30,
    region=geometry.getInfo()['coordinates'],
    fileFormat="GEO_TIFF"
)
task.start()
