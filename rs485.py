import Adafruit_BBIO.UART as UART
import serial
import time

class Rs485:

    def __init__(self):
        self.setup_pins()

    def setup_pins(self):
        UART.setup("UART5")

    def do_rs485_test(self):
        res = ""
        test_val = 'B'
        print("Iniciando teste de RS485")
        ser = serial.Serial(port = '/dev/tty05', baudrate='115200')
        ser.open()
        if ser.isOpen():
            ser.write(test_val)
            res = ser.read()
            ser.close()
            if res is test_val:
                return True
        return False
