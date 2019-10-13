import pandas as pd

pd.read_csv('file.csv', header=None)
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)


fruit_sales = pd.DataFrame({'Apples':[35,41],'Bananas':[21,34]}, index=['2017 Sales', '2018 Sales'])

pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# First row
first_row = reviews.iloc[0]
6
# First description
first_descriptions = reviews.description.iloc[:10]
reviews.loc[:9, "description"]

pd.read
# Some lines
sample_reviews = reviews.iloc[[1,2,3,5,8]]

# Some lines and columns
df = reviews.loc[[0,1,10,100],['country', 'province', 'region_1', 'region_2']]

# Create a variable `df` containing the `country` and `variety` columns of the first 100 records. 
df = reviews.loc[0:99, ['country', 'variety']]

# Create a DataFrame `italian_wines` containing reviews of wines made in `Italy`
italian_wines = reviews.loc[reviews.country == 'Italy']

#Create a DataFrame `top_oceania_wines` containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.
top_oceania_wines = reviews.loc[((reviews.country == 'Australia') | (reviews.country == 'New Zealand')) & (reviews.points >= 95)]

# SUMMARY AND MAPS
# Describe 
reviews.points.describe()
reviews.taster_name.describe()

# One column
reviews.points.mean()

#To see a list of unique values we can use the unique function:
reviews.taster_name.unique()

# VALUE COUNTS ----------------------------
#To see a list of unique values and how often they occur in the dataset, we can use the value_counts method:
reviews.taster_name.value_counts()

#suppose that we wanted to remean the scores the wines recieved to 0. We can do this as follows:
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

#DataFrame.apply is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
#If we had called reviews.apply with axis='index', then instead of passing a function to transform each row, we would need to give a function to transform each column.

#pandas will also understand what to do if we perform these operations between Series of equal length. For example, an easy way of combining country and region information in the dataset would be to do the following:
reviews.country + " - " + reviews.region_1

#Create a variable `bargain_wine` with the title of the wine with the highest points-to-price ratio in the dataset.
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

#Create a Series `descriptor_counts` counting how many times each of these two words appears in the `description` column in the dataset.
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

#Create a series `star_ratings` with the number of stars corresponding to each review in the dataset.
def rating(row):
    if row.country == 'Canada' or row.points >= 95: return 3
    elif row.points >= 85: return 2
    else: return 1

star_ratings = reviews.apply(rating, axis='columns')

# Grouping and sorting
import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# We can replicate what value_counts does using groupby by doing the following:
reviews.groupby('points').points.count()
reviews.groupby('points').size()

reviews.groupby('points').price.min()

#Create a `Series` whose index is reviewers and whose values is the average review score given out by that reviewer.
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
#use the `describe()` method to see a summary of the range of values.
reviewer_mean_ratings.describe()

#here's one way of selecting the name of the first wine reviewed from each winery in the dataset:
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

#here's how we would pick out the best wine by country and province:
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

#we can generate a simple statistical summary of the dataset as follows:
reviews.groupby(['country']).price.agg([len, min, max])

#in general the MultiIndex method you will use most often is the one for converting back to a regular index, the reset_index method:
countries_reviewed.reset_index()

#To get data in the order want it in we can sort it ourselves. The sort_values method is handy for this.
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')

countries_reviewed.sort_values(by='len', ascending=False)

#What combination of countries and varieties are most common? Sort the values in the `Series` in descending order based on wine count.
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)

#To sort by index values, use the companion method sort_index. This method has the same arguments and default order:
countries_reviewed.sort_index()

#Finally, know that you can sort by more than one column at a time:
countries_reviewed.sort_values(by=['country', 'len'])

# TYPES
# You can use the `dtype` property to grab the type of a specific column:
reviews.price.dtype
reviews.dtypes # all columns

# It's possible to convert a column of one type into another wherever such a conversion makes sense by using the `astype` function
reviews.points.astype('float64')

# A `DataFrame` or `Series` index has its own `dtype`, too:
reviews.index.dtype

# To select `NaN` entreis you can use `pd.isnull` (or its companion `pd.notnull`)
reviews[reviews.country.isnull()]
# How many isnull? 
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()

# we can simply replace each `NaN` with an `"Unknown"`:
reviews.region_2.fillna("Unknown")

# Replacing
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

# RENAME AND COMBINING
# rename() lets you change index names and/or column names. For example, to change the points column in our dataset to score
# Column
reviews.rename(columns={'points': 'score'})
# Index
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
