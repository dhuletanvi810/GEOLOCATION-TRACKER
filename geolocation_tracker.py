import folium
import webbrowser

def get_demo_location():
    
    ip = "103.21.75.122"
    city = "Mumbai"
    region = "Maharashtra"
    country = "IN"
    latitude = 19.0760
    longitude = 72.8777

    print(f"IP Address: {ip}")
    print(f"Location: {city}, {region}, {country}")
    print(f"Coordinates: {latitude}, {longitude}")

    return latitude, longitude, city

def create_map(lat, lon, location_name):
    # map 
    demo_map = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker(
        [lat, lon],
        popup=f"Demo Location: {location_name}",
        tooltip="Mumbai (Demo)",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(demo_map)
  
    demo_map.save("demo_mumbai_map.html")
    webbrowser.open("demo_mumbai_map.html") 

if __name__ == "__main__":
    lat, lon, location_name = get_demo_location()
    if lat and lon:
        create_map(lat, lon, location_name)
