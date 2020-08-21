#!/usr/bin/python

import requests
from bs4 import BeautifulSoup


def steal_site():
    url = input("Enter website to steal... I mean totally create yourself...")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = str(soup.find('html'))

    site = open('templates/stolensite.html', 'w+')
    site.write(content)
    site.close()