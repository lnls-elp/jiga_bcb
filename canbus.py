import Adafruit_BBIO.GPIO as GPIO
import can
import sys

sys.dont_write_bytecode = True

class CanBus:

    def __init__(self):
        self._bus = can.interface.Bus(channel='can0', bustype='socketcan_ctypes')
        self._id = 0x010
        self._data = [0xA5]

    def do_can_test(self):
        print("Iniciando teste CAN")
        msg = can.Message(arbitration_id = self._id, data = self._data)
        self._bus.send(msg)
        print('Mensagem enviada: ' + str(msg))
        rcv_msg = self._bus.recv(timeout=1)
        print(rcv_msg.data)
        if rcv_msg is not None and rcv_msg.data[0] is self._data[0]:
            return True
        return False
