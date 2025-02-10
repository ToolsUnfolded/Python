import requests
import json
import os  # Imported os to access environment variables

try:
    # Define your API endpoint and headers
    url = "https://api.oag.com/flight-instances/2023-11-15/6b357fdece31f8d58939ccbdccb2d535306bf67a477cf9695130570caea7cc12?version=v2"
    
    # Retrieve the subscription key from the environment variable
    subscription_key = os.getenv('OAG_SUBSCRIPTION_KEY')

    if not subscription_key:
        raise ValueError("No Subscription-Key found in environment variables.")

    # Request headers
    headers = {
        'Cache-Control': 'no-cache',
        'Subscription-Key': subscription_key,  # Use the environment variable here
    }

    # Send GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Response Code:", response.status_code)

        # Parse the JSON response
        data = response.json()
        print(json.dumps(data, indent=4))  # Pretty print the JSON response
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except ValueError as ve:
    print(ve)
