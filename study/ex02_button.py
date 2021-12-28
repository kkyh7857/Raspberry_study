import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(21, gp.IN)
gp.setup(18, gp.OUT)

while True:
    buttonState = gp.input(21)
    
    if buttonState == 1:
        gp.output(18, gp.HIGH)
    else:
        gp.output(18, gp.LOW)
        
    #gp.output(18, buttonState)