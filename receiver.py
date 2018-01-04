from Adafruit_BBIO.SPI import SPI
import time

class Receiver:

    def __init__(self):
        self._

        self._gpio0_sts_add = 0 # GPIO state for P0-P7
        self._gpio1_sts_add = 1 # GPIO state for P8-P15
        self._gpio0_cfg_add = 6 # GPIO configuration for P0-P7
                                # Default value 0xFF
                                # If bit is 1, the GPIO is input
        self._gpio1_cfg_add = 7 # GPIO configuration for P8-15
                                # Default value 0xFF
                                # If bit is 1, the GPIO is input

        self._spi = SPI(0, 0)


    def do_receiver_test_1(self):

        print("Iniciando teste dos receptores de fibra")

        # TODO: Send command to set GPIOs

        self._spi.writebytes([self._gpio0_sts_add])
        res0 = self._spi.readbytes(1)

        self._spi.writebytes([self._gpio1_sts_add])
        res1 = self._spi.readbytes(1)

        if res0 is 15 and res1 is 15:
            print("Receiver OK")
            return True
        else:
            print("Receiver Falha")
            return False

    def do_receiver_test_2(self):
        return self.do_receiver_test_1()

    def do_receiver_test_3(self):
        return self.do_receiver_test_1()
