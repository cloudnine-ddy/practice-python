import requests
import sys

if sys.stdout != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

try:
    city = input("\nPlease enter the city you would like to check: ")
    print("Checking......")
    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['current_condition'][0]['temp_C']
        weather = data['current_condition'][0]['weatherDesc'][0]['value']
        print(f"The weather in {city} now is {weather} ({temp}°C)")
    elif response.status_codes == 404:
        print("Something went wrong......")
    else:
        print("omg")


except Exception as e:
    print("Error: Please try again!")
    print(f"Reason:\n{e}")