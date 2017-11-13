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

    def scan_keyboard(self):
        pass

    def start_test_bcb_var_1(self):
        pass

    def start_test_bcb_var_2(self):
        pass

    def start_test_bcb_var_3(self):
        pass

"""
    Run Application
"""

app = Application()
app.run()
