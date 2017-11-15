import Adafruit_BBIO.UART as UART
import serial
import time

class Rs485:

    def __init__(self):
        self.setup_pins()

    def setup_pins(self):
        UART.setup("UART5")

    def do_rs485_test(self):
        print("Iniciando teste de RS485")
        # TODO: Envia dado
        # TODO: Pergunta resposta udc
