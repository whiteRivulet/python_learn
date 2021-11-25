import requests
import ctypes
url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
r = requests.get(url)


if r:
    APOD = r.json()['url'] # JSON wird für den Key "URL durchsucht
    pic = requests.get(APOD, allow_redirects=True) # Bild-URL in APOD gestored
    if  "jpg" not in APOD:
        print("No image")
    else:
        open('C:\\Users\\buellesbach\\Desktop\\code\\nasa\\APOD.jpg', 'wb').write(pic.content) # "wb" erlaubt editieren von non-Text Files (binary mode)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\buellesbach\\Desktop\\code\\nasa\\APOD.jpg" , 0)
        print("DONE")
else:
    print("Error")
