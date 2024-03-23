import pytest
import platform
import psutil
import random
import time
import os
import csv
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
from reportlab.lib.styles import getSampleStyleSheet
import sys

algorithms_path = os.path.abspath('algorithms')

from report import bubbleSort
from report import image_generationSortFun
from report import reverseArray
from report import thresholdImg
from report import fibonaccFuncReport
from merge import merge_pdfs  

# Define the list of browsers  
browsers = [
    {"browserName": "chrome", "driver": webdriver.Chrome},
    {"browserName": "firefox", "driver": webdriver.Firefox},
    {"browserName": "MicrosoftEdge", "driver": webdriver.Edge},
    # {"browserName": "opera", "driver": webdriver.Opera},  # Update to use Opera WebDriver
]

# Define the URL of the main page, bubble sort page, and image generation page
MAIN_URL = 'http://127.0.0.1:5500/mainprojectFolder/home.html'
BUBBLE_SORT_URL = 'http://127.0.0.1:5500/Algorithms/bubblesort/bubble.html'
IMG_GEN_URL = 'http://127.0.0.1:5500/wasm_test/index.html'
REVERSE_ARRAY = 'http://127.0.0.1:5500/Algorithms/reversearray/reverse.html'
THESHOLD_URL = 'http://127.0.0.1:5500/Algorithms/reversearray/threshold.html'
