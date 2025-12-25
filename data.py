import json

with open("stats_2025-12-25.json", "r") as file:
    data = json.load(file)

steps = data["daily_stats"]["totalSteps"]
max_hr = data["daily_stats"]["maxHeartRate"]
meters = data["daily_stats"]["totalDistanceMeters"]
calories = data["daily_stats"]["totalKilocalories"]
km = round(meters / 1000, 1)

print(f" Steps for today is: {steps}, which is {km} km")
print(f" Max heartrate was: {max_hr} and estimated calories burned today is: {calories}")
