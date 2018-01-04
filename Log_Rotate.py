'''
Created on Jan 4, 2018

@author: ZhuqinZ
'''

import logging
import time
from logging.handlers import RotatingFileHandler

if __name__ == '__main__':
    logger = logging.getLogger('Rotating Log')
    handler = RotatingFileHandler("C:\\Users\\zhuqinz\\Desktop\\log\\172.24.201.122\\test.log", maxBytes= 100, backupCount=20)
    logger.addHandler(handler)
    
    while(True):
        if handler.shouldRollover(''):
            handler.doRollover()
    
    time.sleep(600)