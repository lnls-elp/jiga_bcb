from Adafruit_I2C import Adafruit_I2C
import time

class I2c:

    def __init__(self):
        self._slave_add = 0xA5
        self._reg_add   = 0x01
        self._test_val  = 0x5A

        self._i2c = Adafruit_I2C(self._slave_add)

    def do_i2c_test(self):
        print("Iniciando teste I2C")
        self._i2c.write8(self._reg_add, self._value)
        res = self._i2c.readU8(self._reg_add)
        if res is not None:
            if res is self._value:
                print("I2C OK")
                return True
        print("I2C Falha")
        return False
