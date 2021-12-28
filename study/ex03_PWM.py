import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)

p = gp.PWM(18, 500)
p.start(0)

while True:
    p.ChangeDutyCycle(0)
    time.sleep(1)
    
    p.ChangeDutyCycle(50)
    time.sleep(1)
    
    p.ChangeDutyCycle(100)
    time.sleep(1)

    