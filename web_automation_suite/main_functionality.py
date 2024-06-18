from web_automation_suite.browsers_links_and_pageURL import *
def read_numbers_and_send_keys(filename, input_element):
    with open(filename, 'r') as file:
        numbers_list = file.readlines()
        numbers_str = ''.join(numbers_list)
        input_element.send_keys(numbers_str)

def read_images_and_send_keys(folder_path, input_element):
    image_files = os.listdir(folder_path)
    image_paths = [os.path.join(folder_path, file) for file in image_files]
    input_element.send_keys(*image_paths)

def write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Browser Name", "Browser Version"])
        writer.writerow([driver.capabilities['browserName'], driver.capabilities['browserVersion']])
        writer.writerow(["Operating System", "Processor Info", "RAM Info"])
        writer.writerow([platform.system(), platform.processor(), f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB"])
        writer.writerow(["Wasm_time_taken", "Js_time_taken"])
        for wasm_time, js_time in zip(webassembly_times, javascript_times):
            writer.writerow([wasm_time, js_time])
        time.sleep(1)

def click_and_execute(driver, category_id, element_id, func, browser_config, back=True):
    try:
        btn_category = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, category_id)))
        ActionChains(driver).move_to_element(btn_category).perform()
        time.sleep(1)
        btn_category.click()
        
        btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, element_id)))
        btn.click()
        time.sleep(1)
        func(driver, browser_config)
        if back:
            driver.back()
        time.sleep(1)
    except Exception as e:
        print(f"An error occurred in {element_id}: {e}")

def timeComplexities(driver, browser_config):
    categories = [
        ("o(1)", [("power", powerFunc), ("summation", SummationFunc)]),
        ("o(n)", [("reversearray", reverseFunc), ("thresh", thresholdFunc)]),
        ("O(n!)", [("factorial", factorialdFunc), ("permutation", permuFunc)]),
        ("O(n^2)", [("bubble_sort", bubleFunc), ("selectionsort", selectionFunc)]),
        ("O(n^3)", [("cubicpoly", cubpolyFunc), ("matrixmul", matrixMul)]),
        ("O(n^4)", [("nesloopmul", nesloopmulFunc), ("nesloopsum", nesloopsumFunc)]),
        ("O(logn)", [("binarysearch", binaryFunc), ("binaryrotated", binaryRotateFunc)]),
        ("O(nlogn)", [("imagegen", imageGenerationFunc), ("quicksort", quickSortFunc)])
    ]

    for category_id, algorithms in categories:
        for element_id, func in algorithms:
            click_and_execute(driver, category_id, element_id, func, browser_config)
        driver.get(MAIN_URL)
        time.sleep(3)

def save_times(folder, file_name, driver, browser_config, webassembly_times, javascript_times):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, file_name)
    time.sleep(1)
    write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)

# Configure logging
logging.basicConfig(filename='web_automation_errors.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')
def get_times(driver, run_id, btn_id, lbl_id, sleep_time=2, iterations=3, retries=3):
    times = []
    for _ in range(iterations):
        attempt = 0
        while attempt < retries:
            try:
                button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, btn_id)))
                button.click()
                time_taken = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, lbl_id)))
                time.sleep(sleep_time)
                times.append(time_taken.text)
                break
            except Exception as e:
                logging.error(f"Attempt {attempt + 1} failed: {e}")
                attempt += 1
                if attempt >= retries:
                    times.append('Error')
    return times

def run_tests(driver, select_id, wasm_id, js_id, run_id, lbl_id, folder, file_prefix, browser_config):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, select_id))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, wasm_id))).click()
        wasm_times = get_times(driver, run_id, run_id, lbl_id)
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, select_id))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, js_id))).click()
        js_times = get_times(driver, run_id, run_id, lbl_id)
        
        save_times(folder, f'{browser_config["browserName"]}_{file_prefix}.csv', driver, browser_config, wasm_times, js_times)
    except Exception as e:
        logging.error(f"An error occurred in run_tests: {e}")
        print(f"An error occurred in run_tests: {e}")

def powerFunc(driver, browser_config):
    run_tests(driver, "testType", "WebAssembly", "JavaScript", "runTestButton", "timeLabel", 
              'Algorithms_csv_generated_files/TimeComplexity_o(1)/power', 'power', browser_config)

def SummationFunc(driver, browser_config):
    run_tests(driver, "methodSelect", "wasm", "js", "runTestButton", "timeTaken", 
              'Algorithms_csv_generated_files/TimeComplexity_o(1)/summation', 'summation', browser_config)

