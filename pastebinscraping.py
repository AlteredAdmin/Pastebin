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
