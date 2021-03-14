from phue import Bridge
import time
import random

b = Bridge('192.168.0.26')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()
lights = b.lights

# Get a dictionary with the light id as the key
lights = b.get_light_objects('id')

# Get a dictionary with the light name as the key
for x in range(1, 40):
    print(x)
    light_names = b.get_light_objects('name')
    light_names["Desk lamp"].transitiontime = 1
    light_names["Desk lamp"].brightness = 100
    light_names["Desk lamp"].hue = random.uniform(0, 90000)
    light_names["Desk lamp"].transitiontime = 0.5
    light_names["Desk lamp"].brightness = 1
    time.sleep(0.3)
