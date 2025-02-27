import requests
import os
from dotenv import load_dotenv
from plyer import notification

# Load API Key
load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")

CITY = "Osaka"
ICON_PATH = os.path.abspath("weather_app/assets/chibi.ico") 

def get_weather():
    try:
        payload = {"q":CITY, "appid":API_KEY, "units":"metric"}
        response = requests.get(URL,params=payload)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"].capitalize()

            return f"{CITY}: {weather_desc}, {temp}°C"
        else:
            return "Error fetching weather."
    except requests.ConnectTimeout as e:
        return f"Timeout Error: {str(e)}"
    
    except requests.JSONDecodeError as e:
        return f"JSON Decode Error: {str(e)}"
    
    except requests.RequestException as e:
        return f"Request Exception Error: {str(e)}"
    
    

def send_notification():
    weather_info = get_weather()
        
    notification.notify(
        app_icon=ICON_PATH,
        message=weather_info,
        timeout=10, 
        title="Here's your Osaka Weather Update Ayaneta Senpai~nya",
    ) 
    
if __name__ == "__main__":
    send_notification()
