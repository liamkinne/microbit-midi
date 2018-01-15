from microbit import *

class Midi:
  def __init__(self, pin_tx, pin_rx):
    self.pin_tx = pin_tx
    self.pin_rx = pin_rx

    self.commands = {
      'note_off' : 0x80,
      'note_on' : 0x90,
      'aftertouch' : 0xA0,
      'continuous_controller' : 0xB0,
      'patch_change' : 0xC0,
      'channel_pressure' : 0xD0,
      'pitch_bend' : 0xE0,
      'non_musical' : 0xF0,
    }

  def send_command(self, command, data):
    uart.write(bytes([command | data]))