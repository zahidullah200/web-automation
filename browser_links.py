import pytest
import platform
import psutil
import random
import time
import os
import csv
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import statistics
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from selenium.webdriver.common.action_chains import ActionChains
from reportlab.lib.styles import getSampleStyleSheet
import sys

algorithms_path = os.path.abspath('algorithms')


# Define the list of browsers  
browsers = [
    {"browserName": "chrome", "driver": webdriver.Chrome},
    {"browserName": "firefox", "driver": webdriver.Firefox},
    {"browserName": "MicrosoftEdge", "driver": webdriver.Edge},
    # {"browserName": "opera", "driver": webdriver.Opera},  # Update to use Opera WebDriver
]

# Define the URL of the main page, bubble sort page, and image generation page
MAIN_URL = 'http://127.0.0.1:5502/index.html'
