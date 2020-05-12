# Functional Specification

## Background
As humans, we are plagued with the knowledge that we will some day die.  This dread is one that is evolutionarily very useful in the sense that we put conscious effort in making decisions to reduce the chance of death, but it's also harmful in the dread and anxiety that it can produce.  Our goal is to put an end to this needless suffering.  Our goal is to cheat death of its surprise.  

How? What wonders of technology can be employed to achieve such a monumental task? Through the united powers of data, intuition, simulation, and a bit of good ole-fashioned made-up nonsense, our death simulator allows users to enter data about themselves and get the answer to when and how they'll shed their mortal coil. More pragmatically, users will enter their state, age, gender, race, and occupation, then our script will use CDC and labor fatality data to simulate each passing day—using random number generator to roll for if they die and how on that day.  With each passing day, the probability of death increases and the causes of death change.  

## User Profile
Users are folks in the US who want to have a laugh in seeing what their simulated date and cause of death are or who need to simulate how large populations will die for other projects.  They should be able to clone a Github repo and run an interactive Jupyter Notebook.

## Data Sources
* [Center for Disease Control Compressed Mortality File](https://www.cdc.gov/nchs/data_access/cmf.htm)
 * Latest data is from 2016 and has deaths by age, gender, race, and specific cause of death
* [Bureau of Labor Statistics Census of Fatal Occupational Injuries](https://www.bls.gov/iif/oshcfoi1.htm)
 * Data which gives the volume of deaths by occupation in the US

## Use cases
* For laughs:
 * Objective: be entertained by the results of your own personal simulated death forecast
  * Expected interactions: user inputs data about themselves into an interactive Jupyter Notebook widget and sees a print of the results
 * To simulate how populations die
  * Objective: for other projects, there may be a goal to simulate how larger groups of people or populations will die
   * Expected interactions: user inputs data about the population into a function which returns the dates and causes of deaths in a list