# Pastebin Scraper

 Python script that scrapes pastebin.com for newly posted paste.

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

## Continuous running:

1. Open a terminal window.

2. Type the following command to create a service file:

```
sudo touch /etc/systemd/system/myscript.service
```

3. Type the following command to open the service file in nano text editor:

```
sudo nano /etc/systemd/system/myscript.service
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
ExecStart=python3 /home/Alteredadmin/my_script.py

[Install]
WantedBy=multi-user.target

```

5. Save the changes and close the nano text editor by pressing CTRL + X, Y, and ENTER.

6. Type the following command to start the service:


```
sudo systemctl start myscript
```

7. Type the following command to enable the service to start automatically after a reboot:


```
sudo systemctl enable myscript

```

8. Type the following command to check the status of the service:

```
sudo systemctl status myscript

```
9. Type the following command to stop the service:

```
sudo systemctl stop myscript
```
