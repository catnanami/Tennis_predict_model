**There is Everything you need to reproduce our work**<br>
# Prerequisites
+ matplotlib>=3.7.1
+ numpy>=1.23.5
+ pandas>=2.0.2
+ torch>=2.0.1
+ sklearn>=0.0.post5


# Contents
## tennis_model.ipynb
This file implements the LSTM model.<br>
You should set the parameter `filename` before running the code to determine the .csv file to be parsed.<br>
```python
#you can change the path of .csv file here
  pathname=" "
```
## C_Wimbledon_featured_matches.csv
The original data to train and evaluate our model.

## new_C_Wimbledon_featured_matches.csv
The data based on women tennis match to test the model's generalization ability.

## Wald-Wolfowitz_Runs_Test.py
the model to evaluate the coherence between different indicators. 

