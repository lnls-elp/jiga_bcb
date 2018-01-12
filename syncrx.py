import Adafruit_BBIO.GPIO as GPIO
from pydrs import SerialDRS
import time
import sys

sys.dont_write_bytecode = True

class SyncRecv:

    def __init__(self):

        self._epwm_sync_pin = 'GPIO2_23'    # Input in BBB perspective
        self._sync_in_pin   = 'GPIO2_25'    # Input in BBB perspective
        self._sync_out_pin   = 'GPIO1_14'   # Output in BBB perspective

        self.setup_pins()

    def setup_pins(self):
        GPIO.setup(self._epwm_sync_pin, GPIO.IN)
        GPIO.setup(self._sync_in_pin, GPIO.IN)

        GPIO.setup(self._sync_out_pin, GPIO.OUT)

    def do_syncrecv_test(self):

        drs = SerialDRS()
        conn = drs.Connect(self._comport, self._baudrate)

        if not conn:
            print("Erro conexao serial")
            return False

        print("Iniciando teste dos receptores de fibra - sync")
        GPIO.output(self._sync_out_pin, GPIO.HIGH)

        sts_sync_in = GPIO.input(self._sync_in_pin)

        if not sts_sync_in:

            GPIO.output(self._sync_out_pin, GPIO.LOW)
            sts_sync_in = GPIO.input(self._sync_in_pin)

            if sts_sync_in:

                drs.ClearPof()

                sts_epwm_sync = GPIO.input(self._epwm_sync_pin)
                if not sts_epwm_sync:

                    drs.SetPof()
                    sts_epwm_sync = GPIO.input(self._epwm_sync_pin)
                    if sts_epwm_sync:
                        drs.Disconnect()
                        return True
        print("Falha receptores sync")
        drs.Disconnect()
        return False
