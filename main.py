from microbit import *
from midi import *

m = Midi(pin0, pin1)

notes = ["F4", "A4", "C4", "E4"] # F,A,C,E

m.set_instrument(10)

while True:
	for n in notes:
		m.note_on(n, 127)
		sleep(500)
		m.note_off(n, 127)
		sleep(500)