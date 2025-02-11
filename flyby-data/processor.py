from contextlib import closing
from urllib.request import urlopen, URLError
from icao_nnumber_converter_us import n_to_icao, icao_to_n
import json
import requests
import os

# Query data from ADS-B receiver and return raw json data from the endpoint
def queryData():
    base_url= os.getenv('ADSB_URL')
    path = '/tar1090/data/aircraft.json'
    url = base_url + path
    with closing(urlopen(url, None, 5.0)) as aircraft_file:
        aircraft_data = json.load(aircraft_file)
    return aircraft_data

# Querying img data and returns a link as a string
def getAircraftImg(hex: str):
    url = f'https://api.planespotters.net/pub/photos/hex/{hex}'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0"}
    page = requests.get(url, headers=headers)
    data = json.loads(page.content).get('photos')
    if data is None: return ""
    if len(data) == 0: return ""
    return data[0]['thumbnail_large']['src']

# Filtering data that is not going to be used from the raw data. Adding new data such as image. Returning json data.
def filterData():
    raw_aircraft_data = queryData()
    aircraft_data = {"time": raw_aircraft_data.get("now"), "aircraft": []}
    for a in raw_aircraft_data['aircraft']:
        hex = a.get('hex')
        id = icao_to_n(a.get('hex')) # doesn't provide id, using  converter to get id / registration
        speed = a.get('gs')
        flight = a.get('flight')
        alt = a.get('alt_baro')
        img = getAircraftImg(hex)

        if flight is None: flight = 'Private'
        if speed is None: speed = 'N/A'
        if alt is None: alt = 'N/A'
        if id is None: id = 'International Aircraft'

        if hex:
            #print("Icao 24 bit hex: {hex} id: {id} flight: {flight} Speed: {speed} Altitude: {alt} Img: {img}".format(hex=hex, id=id, flight=flight, speed=speed, alt=alt, img=img))
            aircraft_data.get("aircraft").append({
                "hex": hex,
                "id": id,
                "speed": str(speed),
                "flight": flight,
                "alt": str(alt),
                "img": img,
            })
    return aircraft_data

def main():
    print("Starting data polling...")

if __name__ == "__main__":
    main()