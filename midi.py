from microbit import *

class Midi:
  def __init__(self, pin_tx, pin_rx):
    self.pin_tx = pin_tx
    self.pin_rx = pin_rx

    self.channel = 0

    # uart settings
    self.uart_config = {
      'baud' : 31250,
      'bits' : 8,
      'parity' : None,
      'stop' : 1,
    }

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

    self.note_offset = {
      'C'  : 0x00,
      'C#' : 0x01,
      'D'  : 0x02,
      'D#' : 0x03,
      'E'  : 0x04,
      'F'  : 0x05,
      'F#' : 0x06,
      'G'  : 0x07,
      'G#' : 0x08,
      'A'  : 0x09,
      'A#' : 0x0A,
      'B'  : 0x0B,
    }

  def set_channel(self, channel):
    if channel in range(0, 15):
      self.channel = channel

  def send_command(self, command, data):
    uart.init(baudrate=self.uart_config['baud'], bits=self.uart_config['bits'], parity=self.uart_config['parity'], stop=self.uart_config['stop'], tx=self.pin_tx, rx=self.pin_rx)
    output = [command | self.channel]
    output.extend(data)
    uart.write(bytes(output))
    uart.init(115200) # restore usb coms

  def split_note(self, note):
    if note[1] == '#':
      octave = note[2:]
      note = note[:2]
    else:
      octave = note[1:]
      note = note[:1]
    return note, int(octave)

  def note_to_hex(self, note):
    note, octave = self.split_note(note)
    return int(self.note_offset[note] + ((octave + 1) * 12))

  def note_on(self, note, velocity):
    self.send_command(self.commands['note_on'], (self.note_to_hex(note), velocity))

  def note_off(self, note, velocity):
    self.send_command(self.commands['note_off'], (self.note_to_hex(note), velocity))
