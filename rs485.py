import Adafruit_BBIO.UART as UART
import serial
import time
import sys

sys.dont_write_bytecode = True

class Rs485:

    def __init__(self):
        self.setup_pins()

    def setup_pins(self):
        UART.setup("UART5")

    def do_rs485_test(self):
        res = ""
        test_val = 'B'
        print("Iniciando teste de RS485")
        ser = serial.Serial(port = '/dev/tty5', baudrate='115200', timeout=0)

        if not ser.isOpen():
            ser.open()

        ser.write(test_val)
        res = ser.read()
        ser.close()
        if res is test_val:
            print("RS485 OK")
            return True
        print("RS485 Falha")
        return False
