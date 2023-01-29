import serial

class ArduinoService():
    ArduinoSeparator = "x"

    def __init__(self, arduinoComPort = "com3", readingFrequency = 9600):
        try:
            self.ArduinoConnection = serial.Serial(arduinoComPort, readingFrequency)
        except:
            print("An exception occurred in ArduinoTicknessService."\
            +" Please check the ArduinoConnection. Maybe, serial port open?")     

    def getArduinoModel(self):
        try:
            return str(self.ArduinoConnection.readline().decode('ascii')).split(self.ArduinoSeparator)
        except:
            print("An exception occurred in ArduinoTicknessService."\
                 + " Please check the Arduino Script. Maybe, some parameters missed")
        return None
