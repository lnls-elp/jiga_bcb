import Adafruit_BBIO.GPIO as GPIO
import time

class Receiver:

    def __init__(self):
        self._receiver =    ['GPIO1_0', 'GPIO1_4', 'GPIO1_12', 'GPIO2_1',
                            'GPIO1_1', 'GPIO1_5', 'GPIO1_14', 'GPIO2_6',
                            'GPIO1_2', 'GPIO1_6', 'GPIO1_29', 'GPIO2_27',
                            'GPIO1_3', 'GPIO1_7', 'GPIO1_31', 'GPIO2_8',
                            'GPIO2_9', 'GPIO2_13']

        # Cannot be used (reserved):
        #   - GPIO1_0
        #   - GPIO1_4
        #   - GPIO1_1
        #   - GPIO1_5
        #   - GPIO1_2
        #   - GPIO1_6
        #   - GPIO1_3
        #   - GPIO1_7
        #   - GPIO1_31
        self.setup_pins(self._receiver)

    def setup_pins(self, pins):
        for item in pins:
            GPIO.setup(item, GPIO.IN)

    def do_receiver_test_bcb_1(self):
        # TODO: Envia comando para Udc
        # Le todos os receivers

    def do_receiver_test_bcb_2(self):
        # TODO: Envia comando para Udc
        # Le todos os receivers

    def do_receiver_test_bcb_3(self):
        # TODO: Envia comando para Udc
        # Le todos os receivers
