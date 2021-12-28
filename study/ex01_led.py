import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)

while True:
    gp.output(18, gp.HIGH)
    time.sleep(1)
    
    gp.output(18, gp.LOW)
    time.sleep(1)

    