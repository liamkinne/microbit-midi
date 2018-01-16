from microbit import *
from midi import Midi

m = Midi(0, 1)

notes = ["F4", "A4", "C4", "E4"] # F,A,C,E

for n in notes:
	print(m.note_to_hex(n))