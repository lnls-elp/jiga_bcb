import Adafruit_BBIO.GPIO as GPIO
import time

class Application:
    LED = "P8_10"
    def __init__(self):
        GPIO.setup(self.LED, GPIO.OUT)

    def run(self):
        while True:
            GPIO.output(self.LED, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.LED, GPIO.LOW)
            time.sleep(0.5)

"""
    Run Application
"""

app = Aplication()
app.run()
