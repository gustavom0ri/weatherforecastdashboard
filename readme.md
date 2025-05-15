# Weather Forecast App 🌦️  


About the Project
-----------------
This is a simple and interactive web application built with Streamlit.
It allows users to:
- Select a city
- Choose how many days to forecast (1 to 5)
- Choose the forecast type (Temperature or Sky)
- View temperatures as a Plotly line chart or weather conditions as icons

## Technologies Used

-----------------
- Streamlit - Web app framework
- Plotly - Interactive visualizations
- OpenWeatherMap API - Weather data
- Python Requests - HTTP requests

## Project Structure

-----------------
weather-forecast-app/
├── app.py           --> Main Streamlit application
├── backend.py       --> API interaction logic
├── images/          --> Weather icons (clear.png, cloud.png, etc.)
└── README.txt       --> Project documentation

## How to Run the App

------------------
1. Clone the repository:
   git clone https://github.com/your-username/weather-forecast-app.git
   cd weather-forecast-app

2. Install dependencies:
   pip install streamlit plotly requests

3. Run the app:
   streamlit run app.py

## App Features

------------
Inputs:
- City name (e.g., Tokyo, London)
- Forecast Days (1 to 5)
- Forecast Type:
  * Temperature: shows a temperature trend using a line chart
  * Sky: displays images for sky conditions (Clear, Clouds, Rain, Snow)

Outputs:
- Line chart for temperatures (in °C)
- Weather icons for sky conditions


## How It Works

------------
- Fetches 5-day weather data in 3-hour intervals (from OpenWeatherMap)
- For temperature: it converts from Kelvin to Celsius (value / 10)
- For sky conditions: uses icons like clear.png, cloud.png, etc.

## API Setup

---------
OpenWeatherMap API endpoint used:
https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}

To use your own key:
1. Go to https://openweathermap.org/api and sign up for a free key
2. Replace the value of API_KEY in backend.py:
   API_KEY = "your_api_key_here"

## Weather Icons

-------------
Make sure to place these PNG icons inside the 'images/' folder:
- clear.png
- cloud.png
- rain.png
- snow.png

## Error Handling

--------------
If the user enters an invalid location, a message will appear:
"This place does not exist."

## Example Usage

-------------
Input:
- Place: Tokyo
- Days: 3
- Type: Temperature

Output:
- Line graph with 24 temperature points (3 days × 8 readings/day)

## Future Enhancements

-------------------
- Add humidity, pressure, and wind information
- Add map location selector
- Use cache to reduce API calls
- Improve city input with auto-complete

Created with ❤️ using Python, Streamlit and OpenWeatherMap.
