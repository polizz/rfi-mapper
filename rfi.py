#!/usr/bin/env python3

import serial

SERIAL_PORT_DESC = '/dev/ttyp0'
PREAMBLE = 0xFE
TRANSCEIVER_ADDR = 0xA4
CONTROLLER_ADDR = 0XE0
GOOD = 0xFB
BAD = 0xFA
END = 0xFD
GPS_READ_CMD = 0x23
GPS_READ_SUB_CMD = 0x00
S_METER_CMD = 0x15
S_METER_SUB_CMD = 0x02

OK_MESSAGE = bytes([PREAMBLE, PREAMBLE, CONTROLLER_ADDR, TRANSCEIVER_ADDR, GOOD, END])

ser = serial.Serial(SERIAL_PORT_DESC, 19200, timeout=0)

while True:
    ser.write(bytes([PREAMBLE, PREAMBLE, TRANSCEIVER_ADDR, CONTROLLER_ADDR, GPS_READ_CMD, GPS_READ_SUB_CMD, END]))
    # s = ser.read(1)
    b = ser.read_until(bytes([PREAMBLE, PREAMBLE, CONTROLLER_ADDR, TRANSCEIVER_ADDR, GOOD, END]))
    print(b)
