from typing_extensions import List, Dict

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.debug("test")


# def verbosity(info: str, verb: bool = True, end: str = '\n'):
#     '''
#     Control the printing of messages based on a verbosity parameter
#     v..0.0
#     '''
#     if verb:
#         print(info, end=end)

def verbosity(msg: str, type: str = 'info', verb: bool = True, tl: int = 1,
               pref: str = '-', prompt: str = '> '):
    '''
    Show logs and save them in log file
    v2.0.0
    '''
    
    pref *= tl
    
    if verb:
            
        if type=='info':
            verbosity_info(msg, tl,
                pref, prompt)
            
        if type=='error':
            verbosity_error(msg, tl,
                pref, prompt)
            
        if type=='debug':
            verbosity_debug(msg, tl,
                pref, prompt)
            
        if type=='warning':
            verbosity_warning(msg, tl,
                pref, prompt)


def verbosity_info(msg: str, tl: int = 1,
                   pref: str = '-', prompt: str = '> '):
    logging.info(f'{pref}{prompt}{msg}')


def verbosity_error(msg: str, tl: int = 1,
                   pref: str = '-', prompt: str = '> '):
    logging.error(f'{pref}{prompt}{msg}')


def verbosity_debug(msg: str, tl: int = 1,
                   pref: str = '-', prompt: str = '> '):
    logging.debug(f'{pref}{prompt}{msg}')


def verbosity_warning(msg: str, tl: int = 1,
                   pref: str = '-', prompt: str = '> '):
    logging.warning(f'{pref}{prompt}{msg}')
        
        
        
        
