# Indexed Liklihood and Probability Converter
'''
This script converts the Bureau of Labor Statistics (BLS)
occupational_hazards_data.csv dataset into an index of likelihoods to die by
each occupation and converts the Center for Disease Control (CDC)
deaths_age_gender_race_mechanism_cause.csv dataset into annual probabilities of
death by age, gender, and race.
'''

import pandas as pd
import numpy as np

JOB_DEATHS = pd.read_csv("../data/occupational_hazards_data.csv")
CDC_DEATHS = pd.read_csv("../data/deaths_age_gender_race_mechanism_cause.csv")

# Cleaning the BLS data
'''
First, the data needs to be subset to the highest hierarchy level (level 0)
since lower hierarchy levels provide too many options from which the user needs
to choose (i.e. a dropdon menu of 200+ occupations is too many).  Level 0
provides 21 occupations and is hence, much more reasonable and less frustrating
for the user to select from.
'''

JOB_DEATHS = JOB_DEATHS[JOB_DEATHS['hierarchy_level'] == 0]

# With subsetting complete, the hierarchy levels are no longer needed.
del JOB_DEATHS['hierarchy_level']

# Currently, population is a string with commas and needs to be converted to
# an integer for calculations.
JOB_DEATHS.population = JOB_DEATHS.population.str.replace(',', '').astype('int')

# Because we're only interested in the indexed liklihood of dying by occupation,
# we won't need the occupation == 'Total' rows.
JOB_DEATHS = JOB_DEATHS[JOB_DEATHS.occupation != 'Total']


# Creating the Indexed Likelihood of Death by occupation
'''
At this point, we'll want to split the data into two tables where the first will
be used to augment the probability of death and the second will be used to
augment the mechanism of death if death occurs.
1. `job_indexed_liklihood`: A table which has the total deaths and population
    for each occupation
2. `job_mechanism_indexed_likelihood`: A table which has the non-total deaths
    and population for each mechanism

`job_indexed_liklihood` will be used to create the indexed likelihood of dying
by occupation and `job_mechanism_indexed_likelihood` will be used to modulate
the probability of dying by a specific mechanism once the dice roll for death
occurs. This section covers creating `job_indexed_liklihood`.
'''

JOB_INDEXED_LIKELIHOOD = JOB_DEATHS[JOB_DEATHS.mechanism_of_death == 'Total']

# express deaths and population as a ratio before generating indexed values
JOB_INDEXED_LIKELIHOOD['deaths_per_capita'] = JOB_INDEXED_LIKELIHOOD.deaths / \
    JOB_INDEXED_LIKELIHOOD.population

# divide by the mean to produce index
JOB_INDEXED_LIKELIHOOD['indexed_likelihood'] = JOB_INDEXED_LIKELIHOOD.deaths_per_capita /\
    np.mean(JOB_INDEXED_LIKELIHOOD.deaths_per_capita)


# Creating the CDC Annual Death Probabilities by Age, Gender, and Race
'''
As with the BLS data, we'll split the CDC data into two datasets where the first
will be used to determine the overall probability of death and the second will
be used to determine the mechanism and cause of death if death occurs.

1. `ANNUALDEATHPROBS_AGE_GENDER_RACE` is, as the name suggests, the probability
    of dying within a year based on age, race, and gender.
2. `ANNUALCAUSEOFDEATHPROBS_AGE_GENDER_RACE` is the annual probability of each
    cause and related mechanism of death given that death occurs within a
    specific age, gender, and race.

This section covers the creation of `ANNUALDEATHPROBS_AGE_GENDER_RACE`
'''

# In order to convert to annual probabilities, we'll want to group deaths on
# age, gender, race, and population, then divide by the population in that grouping.

ANNUALDEATHPROBS_AGE_GENDER_RACE =\
    CDC_DEATHS.groupby(['age', 'gender', 'race', 'population'], as_index=False).sum()

ANNUALDEATHPROBS_AGE_GENDER_RACE['annual_death_prob'] = ANNUALDEATHPROBS_AGE_GENDER_RACE.deaths /\
                                                    ANNUALDEATHPROBS_AGE_GENDER_RACE.population

# Finally, to tidy up, we can remove the population and deaths columns since
# they won't be needed by the death simulator now that we have probability.

ANNUALDEATHPROBS_AGE_GENDER_RACE = ANNUALDEATHPROBS_AGE_GENDER_RACE.drop(\
    ['population', 'deaths'], axis=1)


# Creating the CDC Annual Cause of Death Probabilities by Age, Gender, and Race
ANNUALCAUSEOFDEATHPROBS_AGE_GENDER_RACE = CDC_DEATHS.copy()
'''
Here, population doesn't matter since that field is only used for calculating
the probability of death (used in `ANNUALDEATHPROBS_AGE_GENDER_RACE`).  Instead,
we'll want to know: for those who died, what percent died by each cause.  This
being the case, we can drop population and calculate the cause of death
probability within the age/gender/race combination.
'''
del ANNUALCAUSEOFDEATHPROBS_AGE_GENDER_RACE['population']
ANNUALCAUSEOFDEATHPROBS_AGE_GENDER_RACE = \
    ANNUALCAUSEOFDEATHPROBS_AGE_GENDER_RACE.assign(cause_of_death_prob=\
        ANNUALCAUSEOFDEATHPROBS_AGE_GENDER_RACE.deaths /\
            ANNUALCAUSEOFDEATHPROBS_AGE_GENDER_RACE.groupby(\
                ['age', 'gender', 'race']).deaths.transform('sum'))

# The final step is removing the unneeded deaths column.
del ANNUALCAUSEOFDEATHPROBS_AGE_GENDER_RACE['deaths']

# write results to .csv
JOB_INDEXED_LIKELIHOOD.to_csv('../data/JOB_INDEXED_LIKELIHOOD.csv', index=False)
ANNUALDEATHPROBS_AGE_GENDER_RACE.to_csv(\
    '../data/ANNUALDEATHPROBS_AGE_GENDER_RACE.csv', index=False)
ANNUALCAUSEOFDEATHPROBS_AGE_GENDER_RACE.to_csv(\
    '../data/ANNUALCAUSEOFDEATHPROBS_AGE_GENDER_RACE.csv', index=False)
