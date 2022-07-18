import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv() #take environment variables from .env

#get the google sheet id
id = os.environ.get("ID")#google sheet ID

#initialize the dataframe
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{id}/export?format=csv")

print(df) #print the dataframe

columns = df.columns[3:] # Get column names
#the way the sheet is designed, the items after column 3 are the categories

#while loop for user to enter category for post
while True:
    category = input("Enter a category for your message: ")
    if category in columns:
        break #break out of loop when user enters valid category
    else:
        print("ERROR: Invalid category name")
        print("Category name is CASE-SENSITIVE")
        print("Here are the category options: ")
        for i in columns:
            print(i) #print out the category options


# iterate through each row and select
# 'Server ID' and [category] column respectively.
col1 = "Server ID"
for ind in df.index:
    print(df[col1][ind], df[category][ind])
