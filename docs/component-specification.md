# Component Specification

## Software Components
![component-specification](component-specification_death-simulator.png)

* Data Wrangler: Converts raw mortality data from the CDC and BLS into a cleaned and joined dataset
* Probability Converter: Converts annual volumes into smoothed daily probabilities of death
* Death simulator: rolls for death on a daily basis given user input and outputs cause of death and date
* Interactive User Interface: An interactive ipywidget which allows the user to interact intuitively with the simulator and get simulation results
* Mass Death Module: For users who want to simulate more deaths, a module with a function that allows many simulations to be run at once and outputs a paired list of the results for dates and causes of death.

## Interactions

User does x, y, z, then:
* The Data Wrangler interacts with the Probability Converter by delivering a cleaned dataset of annual death volumes
* The Probability Converted interacts with the Death Simulator by providing the dataset to use as a lookup for the daily death rolls
* The Interactive User Interface interacts with the Death Simulator by passing along user input to the simulator and receiving and presenting the results
* The Mass Death Module interacts with the death simulator by passing it parameters concerning larger populations and receives a list of results in response.


## Preliminary Plan
1. Finish data cleaning and joining for the Data Wrangler
2. Build the Probability Converter
3. Build the Death Simulator
4. Use ipywidgets to create an interactive user interface
5. Create a separate .py module which uses the death simulator, but at scale