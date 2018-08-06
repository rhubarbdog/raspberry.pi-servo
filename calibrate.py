import RPi.GPIO as GPIO
import servo

PIN=4

def do_pulse_mode(servo):
    
    try:
        while True:
            
            try:
                pulse=-abs(int(input("pulse :")))
            except ValueError:
                pulse=None
            except EOFError:
                print("")
                break
            
            if pulse is not None:
                servo._pulse(pulse,1000)
    except KeyboardInterrupt:
        print("")
        

GPIO.setmode(GPIO.BCM)


try:
    while True:
        
        pulse=False
        try:
            min_us=int(input("min :"))
        except ValueError:
            min_us=None
        except EOFError:
            pulse=True
            min_us=None
            print("")
            
        if not pulse:
            try:
                max_us=int(input("max :"))
            except ValueError:
                max_us=None
            except EOFError:
                pulse=True
                max_us=None
                print("")
        else:
            max_us=None
            
        error=False
        if not pulse and min_us is not None and min_us<0:
            error=True
        if not pulse and max_us is not None and max_us<0:
            error=True
        
        if error:
            print("min and max must be greater than 0.")
            continue

        if min_us is None and max_us is None:
            s=servo.AngularServo(PIN)
        elif min_us is None:
            s=servo.AngularServo(PIN, max_us=max_us)
        elif max_us is None:
            s=servo.AngularServo(PIN, min_us=min_us)
        else:
            s=servo.AngularServo(PIN, min_us=min_us, max_us=max_us)

        if pulse:
            do_pulse_mode(s)
            del s
            continue
    
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
    
        del s
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()