class Coefficients:
    
    def __init__(self):
        self.dict_coefficients = {
            
        }
        
    def get_coefficients(self):
        return self.dict_coefficients
        

class DonnetCoefficients(Coefficients):
    
    def __init__(self):
        self.dict_coefficients = {
            'Score': 0.077,
            'Rank': {
                'First': 0.877,
                'Second': 0.318,
                'Third': 0.312,
                'Fourth': 0.139,
                'Other': 0,
                },
            'Country': {
                'Bolivia': -0.148,
                'Colombia': -0.145,
                'El Salvador': -0.191,
                'Honduras': -0.448,
                'Nicaragua': -0.262,
                'Other': 0,
                },
            'Variety': {
                'Catuai': -0.056,
                'Caturra': 0.049,
                'Typica': -0.002,
                'Pacamara': 0.158,
                'Other': 0.002,
                },          
        }