"""
This module is a placeholder to feed the dataframe of input options
"""
#import numpy as np
import pandas as pd
import print_death_cert

def fn_send_input_options():
    """
    returns a dataframe of input options
    """
    df = pd.read_csv('../data/deaths_age_gender_race_mechanism_cause.csv')
    occ_df = pd.read_csv('../data/job_indexed_likelihood.csv')
    
    s = {'exercise': ['Daily','5 times a week','4 times a week','couple times a week', 'rarely', 'never'],
           'bmi': [18,19,20,21,22,23],
           'height': ['3ft something', '4ft something', '5ft something', '6ft something', '7ft something', '8ft something'],
           'weight': ['less than 150lbs', 'around 160lbs', 'around 170lbs', 'around 180lbs', 'around 190lbs', '200lbs or larger'],
           'diabetic': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
           'mcdonalds': ['Today', 'Yesterday', 'Recently', 'Last Month', 'Never', 'McDonalds?'],
           'new_gender': ['Female', 'Male', 'Unspecified', 'Non-Binary', 'Male', 'Male']
        }
    
    #s is a dict
    # append age, race, occupation series
    
    #PROBABLY SHOULD SORT THIS HERE

    s["occupation"] = list(occ_df.occupation.unique())
    #AGE NEEDS TO GO LARGER THAN 85 WHICH MEANS THIS NEEDS TO PULL FROM A DIFF DF OR ADD 85 thru 100
    s["age"] = list(df.age.unique())
    #MAYBE ADD AN OPTION WHERE THEY OPT OUT OF RACE
    s["race"] = list(df.race.unique())

    #s_df = pd.DataFrame(s, columns = ['exercise', 'bmi', 'height', 'weight', 'diabetic', 'mcdonalds', 'new_gender'])
    
    #df = pd.read_csv(input_csv)
    return s

def fn_send_output_string(collected_inputs_dict):
    #function saves pdf death cert and sends string to notebook frontend
    data_dict = {
       'introduction': 'The team would like to make an announcement of your death',
       'name': 'Grim Reaper',
       'description': 'Unfortunately by death by having too much fun, you die at 0 year 0 months 1 day from today or at YY/MM/DD'
    }
    #data_dict = collected_inputs_dict
    input_pdf_path = '../docs/death_certificate_template.pdf'
    output_pdf_path = "../docs/death_certificate_{fname}.pdf".format(fname = data_dict['name'])
    
    print_death_cert.write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict)
    return data_dict["description"]



    #return "You will die of {cause} at the age of {age_of_death} years old on {date_of_death}".format(
    #    cause = data_dict['cause'],
    #    age_of_death = data_dict['age_of_death'],
    #    date_of_death = data_dict['date_of_death']
    #)

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