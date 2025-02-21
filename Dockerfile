FROM python:3.10.4-slim-buster

# Update and install required packages in one layer
RUN apt update && apt upgrade -y && \
    apt-get install -y git curl python3-pip ffmpeg wget bash neofetch software-properties-common

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip3 install wheel && pip3 install --no-cache-dir -U -r requirements.txt

# Set the working directory and copy the entire repository
WORKDIR /app
COPY . .

# Expose the port for your Flask app (adjust if needed)
EXPOSE 8000

# Start the Flask app (app.py) and the Telegram bot concurrently
CMD ["sh", "-c", "python3 app.py & python3 -m Restriction"]


 
