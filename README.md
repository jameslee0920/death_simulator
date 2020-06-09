# Death Simulator
Team: Thomas Winegarden, James Lee, Aniruddha Dutta, Will Wright | Course project for DATA 515 in the UW MSDS program
### Background:
As humans, we are plagued with the knowledge that we will some day die.  This dread is one that is evolutionarily very useful in the sense that we put conscious effort in making decisions to reduce the chance of death, but it's also harmful in the dread and anxiety that it can produce.  Our goal is to put an end to this needless suffering.  Our goal is to cheat death of its surprise.  

How? What wonders of technology can be employed to achieve such a monumental task? Through the united powers of data, simulation, and a bit of good ole-fashioned made-up nonsense, our death simulator allows users to enter data about themselves and get the answer to when and how they'll shed their mortal coil. More pragmatically, users will enter their state, age, gender, race, and occupation, then our script will use Center for Disease control mortality data and Bureau of Labor Statistics occupational fatality data to simulate each passing day—using random number generator to roll for if they die and how on that day.  With each passing day, the probability of death increases and the causes of death change.  

### Organization of the project

[TODO: update with final directory structure] The project has the following repository structure:  

```
death_simulator/
  |- README.md
  |- death_simulator/
     |- data/
        |-Merged_Data.csv
        |-Database_HousePrice.py
     |- html_landing_page/ 
        |- ...
     |- Scripts/
        |-part1_predict_price.py
        |-part2_bid_price.py
        |-part3_monthly_cost.py
        |-house_price_model_2
     |- tests/
        |- ...
  |- examples
     |- User_Guide
  |- logos
     |- logo_v1  
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
### Installation

[TODO: update with actual steps] To install FirstStop perform following steps:

* clone the repo: git clone https://github.com/sliwhu/UWHousingTeam
* run the setup.py file: python setup.py install
* run requirements.txt to ensure all dependencies exist : pip install -r requirements.txt
* go to Scripts folder: cd UWHousing/Scripts
* properly set data path os.environ ["SALES_DATA_PATH"](\UWHousingTeam\data) and 
  os.environ["SALES_DATA_FILE"] ('Merged_Data.csv') follow instructions in the house_price_model_2.py file
* run bokeh server: bokeh serve --port 5001 part1_predict_price.py
* Open another terminal and go to Scripts folder: cd UWHousing/Scripts
* run bokeh server: bokeh serve --port 5002 part2_bid_price.py
* Open another terminal and go to Scripts folder: cd UWHousing/Scripts
* run bokeh server: bokeh serve --port 5003 part3_monthly_cost.py
* go to landing page http://housing-prediction.azurewebsites.net/UWHousingTeam/html_landing_page/
* follow the User_Guide in examples folder 
	
