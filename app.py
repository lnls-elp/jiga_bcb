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
        GPIO.setup(self.LED_TEST_BCB_1, GPIO.OUT)
        GPIO.setup(self.LED_TEST_BCB_2, GPIO.OUT)
        GPIO.setup(self.LED_TEST_BCB_3, GPIO.OUT)
        GPIO.setup(self.LED_FAIL, GPIO.OUT)
        GPIO.setup(self.LED_PASS, GPIO.OUT)

        GPIO.setup(self.BUTTON_TEST_BCB_1, GPIO.IN)
        GPIO.setup(self.BUTTON_TEST_BCB_2, GPIO.IN)
        GPIO.setup(self.BUTTON_TEST_BCB_3, GPIO.IN)

        GPIO.output(self.LED_PASS, GPIO.HIGH)
        GPIO.output(self.LED_FAIL, GPIO.HIGH)

    def run(self):
        while True:
            self.scan_keyboard()

    def scan_keyboard(self):
        if not GPIO.input(self.BUTTON_TEST_BCB_1):
            self.start_test_bcb_var_1()

        if not GPIO.input(self.BUTTON_TEST_BCB_2):
            self.start_test_bcb_var_2()

        if not GPIO.input(self.BUTTON_TEST_BCB_3):
            self.start_test_bcb_var_3()

    def start_test_bcb_var_1(self):
        #TODO: Put here test routin
        GPIO.output(self.LED_TEST_BCB_1, GPIO.HIGH)
        print("Teste 1 Iniciado")

    def start_test_bcb_var_2(self):
        #TODO: Put here test routin
        GPIO.output(self.LED_TEST_BCB_2, GPIO.HIGH)
        print("Teste 2 Initiado")

    def start_test_bcb_var_3(self):
        GPIO.output(self.LED_TEST_BCB_3, GPIO.HIGH)
        #TODO: Put here test routin
        print("Teste 2 Initiado")


"""
    Run Application
"""

app = Application()
app.run()
