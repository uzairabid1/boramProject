from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, ElementClickInterceptedException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import os
import shutil
import pandas as pd
import time
from geopy.geocoders import Nominatim
import requests
import urllib.parse
import re
from bs4 import BeautifulSoup
from itertools import product
from requests.exceptions import RequestException, JSONDecodeError

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='meow')
location = geolocator.geocode("서울 성동구 행당로 75")
print(location.longitude)