import serial

def read_signal(port='COM3', baudrate=9600):
    ser = serial.Serial(port, baudrate)
    while True:
        data = ser.readline().decode('utf-8').strip()
        yield float(data)
