import Adafruit_BBIO.GPIO as GPIO
import time

class Rs485:

    def __init__(self):
        self.setup_pins()

    def setup_pins(self):
        UART.setup("UART5")

    def do_rs485_test_bcb(self):
        # TODO: Envia dado
        # TODO: Pergunta resposta udc
