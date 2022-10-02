import pywhatkit
import time
import requests
import json
import socket



class Whatsapp:
    def __init__(self) -> None:
        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)
        print("Your Computer IP Address is:" + IP)

        request_url = 'https://geolocation-db.com/jsonp/'

        response = requests.get(request_url)
        result = response.content.decode()

        result = result.split("(")[1].strip(")")

        result  = json.loads(result)
        latitude = result["latitude"]
        longitude = result["longitude"]
        
        t = time.localtime()
        hour = time.strftime("%H", t)
        minute = time.strftime("%M", t)
        Hour = int(hour)
        Minute = int(minute)+1

        pywhatkit.sendwhatmsg("+919663628104", "Fire at Latitude and Longitude:"+str(latitude)+","+str(longitude), Hour, Minute)