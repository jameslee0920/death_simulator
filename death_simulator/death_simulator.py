"""
Author: Thomas Winegarden, James Lee, Aniruddha Dutta

This module is designed to perform the following tasks:
    1. a placeholder to feed the dataframe of input options
    2. Run death_simulator and store the results in a dictionary
    3. Use the death simulator results to create death certificate
"""

import numpy as np
import pandas as pd
import print_death_cert
import sys
import time
from datetime import date
from datetime import datetime, timedelta
import random
from numpy import inf

def fn_send_input_options():
    df = pd.read_csv('../data/deaths_age_gender_race_mechanism_cause.csv')
    occ_df = pd.read_csv('../data/job_indexed_likelihood.csv')
    s = {'exercise': ['Daily', '5 times a week', '4 times a week',
                      'couple times a week', 'rarely', 'never'],
         'bmi': [18, 19, 20, 21, 22, 23],
         'height': ['3ft something', '4ft something', '5ft something',
                    '6ft something', '7ft something', '8ft something'],
         'weight': ['less than 150lbs', 'around 160lbs', 'around 170lbs',
                    'around 180lbs', 'around 190lbs', '200lbs or larger'],
         'diabetic': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
         'mcdonalds': ['Today', 'Yesterday', 'Recently', 'Last Month',
                       'Never', 'McDonalds?'],
         'new_gender': ['Female', 'Male']
        }
    s["occupation"] = list(occ_df.occupation.unique())
    s["age"] = sorted(list(df.age.unique()))
    s["race"] = sorted(list(df.race.unique()))
    s["name"] = ""
    return s


def death_simulator(collected_inputs_dict):
    """
    Takes the parameters input by the user and computes their day of death based on the death probability
    Methodology:
    1. Calculate current age using the date of birth
    2. Filter dataset for age >= current_age to get annual probabilities for each age group
    3. convert them to daily probability and gerenate sequence of 0/1 based on the death probability.
    4. continue this till the first 1 occurs. the index of this 1 gives the date of death.
    """
    causeOfDeath = pd.read_csv('../data/annualCauseofDeathProbs_age_gender_race.csv')
    deathProb = pd.read_csv('../data/annualDeathProbs_age_gender_race.csv')
    deathProb[deathProb.annual_death_prob == inf] = 1.0
    jobIndex = pd.read_csv('../data/job_indexed_likelihood.csv')
    
    curr_age = collected_inputs_dict['age']
    job = collected_inputs_dict['job']
    gender = collected_inputs_dict['gender']
    race = collected_inputs_dict['race']
    today = date.today()
    year = today.year
    iter_ = 0

    if(curr_age <= 85):
        data_subset = deathProb.loc[(deathProb['age'] >= curr_age) &\
                                    (deathProb['gender'] == gender) &\
                                    (deathProb['race'] == race)]
        death_Prob = data_subset['annual_death_prob'].tolist()
    else:
        data_subset = deathProb.loc[(deathProb['age'] >= 85) &\
                                    (deathProb['gender'] == gender)&\
                                    (deathProb['race'] == race)]
        death_Prob = data_subset['annual_death_prob'].tolist()

    job_likelihood = jobIndex.loc[(jobIndex['occupation'] == job)]\
                             .iloc[0]['indexed_likelihood']  
    death_age = curr_age

    while True:
        l = len(death_Prob)
        outcome = [0, 1]
        leapYear = year%4

        if(iter_ >= l):
            prob = death_Prob[l-1]*job_likelihood
        else:
            prob = death_Prob[iter_]*job_likelihood

        daily_prob = 1- (1-prob)**(1/365)

        if(leapYear == 0):
            day_len = 366
            days = np.random.choice(outcome,day_len, p = [1 - daily_prob, daily_prob])
        else:
            day_len = 365
            days = np.random.choice(outcome,day_len, p = [1 - daily_prob, daily_prob])
        if(iter_ == 0):
            total_days = np.array(days).tolist()
        else:
            total_days = total_days + np.array(days).tolist()
        year += 1
        death_age += 1
        iter_ += 1
        if np.sum(total_days) > 0:
            break

    if(death_age > 85):
        if(death_age <= 91):
            cod = causeOfDeath.loc[(causeOfDeath['age'] == death_age)]\
                              .sort_values(by = 'cause_of_death_prob', ascending=False)
            rand = random.randrange(len(cod.index))
            mechanism = cod.iloc[rand]['mechanism_of_death']
            cause = cod.iloc[rand]['cause_of_death']
        elif(death_age > 91):
            cod = causeOfDeath.loc[(causeOfDeath['age'] == 91)]\
                              .sort_values(by = 'cause_of_death_prob', ascending = False)
            rand = random.randrange(len(cod.index))
            mechanism = cod.iloc[rand]['mechanism_of_death']
            cause = cod.iloc[rand]['cause_of_death']
    else:
        cod = causeOfDeath.loc[(causeOfDeath['age'] == death_age)&\
                               (causeOfDeath['gender'] == gender)&\
                               (causeOfDeath['race'] == race)]\
                          .sort_values(by = 'cause_of_death_prob', ascending=False)
        rand = random.randrange(len(cod.index))
        mechanism = cod.iloc[rand]['mechanism_of_death']
        cause = cod.iloc[rand]['cause_of_death']

    if(1 in total_days) == True:
        ndays = total_days.index(1)
        death_date = today + timedelta(ndays)
        if(death_age >= 110):
            proxy_death_age = 110
            result = 'You will die on '+str(death_date)+' from "'+str(mechanism)+'", at the age of '+ str(proxy_death_age)+'. Cause of death will be '+str(cause)+'. You have '+ str(int(ndays/365))+' more years to live.'
            return result
        else:
            result = 'You will die on '+str(death_date)+' from "'+str(mechanism)+'", at the age of '+ str(death_age)+'. Cause of death will be '+str(cause)+'. You have '+ str(int(ndays/365))+' more years to live.'
        return result
    else:
        result = 'You will get the surprise of death as a SURPRISE!'
        return result

    
def fn_send_output_string(collected_inputs_dict):
    disc = death_simulator(collected_inputs_dict)
    data_dict = {
       'introduction': 'This is how you die...',
       'name': collected_inputs_dict['name'],
       'description': disc
    }
    input_pdf_path = '../docs/death_certificate_template.pdf'
    output_pdf_path = "../docs/death_certificate_{fname}.pdf".format(fname = data_dict['name'])
    print_death_cert.write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict)
    
    return data_dict
