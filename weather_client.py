import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "25447ee352dc69ac94977e1e38dde737"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

#other API implemented in joke.py!!!



def main():
    temp = get_weather("London")
    print(temp)

if __name__ == "__main__":
    main()
