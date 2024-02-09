import requests
import time
import random

# Number of times to refresh the page
refresh_count = 20

# URL of the website to refresh
url = "your-website-url-here"

# Loop to refresh the page
for i in range(refresh_count):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(f"Refresh {i+1}: Page refreshed successfully")
        else:
            print(f"Refresh {i+1}: Failed to refresh page (Status code: {response.status_code})")
    except Exception as e:
        print(f"Refresh {i+1}: An error occurred: {str(e)}")

    # Wait for 1.5 seconds before the next refresh
    # time.sleep(1.5)
    delay = random.uniform(1, 8)
    print(f"Waiting for {delay:.2f} seconds before the next refresh")
    time.sleep(delay)
