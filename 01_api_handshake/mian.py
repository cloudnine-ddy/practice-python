import requests
import sys

if sys.stdout != "utf-8":               #to ensure Chinese character won't cause error
    sys.stdout.reconfigure(encoding = "utf-8")

url = "https://official-joke-api.appspot.com/jokes/programming/random"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()          #.json() is like a translator
        print(f"\nThe original data: {type(data)}\n{data}")
        print("\nThe Joke:")
        print(data[0]["setup"])
        print(data[0]["punchline"])
    elif response.status_code == 400:
        print("fail")

except Exception as e:
    print(f"\nError: Please check your connection or URL.")
    print(f"reason:\n{e}")
