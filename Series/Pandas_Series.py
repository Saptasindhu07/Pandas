import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

country=["India","Pakistan","Bangladesh","China","Mongolia"]

countries=pd.Series(country,index=["Best","Jongi","Jongi 2.O","Chor","OogaBooga ahh Land"],name="Country Table")
print(countries)
### Same can be done from dictionary

###Attributes

print(countries.size)
print(countries.name)
print(countries.is_unique)
print(countries.index)
print(countries.values)

subscribers=pd.read_csv('Pandas\Series\datasets-session-16\subs.csv')
print(type(subscribers))
print(type(subscribers.squeeze())) ### Squeeze turns the Pandas Dataframe to Pandas Series

print(subscribers)

vk_score=pd.read_csv("Pandas\Series\datasets-session-16\kohli_ipl.csv",index_col='match_no')
vk_score2=vk_score.squeeze()
print(vk_score2.head(100)) ###head gives that number of elements from the top
print(vk_score2.tail(10))  ###tail gives that number of elements from the bottom


bolllywood=pd.read_csv("Pandas\Series\datasets-session-16\Bollywood.csv",index_col="movie")
bolllywood2=bolllywood.squeeze()
print(bolllywood2)

print(bolllywood2.value_counts()) ### Counts the number of times a value occurs in the list 

print(bolllywood2.sort_values(ascending=True,inplace=False))     ### implace makes changes to target panda series
print(bolllywood2.sort_index(ascending=True,inplace=False))     


### Count - number of non null values 
### mean, median, mode, sum, product, standard variation, variance
### min/max/ describe

print(bolllywood.describe())

''' series indexing, slicing, fancy indexing'''
print(bolllywood2[0])

test_series=pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(test_series[2:19:2])
print(test_series[[1,2,3,4,5,6,7,8,9,10]]) ##Fancy indexing

###Looping same as arrays and numpy

###Boolean indexing 
print(vk_score2[vk_score2>50].sort_values()) #number of matches VK has scored more than 50


###Plotting Graphs 
vk_score2[::10].plot(kind='bar')
plt.show()