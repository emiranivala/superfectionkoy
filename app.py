import os
import threading
from flask import Flask, jsonify
import requests
import time
import logging
from config import KOYEB_URL

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

# URL of your Koyeb service
url = KOYEB_URL if KOYEB_URL.startswith('https://') else f'https://{KOYEB_URL}'  # Ensure URL has https:// scheme

@app.route('/')
def index():
    return "Restriction Bot is Running!"

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

def keep_alive():
    while True:
        try:
            response = requests.get(url)
            logging.info(f"Keep-alive request sent. Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Keep-alive request failed: {e}")
        time.sleep(20)

def start_keep_alive():
    keep_alive_thread = threading.Thread(target=keep_alive, daemon=True)
    keep_alive_thread.start()

if __name__ == "__main__":
    logging.info("Starting keep-alive service...")
    start_keep_alive()
    app.run(host="0.0.0.0", port=8000, threaded=True)
