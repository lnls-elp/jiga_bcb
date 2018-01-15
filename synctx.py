import Adafruit_BBIO.GPIO as GPIO
from pydrs import SerialDRS
import time
import sys

sys.dont_write_bytecode = True

class Transmitter:

    def __init__(self):
        self._comport       = '/dev/ttyUSB0'
        self._baudrate      = '115200'
        self._transmitter   = ['GPIO1_12', 'GPIO1_13', 'GPIO1_14', 'GPIO1_15']
        self.setup_pins()

    def setup_pins(self):
        for item in self._transmitter:
            GPIO.setup(item, GPIO.OUT)

        self.disable_all()

    def do_transmitter_test(self):

        drs = SerialDRS()
        conn = drs.Connect(self._comport, self._baudrate)

        if not conn:
            print("Erro conexao serial")
            return False

        print("Iniciando teste dos transmissores de fibra")

        print('Desligando transmissores')
        self.disable_all()

        print('Lendo transmissores')
        data = ReadPof()
        sts = ord(data[4]) # Convert to int
        print('Valor lido: ' + str(sts))

        if sts is 15:
            print('Ligando transmissores')
            self.enable_all()

            print('Lendo transmissores')
            data = drs.ReadPof()
            sts = ord(data[4]) # Convert to int
            print('Valor lido: ' + str(sts))

            drs.Disconnect()

            if sts is 0:
                print("Transmissores OK")
                return True
            else:
                return False
        else:
            print("Transmissores Falha")
            return False
            drs.Disconnect()

    def enable_all(self):
        for item in self._transmitter:
            GPIO.output(item, GPIO.LOW)    # Enable transmitters

    def disable_all(self):
        for item in self._transmitter:
            GPIO.output(item, GPIO.HIGH)    # Disable transmitters
