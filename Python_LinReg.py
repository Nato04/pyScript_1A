#!/usr/bin/env python

# Module Loading
print("Loading Modules")
print()

import os
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import sys

# Data input - Filename via sys argument

print("Importing CSV Data")
print()

if len(sys.argv) < 2:
    print("Filename missing from command line")
    sys.exit(-1)

filename = sys.argv[1]

base,ext = os.path.splitext(filename)

print("Loading dataset {}".format(filename))
print()

answer = input('Is this filename correct: [y/n]: ')
if not answer or answer[0].lower() != 'y':
    print('Program will now abort')
    sys.exit(-1)

# Use read_csv() to read regex1.csv File¶

dataset = pd.read_csv(filename)
print (dataset)

# Creating Scatterplot of data, user will be asked for filename 
plt.scatter(dataset[['x']], dataset [['y']], color = 'red')
plt.title("Y over X for {}".format(filename))
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
figlabel = input('Provide a filename for scatterplot: ')
plt.savefig("{}.png".format(figlabel))

# Fitting Linear Regression to the Dataset¶

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[['x']], dataset[['y']])
# Adjusted R-Square readout¶
model.score(dataset[['x']], dataset[['y']])

# Creating Scatterplot with linear regressino model, user will be asked for filename
plt.scatter(dataset[['x']], dataset [['y']], color = 'red')
plt.plot(dataset[['x']], model.predict(dataset[['x']]), color = 'blue')
plt.title('Y over X')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
figlabel1 = input('Provide a filename for linear regression model: ')
plt.savefig("{}.png".format(figlabel1))