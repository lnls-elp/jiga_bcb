import Adafruit_BBIO.GPIO as GPIO
import time

class Transmitter:

    def __init__(self):
        self._transmitter = ['GPIO1_16', 'GPIO1_17', 'GPIO3_21', 'GPIO3_19']
        self.setup_pins(self._transmitter)

    def setup_pins(self, pins):
        for item in pins:
            GPIO.setup(item, GPIO.OUT)

        for item in pins:
            GPIO.output(item, GPIO.LOW)

    def do_transmitter_test(self):

        print("Iniciando teste dos transmissores de fibra")

        for item in self._transmitter:
            GPIO.output(item, GPIO.LOW)

        #TODO: Ask status from UdcComTest
        # sts = self._tx_status()
        sts = None

        if sts is 0:
            for item in self._transmitter:
                GPIO.output(item, GPIO.HIGH)

            #TODO: Ask status from UdcComTest
            # sts = self._tx_status()
            if sts is 15:
                print("Transmissores OK")
                return True
            else:
                return False
        else:
            print("Transmissores Falha")
            return False