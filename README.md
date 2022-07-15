# Python Campaign Manager
Import/Read Google Sheet in Python: https://www.youtube.com/watch?v=t6WSY9D_ORQ
Post on Discord using Python Requests: https://www.youtube.com/watch?v=DArlLAq56Mo

# Purpose
Using Python, this program will be able to send messages and posts across several social media platforms.

## .env
This program contains an `.env` file which contains the following
- `ID`: ID for Google Sheet containing server IDs
    - Put in the `.env` file (hidden via the `.gitignore` file) for the sake of privacy.
- `AUTHORITY`: Authorization tag for Discord. Go to Discord on desktop, click f12, go to request headers -> authorization. This appears to work for any channel from what I can tell.
    - Also put in the `.env` file, although this varaible works for all servers.