import datetime
import pandas as pd


c = 3
d = 7.9
e = "Windsor Election Result"
f = True 
g = 2021-12-31

# What are the datatypes of our variable?
type (g)

# Printing datetime using the Python datetime library

import datetime

g = datetime.datetime(2021, 12, 31)

print (g)

# Loading the csv file from open website of Windsor
dataframe = pd.read_csv("https://opendata.citywindsor.ca/Uploads/detailedresults-2018.csv" , encoding='unicode_escape')

# dataframe = pd.read_excel("https://opendata.citywindsor.ca/Uploads/Election2014.xlsx" , encoding='unicode_escape')

# What type is our variable named dataframe?
type(dataframe)

# How many records (rows) and attributes (columns) did we load?
print(dataframe.shape)

# What type of data did Python auto-detect?
print(dataframe.dtypes)

# What does the top and bottom of my tabular dataframe look like?
print(dataframe.head)

# If we want to see the top 3 rows we use arguments 
print(dataframe.head(3))

# If we want to see the bottom 3 rows we use arguments
print(dataframe.tail(3))

# Using Slicing to get the rows 9 to row 15
print(dataframe[9:16])

# Counting the frequency/ number of different types of Contest Titles are present in dataframe
print(dataframe["Contest Title"].value_counts())

# Picking the rows based on condition whether the candidate is electing for Mayor or not and moving them to a new dataframe
df = dataframe[dataframe['Contest Title'] == 'MAYOR']

print(df.shape)

# Who are the candidates? We find the Unique Candidates and filter out all the rest 
print(pd.unique(df['Candidate Name']))

# Grouping the candidates up for election and their respective votes in Descending order
total_votes=df.groupby(["Candidate Name"])["Total"].sum().sort_values(ascending=False)

print(total_votes)
