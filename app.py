import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv() #take environment variables from .env

import requests #for sending message

#get the google sheet id
id = os.environ.get("ID")#google sheet ID
demo_id = os.environ.get("DEMO_ID")#demo id
authority = os.environ.get("AUTHORITY") #get the authorization tag from env fie


#sends a message to specific discord channel
def makeMessage(content, channel):
    #go to discord on desktop, click f12, go under the payload tab, copy content
    payload = {
        "content": content
    }

    #go to discord on desktop, click f12, go to request headers -> authorization
    header = {
        "authorization": authority
    }
    #go to discord on desktop, click f12, go to network tab, click anything to see request posted
    #get the id by right clicking a channel and selcting "copy id" (developer mode must be enabled for option to appear)
    url = "https://discord.com/api/v9/channels/"+channel+"/messages"

    #make the post with the data and header
    r = requests.post(url, data=payload, headers=header)


#initialize the dataframe
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{id}/export?format=csv")

print(df) #print the dataframe

columns = df.columns[4:] # Get column names

#print the column names to the user so they can check everything is ok
print("Categories: ", end = " ")
for i in columns:
    print(i, end = " ")
print()

#the way the sheet is designed, the items after column 4 are the categories

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

print("Sending demo message")
makeMessage("demo message", demo_id) #send demo message
print("Demo message sent")

#Open file to put message, if it doesn't exist
fileInput = "message.txt" #message.txt is where you type your message to send. it is in the gitignore so it isn't pushed to the public repo
from pathlib import Path

fle = Path(fileInput)
fle.touch(exist_ok=True)
print("File setup complete.")
print("Type the message you want to send in message.txt.")
while True:
    status = input("Type 'done' when finished, or type 'exit' to exit the program. ")
    if status == "done":
        print("Message complete")
        break
    elif status == "exit":
        print("Quitting program")
        quit()
        

output = open(fileInput, "r") #r is read
text = output.read() #get text to send from file
makeMessage(text, demo_id) #send another demo message with the message you made
print("The message you drafted has been sent to the demo server id. Please inspect it and correct it if need be.")

# iterate through each row and select
# 'Server ID' and [category] column respectively.
col1 = "Server ID"
for ind in df.index:
    inCategory = df[category][ind] #whether or not a server is in that category
    platform = df["Platform"][ind] #which platform to post
    if(inCategory):
        print(df[col1][ind], inCategory) #display given server ID only if it's in that given category
        print(platform) #which platform to post on