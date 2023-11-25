from datetime import datetime
from textblob import TextBlob
import requests

def fetch_weather_data(api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city = "Zurich"  # Replace with the city name or city ID
    units = "metric"  # Use "metric" for Celsius, "imperial" for Fahrenheit

    params = {
        "q": city,
        "appid": api_key,
        "units": units
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"{weather_description}, Temperature: {temperature}°C"
        else:
            return "Weather data unavailable"
    except requests.RequestException as e:
        return f"Error fetching weather data: {str(e)}"

# Handle Missing Values
def handle_missing_values(users):
    missing_values = any(activity == "" for activity in users.values())
    if missing_values:
        # Implement your logic to handle missing values
        pass

# Text Data Processing
def get_sentiment_score(text):
    # Implement sentiment analysis and return the score
    # Create a TextBlob object
    blob = TextBlob(text)

    # Perform sentiment analysis and get the polarity score
    score = blob.sentiment.polarity

    return score

# Temporal Features
def add_temporal_features(users, active_user):
    current_time = datetime.now()
    day_of_week = current_time.strftime("%A")  # Get the current day of the week
    # Add 'day_of_week' as a feature in the user activities
    users[active_user] = users[active_user] + f"\nDay of the Week: {day_of_week}"


# Activity Patterns
def calculate_activity_frequency(users, active_user):
    activities_count = users[active_user].count("\n") if active_user in users else 0
    users[active_user] = users[active_user] + f"\nActivity Frequency: {activities_count}"

# Sentiment Scores
def add_sentiment_scores(users, active_user):
    text = users[active_user] if active_user in users else ""
    sentiment_score = get_sentiment_score(text)
    users[active_user] = users[active_user] + f"\nSentiment Score: {sentiment_score}"

# Derived Features
def aggregate_similar_activities(users, active_user):
    # Split the activities for the active user
    user_activities = users.get(active_user, "").split("\n")

    # Logic to aggregate similar activities
    aggregated_activities = {}
    for activity in user_activities:
        # Extracting keyword if ':' is present, else consider entire activity as keyword
        if ':' in activity:
            keyword = activity.split(":")[0]
            details = activity.split(":")[1].strip()
        else:
            keyword = "Uncategorized"
            details = activity.strip()

        # Aggregating activities based on the keyword (or 'Uncategorized')
        if keyword not in aggregated_activities:
            aggregated_activities[keyword] = [details]
        else:
            aggregated_activities[keyword].append(details)

    # Combine the aggregated activities back into a single string
    updated_activities = "\n".join(
        ":".join([keyword, ", ".join(activities)])
        for keyword, activities in aggregated_activities.items()
    )

    # Update the activities for the active user
    users[active_user] = updated_activities


# Domain-Specific Features
def add_weather_condition(users, active_user):
    # Your code to fetch weather data from an API or other source
    weather_data = fetch_weather_data("8e7cc745a46558367c9f67b702e687f1")

    # Update the user's activities with weather information
    users[active_user] += f"\nWeather: {weather_data}"
