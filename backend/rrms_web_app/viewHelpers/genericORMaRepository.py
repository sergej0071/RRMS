from rrms_web_app.models import MainData
from datetime import datetime
import logging
from varname import nameof

class GenericORMaRepository():
    def __init__(self):
        self.logger = logging.getLogger('error_logger')

    def getLastElements(self, model, amount, *fields):
        try:
            return list(model
                        .objects
                        .reverse()
                        .values(*fields)[:int(amount)][::-1])        
        except Exception as e:
            self.logger.error(f"""'An exception occurred in {nameof(GenericORMaRepository)}. method {nameof(self.getLastElement)} exeption - {e} '""")
        return None
    
    def getLastElement(self, model, *fields):
        try:
            f = MainData.objects.all().values(*fields).last()
            return(f)
        except Exception as e:
            self.logger.error(f'An exception occurred in CurrentStatus. exeption - {e} ')
        return None
        

    
        