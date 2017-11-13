import Adafruit_BBIO.GPIO as GPIO
import time

class Application:
    LED_TEST_BCB_1      = "GPIO1_15"
    LED_TEST_BCB_2      = "GPIO1_30"
    LED_TEST_BCB_3      = "GPIO2_10"
    LED_PASS            = "GPIO2_12"
    LED_FAIL            = "GPIO2_11"

    BUTTON_TEST_BCB_1   = "GPIO2_23"
    BUTTON_TEST_BCB_2   = "GPIO2_24"
    BUTTON_TEST_BCB_3   = "GPIO2_25"

    def __init__(self):
        GPIO.setup(self._TEST_BCB_1, GPIO.OUT)

    def run(self):
        while True:
            GPIO.output(self.LED_TEST_BCB_1, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.LED_TEST_BCB_1, GPIO.LOW)
            time.sleep(0.5)

    def scan_keyboard(self):
        pass

    def start_test_bcb_var_1(self):
        #TODO: Put here test routin
        print("Teste 1 Iniciado")

    def start_test_bcb_var_2(self):
        #TODO: Put here test routin
        print("Teste 2 Initiado")

    def start_test_bcb_var_3(self):
        #TODO: Put here test routin
        print("Teste 2 Initiado")

"""
    Run Application
"""

app = Application()
app.run()
