import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.GPIO as GPIO
import serial
import time
import sys

sys.dont_write_bytecode = True

class Rs485:

    def __init__(self):
        self.setup_pins()

    def setup_pins(self):
        UART.setup("UART5")
        GPIO.setup('GPIO1_29', GPIO.OUT)
        GPIO.output('GPIO1_29', GPIO.LOW)

    def do_rs485_test(self):
        res = ""
        test_val = 'B'
        print("Iniciando teste de RS485")
        ser = serial.Serial(port = '/dev/ttyO5', baudrate='390625', timeout=1)
        ser.close()
        ser.open()

        if not ser.isOpen():
            print("Erro conexao UART5")
            return False

        GPIO.output('GPIO1_29', GPIO.HIGH)
        ser.write(test_val)
        GPIO.output('GPIO1_29', GPIO.LOW)
        res = ser.read()
        print(res)
        ser.close()
        if res is test_val:
            print("RS485 OK")
            return True
        print("RS485 Falha")
        return False
