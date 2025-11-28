# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all Python scripts
COPY . .

# Default command: run all scripts
CMD ["sh", "-c", "python extract_weather.py && python transform_weather.py && python load_weather.py && tail -f /dev/null"]
