import os
from dotenv import load_dotenv
from garminconnect import Garmin
from datetime import date
import json

load_dotenv()

client = Garmin(
    os.getenv("GARMIN_USER", "<YOUR_EMAIL>"),
    os.getenv("GARMIN_PASS", "<YOUR_PASSWORD>")
)
client.login()

today = date.today().strftime("%Y-%m-%d")

all_data = {
    "daily_stats": client.get_stats(today),
    "heart_rate": client.get_heart_rates(today),
    "body_composition": client.get_body_composition(today)
}


with open(f"stats_{today}.json", "w") as file:
    json_stat = json.dump(all_data, file, indent=4)

with open(f"stats_{today}.json", "r") as read:
    readable_stat = json.load(read)

print(readable_stat["daily_stats"]["totalDistanceMeters"])
