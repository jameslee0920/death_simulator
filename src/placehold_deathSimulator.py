"""
This module is a placeholder to feed the dataframe of input options
"""
import numpy as np
import pandas as pd
import print_death_cert
import sys
import time
from datetime import date
from datetime import datetime, timedelta
import random

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
           'new_gender': ['Female', 'Male', 'Unspecified', 'Non-Binary']
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



def death_simulator(collected_inputs_dict):
    """
    Takes the parameters input by the user and computes their day of death based on the death probability
    """
    """
    Methodology:
    1. Calculate current age using the date of birth
    2. Filter dataset for age >= current_age to get annual probabilities for each age group
    3. convert them to daily probability and gerenate sequence of 0/1 based on the death probability.
    4. continue this till the first 1 occurs. the index of this 1 gives the date of death.
    """
    #load datasets
    causeOfDeath = pd.read_csv('../data/annualCauseofDeathProbs_age_gender_race.csv')
    deathProb = pd.read_csv('../data/annualDeathProbs_age_gender_race.csv')
    jobIndex = pd.read_csv('../data/job_indexed_likelihood.csv')
    
    #collected input parameters
    curr_age = collected_inputs_dict['age']
    job = collected_inputs_dict['job']
    gender = collected_inputs_dict['gender']
    race = collected_inputs_dict['race']
                            
                            
    #calculating present age from the given birthDate
    today = date.today() 
    year = today.year
    #curr_age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    
    #Subset data as per the given input parameters
    data_subset = deathProb.loc[(deathProb['age']>= curr_age)&(deathProb['gender'] == gender)& (deathProb['race'] == race)]
    death_Prob = data_subset['annual_death_prob'].to_list()
    
    #indexed death_likelihood as per the selected occupation of the user
    job_likelihood = jobIndex.loc[(jobIndex['occupation'] == job)].iloc[0]['indexed_likelihood']
    
    iter_ = 0
    death_age = curr_age
    
    #simulation
    while True:
        l = len(death_Prob)
        outcome = [0,1] 
        #to account for leap years
        leapYear = year%4
        
        if(iter_>=l):
            prob = death_Prob[l-1]*job_likelihood
        else:
            prob = death_Prob[iter_]*job_likelihood
            
        daily_prob = 1- (1-prob)**(1/365)
        
        if(leapYear == 0):
            days = np.random.choice(outcome,366, p=[1-daily_prob, daily_prob])
        else:
            days = np.random.choice(outcome,365, p=[1-daily_prob, daily_prob])                    
        if(iter_ == 0):
            total_days = np.array(days).tolist()
        else:
            total_days = total_days + np.array(days).tolist()                   
        year += 1
        death_age += 1
        iter_ += 1
        
        if np.sum(total_days)> 0:
            break
                            
    #Code after this line needs to be modified to include cause of death for ages > 85
    if(death_age > 85):
        cod = causeOfDeath.loc[(causeOfDeath['age']== 85)&(causeOfDeath['gender'] == gender)& (causeOfDeath['race'] == race)]\
                      .sort_values(by='cause_of_death_prob', ascending=False)
        mechanism = cod.iloc[0]['mechanism_of_death']
        cause = cod.iloc[0]['cause_of_death']
    else:
        cod = causeOfDeath.loc[(causeOfDeath['age']== death_age)&(causeOfDeath['gender'] == gender)& (causeOfDeath['race'] == race)]\
                      .sort_values(by='cause_of_death_prob', ascending=False)
        mechanism = cod.iloc[0]['mechanism_of_death']
        cause = cod.iloc[0]['cause_of_death']
  
    if(1 in total_days) == True:
        c = total_days.index(1)
        death_date = today + timedelta(c)
        if(death_age>= 110):
            proxy_death_age = 110
            v = 'You will die on '+str(death_date)+' from "'+str(mechanism)+'", at the age of '+ str(proxy_death_age)+'.Cause of death will be '+str(cause)+'. You have '+ str(int(c/365))+' more years to live, make the most of it!'
            return v
        else:
            v = 'You will die on '+str(death_date)+' from "'+str(mechanism)+'", at the age of '+ str(death_age)+'.Cause of death will be '+str(cause)+'. You have '+ str(int(c/365))+' more years to live, make the most of it!'
        return v
    else:
        v = 'You will get the surprise of death as a SURPRISE!'
        return v
    
    

def fn_send_output_string(collected_inputs_dict):
    #function saves pdf death cert and sends string to notebook frontend

    
    disc = death_simulator(collected_inputs_dict)
    data_dict = {
       'introduction': 'The team would like to make an announcement of your death',
       'name': 'Grim Reaper',#replace with collected_inputs_dict['name']
       'result': disc
    }
    
    #data_dict = collected_inputs_dict
    input_pdf_path = '../docs/death_certificate_template.pdf'
    output_pdf_path = "../docs/death_certificate_{fname}.pdf".format(fname = data_dict['name'])
    
    print_death_cert.write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict)
    #return data_dict["description"]
    return data_dict



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