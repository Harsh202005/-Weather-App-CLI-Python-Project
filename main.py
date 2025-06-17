import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("cod") != 200:
        print("❌ City not found or error in fetching data.")
        return

    print(f"\n📍 Weather in {data['name']}, {data['sys']['country']}:")
    print(f"🌡️ Temperature: {data['main']['temp']}°C")
    print(f"🌤️ Condition: {data['weather'][0]['description'].capitalize()}")
    print(f"💧 Humidity: {data['main']['humidity']}%")
    print(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY_HERE"  # Replace with your real API key
    city = input("Enter city name: ")
    get_weather(city, api_key)
