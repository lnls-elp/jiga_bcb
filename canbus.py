import can
import time

class CanBus:

    def __init__(self):
        self._bus = can.interface.Bus(channel='can0', bustype='socketcan_ctypes')
        self._id = 0x123
        self._data = 0xA5

    def do_can_test(self):
        msg = can.Message(arbitration_id = self._id, data = self._data)
        self._bus.send(msg)
        print('Mensagem enviada: ' + str(msg))
        rcv_msg = self._bus.recv()
        if rcv_msg.data is self._data:
            return True
        return False
