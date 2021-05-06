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

p_ds = 1/4
num_billboards = ncols = 2
#use n_trials from before
p_webdev = 3/4
# 1 = data science 0 = webdev

trials = np.random.choice([0,1], num_billboards*n_trials, p = [p_webdev, p_ds]).reshape(nrows,ncols)

(trials.sum(axis = 1) == 2).mean()

# 0.062329 percent chance that you drive 2 billboards with a data science student on them

# ---  4. ---
# Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. 
# If on monday the machine is restocked with 17 poptart packages, 
# how likely is it that I will be able to buy some poptarts on Friday afternoon?

# this assumes that Friday is a part of the day count (i.e. not stopping on Thursday)
n_days = ncols = 5

vending_results = np.random.normal(3, 1.5, nrows * ncols).reshape(nrows,ncols)

#sum of poptarts taken pre Friday
vending_results.sum(axis = 1)
#use <= 16 so that there's at least 1 whole pop tart left to buy < 17 would give you fraction of poptarts
vending_results.sum(axis = 1) <= 16

(vending_results.sum(axis = 1) <= 16).mean()

# 0.616912 chance that I can get at least a single poptart

# --- 5. ---
# Compare Heights
# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# If a man and woman are chosen at random, P(woman taller than man)?

#create two arrays of men heights and women heights
men = np.random.normal(178, 8, n_trials)
women = np.random.normal(170, 6, n_trials)

differences = women - men

(differences > 0).mean()

# there's a 0.211811 chance the woman is taller than a man


# --- 6. --- 
# When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. 
# What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?
p_corrupt = 1/250 
students = ncols =  50
p_notcorrupt = 249/250

installs = np.random.choice([0,1], nrows*ncols, p = [p_notcorrupt, p_corrupt]).reshape(nrows,ncols)
(installs.sum(axis=1) == 1).mean()

# - 0.164456 chance for 50 students

students2 = 100
installs = np.random.choice([0,1], nrows*students2, p = [p_notcorrupt, p_corrupt]).reshape(nrows,students2)
(installs.sum(axis = 1) == 1).mean()

# - 0.268968 chance for 100 students
# - in other words very very small chance 

# What is the probability that we observe an installation issue within the first 150 students that download anaconda?
students3 = 150
installs = np.random.choice([0,1], size = (nrows, students3), p = [p_notcorrupt, p_corrupt])
(installs.sum(axis = 1) == 1).mean()

# 0.330174 chance issue in first 150 students

# How likely is it that 450 students all download anaconda without an issue
students4 = 450
installs = np.random.choice([0,1], size = (nrows, students4), p = [p_notcorrupt, p_corrupt])
(installs.sum(axis = 1) == 0).mean()

# 0.164471 that all 450 students will download anaconda without an issue

# --- 7. ---
# There's a 70% chance on any given day that there will be at least one food truck at Travis Park. 
# However, you haven't seen a food truck there in 3 days. How unlikely is this?
p_foodtruck = .7
p_nofoodtruck = .3
days = ncols = 3

# 1 = at least one food truck. 0 = no food trucks
days_in_a_row = np.random.choice([0,1], size = (nrows, ncols), p = [p_nofoodtruck, p_foodtruck])
(days_in_a_row == 0).mean()

# 0.29993 chance of 3 days with no food truck

# How likely is it that a food truck will show up sometime this week?
# assuming week is 7 days (work and weekends) 
# does this mean 3 days no truck then yes truck? 

days = ncols = 7
days_in_a_row = np.random.choice([0,1], size = (nrows, ncols), p = [p_nofoodtruck, p_foodtruck])
(days_in_a_row >=1 ).mean()

# .70 chance food truck will show up sometime any week 

# --- 8. ---
# If 23 people are in the same room, what are the odds that two of them share a birthday? 
# What if it's 20 people? 40?

n_trials = nrows = 1_000_000
n_people = ncols = 23
days = 366
days_of_year = list(np.arange(1, days))

room_trials = np.random.choice(days_of_year, size = (nrows, n_people))

np.unique(room_trials[0])

# FOR LOOP DOES THIS: make list that has 1 for each time the value of unique people in a classroom is less than (aka not equal to) 23

# initalize empty list
shared_birthdays = []
# for loop loops through each row in the array (trial = room_trials[n])
for trial in room_trials:
    # np.unique ouputs a list of uniqe values in an array, check the length of this
    # if there no one shares a birthday the length of the list will be 23
    if len(np.unique(trial)) < 23: # <--- this could also be the variable n_people
        # add 1 to the empty list (in a later example I just use a variable and do variable += 1 instead)
        shared_birthdays.append(1)

# the probability that someone shares a birthday is how many times there were shared birthdays over how many trials
p_shared_birthdays = len(shared_birthdays)/n_trials
p_shared_birthdays

# %50.7 percent people share a birthday in a class of 23

n_people20 = 20

trials2 = np.random.choice(days_of_year, size = (nrows, n_people20))
shared_birthdays2 = 0
for trial in trials2:
    if len(np.unique(trial)) != n_people20:
        shared_birthdays2 += 1

p_shared_birthdays = shared_birthdays2 / n_trials

# 41% people share a birthday, in a room of 20 people

n_people40 = 40
trials3 = np.random.choice(days_of_year, size = (nrows, n_people40))
shared_birthdays3 = 0
for trial in trials3:
    if len(np.unique(trial)) != n_people40:
        shared_birthdays3 += 1

p_shared_birthdays = shared_birthdays3 / n_trials

# 89.1786% chance people share a birthday in a room of 40 people