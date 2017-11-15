import Adafruit_BBIO.GPIO as GPIO
import time

class Receiver:

    def __init__(self):
        self._receiver =    ['GPIO1_0', 'GPIO1_4', 'GPIO1_12', 'GPIO2_1',
                            'GPIO1_1', 'GPIO1_5', 'GPIO1_14', 'GPIO2_6',
                            'GPIO1_2', 'GPIO1_6', 'GPIO1_29', 'GPIO2_27',
                            'GPIO1_3', 'GPIO1_7', 'GPIO1_31', 'GPIO2_8',
                            'GPIO2_9', 'GPIO2_13']

        # Cannot be used (reserved):fr
        #   - GPIO1_0
        #   - GPIO1_4
        #   - GPIO1_1
        #   - GPIO1_5
        #   - GPIO1_2
        #   - GPIO1_6
        #   - GPIO1_3
        #   - GPIO1_7
        #   - GPIO1_31
        self.setup_pins(self._receiver)

    def setup_pins(self, pins):
        for item in pins:
            GPIO.setup(item, GPIO.IN)

    def do_receiver_test_1(self):
        acum = 0
        expected = 18

        print("Iniciando teste dos receptores de fibra")

        for item in self._receiver:
            GPIO.add_event_detect(item, GPIO.FALLING)
        # TODO: Manda o UDC iniciar o teste

        time.sleep(0.3)
        for item in self._receiver:
            if GPIO.event_detected(item):
                acum += 1

        if acum is expected:
            print("Receiver OK")
            return True
        print("Receiver Falha")
        return False

    def do_receiver_test_2(self):
        return self.do_receiver_test_1()

    def do_receiver_test_3(self):
        return self.do_receiver_test_1()
