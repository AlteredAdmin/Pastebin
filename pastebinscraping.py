'''

####################################################################

_______        _______ _______  ______ _______ ______       _______ ______  _______ _____ __   _
|_____| |         |    |______ |_____/ |______ |     \      |_____| |     \ |  |  |   |   | \  |
|     | |_____    |    |______ |    \_ |______ |_____/      |     | |_____/ |  |  | __|__ |  \_|
                                                                                                

Title: Pastebin Scraper
Description: This script is a web scraper that retrieves information from pastebin and saves it as text files in a folder named "scrapes" with random 
wait time between iterations.
More info: https://alteredadmin.github.io/
=====================================================
Name: Altered Admin
Website: https://alteredadmin.github.io
Twitter: https://twitter.com/Alt3r3dAdm1n
If you found this helpful Please consider:
Buymeacoffee: http://buymeacoffee.com/alteredadmin
BTC: bc1qhkw7kv9dtdk8xwvetreya2evjqtxn06cghyxt7
LTC: ltc1q2mrh9s8sgmh8h5jtra3gqxuhvy04vuagpm3dk9
ETH: 0xef053b0d936746Df00C9CCe0454b7b8afb1497ac


####################################################################
OS Support: Any

Requirements:
you will need a pastbin pro account. (https://pastebin.com/pro)

Long Description:

The script is a web scraper that retrieves information from "https://scrape.pastebin.com/api_scraping.php" and saves it in a folder named "scrapes" 
under the user's home directory. The script first creates the folder (and parent directories if not exist) using the "pathlib" library. 
It then defines a "randomsleep()" function that prints a countdown message for a random time between 120 to 160 seconds.

The "scrape()" function retrieves the data from the website by sending a GET request and converts the response to a JSON object. 
It then creates a subfolder under "scrapes" with the current date (in the format of MM-DD-YYYY) and retrieves the metadata and content of each item 
in the JSON object by sending further GET requests. The metadata and content of each item are saved in a text file with the item's key as the file name. 
If the file with the same name already exists, the function skips it and breaks the loop. The script runs in an infinite loop, performing the scrape 
every time and waiting for a random time after each iteration.

Example:

NOTES
    Author:         Altered Admin & ChatGPT
    Email:          
    Date:           FEB 06 2023

####################################################################


'''


from pathlib import Path
from datetime import datetime
import requests
import json
import time
from random import randint
import sys
from os.path import expanduser

scrapes_folder = Path(expanduser("~")) / 'pastebin' / 'scrapes'
scrapes_folder.mkdir(parents=True, exist_ok=True)


def randomsleep():
    for remaining in range(randint(120, 160), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rComplete!\n")


def scrape():
    url = "https://scrape.pastebin.com/api_scraping.php?limit=250"
    r = requests.get(url)
    items = r.json()
    date_today = datetime.today().strftime('%m-%d-%Y')
    date_folder = scrapes_folder / date_today
    date_folder.mkdir(exist_ok=True)
    for item in items:
        key = item['key']
        meta_url = f'https://scrape.pastebin.com/api_scrape_item_meta.php?i={key}'
        paste_url = f'https://scrape.pastebin.com/api_scrape_item.php?i={key}'
        meta_response = requests.get(meta_url)
        paste_response = requests.get(paste_url)
        meta_data = json.loads(meta_response.content)
        paste_data = paste_response.content
        file_path = date_folder / f"{key}.txt"
        if file_path.exists():
            print(f"{key} already exists.")
            print()
            randomsleep()
            print()
            break
        else:
            print('Found new Paste!!!')
            print(key)
            print()
            with open(file_path, 'w') as f:
                f.write("More info: https://github.com/AlteredAdmin/PastebinCreated\n")
                f.write("\n")
                f.write(json.dumps(meta_data, indent=2))
                f.write("\n\n")
                f.write("------------------------------------------------------------\n")
                f.write("\n")
                try:
                    f.write(paste_data.decode())
                except Exception as e:
                    print()
                    print("Exception will Continue")
                    print()
                    continue


while True:
    scrape()
    # time.sleep(900) # scrape every 15 minutes
    randomsleep()
