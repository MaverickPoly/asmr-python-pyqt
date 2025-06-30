import sys
import requests

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

API_KEY = ""  # Open Weather Map Api KEY
URL = "http://api.openweathermap.org/data/2.5/weather"


class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window
        self.setWindowTitle("Weather App")
        self.setGeometry(500, 200, 600, 800)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Centering layout
        outer_layout = QVBoxLayout(central_widget)
        outer_layout.setAlignment(Qt.AlignCenter)

        # Frame acts like a container
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("padding: 20px; border-radius: 10px; background-color: #f0f0f0;")
        frame_layout = QVBoxLayout()
        frame.setLayout(frame_layout)

        # Form
        input_form = QHBoxLayout()
        self.city_input = QLineEdit()
        self.city_input.setStyleSheet("padding: 12px; border-radius: 12px; font-size: 26px; border: 1px solid #bbb")
        self.city_input.setPlaceholderText("Enter city")
        submit_btn = QPushButton("Get Weather")
        submit_btn.setStyleSheet("padding: 12px 28px; border-radius: 12px; background: blue; color: white; font-size: 20px;")
        submit_btn.clicked.connect(self.fetch_weather)
        input_form.addWidget(self.city_input)
        input_form.addWidget(submit_btn)
        frame_layout.addLayout(input_form)

        # Fetched Info
        self.city_label = QLabel("City")
        self.city_label.setStyleSheet("font-size: 34px; font-weight: bold;")
        self.country_label = QLabel("Country")
        self.country_label.setStyleSheet("font-size: 30px; margin-bottom: 80px;")
        self.temp_label = QLabel("Temp")
        self.temp_label.setStyleSheet("font-size: 40px; font-weight: bold;")
        self.description_label = QLabel("Description")
        self.description_label.setStyleSheet("font-size: 26px; margin-bottom: 60px;")
        self.humidity_label = QLabel("Humidity")
        self.humidity_label.setStyleSheet("font-size: 30px;")
        self.wind_speed_label = QLabel("Wind Speed")
        self.wind_speed_label.setStyleSheet("font-size: 30px;")

        for label in [
            self.city_label, self.country_label, self.temp_label,
            self.description_label, self.humidity_label, self.wind_speed_label
        ]:
            label.setAlignment(Qt.AlignCenter)
            frame_layout.addWidget(label)

        # Add frame to center layout
        outer_layout.addWidget(frame)


    def fetch_weather(self):
        city_name = self.city_input.text().strip()
        if not city_name:
            return
        params = {
            'q': city_name,
            'appid': API_KEY,
            'units': "metric"
        }

        try:
            response = requests.get(URL, params=params)
            response.raise_for_status()
            weather_data = response.json()

            city = weather_data.get("name")
            country = weather_data.get("sys", {}).get("country")
            temp = weather_data.get("main", {}).get("temp")
            description = weather_data.get("weather", [])[0].get("description", "N/A")
            humidity = weather_data.get('main', {}).get('humidity')
            wind_speed = weather_data.get("wind", {}).get("speed")

            self.city_label.setText(city)
            self.country_label.setText(country)
            self.temp_label.setText(str(temp))
            self.description_label.setText(description)
            self.humidity_label.setText(str(humidity))
            self.wind_speed_label.setText(str(wind_speed))
        except Exception as e:
            print(f"Error: {e}")



def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
