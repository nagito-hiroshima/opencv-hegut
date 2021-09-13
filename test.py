import numpy as np
import yeelight


bulb = yeelight.Bulb("192.168.11.4")
bulb.turn_on()
bulb.set_rgb(255, 255, 255)
bulb.set_brightness(10)