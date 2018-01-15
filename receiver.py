from Adafruit_BBIO.SPI import SPI
from pydrs import SerialDRS
import time
import sys

sys.dont_write_bytecode = True

class Receiver:

    def __init__(self):

        self._gpio0_sts_read     = 0 | (1 << 7)     # GPIO state for P0-P7
        self._gpio1_sts_read     = 1 | (1 << 7)     # GPIO state for P8-P15
        self._dummy_data         = 0

        self._comport           = '/dev/ttyUSB0'
        self._baudrate          = '115200'

        self._spi = SPI(1,0)
        self._spi.msh = 1000000

        self._spi.xfer2([0x06, 0xFF])   # Configure GPIO0 as input
        self._spi.xfer2([0x07, 0xFF])   # Configure GPIO1 as input
        self._spi.xfer2([0x08, 0])      # Disable internal pull-ups for GPIO0
        self._spi.xfer2([0x09, 0])      # Disable internal pull-ups for GPIO1
        self._spi.xfer2([0x0A, 0])      # Disable interrupts for GPIO0
        self._spi.xfer2([0x0B, 0])      # Disable interrupts for GPIO1


    """
        Test all receivers
    """
    def do_receiver_test_1(self):

        drs = SerialDRS()
        conn = drs.Connect(self._comport, self._baudrate)

        if not conn:
            print("Erro conexao serial")
            return False

        print("Iniciando teste dos receptores de fibra")

        print('Desligando transmissores')
        drs.ClearPof()

        print('Lendo status')
        data_reg0 = self._spi.xfer2([self._gpio0_sts_read, self._dummy_data])
        data_reg1 = self._spi.xfer2([self._gpio1_sts_read, self._dummy_data])

        res0 = data_reg0[1]
        res1 = data_reg1[1]

        print('Res 0: ' + str(res0))
        print('Res 1: ' + str(res1))

        if res0 is 255 and res1 is 255:

            print('Ligando transmissores')
            drs.SetPof()

            print('Lendo status')
            data_reg0 = self._spi.xfer([self._gpio0_sts_read, self._dummy_data])
            res0 = data_reg0[1]

            data_reg1 = self._spi.xfer([self._gpio1_sts_read, self._dummy_data])
            res1 = data_reg1[1]

            print('Res 0: ' + str(res0))
            print('Res 1: ' + str(res1))

            if res0 is 0 and res1 is 0:
                print("Receptores OK")
                drs.Disconnect()
                return True

        print("Falha Receptores")
        drs.Disconnect()
        return False

    """
        Test odd receivers
    """
    def do_receiver_test_2(self):

        drs = SerialDRS()
        conn = drs.Connect(self._comport, self._baudrate)

        if not conn:
            print("Erro conexao serial")
            return False

        print("Iniciando teste dos receptores de fibra")

        drs.ClearPof()

        data_reg0 = self._spi.xfer2([self._gpio0_sts_read, self._dummy_data])
        data_reg1 = self._spi.xfer2([self._gpio1_sts_read, self._dummy_data])

        res0 = data_reg0[1]
        res1 = data_reg1[1]

        print('Res 0: ' + str(res0))
        print('Res 1: ' + str(res1))

        if res0 is 0 and res1 is 0:
            drs.SetPof()

            data_reg0 = self._spi.xfer2([self._gpio0_sts_read, self._dummy_data])
            res0 = data_reg0[1]

            data_reg1 = self._spi.xfer2([self._gpio1_sts_read, self._dummy_data])
            res1 = data_reg1[1]

            if res0 is 21 and res1 is 94:
                print("Receptores OK")
                drs.Disconnect()
                return True

        print("Falha Receptores")
        drs.Disconnect()
        return False

    """
        Test receivers 1 and 3
    """
    def do_receiver_test_3(self):

        drs = SerialDRS()
        conn = drs.Connect(self._comport, self._baudrate)

        if not conn:
            print("Erro conexao serial")
            return False

        print("Iniciando teste dos receptores de fibra")

        drs.ClearPof()

        data_reg1 = self._spi.xfer2([self._gpio1_sts_read, self._dummy_data])
        res1 = data_reg1[1]

        if not res1:
            drs.SetPof()

            data_reg1 = self._spi.xfer2([self._gpio1_sts_read, self._dummy_data])
            res1 = data_reg1[1]

            print('Res 1: ' + str(res1))

            if res1 is 20:
                print("Receptores OK")
                drs.Disconnect()
                return True

        print("Falha Receptores")
        drs.Disconnect()
        return False
