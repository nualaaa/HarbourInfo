# This is a small script to compare basic real time information useful for launching boats.

# Import required modules.

import requests
import datetime
import os

# Set up the API connection for openweathermap.

from config import APIKEY

APIKey = APIKEY
endpoint = "https://api.openweathermap.org/data/2.5/weather"

# Define the function to get the required data from the API.

def data():
    print("Please answer the following questions about the location:")
    payload = {'lon': input("what is the longitude"),
               'lat': input("what is the latitude"),
               'appid': APIKey}
    response = requests.get(endpoint, params=payload)
    info = response.json()
    return info

# Two variables so we can store the data about the two locations to compare.

location1 = data()
location2 = data()

# Function to output which location is further north.

def north():
    if location1["coord"]["lon"] > location2["coord"]["lon"]:
        return "Location 1 is further north"
    if location1["coord"]["lon"] < location2["coord"]["lon"]:
        return "Location 2 is further north"
    else:
        return None

# Function to output which location is further west.

def west():
    if location1["coord"]["lat"] < location2["coord"]["lat"]:
        return "Location 1 is further west"
    if location1["coord"]["lat"] < location2["coord"]["lat"]:
        return "Location 2 is further west"

# Function to compare weather.

def weather():
    if location1["weather"][0]["description"] == location2["weather"][0]["description"]:
        return "Both locations have the same weather: " + str(location1["weather"][0]["description"])
    else:
        return "The weathers are different. In location 1 there is " + str(location1["weather"][0]["description"]) + ", in location 2 there is " + str(location2["weather"][0]["description"])

# Function to compare visibility.

def seeing():
    if location1["visibility"] == location2["visibility"]:
        return "The visibility at both locations is " + str(location1["visibility"])
    elif location1["visibility"] > location2["visibility"]:
        return "The visibility is better at location 1, with a measurement of " + str(location1["visibility"]), " in comparison with location 2, which is ", str(location2["visibility"])
    else:
        return "The visibility is better at location 2, with a measurement of " + str(location2["visibility"]), " in comparison with location 1, which is ", str(location1["visibility"])

# Call the functions and store the outputs as variables.

northResult = north()
westResult = west()
weatherResult = weather()
seeingResult = seeing()

# Date and timestamp the data.

now = datetime.datetime.now()

# Output and store the data in a file.

file = open(f"{now}.txt", "w")


if location1["coord"] == location2["coord"]:
    file.write("These are both the same location: " + str(location1["coord"]["lon"]) + ", " + str(location1["coord"]["lan"]))
else:
    file.write(f"It is currently {now}\n")
    file.write("You are comparing: " + str(location1["coord"]["lon"]) + ", " + str(location1["coord"]["lat"]) + " and " + str(location2["coord"]["lon"]) + ", " + str(location2["coord"]["lat"]) + ".\n")
    for r in northResult, westResult, weatherResult, seeingResult:
        if r != None:
            file.write(r + "\n")
    if float(str(location1["coord"]["lon"])[0:3]) == float(str(location2["coord"]["lon"])[0:2]):
        if float(str(location1["coord"]["lat"])[0:3]) == float(str(location2["coord"]["lat"])[0:2]):
            file.write("These locations are very close to one another. Please consult a map or the locals for more information.")

file.close()

# Try it for yourself!
# Suggested coordinates to start off with:
# Bundoran 54.47782 -8.28094
# Creevey Pier 54.529572 -8.255077
# St John's Point 54.5921548 -8.4291171
# Bellanaleck 54.3025205 -7.6398115

