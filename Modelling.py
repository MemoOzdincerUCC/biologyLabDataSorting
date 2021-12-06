import pandas as pd
from Counting import countSpecies

afterFire = pd.read_csv('data/AfterFire.csv')

beforeFire = pd.read_csv('data/BeforeFire.csv')

beforeFire.head()


# def cleanData(data):
#     data.dropna(subset=['scientific_name'], inplace=True)
#     data.drop(data[data['scientific_name'].str.split().str.len()
#               < 2].index, inplace=True)
#     # data.to_csv('data/AfterFireCleaned.csv')
#     data.to_csv('data/BeforeFireCleaned.csv')


# cleanData(afterFire)
# cleanData(beforeFire)

# For each dataframe, look at the "scientific_name" column and count how many of each there are.
# Create a new CSV file with the Scientific Name, the "common_name" from the original CSV file, and the count.
# Sort the new CSV file by the count.

# BeforeFireCleaned = pd.read_csv('data/BeforeFireCleaned.csv')
# AfterFireCleaned = pd.read_csv('data/AfterFireCleaned.csv')
# countSpecies(BeforeFireCleaned, 'BeforeFireCleaned')
# countSpecies(AfterFireCleaned, 'AfterFireCleaned')

CountedBeforeFireCleaned = pd.read_csv('CountedBeforeFireCleaned.csv')
CountedAfterFireCleaned = pd.read_csv('CountedAfterFireCleaned.csv')
