# FlyBy Data processor

- Processes the data from tar1090/data/aircraft.json
- Adds images for each aircraft scanned, if available.

## Tech stack
- Python3
- FastAPI

### Run local
- Set ADS-B url
    - export ADSB_URL=http://<IP_ADDR>
- uvicorn main:app --host 0.0.0.0 --port 3001 --reload