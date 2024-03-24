from browser_links import *
from functions_algorithms import thresholdFunc, bubleFunc, imageGenerationFunc, reverseFunc, fiboFunc
from report import *
from merge import merge_pdfs

# Path to the folder containing the images
image_folder = "images"

def generate_reports():
    bubbleSortReport()
    image_generationSortReport()
    reverseArrayReport()
    thresholdImgReport()
    fibonacciReport()
    # List of PDF files to merge
    pdf_files = ['reports/imageGenerationSort.pdf', 'reports/bubbleSort.pdf', 'reports/revereseArray.pdf', 'reports/threshold.pdf', 'reports/fibonacci.pdf']

    # Output path for the merged PDF
    output_path = 'all_reports_combined.pdf'

    # Call the merge_pdfs function
    merge_pdfs(pdf_files, output_path)

@pytest.mark.parametrize("browser_config", browsers)
def test_parallel_serial(browser_config):
    try:
        driver = browser_config["driver"]()
        driver.maximize_window()
        driver.get(MAIN_URL)
        #driver.implicitly_wait(20)

        # Bubble sort function
        bubleFunc(driver, browser_config)

        # Image generation function calling from functions_algorithms
        imageGenerationFunc(driver, browser_config)

        # Reverse array
        reverseFunc(driver, browser_config)

        # Image threshold algorithm
        thresholdFunc(driver, browser_config)

        # Fibonacci function calling
        fiboFunc(driver, browser_config)

        # Generate reports
        generate_reports()

        driver.get(MAIN_URL)
        time.sleep(20)
        driver.quit()
    except Exception as e:
        print(f"An exception occurred in {browser_config['browserName']}: {e}")
