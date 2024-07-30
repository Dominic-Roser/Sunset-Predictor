# import openmeteo_requests #type: ignore
import numpy
# import requests_cache #type: ignore
# import pandas as pd #type: ignore
# from retry_requests import retry 

# # Setup the Open-Meteo API client with cache and retry on error
# cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
# retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
# openmeteo = openmeteo_requests.Client(session = retry_session)

# # Make sure all required weather variables are listed here
# # The order of variables in hourly or daily is important to assign them correctly below
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
# 	"latitude": 52.52,
# 	"longitude": 13.41,
# 	"hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "rain", "snowfall", "snow_depth", "cloud_cover_low", "cloud_cover_mid", "cloud_cover_high", "wind_speed_10m", "wind_speed_80m", "wind_speed_120m", "temperature_80m", "temperature_120m", "temperature_180m"],
# 	"temperature_unit": "fahrenheit",
# 	"wind_speed_unit": "mph",
# 	"precipitation_unit": "inch",
# 	"forecast_days": 1
# }
# responses = openmeteo.weather_api(url, params=params)

# # Process first location. Add a for-loop for multiple locations or weather models
# response = responses[0]
# print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
# print(f"Elevation {response.Elevation()} m asl")
# print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
# print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# # Process hourly data. The order of variables needs to be the same as requested.
# hourly = response.Hourly()
# hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
# hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
# hourly_precipitation = hourly.Variables(2).ValuesAsNumpy()
# hourly_rain = hourly.Variables(3).ValuesAsNumpy()
# hourly_snowfall = hourly.Variables(4).ValuesAsNumpy()
# hourly_snow_depth = hourly.Variables(5).ValuesAsNumpy()
# hourly_cloud_cover_low = hourly.Variables(6).ValuesAsNumpy()
# hourly_cloud_cover_mid = hourly.Variables(7).ValuesAsNumpy()
# hourly_cloud_cover_high = hourly.Variables(8).ValuesAsNumpy()
# hourly_wind_speed_10m = hourly.Variables(9).ValuesAsNumpy()
# hourly_wind_speed_80m = hourly.Variables(10).ValuesAsNumpy()
# hourly_wind_speed_120m = hourly.Variables(11).ValuesAsNumpy()
# hourly_temperature_80m = hourly.Variables(12).ValuesAsNumpy()
# hourly_temperature_120m = hourly.Variables(13).ValuesAsNumpy()
# hourly_temperature_180m = hourly.Variables(14).ValuesAsNumpy()

# hourly_data = {"date": pd.date_range(
# 	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
# 	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
# 	freq = pd.Timedelta(seconds = hourly.Interval()),
# 	inclusive = "left"
# )}
# hourly_data["temperature_2m"] = hourly_temperature_2m
# hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
# hourly_data["precipitation"] = hourly_precipitation
# hourly_data["rain"] = hourly_rain
# hourly_data["snowfall"] = hourly_snowfall
# hourly_data["snow_depth"] = hourly_snow_depth
# hourly_data["cloud_cover_low"] = hourly_cloud_cover_low
# hourly_data["cloud_cover_mid"] = hourly_cloud_cover_mid
# hourly_data["cloud_cover_high"] = hourly_cloud_cover_high
# hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
# hourly_data["wind_speed_80m"] = hourly_wind_speed_80m
# hourly_data["wind_speed_120m"] = hourly_wind_speed_120m
# hourly_data["temperature_80m"] = hourly_temperature_80m
# hourly_data["temperature_120m"] = hourly_temperature_120m
# hourly_data["temperature_180m"] = hourly_temperature_180m

# hourly_dataframe = pd.DataFrame(data = hourly_data)
# print(hourly_dataframe)