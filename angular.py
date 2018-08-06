import RPi.GPIO as GPIO
import servo

GPIO.setmode(GPIO.BCM)

s=servo.AngularServo(4,min_us=200,max_us=2200,max_angle=200)

try:
    while True:
        
        try:
            angle=float(input("angle :"))
        except ValueError:
            angle=None
        except EOFError:
            print("")
            break
        
        s.angle(angle)
        
except KeyboardInterrupt:
    print("")
    pass

GPIO.cleanup()
