# Death Simulator
Team: Thomas Winegarden, James Lee, Aniruddha Dutta, Will Wright | Course project for DATA 515 in the UW MSDS program
### Background:
As humans, we are plagued with the knowledge that we will some day die.  This dread is one that is evolutionarily very useful in the sense that we put conscious effort in making decisions to reduce the chance of death, but it's also harmful in the dread and anxiety that it can produce.  Our goal is to put an end to this needless suffering.  Our goal is to cheat death of its surprise.  

How? What wonders of technology can be employed to achieve such a monumental task? Through the united powers of data, simulation, and a bit of good ole-fashioned made-up nonsense, our death simulator allows users to enter data about themselves and get the answer to when and how they'll shed their mortal coil. More pragmatically, users will enter their state, age, gender, race, and occupation, then our script will use Center for Disease control mortality data and Bureau of Labor Statistics occupational fatality data to simulate each passing day—using random number generator to roll for if they die and how on that day.  With each passing day, the probability of death increases and the causes of death change.  

### Organization of the project

```
death_simulator/
  |- README.md
  |- death_simulator/
     |- death_simulator/
        |-print_death_cert.py
        |-probability_converter.py
        |-death_simulator.py
        |-create_death_data.py
        |-interactive_frontend.ipynb
   |- tests/
     |-...
  |-data
     |-annualCauseOfDeathProbs_age_gender_race.csv
     |-annualDeathProbs_age_gender_race.csv
     |-job_indexed_likelihood.csv
     |-deaths_age_gender_race_mechanism_cause.csv
     |-occupational_hazards_data.csv
  |- data_raw
     |-mortality_ages0-10.txt
     |-mortality_ages11-15.txt
     |-...  
  |- doc/
     |- FunctionalSpec
     |- Designspec
     |- Projectplan
     |- TechnologyReview
     |-Final presentation
  |- setup.py
  |- LICENSE
  |- requirements.txt
```

	
