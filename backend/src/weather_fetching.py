import openmeteo_requests # type: ignore

import requests_cache # type: ignore
import pandas as pd # type: ignore
from retry_requests import retry # type: ignore

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 47.61,
	"longitude": 122.33,
	"hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "precipitation_probability", "precipitation", "rain", "showers", "snowfall", "snow_depth", "pressure_msl", "surface_pressure", "cloud_cover", "cloud_cover_low", "cloud_cover_mid", "cloud_cover_high", "visibility", "evapotranspiration", "wind_speed_10m", "wind_speed_80m", "wind_speed_120m", "wind_speed_180m", "wind_direction_10m", "wind_direction_80m", "wind_direction_120m", "wind_direction_180m", "wind_gusts_10m", "temperature_80m", "temperature_120m", "temperature_180m"],
	"timezone": "America/Los_Angeles"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
hourly_dew_point_2m = hourly.Variables(2).ValuesAsNumpy()
hourly_precipitation_probability = hourly.Variables(3).ValuesAsNumpy()
hourly_precipitation = hourly.Variables(4).ValuesAsNumpy()
hourly_rain = hourly.Variables(5).ValuesAsNumpy()
hourly_showers = hourly.Variables(6).ValuesAsNumpy()
hourly_snowfall = hourly.Variables(7).ValuesAsNumpy()
hourly_snow_depth = hourly.Variables(8).ValuesAsNumpy()
hourly_pressure_msl = hourly.Variables(9).ValuesAsNumpy()
hourly_surface_pressure = hourly.Variables(10).ValuesAsNumpy()
hourly_cloud_cover = hourly.Variables(11).ValuesAsNumpy()
hourly_cloud_cover_low = hourly.Variables(12).ValuesAsNumpy()
hourly_cloud_cover_mid = hourly.Variables(13).ValuesAsNumpy()
hourly_cloud_cover_high = hourly.Variables(14).ValuesAsNumpy()
hourly_visibility = hourly.Variables(15).ValuesAsNumpy()
hourly_evapotranspiration = hourly.Variables(16).ValuesAsNumpy()
hourly_wind_speed_10m = hourly.Variables(17).ValuesAsNumpy()
hourly_wind_speed_80m = hourly.Variables(18).ValuesAsNumpy()
hourly_wind_speed_120m = hourly.Variables(19).ValuesAsNumpy()
hourly_wind_speed_180m = hourly.Variables(20).ValuesAsNumpy()
hourly_wind_direction_10m = hourly.Variables(21).ValuesAsNumpy()
hourly_wind_direction_80m = hourly.Variables(22).ValuesAsNumpy()
hourly_wind_direction_120m = hourly.Variables(23).ValuesAsNumpy()
hourly_wind_direction_180m = hourly.Variables(24).ValuesAsNumpy()
hourly_wind_gusts_10m = hourly.Variables(25).ValuesAsNumpy()
hourly_temperature_80m = hourly.Variables(26).ValuesAsNumpy()
hourly_temperature_120m = hourly.Variables(27).ValuesAsNumpy()
hourly_temperature_180m = hourly.Variables(28).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
hourly_data["dew_point_2m"] = hourly_dew_point_2m
hourly_data["precipitation_probability"] = hourly_precipitation_probability
hourly_data["precipitation"] = hourly_precipitation
hourly_data["rain"] = hourly_rain
hourly_data["showers"] = hourly_showers
hourly_data["snowfall"] = hourly_snowfall
hourly_data["snow_depth"] = hourly_snow_depth
hourly_data["pressure_msl"] = hourly_pressure_msl
hourly_data["surface_pressure"] = hourly_surface_pressure
hourly_data["cloud_cover"] = hourly_cloud_cover
hourly_data["cloud_cover_low"] = hourly_cloud_cover_low
hourly_data["cloud_cover_mid"] = hourly_cloud_cover_mid
hourly_data["cloud_cover_high"] = hourly_cloud_cover_high
hourly_data["visibility"] = hourly_visibility
hourly_data["evapotranspiration"] = hourly_evapotranspiration
hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
hourly_data["wind_speed_80m"] = hourly_wind_speed_80m
hourly_data["wind_speed_120m"] = hourly_wind_speed_120m
hourly_data["wind_speed_180m"] = hourly_wind_speed_180m
hourly_data["wind_direction_10m"] = hourly_wind_direction_10m
hourly_data["wind_direction_80m"] = hourly_wind_direction_80m
hourly_data["wind_direction_120m"] = hourly_wind_direction_120m
hourly_data["wind_direction_180m"] = hourly_wind_direction_180m
hourly_data["wind_gusts_10m"] = hourly_wind_gusts_10m
hourly_data["temperature_80m"] = hourly_temperature_80m
hourly_data["temperature_120m"] = hourly_temperature_120m
hourly_data["temperature_180m"] = hourly_temperature_180m

hourly_dataframe = pd.DataFrame(data = hourly_data)
print(hourly_dataframe)