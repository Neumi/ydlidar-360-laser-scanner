import serial
print (serial.__version__)

ser = serial.Serial(
    # port='/dev/tty.usbserial-A50285BI',
    port='/dev/tty.SLAB_USBtoUART',
    baudrate=128000,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=None
)


print(ser.write("\xa5"))
print(ser.write("\x00"))
print(ser.write("\xa5"))
print(ser.write("\x60"))
## exit()



while 1:
    a = ser.read()
    print hex(int(a.encode('hex'), 16))
