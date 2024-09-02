import sys
sys.path.insert(1, '../../shared')
import os.path
from os import path
from utils import verbosity

import pandas as pd

class File:
    def __init__(self):
        pass
    
    def file_exist(self, file_path):
        
        return path.exists(file_path)
    
    
class XlsxOperations(File):
            
    def __init__(self):
        pass
    
    
    def load_file(self, file_name):
        file_path = f"../../static/{file_name}"
        verbosity(msg=f'enter in load_file_xlsx function',
                    tl=1)
        verbosity(msg=f'checking if the file exist',
                    tl=2)
        if(self.file_exist(file_path)):
            verbosity(msg=f'the file exist',
                        tl=2)
            df = pd.read_excel(file_path)
            verbosity(msg=f'File loaded: {file_name}',
                        tl= 3)
            return df
        else:
            verbosity(msg=f"the file doesn't exist",
                        tl=2)
            return False
            
        

class HtmlOperations(File):
            
    def __init__(self):
        pass
    
    
    def save_html_page(self, html_code, file_name):
        verbosity(msg=f'enter in save_html_page function',
                    tl=1)
        verbosity(msg=f'checking if the file exist',
                    tl=2)
        if(self.file_exist(file_name)):
            verbosity(msg=f'the file exist',
                        tl=2)
            verbosity(msg=f'saving html page',
                        tl= 3)
            f = open(f'../static/{file_name}','w')
            f.write(html_code)
            f.close()
        else:
            verbosity(msg=f"the file doesn't exist",
                        tl=2)
            verbosity(msg=f"creating file",
                        tl=3)
            f = open(f'../static/{file_name}', "x")
            verbosity(msg=f"saving html page",
                        tl=3)
            f.write(html_code)
            f.close()
        verbosity(msg=f'out from save_html_page function',
                    tl=1)