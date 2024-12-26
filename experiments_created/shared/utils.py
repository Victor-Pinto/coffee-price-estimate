
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

def verbosity(msg: str, verb: bool = True, tl: int = 1,
               pref: str = '-', prompt: str = '> ',
               level: str = 'info'):
    '''
    Show logs and save them in log file
    v2.2.0
    level = |info, error, success, notif, debug|
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
        elif level == 'debug':
            logging.info(f'{Fore.YELLOW}\033[1m{pref}{prompt}{msg}{Style.RESET_ALL}')


        
        
        
        
