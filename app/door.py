import time
import RPi.GPIO as GPIO

class Door(object):
    def __init__(self, output_pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.output_pin = output_pin
        GPIO.setup(self.output_pin, GPIO.OUT)

    def open(self):
        GPIO.output(self.output_pin, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(self.output_pin, GPIO.LOW)
