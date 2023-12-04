import logging
logger=logging.getLogger(__name__)
formater=logging.Formatter('%(levelname)s:%  %(name)s: %(message)s')
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler('employee.log')
file_handler.setFormatter(formater)
logger.addHandler(file_handler)

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(levelname)s:%  %(name)s: %(message)s')


class employ:
    def __int__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee :{} - {} '.format(self.fullname,self.email))

    
    @property
    def email(self):
        return '{} .{}@email.com'.format(self.first,self.last)
    @property   
    def fullname(self):
        return '{} {}'.format(self.first,self.last) 


