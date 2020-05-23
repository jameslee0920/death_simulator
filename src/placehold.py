"""
This module is a placeholder to feed the dataframe of input options
"""
#import numpy as np
import pandas as pd

def fn_send_input_options():
    """
    returns a dataframe of input options
    """
    s = {'exercise': ['Daily','5 times a week','4 times a week','couple times a week', 'rarely', 'never'],
           'bmi': [18,19,20,21,22,23],
           'height': ['3ft something', '4ft something', '5ft something', '6ft something', '7ft something', '8ft something'],
           'weight': ['less than 150lbs', 'around 160lbs', 'around 170lbs', 'around 180lbs', 'around 190lbs', '200lbs or larger'],
           'diabetic': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
           'mcdonalds': ['Today', 'Yesterday', 'Recently', 'Last Month', 'Never', 'McDonalds?'],
           'new_gender': ['Female', 'Male', 'Unspecified', 'Non-Binary', 'Male', 'Male']
        }

    s_df = pd.DataFrame(s, columns = ['exercise', 'bmi', 'height', 'weight', 'diabetic', 'mcdonalds', 'new_gender'])
    
    #df = pd.read_csv(input_csv)
    return s_df


#special = {'Exercise': ['Daily','5 times a week','4 times a week','couple times a week', 'rarely', 'never'],
#           'BMI': [18,19,20,21,22,23],
#           'Height': ['3ft something', '4ft something', '5ft something', '6ft something', '7ft something', '8ft something'],
#           'Weight': ['less than 150lbs', 'around 160lbs', 'around 170lbs', 'around 180lbs', 'around 190lbs', '200lbs or #larger'],
#           'Diabetic': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
#           'McDonalds': ['Today', 'Yesterday', 'Recently', 'Last Month', 'Never', 'McDonalds?']
#        }
#
#special_df = pd.DataFrame(special, columns = ['Exercise', 'BMI', 'Height', 'Weight', 'Diabetic', 'McDonalds'])
#
#s = {'exercise': ['Daily','5 times a week','4 times a week','couple times a week', 'rarely', 'never'],
#           'bmi': [18,19,20,21,22,23],
#           'height': ['3ft something', '4ft something', '5ft something', '6ft something', '7ft something', '8ft something'],
#           'weight': ['less than 150lbs', 'around 160lbs', 'around 170lbs', 'around 180lbs', 'around 190lbs', '200lbs or #larger'],
#           'diabetic': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
#           'mcdonalds': ['Today', 'Yesterday', 'Recently', 'Last Month', 'Never', 'McDonalds?'],
#           'new_gender': ['Female', 'Male', 'Unspecified', 'Non-Binary', 'Male', 'Male']
#        }
#
#s_df = pd.DataFrame(special, columns = ['exercise', 'bmi', 'height', 'weight', 'diabetic', 'mcdonalds', 'new_gender'])

