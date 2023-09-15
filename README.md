# Pastebin Scraper

 Python script that scrapes pastebin.com for newly posted paste.

## Overview
This script provides an automated tool to scrape data from Pastebin using its scraping API. It fetches the latest pastes and their associated metadata and saves them in individual files. Each file is saved in a folder named by the current date, under a parent directory pastebin/scrapes in the user's home directory.

## Features
- Utilizes Pastebin's scraping API to fetch latest pastes.
- Saves each paste in a dedicated `.txt` file with metadata and actual content.
- Adds a delay between each scrape using a `randomsleep` function to mimic human-like behavior.
- Automatically creates directories for saving pastes based on current date.
- Handles potential decoding exceptions gracefully.

## Description:

The script is a web scraper that retrieves information from "https://scrape.pastebin.com/api_scraping.php" and saves it in a folder named "scrapes" 
under the user's home directory. The script first creates the folder (and parent directories if not exist) using the "pathlib" library. 
It then defines a "randomsleep()" function that prints a countdown message for a random time between 120 to 160 seconds.

The "scrape()" function retrieves the data from the website by sending a GET request and converts the response to a JSON object. 
It then creates a subfolder under "scrapes" with the current date (in the format of MM-DD-YYYY) and retrieves the metadata and content of each item 
in the JSON object by sending further GET requests. The metadata and content of each item are saved in a text file with the item's key as the file name. 
If the file with the same name already exists, the function skips it and breaks the loop. The script runs in an infinite loop, performing the scrape 
every time and waiting for a random time after each iteration.

## Requirements:

1. Pastbin pro account. (https://pastebin.com/pro)
2. Whitelist your IP on pastebin.com
3. Python 3
4. Python libraries:
  - `pathlib`
  - `datetime`
  - `requests`
  - `json`
  - `time`
  - `sys`
  - `os`

## Continuous running:

1. Open a terminal window.

2. Type the following command to create a service file:

```
sudo touch /etc/systemd/system/paste.service
```

3. Type the following command to open the service file in nano text editor:

```
sudo nano /etc/systemd/system/paste.service
```

4. In nano text editor, copy and paste the following code:

```
[Unit]
Description=Pastebin Scraper
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
User=Alteredadmin
Restart=always
RestartSec=1
ExecStart=python3 /home/Alteredadmin/paste.py

[Install]
WantedBy=multi-user.target

```

5. Save the changes and close the nano text editor by pressing CTRL + X, Y, and ENTER.

6. Type the following command to start the service:


```
sudo systemctl start paste
```

7. Type the following command to enable the service to start automatically after a reboot:


```
sudo systemctl enable paste

```

8. Type the following command to check the status of the service:

```
sudo systemctl status paste

```

9. Type the following command to see output of the service

```
sudo journalctl -u paste -f

```

10. Type the following command to stop the service:

```
sudo systemctl stop paste
```

## Notes

- The script continuously runs, fetching new data from Pastebin at random intervals between 120 and 160 seconds. This mimics human-like behavior and is meant to reduce the risk of being detected or banned by Pastebin.
- Scraped data will be saved in the user's home directory under `pastebin/scrapes/`.
- If the script encounters an already scraped paste, it will move on to the next paste.
- In the case of any decoding exceptions during writing the file, the script will gracefully handle the exception and continue.


## Reference
For more details about the Pastebin scraping API, visit [this link](https://pastebin.com/doc_api).


## Support the Developer
If you found this helpful, please consider:
- **Buymeacoffee:** [Link](http://buymeacoffee.com/alteredadmin)
