import sys

# sys.path.insert(-1, '../../shared')
from utils import verbosity


class DictionaryTranslator:
    def __init__(self):
        print('Father class')
        self.dict_translator = {

        }
        
        
    def refresh_dict_translator(self, variable_name):
        pass
        

    def translate_attribute(self, value_attribute, variable_name):
        self.refresh_dict_translator(variable_name)
        name_attribute = ''
        verbosity(msg = f'Translating {value_attribute}, {variable_name}',
                        verb=self.is_verbose, tl=1)
        
        
        for key, value in self.dict_translator.items():
            for attribute in value:
                try:
                    if attribute.lower() in value_attribute.lower():
                        name_attribute = key
                        
                        verbosity(msg = f'Value is {name_attribute}',
                        verb=self.is_verbose, tl=2)

                        return name_attribute
                except:
                    verbosity(msg = f'Attribute Error in {name_attribute}',
                        verb=self.is_verbose, type='error',	tl=2)
                    return None

        verbosity(msg = f'Value {value_attribute} not found',
        verb=self.is_verbose, tl=3)
        return 'Other'


class DonnetTranslator(DictionaryTranslator):

    def __init__(self):
        self.variables = ['Score', 'Rank', 'Country', 'Variety']
        self.dict_translator = {

        }
        
        self.is_verbose=False
        

    def refresh_dict_translator(self, variable_name):
        is_verbosity= False
        if (variable_name == 'Variety'):
            verbosity(msg=f' Translating, Variety',
                      verb=is_verbosity, tl=1)
            self.dict_translator = {
                'Catuai': ['Catuai'],
                'Caturra': ['Caturra'],
                'Typica': ['Typica'],
                'Pacamara': ['Pacamara'],
            }

        elif (variable_name == 'Rank'):
            verbosity(msg=f' Translating, ranking',
                      verb=is_verbosity, tl=1)
            self.dict_translator = {
                'First': ['1a', '1b'],
                'Second': ['2a', '2b'],
                'Third': ['3a', '3b'],
                'Fourth': ['4'],
            }
        elif (variable_name == 'Country'):
            verbosity(msg=f' Translating, origin',
                      verb=is_verbosity, tl=1)
            self.dict_translator = {
                'Colombia': ['Colombia'],
                'Bolivia': ['Bolivia'],
                'Honduras': ['Honduras'],
                'Nicaragua': ['Nicaragua'],
                'El Salvador': ['El Salvador'],
            }
