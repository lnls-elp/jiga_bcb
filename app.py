import Adafruit_BBIO.GPIO as GPIO
from canbus import CanBus
from i2c import I2c
from rs485 import Rs485
from receiver import Receiver
from synctx import Transmitter
from syncrx import SyncRecv
from pydrs import SerialDRS
import time
import sys

sys.dont_write_bytecode = True

class Application:
    LED_TEST_BCB_1      = "GPIO0_27"
    LED_TEST_BCB_2      = "GPIO2_1"
    LED_TEST_BCB_3      = "GPIO2_12"
    LED_PASS            = "GPIO2_24"
    LED_FAIL            = "GPIO2_22"

    BUTTON_TEST_BCB_1   = "GPIO1_16"
    BUTTON_TEST_BCB_2   = "GPIO1_17"
    BUTTON_TEST_BCB_3   = "GPIO1_28"

    def __init__(self):

        self._can_test      = CanBus()
        self._i2c_test      = I2c()
        self._rs485_test    = Rs485()
        self._rx_test       = Receiver()
        self._tx_test       = Transmitter()
        self._rx_sync_test  = SyncRecv()

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
        print("Iniciando Teste BCB - Versao 1")
        GPIO.output(self.LED_PASS, GPIO.LOW)
        GPIO.output(self.LED_FAIL, GPIO.LOW)
        GPIO.output(self.LED_TEST_BCB_1, GPIO.HIGH)

        rs485_res   = self._rs485_test.do_rs485_test()
        tx_res      = self._tx_test.do_transmitter_test()
        rx_res      = self._rx_test.do_receiver_test_1()
        can_res     = self._can_test.do_can_test()
        i2c_res     = self._i2c_test.do_i2c_test()
        sync_recv   = self._rx_sync_test.do_syncrecv_test()

        if rs485_res and tx_res and rx_res and can_res and i2c_res:
            GPIO.output(self.LED_PASS, GPIO.HIGH)
        else:
            GPIO.output(self.LED_FAIL, GPIO.HIGH)

        GPIO.output(self.LED_TEST_BCB_1, GPIO.LOW)

    def start_test_bcb_var_2(self):
        print("Iniciando Teste BCB - Versao 2")
        GPIO.output(self.LED_PASS, GPIO.LOW)
        GPIO.output(self.LED_FAIL, GPIO.LOW)
        GPIO.output(self.LED_TEST_BCB_2, GPIO.HIGH)

        rs485_res   = self._rs485_test.do_rs485_test()
        tx_res      = self._tx_test.do_transmitter_test()
        rx_res      = self._rx_test.do_receiver_test_2()
        can_res     = self._can_test.do_can_test()
        i2c_res     = self._i2c_test.do_i2c_test()
        sync_recv   = self._rx_sync_test.do_syncrecv_test()

        if rs485_res and tx_res and rx_res and can_res and i2c_res:
            GPIO.output(self.LED_PASS, GPIO.HIGH)
        else:
            GPIO.output(self.LED_FAIL, GPIO.HIGH)

        GPIO.output(self.LED_TEST_BCB_2, GPIO.LOW)

    def start_test_bcb_var_3(self):
        print("Iniciando Teste BCB - Versao 3")
        GPIO.output(self.LED_PASS, GPIO.LOW)
        GPIO.output(self.LED_FAIL, GPIO.LOW)
        GPIO.output(self.LED_TEST_BCB_3, GPIO.HIGH)

        rs485_res   = self._rs485_test.do_rs485_test()
        tx_res      = self._tx_test.do_transmitter_test()
        rx_res      = self._rx_test.do_receiver_test_3()
        can_res     = self._can_test.do_can_test()
        i2c_res     = self._i2c_test.do_i2c_test()
        sync_recv   = self._rx_sync_test.do_syncrecv_test()

        if rs485_res and tx_res and rx_res and can_res and i2c_res:
            GPIO.output(self.LED_PASS, GPIO.HIGH)
        else:
            GPIO.output(self.LED_FAIL, GPIO.HIGH)

        GPIO.output(self.LED_TEST_BCB_3, GPIO.LOW)

"""
    Run Application
"""
app = Application()
app.run()
