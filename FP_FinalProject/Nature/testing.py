import math
import pandas as pd
import os
import numpy 
import matplotlib
import csv

csvFile = pd.read_csv('/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/FP_FinalProject/Nature/testdata.csv')
# print(csvFile)

df = pd.DataFrame(csvFile)
df.to_csv(r'/Users/lorenzor.bartolo/Desktop/FALL_20/CS_151_001/FP_FinalProject/Nature/write.csv', index = False)

print('Done...')