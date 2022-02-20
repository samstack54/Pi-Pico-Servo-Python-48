from machine import Pin, PWM
from utime import sleep

servo = PWM(Pin(16))

servo.freq(50)

while True:
    # 0 degrees (2 per cent duty cycle)
    servo.duty_u16(1310)  # 65535*0.02 = 1310
    sleep(2)
    # 180 degrees (12.5 per cent duty cycle)
    servo.duty_u16(8200)  # 65535*12.5 = 8192
    sleep(2)