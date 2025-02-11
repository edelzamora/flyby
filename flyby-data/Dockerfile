# Use lightweight Python image
FROM python:3.11-slim

# ENV for ADS-B tar1090
ENV ADSB_URL="http://"

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy API code
COPY main.py .

# Expose port
EXPOSE 8000

# Run API server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]