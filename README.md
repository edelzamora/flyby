# FlyBy

### Purpose
This project uses an ADS-B Receiver to capture real-time data from aircraft flying nearby. I wanted to display what the receiver picked up near me. The goal is to visualize the detected aircraft using a custom dashboard and add an image.

Even with a stock antenna, the receiver picks up a surprising number of aircraft. This project processes and displays the data the aircrafts.

Work In Progress (WIP) but a demo can be found here -> [flyby.edelzamora.tech](flyby.edelzamora.tech)

### Hardware
- Raspberry Pi 3
- ADS-B Receiver
- Stock antenna from ADS-B kit

### Tech stack (ui/web server)
- Golang
- Chi

# FlyBy Data processor

- Microservice that processes the data from tar1090/data/aircraft.json
- Adds images for each aircraft scanned, if available.

### Tech stack (microservice)
- Python3
- FastAPI
## Demo

Link to demo:
[flyby](flyby.edelzamora.tech)

## Acknowledgements

 - [Planespotters](https://www.planespotters.net/)
    - Using images from planespotters.
    - They provide a free api.