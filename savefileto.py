import os
import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

fh=logging.FileHandler('savetofile.log')
fh.setFormatter(f)

logger.addHandler(fh)

def namecheck(name):
    logger.debug(f'checking name"{name}"')
    if len(name)==0:
        logger.critical('name cannot be blank')
        return False
    elif not name.isalpha():
        logger.critical('name must be an alphabet')
        return False
    else:
        logger.error('check successfull')
        return True

def savedata(name,age,email):
    logger.debug(f'saving details of {name}')
    f=open('data.txt','a')
    f.write(f'Name:{name} - Age:{age} - Email:{email}\n')
    f.close()
    logger.error('Info saved successfully')

logger.info('End of saveToFile Program')



