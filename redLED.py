from gpiozero import LED
import time
red = LED(17)

red.on()
time.sleep(2)