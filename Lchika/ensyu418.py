import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)


try:
    while True:
        GPIO.output(2, 1)

        GPIO.output(3, 0)
        time.sleep(0.5)

        GPIO.output(3, 1)

        GPIO.output(2, 0)
        time.sleep(0.5) 

except KeyboardInterrupt:
    GPIO.cleanup()