import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
print("Setup Complete")

# Set up code checking
# import os
# if not os.path.exists("../input/museum_visitors.csv"):
#     os.symlink("../input/data-for-datavis/museum_visitors.csv", "../input/museum_visitors.csv") 
# from learntools.core import binder
# binder.bind(globals())
# from learntools.data_viz_to_coder.ex2 import *
# print("Setup Complete")

# Path of the file to read
museum_filepath = "../input/museum_visitors.csv"

# Fill in the line below to read the file into a variable museum_data
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)


# Imprimir coluna
print(museum_data.columns)

# Add label for horizontal axis
plt.xlabel("Date")

# LINEAR CHART-----------------------------------
# Set the width and height of the figure
plt.figure(figsize=(12,6))
# Line chart showing the number of visitors to each museum over time
sns.lineplot(data=museum_data)
# Add title
plt.title("Monthly Visitors to Los Angeles City Museums")


flight_data = None

# BAR CHART--------------------------------------
# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")


# HEAT MAP---------------------------------------
# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)

# Add label for horizontal axis
plt.xlabel("Airline")




insurance_data = None

# SCATTER PLOT 
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# REGRESSION LINE
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# COLORIZE BY ANOTHER DATA INPUT
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])

# TWO REGRESSION LINES COMPARISON
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)

# SWARMPLOT - AGRUPA POR TIPO (caso eixo X seja um SIM/NAO)
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])






# Histogram 
sns.distplot(a=iris_data['Petal Length (cm)'], kde=False)

# KDE plot - you can think of it as a smoothed histogram.
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)

# 2D KDE plot
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")



# Histograms for each species
sns.distplot(a=iris_set_data['Petal Length (cm)'], label="Iris-setosa", kde=False)
sns.distplot(a=iris_ver_data['Petal Length (cm)'], label="Iris-versicolor", kde=False)
sns.distplot(a=iris_vir_data['Petal Length (cm)'], label="Iris-virginica", kde=False)

# Add title
plt.title("Histogram of Petal Lengths, by Species")

# Force legend to appear
plt.legend()



'''
Since it's not always easy to decide how to best tell the story behind your data, we've broken the chart types into three broad categories to help with this.

Trends - A trend is defined as a pattern of change.
sns.lineplot - Line charts are best to show trends over a period of time, and multiple lines can be used to show trends in more than one group.

Relationship - There are many different chart types that you can use to understand relationships between variables in your data.
sns.barplot - Bar charts are useful for comparing quantities corresponding to different groups.
sns.heatmap - Heatmaps can be used to find color-coded patterns in tables of numbers.
sns.scatterplot - Scatter plots show the relationship between two continuous variables; if color-coded, we can also show the relationship with a third categorical variable.
sns.regplot - Including a regression line in the scatter plot makes it easier to see any linear relationship between two variables.
sns.lmplot - This command is useful for drawing multiple regression lines, if the scatter plot contains multiple, color-coded groups.
sns.swarmplot - Categorical scatter plots show the relationship between a continuous variable and a categorical variable.

Distribution - We visualize distributions to show the possible values that we can expect to see in a variable, along with how likely they are.
sns.distplot - Histograms show the distribution of a single numerical variable.
sns.kdeplot - KDE plots (or 2D KDE plots) show an estimated, smooth distribution of a single numerical variable (or two numerical variables).
sns.jointplot - This command is useful for simultaneously displaying a 2D KDE plot with the corresponding KDE plots for each individual variable.
'''

# Change the style of the figure
sns.set_style("whitegrid")

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large'  
)