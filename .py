# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
%matplotlib inline
import seaborn as sns


.............................................................................


# import csv file
df = pd.read_csv(r'C:\Users\Nehan reddy\Downloads\amazon big billion days Sales Data.csv', encoding= 'unicode_escape')


.................................................................................

df.shape
(11251, 15)

.................................................................................

df.head(4) # shows first 4 rows  in the  table

..............................................................

df.info() 
............................................................

#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

.........................................................


# check for null values
pd.isnull(df).sum()

................................................

df['Amount'].dtypes   # showsdata type of amount column 

............................................


df.columns  # it outputs columns present in df .dataframe

...............................

#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})

.......................................

# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()

......................................................

# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()


......................................................

# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)  

..........................................................


  # plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

..................................

#age and gender wise oreders distribustions 

ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)

....................................................

# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)

.........................................................................

  # total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


..................................................................

# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')

.........................................................................

  ###  marital status 

  
ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


...........................................................................

# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

.............................................................................
#sold product wise sold quantity in bar chart

sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')

..............................................................................







