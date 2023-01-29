import serial
import logger


class ArduinoService():
    ArduinoSeparator = "x"

    def __init__(self, arduinoComPort = "com3", readingFrequency = 9600):
        try:
            self.logger = logging.getLogger('error_logger')
            self.ArduinoConnection = serial.Serial(arduinoComPort, readingFrequency)
        except:
            self.logger.error(f'An exception occurred in ArduinoTicknessService."\
            +" Please check the ArduinoConnection. Maybe, serial port open? : {e}')

    def getArduinoModel(self):
        try:
            return str(self.ArduinoConnection.readline().decode('ascii')).split(self.ArduinoSeparator)
        except:
            self.logger.error(f'An exception occurred in ArduinoTicknessService."\
            +" Please check the ArduinoConnection. Maybe, serial port open? : {e}')
        return None
