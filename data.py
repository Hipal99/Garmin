import json

with open("stats_2025-12-26.json", "r") as file:
    data = json.load(file)

steps = data["daily_stats"]["totalSteps"]
max_hr = data["daily_stats"]["maxHeartRate"]
meters = data["daily_stats"]["totalDistanceMeters"]
calories = data["daily_stats"]["totalKilocalories"]
km = round(meters / 1000, 1)
sleep_time_seconds = data["sleep_data"]["dailySleepDTO"]["sleepTimeSeconds"]
sleep_time_hours = round(sleep_time_seconds / 3600)
sleep_score = data["sleep_data"]["dailySleepDTO"]["sleepScores"]["overall"]["value"]

print(f" Steps for today is: {steps}, which is {km} km")
print(f" Max heartrate was: {max_hr} and estimated calories burned today is: {calories}")
print(f"You slept for around {sleep_time_hours} with a overall sleep score of {sleep_score}")