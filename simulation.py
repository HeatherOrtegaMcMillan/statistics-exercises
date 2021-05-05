# statistics exercises
%matplotlib inline
import numpy as np
import pandas as pd
np.random.seed(1349)

# 1. How likely is it that you roll doubles when rolling two dice?
n_trials = nrows = 10 ** 6
n_rolls = ncols = 2
die = [1,2,3,4,5,6]

all_rolls = np.random.choice(die, n_trials*n_rolls).reshape(nrows,ncols)

# figure out how to apply this, all_rolls[n][0] == all_rolls[n][1]
# compares first element to second element if same == True

# turn to dataframe and use a lambda function to apply above logic then take mean
pd.DataFrame(all_rolls).apply(lambda x: x[0] == x[1], axis = 1).mean()
# 0.166 chance of rolling doubles



