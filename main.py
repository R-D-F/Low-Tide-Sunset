import requests
import pandas as pd
from datetime import datetime, timedelta


def get_tide_data(station_id):
    # NOAA API URL for tides
    url = f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"

    # Parameters for the API
    params = {
        "date": "today",
        "station": station_id,
        "product": "water_level",
        "datum": "MLLW",  # Changed datum to STND (Station Datum)
        "units": "metric",
        "time_zone": "lst_ldt",
        "application": "tide_chart",
        "format": "json",
    }

    # Make the request to the NOAA API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Check if 'predictions' key is in the data
        print(data)


if __name__ == "__main__":
    station_id = 9449424  # Bellingham, WA station ID
    start_date = (datetime.now()).strftime(r"%Y%m%d")
    end_date = (datetime.now() - timedelta(days=7)).strftime(r"%Y%m%d")

get_tide_data(station_id)
