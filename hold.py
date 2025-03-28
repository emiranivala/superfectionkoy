import requests
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

from config import KOYEB_URL

# URL of your Koyeb service
url = KOYEB_URL  # Using the configured Koyeb service URL

def keep_alive():
    while True:
        try:
            response = requests.get(url)
            logging.info(f"Keep-alive request sent. Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Keep-alive request failed: {e}")
        
        # Wait for 20 seconds before sending the next request
        time.sleep(20)

if __name__ == "__main__":
    logging.info("Starting keep-alive service...")
    keep_alive()
