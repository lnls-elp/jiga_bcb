import Adafruit_BBIO.GPIO as GPIO
import time

class SyncRecv:

    def __init__(self):
        self._syncrecv = ['GPIO2_25', 'GPIO2_23']
        self.setup_pins(self._syncrecv)

    def setup_pins(self, pins):
        for item in pins:
            GPIO.setup(item, GPIO.IN)

    def do_syncrecv_test(self):

        print("Iniciando teste dos receptores de fibra - sync")

        # TODO: Command to clear GPIOs

        sts_recv_0 = GPIO.input(self._syncrecv[0])
        sts_recv_1 = GPIO.input(self._syncrecv[1])

        if not sts_recv_0 and not sts_recv_1:
            # TODO: Send command to set GPIOs
            sts_recv_0 = GPIO.input(self._syncrecv[0])
            sts_recv_1 = GPIO.input(self._syncrecv[1])

            if sts_recv_0 and sts_recv_1:
                print("Receptores sync ok")
                return True

        print("Falha receptores sync")
        return False
