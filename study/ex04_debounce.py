import RPi.GPIO as gp
import time

gp.setmode(gp.BCM)
gp.setup(18, gp.OUT)
gp.setup(21, gp.IN)

p = gp.PWM(18, 500)
p.start(0)

check = True
cnt = 0

while True:
    buttonState = gp.input(21)
    if buttonState == 1:
        if check == True:
            cnt += 1
            check = False
    else
        check = True
        
    if cnt % 3 == 0:
        p.ChangeDutyCycle(0)
    elif cnt % 3 == 1:
        p.ChangeDutyCycle(50)
    else:
        p.ChangeDutyCycle(100)
        
    

    
