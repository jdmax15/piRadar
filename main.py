# piRadar - Continuously downloads and displays the bom.gov.au Sydney radar picture.

import os
import time
import requests
from bs4 import BeautifulSoup
from PIL import Image
from ftplib import FTP


def fetch_images():
    # Connect to the FTP server
    ftp = FTP("ftp.bom.gov.au")
    ftp.login()
    print('ftp.bom.gov.au logged in.')

    print('Checking for new images...')

    # Navigate to the radar directory
    ftp.cwd("anon/gen/radar")

    # Download radar images
    local_directory = "./radar_images"
    os.makedirs(local_directory, exist_ok=True)


    for file in ftp.nlst():
        if "IDR713.T" in file and file.endswith(".png"):
            if file in os.listdir(local_directory):
                continue
            else:
                with open(f"{local_directory}/{file}", "wb") as f:
                    ftp.retrbinary(f"RETR {file}", f.write)
                print(f"Downloaded: {file}")

    ftp.quit()

def main():
    fetch_images()

if __name__ == '__main__':
    main()