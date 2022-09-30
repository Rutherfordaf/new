# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:03:00 2022

@author: arutherford
"""

#Load reloaded datasets from seaborn
import matplotlib.pyplot as plt
import seaborn as sns
sns.get_dataset_names()

iris = sns.load_dataset('iris')
brain_networks = sns.load_dataset('brain_networks')
mpg = sns.load_dataset('mpg')

#all different preloaded SNS datasets
anagrams= sns.load_dataset('anagrams')
anscombe= sns.load_dataset('anscombe')
attention= sns.load_dataset('attention')
brain_networks= sns.load_dataset('brain_networks')
car_crashes= sns.load_dataset('car_crashes')
diamonds= sns.load_dataset('diamonds')
dots= sns.load_dataset('dots')
dowjones= sns.load_dataset('dowjones')
exercise= sns.load_dataset('exercise')
flights= sns.load_dataset('flights')
fmri= sns.load_dataset('fmri')
geyser= sns.load_dataset('geyser')
glue= sns.load_dataset('glue')
healthexp= sns.load_dataset('healthexp')
iris= sns.load_dataset('iris')
mpg= sns.load_dataset('mpg')
penguins= sns.load_dataset('penguins')
planets= sns.load_dataset('planets')
seaice= sns.load_dataset('seaice')
taxis= sns.load_dataset('taxis')
tips= sns.load_dataset('tips')
titanic= sns.load_dataset('titanic')

titanic.count('age')

#list of preloaded
#['anagrams',
 #'anscombe',
 #'attention',
# 'brain_networks',
# 'car_crashes',
# 'diamonds',
# 'dots',
# 'dowjones',
# 'exercise',
# 'flights',
# 'fmri',
# 'geyser',
# 'glue',
# 'healthexp',
# 'iris',
# 'mpg',
# 'penguins',
# 'planets',
# 'seaice',
# 'taxis',
# 'tips',
# 'titanic']




#Seaborn plot with mpgs
sns.scatterplot(x = 'Date', y = 'Extent', data = seaice)

#boxplot with titles
sns.boxplot(x= 'origin', y = 'weight', data = mpg)
plt.title('Weight vs Country')
plt.ylabel('Weight (lbs.)')
plt.xlabel('Country of Origin')

sns.lineplot(x = 'Date', y = 'Price', data = dowjones)


