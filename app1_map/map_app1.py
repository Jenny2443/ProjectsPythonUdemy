import folium
import pandas

# List of the markers
#coordenadas = [[40.349409,-3.836135],[40.338375,-3.870515],[40.316064,-3.877072]]
#names_hospitals = ["Hospital de Alcorcón", "Hospital Rey Juan Carlos", "Hospital Universitario de Móstoles"]


# READ THE INFORMATION IN THE TXT FILE
data = pandas.read_csv("hospitales.txt")
    # get the coordenates
names_hospitals = list(data["NOMBRE"])
latitud = list(data["LAT"])
longitud = list(data["LON"])
coordenadas = [(lat,lon) for lat, lon in zip(latitud,longitud)]
# dictionary to know if a certain hospital has heliport
has_helo = dict(zip(data["NOMBRE"],data["HELO"]))

def colorMarker(hospital):
    if hospital in has_helo and has_helo.get(hospital) == "YES":
        return "blue"
    else:
        return "red"

map = folium.Map(location=[40.419241, -3.71], zoom_start=10) 
    # Get the map centered at location (Madrid) 
    # with started zoom on the location
    # width and height as default 100%
    
# HERE WE CAN ADD ELEMENTS (CHILDREN) on feature groups
fg_hospitals = folium.FeatureGroup(name="Hospitals")


#Adding the markers
for coordenada, nombre in zip(coordenadas,names_hospitals):
    fg_hospitals.add_child(folium.Marker(location=coordenada,popup=nombre,icon=folium.Icon(color=colorMarker(nombre))))
    # Another way to make the marker as a circle
    #fg.add_child(folium.CircleMarker(location=coordenada,radius=8,popup=nombre,fill_color=colorMarker(nombre),color="grey",fill_opacity=0.7))

# To add the lines of the borders and style the color based on population
fg_population = folium.FeatureGroup(name="Population")
fg_population.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
                            style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
                                                      else "yellow" if x["properties"]["POP2005"] < 20000000
                                                      else "red"}))

#Adding the feature group
map.add_child(fg_hospitals)
map.add_child(fg_population)

# Adding control layer feature (if we do this you can only have the option to have all the markers or none of them) -> to solve create different fg
map.add_child(folium.LayerControl())
    
map.save("Map1.html") # Save the map in html to see it on the web

