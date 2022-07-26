# Python Campaign Manager

## Reading Data from Google Sheets
Import/Read Google Sheet in Python: https://www.youtube.com/watch?v=t6WSY9D_ORQ
Get column names in Pandas Dataframe: https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/
Iterating over rows in Pandas Dataframe: https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/

## Create a file it it doesn't exist using touch()
https://appdividend.com/2022/03/15/how-to-create-file-if-not-exist/#:~:text=Create%20File%20if%20it%20does%20not%20exist%20using%20the%20touch()

## Reading from File
https://www.pythontutorial.net/python-basics/python-read-text-file/

## System Exit
https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/

## Posting on Social Apps via Python
Post on Discord using Python Requests: https://www.youtube.com/watch?v=DArlLAq56Mo

# Sheet Format
The servers and categories are stored on a Google Sheet. Make sure that the sheet's sharing settings are set such that whoever has the link can view it. Keeping the sheet ID in the `.env` keeps the sheet ID hidden from the public, alleviating privacy concerns.

This program requires the Google sheet in question to have this format:
- The leftmost column is the server ID.
    - Developer Mode must be enabled for the ability to get a server's ID.
    - To get the server ID from a specific channel, right click the channel in question and select "Copy ID". Paste this ID number in the first column in a new row in your Google Sheet.
- The next 2 columns are unused; merely used for notes for human readability.
- Column 3 is the "Platform" column. This can be discord, slack, etc.
- The columns after column 4 are the categories.
    - For each server, indicate whether the server is in a given category by adding `TRUE` or `FALSE` in the cell in the catagory's column that server's row.
    - A given sheet can have an unlimited number of categories; just make sure each server in the sheet is marked as `TRUE` or `FALSE` for being in that specific category.
    - Give a category a name by naming that cell in the column for the header row. To specify a category in the program, type it when prompted.

Here is what that looks like visually:

|Server ID|Server|Channel Name|Platform|Category 1|Category 2|...|
|--- |--- |--- |--- |--- |--- |--- |
|ID|Name|Name|discord/slack/etc|TRUE/FALSE|TRUE/FALSE|...|
|...|...|...|...|...|...|...|
|ID|Name|Name|discord/slack/etc|TRUE/FALSE|TRUE/FALSE|...|

# Purpose
Using Python, this program will be able to send messages and posts across several social media platforms.

## .env
This program contains an `.env` file which contains the following
- `ID`: ID for Google Sheet containing server IDs
    - Put in the `.env` file (hidden via the `.gitignore` file) for the sake of privacy.
- `DEMO_ID`: ID for Discord channel to preview post before sending it.
    - Put in the `.env` file (hidden via the `.gitignore` file) for the sake of privacy.
- `AUTHORITY`: Authorization tag for Discord. Go to Discord on desktop, click f12, go to request headers -> authorization. This appears to work for any channel from what I can tell.
    - Also put in the `.env` file, although this variable works for all servers.