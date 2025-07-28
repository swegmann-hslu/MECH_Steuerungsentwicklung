# To run this code on your RaspberryPi Pico, check the instructions in the
# README.md file in the root folder.
from machine import Pin
from utime import sleep


# Create an object to control the onboard LED. We use the generic name "LED" as
# parameter so that we will always use the onboard LED on Pico, Pico W, Pico 2
# and Pico W 2. These devices have slightly different ways how they connect to
# the onboard LED and using this method keeps LED-code generic. To control a
# physical GPIO, say GPIO10, we would use the GPIO number as in this:
#
#   pin10 = Pin(10, Pin.OUT)
pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        # turn LED from off to on or vice-versa
        pin.toggle()
        # sleep 1sec
        sleep(1)
    except KeyboardInterrupt:
        # Wait for the user to break out of the endless loop by pressing the
        # stop button
        break
# As soon as we break out of the endless loop, turn of the LED
pin.off()
print("Finished.")
