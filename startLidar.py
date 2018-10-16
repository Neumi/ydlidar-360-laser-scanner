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

# print cloud data
# ser.write("\xa5")
# ser.write("\x00")
# ser.write("\xa5")
# ser.write("\x60")

# ser.write("\xa5")
# ser.write("\x40")
## exit()



while 1:
    a = ser.read()
    print hex(int(a.encode('hex'), 16))
    # print int(a)

