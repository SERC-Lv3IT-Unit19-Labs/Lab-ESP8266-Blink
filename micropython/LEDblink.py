#
# ESP8266 LED Blink
# micropython exercise
#

import machine  # the machine library lets us interact with the microcontroller, like setting inputs and outputs.
import time

LED_PIN = 5 # define the pin the LED is attached to

# the Pin function takes a pin number and sets it to either input or output
LED = machine.Pin(LED_PIN, machine.Pin.OUT)

# We need to create a loop that will run for ever. We do this with while True, since
# True will always be true.
while True:
    LED.on()        # Turn the LED on
    time.sleep(1)   # Wait for 1 second
    LED.off()       # Turn the LED off
    time.sleep(1)   # Wait for 1 second
