from typing_extensions import List, Dict

import logging
from colorama import Fore, Style

log_file_path='info.log'
dic_params = {
        'level': logging.INFO,
        'format': "%(asctime)s [%(levelname)s]:\t %(message)s",
        'datefmt': '%Y-%m-%d %H:%M:%S',
        'handlers': [logging.StreamHandler(),
                    logging.FileHandler(log_file_path)]
        }
logging.basicConfig(**dic_params)

# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='info.log', filemode='w', encoding='utf-8', level=logging.DEBUG)
# logger.setLevel(logging.DEBUG)
# logging.debug("test")


# def verbosity(info: str, verb: bool = True, end: str = '\n'):
#     '''
#     Control the printing of messages based on a verbosity parameter
#     v..0.0
#     '''
#     if verb:
#         print(info, end=end)

def verbosity(msg: str, verb: bool = True, tl: int = 1,
               pref: str = '-', prompt: str = '> ',
               level: str = 'info'):
    '''
    Show logs and save them in log file
    v2.2.0
    '''

    if verb:
        pref *= tl
        if level == 'info':
            logging.info(f'{pref}{prompt}{msg}{Style.RESET_ALL}')
        elif level == 'error':
            logging.error(f'{Fore.RED}\033[1m{pref}{prompt}{msg}{Style.RESET_ALL}')
        elif level == 'success':
            logging.info(f'{Fore.GREEN}\033[1m{pref}{prompt}{msg}{Style.RESET_ALL}')
        elif level == 'notif':
            logging.info(f'{Fore.CYAN}\033[1m{pref}{prompt}{msg}{Style.RESET_ALL}')


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



def save_logging():
    pass
        
        
        
        
