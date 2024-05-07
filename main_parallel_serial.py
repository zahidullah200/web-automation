from browser_links import *
from functions_algorithms import *
from report import *
from merge import merge_pdfs

# Path to the folder containing the images
image_folder = "images"

def generate_reports():
    # Call the function for each performance metric
    generate_report('power', 'Algorithms_csv_generated_files/TimeComplexity_o(1)/power', 'Power of a number Report in 3 Major Browsers')
    generate_report('summation', 'Algorithms_csv_generated_files/TimeComplexity_o(1)/summation', 'Summation of Numbers Report in 3 Major Browsers')
  
    generate_report('reverseArray', 'Algorithms_csv_generated_files/TimeComplexity_o(n)/reverse-array', 'Reverse Array Report in 3 Major Browsers')
    generate_report('threshold', 'Algorithms_csv_generated_files/TimeComplexity_o(n)/threshold', 'Threshold Image Processing Report in 3 Major Browsers')

    generate_report('factorialcon', 'Algorithms_csv_generated_files/TimeComplexity_O(n!)/factorial', 'Factorial of a Number Report in 3 Major Browsers')
    generate_report('contpermutation', 'Algorithms_csv_generated_files/TimeComplexity_O(n!)/permutation', 'Continus permutaion of numbers Report in 3 Major Browsers')

    generate_report('bubble_sort', 'Algorithms_csv_generated_files/TimeComplexity_O(n^2)/bubble', 'Bubble Sort of Numbers Report in 3 Major Browsers')
    generate_report('fibonacci', 'Algorithms_csv_generated_files/TimeComplexity_O(n^2)/fibonacci', 'Fibonacci of Number Report in 3 Major Browsers')

    generate_report('cubicpolynomial', 'Algorithms_csv_generated_files/TimeComplexity_O(n^3)/cubicpoly', 'Cubic Polynomilal of Number Report in 3 Major Browsers')
    generate_report('matrixmul', 'Algorithms_csv_generated_files/TimeComplexity_O(n^3)/matrixmul', 'Matrix Multiplication Report in 3 Major Browsers')

    generate_report('nestloopmul', 'Algorithms_csv_generated_files/TimeComplexity_O(n^4)/nesloopmul', 'Nested loop Multiplication Report in 3 Major Browsers')
    generate_report('nestloopsum', 'Algorithms_csv_generated_files/TimeComplexity_O(n^4)/nesloosum', 'Nested loop Summation Report in 3 Major Browsers')

    generate_report('binarysearch', 'Algorithms_csv_generated_files/TimeComplexity_O(log n)/binarysearch', 'Binary Search Report in 3 Major Browsers')
    generate_report('binarysearchrotated', 'Algorithms_csv_generated_files/TimeComplexity_O(log n)/binarysearchrotated', 'Binary search rotated Report in 3 Major Browsers')


    generate_report('image_generation_sort', 'Algorithms_csv_generated_files/TimeComplexity_O(n log n)/image-generation', 'Image Generation and Sort Report in 3 Major Browsers')
    generate_report('quicksort', 'Algorithms_csv_generated_files/TimeComplexity_O(n log n)/quick_sort', 'Quick Sort Report in 3 Major Browsers')


    # List of PDF files to merge
    pdf_files = ['reports/power.pdf', 'reports/summation.pdf', 'reports/reverseArray.pdf', 'reports/threshold.pdf', 'reports/factorialcon.pdf', 'reports/contpermutation.pdf', 'reports/bubble_sort.pdf', 'reports/fibonacci.pdf', 
                 'reports/cubicpolynomial.pdf', 'reports/matrixmul.pdf', 'reports/nestloopmul.pdf', 'reports/nestloopsum.pdf', 'reports/binarysearch.pdf', 'reports/binarysearchrotated.pdf', 'reports/image_generation_sort.pdf', 'reports/quicksort.pdf']

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

        #common function for all of the algorithms
        timeComplexities(driver, browser_config)


        # Generate reports
        generate_reports()

        #driver.get(MAIN_URL)
        time.sleep(30)
        driver.quit()
    except Exception as e:
        print(f"An exception occurred in {browser_config['browserName']}: {e}")
