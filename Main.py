# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:02:21 2019

@author: SUNNY DHOKE
"""

import wsurlopen
import bs4
from urllib.error import HTTPError
from requests.exceptions import ConnectionError

def urlOpen(url):
    try:
        var = "no problem"
        read = requests.get(url)
    except HTTPError as e:
        var = "There's some problem, captain"
    except URLError as e:
        var = "It's an URL error , Sir!"
    except ConnectionError as e:
        var = "Please check the connectivity."
    
    if(var = "no problem"):
        return read
    else:
        return "Error occured while I was opening the website.Oh oh"
    
