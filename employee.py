import savefileto as sft
import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

fh=logging.FileHandler('employee.log')
fh.setFormatter(f)

logger.addHandler(fh)

stream_handler = logging.StreamHandler()

logger.addHandler(stream_handler)

stream_handler.setFormatter(f)

logger.debug('Start of employee program')

name='aditya'
age='25'
email='abc@gmail.com'

if sft.namecheck(name) is True:
    sft.savedata(name, age, email)
else:
    logger.critical('Employee check failed')


logger.debug('End of employee check')

