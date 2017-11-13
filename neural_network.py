#!/usr/bin/python

import numpy as np
import pandas as pd
import csv

# Get training data
dataFile = pd.read_csv('letter-recognition.data.txt',header=None)
y = dataFile.loc[:,0]
x = dataFile.loc[:,1:]
print(x)