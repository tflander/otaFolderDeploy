import machine
import time

led = machine.Pin(22, machine.Pin.OUT)

for i in range(9):
    led.value(1)
    time.sleep_ms(500)
    led.value(0)
    time.sleep_ms(500)

f = open('red/main.py')
updated_code = f.read()
f.close()

f = open('main.py', "w")
f.write(updated_code)
f.close()
machine.reset()