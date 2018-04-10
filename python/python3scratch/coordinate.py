import simplekml
import pandas

df= pandas.read_csv('/users/robpecor/Downloads/coordinates.csv')

kml = simplekml.Kml()

for lon, lat in zip(df["Longitude"], df["Latitude"]):
    kml.newpoint(coords=[(lon, lat)])

kml.save('myPoints.kml')
