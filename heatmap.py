# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 09:42:13 2022

@author: arutherford
"""

# Import Matplotlib and Seaborn
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


data2 = pd.read_table('https://raw.githubusercontent.com/pine-bio-support/DataScience/main/Final_cell_lines_RNA-expression_FPKM_values_1000genes_with_NA.txt')
data2.head()
data2.describe()



# Load the example flights dataset and convert to long-form
flights_long = sns.load_dataset("flights")
flights_long.head()
flights = flights_long.pivot("month", "year", "passengers")
flights.head()

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5)


