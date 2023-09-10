import tkinter as tk
import requests

API_KEY = "80e5b9b5de2a13cb9a45f2838b8ebd36"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.location_label = tk.Label(root, text="Enter location:")
        self.location_label.pack()

        self.location_entry = tk.Entry(root)
        self.location_entry.pack()

        self.fetch_button = tk.Button(root, text="Fetch Weather", command=self.fetch_weather)
        self.fetch_button.pack()

        self.weather_label = tk.Label(root, text="")
        self.weather_label.pack()

    def fetch_weather(self):
        location = self.location_entry.get()
        if location:
            weather_data = self.get_weather_data(location)
            if weather_data:
                self.display_weather(weather_data)
            else:
                self.weather_label.config(text="Location not found.")
        else:
            self.weather_label.config(text="Please enter a location.")

    def get_weather_data(self, location):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
            response = requests.get(url)
            data = response.json()
            return data

        except requests.exceptions.RequestException as e:
            print("Request Exception:", e)

    def display_weather(self, weather_data):
        print(weather_data)  # Add this line to inspect the response

        if 'main' in weather_data:
            temperature = weather_data['main'].get('temp')

            if temperature is not None:
                humidity = weather_data['main'].get('humidity')
                wind_speed = weather_data['wind'].get('speed')
                weather_condition = weather_data['weather'][0].get('description')

                weather_info = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nCondition: {weather_condition}"
                self.weather_label.config(text=weather_info)

            else:
                self.weather_label.config(text="Temperature data not found.")
        else:
            self.weather_label.config(text="Weather data not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
