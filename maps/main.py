#This program allows you to display a map in the browser using coordinates entered by the user.
import folium
x = float(input("Input coordinate X:"))
y = float(input("Input coordinate Y:"))
place = folium.Map([x,y])
place.save('index.html')