from browser_links import *
from main_functions import *
from report import *

# Path to the folder containing the images
image_folder = "images"
@pytest.mark.parametrize("browser_config", browsers)
def test_parallel_serial(browser_config):
    try:
        driver = browser_config["driver"]()
        driver.maximize_window()
        driver.get(MAIN_URL)
        time.sleep(2)
        timeComplexities(driver, browser_config)
        time.sleep(2)
        generate_reports()
        time.sleep(5)
        driver.quit()
        time.sleep(5)
    except Exception as e:
        print(f"An exception occurred in {browser_config['browserName']}: {e}")
