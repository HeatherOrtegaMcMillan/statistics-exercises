# ------ Simulating Chuck a Luck ------
# "Pay a Buck and Chuck-a-Luck"
# Chuck-a-Luck is a game of chance often associated with charity fundraisers or street gambling rather than casinos.
# To play, the House says, "Pay $1, pick a number and roll 3 dice. If any of those dice come up, you'll win $1, $2, or $3".
# "It's even odds", they say, "because the probability of rolling your number is 1/6 and you get to roll 3 dice! 1/6 + 1/6 + 1/6 is 3/6 which is 1/2".
# You know better than this, so it's time to make an experiment to approximate the actual risk and payoff...

# Rules:
# The player pays $1 to play and picks a number.
# The House rolls 3 dice at once.

# Payouts:
# $3 if all three dice match the chosen number
# $2 if exactly two dice match the chosen number
# $1 is exactly one of the dice matches the chosen number
# If none of the dice match the player's chosen number, then the House keeps the $1.

# Exercises:
import numpy as np
import pandas as pd
die = [1, 2, 3, 4, 5, 6]
rolls = ncols = 3
trials = nrows = 1_00_000
sim1 = np.random.choice(die, rolls*trials).reshape(nrows, ncols)
# What are your chances of getting an outcome payout of $2? (where we earned $3 on the $1 ante)
# should be close to 1/36 which is a .27% chance (the theoretical probability)
# we're going to guess 1 as our number
# to check sum of all elements needs to be 3
win2 = (sim1.sum(axis = 1) == 3).mean()
# ------ 0.45%  chance 

# What are your chances of getting an payout of $1?
# create true false values for 1s 
rows_with_ones = (sim1 == 1) 
# count up the true values
true_values = rows_with_ones.sum(axis = 1)
# if true value count is == 2 for rolling exactly 2 ones return true
# this is all the trials where we rolled exactly 2 ones
true_values == 2
# take mean of that return
win1 = (true_values == 2).mean()


#------ ~6.88% chance of getting a payout of 1 (rolling 2 of the same die)

# pd.DataFrame(rolls).apply(lambda row: 3 in row.values, axis =1).mean()

# What are your chances of getting a payout of $0 where you ante $1 and win $1?
# Do the same type of check as the question above use 1 true value this time
true_values == 1
win0 = (true_values == 1).mean()

# ------ ~34.6% chance of ggetting a payout of $0

# What are your chances of getting a payout of -$1 where you ante up, but don't win anything?
true_values == 0
lose = (true_values == 0).mean()
# ------ ~58.08% of losing money

# What is the average cost/gain per game? (think of averaging the total payout calculation across all simulations)

# Chart out a histogram of all the outcomes of those 1,000,000 games

# Is this really a fair game of 1/6 + 1/6 + 1/6 odds?

# If you play 1,000,000 games in a row, what are your winnings/losses?