def reverseFunc(driver, browser_config):
    folder = 'Algorithms_csv_generated_files/TimeComplexity_o(n)/reverse-array'
    input_numbers = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "inputArray")))
    read_numbers_and_send_keys("random.txt", input_numbers)
    run_tests(driver, "method", "webassembly", "javascript", "r_btn", "time_taken", folder, 'reverseArray', browser_config)

def thresholdFunc(driver, browser_config):
    folder = 'Algorithms_csv_generated_files/TimeComplexity_o(n)/threshold'
    file_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'thresholdImageInput')))
    file_input.send_keys(os.path.abspath("images/coverimage2.jpg"))
    run_tests(driver, "implementationSelect", "WebAssembly", "JavaScript", "processButton", "timeLabel", folder, 'threshold', browser_config)

def factorialdFunc(driver, browser_config):
    run_tests(driver, "implementationSelect", "webassembly", "javascript", "fact", "timetaken", 
              'Algorithms_csv_generated_files/TimeComplexity_O(n!)/factorial', 'factorialcon', browser_config)

def permuFunc(driver, browser_config):
    run_tests(driver, "implementationSelect", "webassembly", "javascript", "permutation", "timeTaken", 
              'Algorithms_csv_generated_files/TimeComplexity_O(n!)/permutation', 'contpermutation', browser_config)

def bubleFunc(driver, browser_config):
    folder = 'Algorithms_csv_generated_files/TimeComplexity_O(n^2)/bubble'
    input_numbers = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inputNumbers")))
    read_numbers_and_send_keys("random.txt", input_numbers)
    run_tests(driver, "sortingMethod", "wasm", "js", "buble_btn", "time_taken", folder, 'bubble_sort', browser_config)

def selectionFunc(driver, browser_config):
    folder = 'Algorithms_csv_generated_files/TimeComplexity_O(n^2)/selectionsort'
    input_numbers = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inputArray")))
    read_numbers_and_send_keys("random.txt", input_numbers)
    run_tests(driver, "sortingMethod", "WebAssembly", "JavaScript", "sortButton", "time_taken", folder, 'selectionsort', browser_config)

def cubpolyFunc(driver, browser_config):
    run_tests(driver, "selection", "webassembly", "javascript", "cubpoly", "timetaken", 
              'Algorithms_csv_generated_files/TimeComplexity_O(n^3)/cubicpoly', 'cubicpolynomial', browser_config)

def matrixMul(driver, browser_config):
    run_tests(driver, "methodSelect", "webassembly", "javascript", "matrixmul", "timetaken", 
              'Algorithms_csv_generated_files/TimeComplexity_O(n^3)/matrixmul', 'matrixmul', browser_config)

def nesloopmulFunc(driver, browser_config):
    run_tests(driver, "selection", "webassembly", "javascript", "nesloobtn", "timetaken", 
              'Algorithms_csv_generated_files/TimeComplexity_O(n^4)/nesloopmul', 'nestloopmul', browser_config)

def nesloopsumFunc(driver, browser_config):
    run_tests(driver, "implementation", "webassembly", "javascript", "nesloopsumbtn", "timetaken", 
              'Algorithms_csv_generated_files/TimeComplexity_O(n^4)/nesloosum', 'nestloopsum', browser_config)

def binaryFunc(driver, browser_config):
    run_tests(driver, "method", "webassembly", "javascript", "binarysearchbtn", "timetaken", 
              'Algorithms_csv_generated_files/TimeComplexity_O(log n)/binarysearch', 'binarysearch', browser_config)
    
def binaryRotateFunc(driver, browser_config):
    run_tests(driver, "method", "webassembly", "javascript", "binrotatbtn", "timetaken", 
              'Algorithms_csv_generated_files/TimeComplexity_O(log n)/binarysearchrotated', 'binarysearchrotated', browser_config)

def imageGenerationFunc(driver, browser_config):
    run_tests(driver, "implementationSelect", "webassembly", "javascript", "sortButton", "time_taken", 
              'Algorithms_csv_generated_files/TimeComplexity_O(n log n)/image-generation', 'image_generation_sort', browser_config)

def quickSortFunc(driver, browser_config):
    folder = 'Algorithms_csv_generated_files/TimeComplexity_O(n log n)/quick_sort'
    input_numbers = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inputArray")))
    read_numbers_and_send_keys("random.txt", input_numbers)
    run_tests(driver, "method", "webassembly", "javascript", "quick_btn", "timetaken", folder, 'quicksort', browser_config)