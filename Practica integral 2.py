from hcsr04 import HCSR04
from machine import Pin, PWM
from time import sleep, sleep_ms

rojo = Pin(16, Pin.OUT)
verde = Pin(17, Pin.OUT)
azul = Pin(5, Pin.OUT)

sensor = HCSR04(trigger_pin=15, echo_pin=4, echo_timeout_us=24000)

C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
alerta = [C4, D4, E4, F4, G4]

class Buzzer:
    def __init__(self, sig_pin):
        self.pwm = PWM(Pin(sig_pin, Pin.OUT))

    def play(self, melody, wait, duty):
        for note in melody:
            self.pwm.freq(note)
            self.pwm.duty_u16(duty)
            sleep_ms(wait)
        self.pwm.duty_u16(0)

buzzer = Buzzer(23)

while True:
    distancia = sensor.distance_cm()
    print(f"Distancia: {distancia} cm")

    if distancia > 100:
        verde.value(1)
        rojo.value(0)
    elif distancia > 50 and distancia < 100:
        rojo.value(1)
        verde.value(1)
    else:
        rojo.value(1)
        verde.value(0)
        buzzer.play(alerta, 150, 32768)

    sleep(0.5)
