import Adafruit_BBIO.GPIO as GPIO
from pydrs import SerialDRS
import time
import sys

sys.dont_write_bytecode = True

class Transmitter:

    def __init__(self):
        self._transmitter = ['GPIO1_12', 'GPIO1_13', 'GPIO1_14', 'GPIO1_15']
        self.setup_pins(self._transmitter)

    def setup_pins(self, pins):
        for item in pins:
            GPIO.setup(item, GPIO.OUT)

        for item in pins:
            GPIO.output(item, GPIO.LOW)

    def do_transmitter_test(self):

        drs = SerialDRS()
        conn = drs.Connect(self._comport, self._baudrate)

        if not conn:
            print("Erro conexao serial")
            return False

        print("Iniciando teste dos transmissores de fibra")

        for item in self._transmitter:
            GPIO.output(item, GPIO.LOW)

        sts = drs.ReadPof()

        if sts is 0:
            for item in self._transmitter:
                GPIO.output(item, GPIO.HIGH)

            drs.ReadPof()

            drs.Disconnect()

            if sts is 15:
                print("Transmissores OK")
                return True
            else:
                return False
        else:
            print("Transmissores Falha")
            drs.Disconnect()
            return False
