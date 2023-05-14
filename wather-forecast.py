import pandas as pd
from sklearn.linear_model import LinearRegression

# Load historical weather data
data = pd.read_csv('historical_weather.csv')

# Extract relevant columns for modeling
X = data[['humidity', 'wind_speed', 'temperature']]
y = data['rain']

# Train linear regression model
model = LinearRegression()
model.fit(X, y)

# Get current weather data
current_humidity = 70
current_wind_speed = 10
current_temperature = 20

# Make prediction
prediction = model.predict([[current_humidity, current_wind_speed, current_temperature]])

if prediction > 0.5:
    print("It's likely to rain today!")
else:
    print("No rain expected today.")
