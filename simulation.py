# statistics exercises
%matplotlib inline
import numpy as np
import pandas as pd
np.random.seed(1349)

# --- 1. --- 
# How likely is it that you roll doubles when rolling two dice?
n_trials = nrows = 10 ** 6
n_rolls = ncols = 2
die = [1,2,3,4,5,6]

all_rolls = np.random.choice(die, n_trials*n_rolls).reshape(nrows,ncols)

# figure out how to apply this, all_rolls[n][0] == all_rolls[n][1]
# compares first element to second element if same == True

# turn to dataframe and use a lambda function to apply above logic then take mean
pd.DataFrame(all_rolls).apply(lambda x: x[0] == x[1], axis = 1).mean()
# 0.166 chance of rolling doubles

# --- 2.--- 
# If you flip 8 coins, what is the probability of getting exactly 3 heads? 
# What is the probability of getting more than 3 heads?
n_trials = nrows = 10 ** 6
n_flips = ncols = 8
# heads is 1 tails is 0
coin = [0, 1]

coin_flippys = np.random.choice(coin, n_trials*n_flips).reshape(nrows, ncols)

(coin_flippys.sum(axis = 1) == 3).mean()
# 0.218688 chance of getting exactly 3 heads

(coin_flippys.sum(axis = 1) > 3).mean()
# 0.636872 chance of getting more than 3 heads


# --- 3. ---
# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. 
# Assuming that Codeup randomly selects an alumni to put on a billboard, 
# what are the odds that the two billboards I drive past both have data science students on them?

p_ds = 1/3
num_billboards = ncols = 2
#use n_trials from before
p_webdev = 2/3
# 1 = data science 0 = webdev

trials = np.random.choice([0,1], num_billboards*n_trials, p = [p_ds, p_webdev]).reshape(nrows,ncols)

(trials.sum(axis = 1) == 2).mean()

# 0.443073 percent chance that you drive 2 billboards with a data science student on them

# ---  4. ---
# Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. 
# If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?