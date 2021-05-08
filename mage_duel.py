# Mage Duel!
# Let's use what we've learned to play a mage duel!
import numpy as np
import pandas as pd
import seaborn as sns

# Imagine your wizard has 6d4 health points and you have spells that do 6d4 damage. "6d4" means rolling six 4-sided dice and summing the result.
# Create 4 sided die 
# simulate rolling it 6 times

die_4 = [1, 2, 3, 4]


# Your opposing mage has 4d6 health points and spells that do 4d6. "4d6" means rolling four six-sided dice and summing the result.
# create 6 sideded die 
die_6 = [1, 2, 3, 4, 5, 6]

# Exercises
# Simulate mage duels to answer who is the more powerful mage?
duels = 10

# Before running simulations, do you have a hypothesis of which mage will win? Do you have a hunch? Write it down. This is your first exercise.
# ---  I believe the mage will win more often. it seems like he has a higher chance of getting higher numbers with 6 die to pull from
# --- my second guess is that they'll be about the same 

# Simulate 10 mage duels. Is there a clear winner? Run that 10 duel simulation again. Was the answer similar?

wizards = np.random.choice(die_4, 10 * 6).reshape(10, 6)
wizard_rolls = wizards.sum(axis=1)

mage = np.random.choice(die_6, 10 * 4).reshape(10,4)
mage_rolls = mage.sum(axis=1)

(wizard_rolls > mage_rolls).mean()

#Trial 1 -- Wizard won 70% of the time
#Trial 2 -- Wizard won 70% of the time
#Trial 3 -- Wizard won 50% of the time

# Do the results change much at 100 duels?
wizards = np.random.choice(die_4, 100 * 6).reshape(100, 6)
wizard_rolls = wizards.sum(axis=1)

mage = np.random.choice(die_6, 100 * 4).reshape(100,4)
mage_rolls = mage.sum(axis=1)

(wizard_rolls > mage_rolls).mean()
# Trial 1 -- wizard won 54% of the time
# Trial 2 -- wizard won 51% of the time

# Now, simulate 10,000 mage duels. Is there a clear winner?
wizards = np.random.choice(die_4, 10000 * 6).reshape(10000, 6)
wizard_rolls = wizards.sum(axis=1)

mage = np.random.choice(die_6, 10000 * 4).reshape(10000,4)
mage_rolls = mage.sum(axis=1)

(wizard_rolls > mage_rolls).mean()

# Wizard won 54.3% of the time
# the clear winner is my Wizard, which I did not expect (knowing nothing about DnD). 
# I say clear but he won only a little bit more than 50% of the time (which was close to my guess #2)
# Wizards > Mages 

