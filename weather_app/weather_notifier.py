import requests
import os
from dotenv import load_dotenv
from plyer import notification

# Load API Key
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Set city and API URL
CITY = "Osaka"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"].capitalize()

            return f"{CITY}: {weather_desc}, {temp}°C"
        else:
            return "Error fetching weather."
    except Exception as e:
        return f"Error: {str(e)}"
    
ICON_PATH = os.path.abspath("weather_app/assets/chibi.ico") 

def send_notification():
    weather_info = get_weather()
    
    
    notification.notify(
        title="Here's your Osaka Weather Update Ayaneta Senpai~nya",
        message=weather_info,
        app_icon=ICON_PATH,
        timeout=10 
    )

if __name__ == "__main__":
    send_notification()
