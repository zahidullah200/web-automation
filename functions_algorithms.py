from browser_links import *
def read_numbers_and_send_keys(filename, input_element):
    with open(filename, 'r') as file:
        # Read all numbers from the file
        numbers_list = file.readlines()

        # Concatenate all numbers into a single string
        numbers_str = ''.join(numbers_list)
    # Send the entire string to the input element
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

def timeComplexities(driver, browser_config):
    try:
        # Hover over the button before clicking
        btn_o1 = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "o(1)")))
        ActionChains(driver).move_to_element(btn_o1).perform()
        # Wait for 1 second
        time.sleep(1)
        # Click the button
        btn_o1.click()
        # Code for btn_o1
        btn_power = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "power")))
        time.sleep(1)
        btn_power.click()
        time.sleep(1)
        #powerFunc(driver, browser_config)
        driver.back()
        time.sleep(1)
        btn_summation = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "summation")))
        btn_summation.click()
        time.sleep(1)
        #SummationFunc(driver, browser_config)
        driver.get(MAIN_URL)
        time.sleep(3)
    except:
        pass

    try:
        btn_on = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "o(n)")))
        btn_on.click()
        print("btn_on clicked")
        btn_reversearray = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "reversearray")))
        time.sleep(1)
        btn_reversearray.click()
        time.sleep(1)
        #reverseFunc(driver, browser_config)
        driver.back()
        time.sleep(1)
        btn_thrs = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "thresh")))
        btn_thrs.click()
        time.sleep(1)
        #thresholdFunc(driver, browser_config)
        driver.get(MAIN_URL)
        time.sleep(3)
    except:
        pass

    try:
        btn_onnot = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "O(n!)")))
        time.sleep(1)
        btn_onnot.click()
        time.sleep(1)
        btn_factorial = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "factorial")))
        time.sleep(1)
        #btn_factorial.click()
        time.sleep(1)
        factorialdFunc(driver, browser_config)
        driver.back()
        time.sleep(1)
        btn_permu = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "permutation")))
        btn_permu.click()
        time.sleep(1)
        #permuFunc(driver, browser_config)
        driver.get(MAIN_URL)
        time.sleep(3)
    except:
        pass

    try:
        btn_Onp2= WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "O(n^2)")))
        time.sleep(1)
        btn_Onp2.click()
        time.sleep(1)
        btn_bubble = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "bubble_sort")))
        time.sleep(1)
        btn_bubble.click()
        time.sleep(1)
        #bubleFunc(driver, browser_config)
        time.sleep(1)
        driver.back()
        time.sleep(1)
        btn_selec = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "selectionsort")))
        btn_selec.click()
        time.sleep(1)
        #selectionFunc(driver, browser_config)
        time.sleep(1)
        driver.get(MAIN_URL)
        time.sleep(3)
    except:
        pass

    try:
        btn_Onp3= WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "O(n^3)")))
        time.sleep(1)
        btn_Onp3.click()
        time.sleep(1)
        btn_bubble = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "cobicpoly")))
        time.sleep(1)
        btn_bubble.click()
        time.sleep(1)
        #cubpolyFunc(driver, browser_config)
        driver.back()
        time.sleep(1)
        btn_matrix = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "matrixmul")))
        btn_matrix.click()
        time.sleep(1)
        #matrixMul(driver, browser_config)
        time.sleep(1)
        driver.get(MAIN_URL)
        time.sleep(3)
    except:
        pass
    try:
        btn_Onp4= WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "O(n^4)")))
        time.sleep(1)
        btn_Onp4.click()
        time.sleep(1)
        btn_bubble = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "nesloopmul")))
        time.sleep(1)
        btn_bubble.click()
        time.sleep(1)
        nesloopmulFunc(driver, browser_config)
        driver.back()
        time.sleep(1)
        btn_matrix = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "nesloopsum")))
        btn_matrix.click()
        time.sleep(1)
        nesloopsumFunc(driver, browser_config)
        time.sleep(1)
        driver.get(MAIN_URL)
        time.sleep(3)
    except:
        pass

    try:
        btn_Ologn= WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "O(logn)")))
        time.sleep(1)
        btn_Ologn.click()
        time.sleep(1)
        btn_binary = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "binarysearch")))
        time.sleep(1)
        btn_binary.click()
        time.sleep(1)
        #binaryFunc(driver, browser_config)
        driver.back()
        time.sleep(1)
        btn_inaryrotated = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "binaryrotated")))
        btn_inaryrotated.click()
        time.sleep(1)
        #binaryrotatedFunc(driver, browser_config)
        time.sleep(1)
        driver.get(MAIN_URL)
        time.sleep(3)
    except:
        pass


    try:
        btn_Onlogn= WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "O(nlogn)")))
        time.sleep(1)
        btn_Onlogn.click()
        time.sleep(1)
        btn_imggen = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "imagegen")))
        time.sleep(1)
        btn_imggen.click()
        time.sleep(1)
        #imageGenerationFunc(driver, browser_config)
        driver.back()
        time.sleep(1)
        btn_inaryrotated = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, "quichsort")))
        btn_inaryrotated.click()
        time.sleep(1)
        #quickSortFunc(driver, browser_config)
        time.sleep(1)
        driver.get(MAIN_URL)
        time.sleep(3)
    except:
        pass


def powerFunc(driver, browser_config):
    try:
        POWER_FOLDER = 'Algorithms_csv_generated_files/TimeComplexity_o(1)/power'
        if not os.path.exists(POWER_FOLDER):
            os.makedirs(POWER_FOLDER)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "testType")))
        combo_box.click()
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//option[text()='WebAssembly']")))
        option_webassembly.click()
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "runTestButton")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeLabel")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        
        combo_box.click()
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//option[text()='JavaScript']")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "runTestButton")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeLabel")))
            time.sleep(1)
            javascript_times.append(time_taken.text)
        
        time.sleep(1)
        file_path = os.path.join(POWER_FOLDER, f'{browser_config["browserName"]}_power.csv')
        time.sleep(1)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)
    
    except Exception as e:
        print("An error occurred:", e)


def SummationFunc(driver, browser_config):
    try:
        SUMMATION_FOLDER = 'Algorithms_csv_generated_files/TimeComplexity_o(1)/summation'
        if not os.path.exists(SUMMATION_FOLDER):
            os.makedirs(SUMMATION_FOLDER)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "methodSelect")))
        combo_box.click()
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//option[text()='WebAssembly']")))
        option_webassembly.click()
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "runTestButton")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeTaken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        
        combo_box.click()
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//option[text()='JavaScript']")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "runTestButton")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeTaken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)
        time.sleep(1)
        file_path = os.path.join(SUMMATION_FOLDER, f'{browser_config["browserName"]}_summation.csv')
        time.sleep(1)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)
    
    except Exception as e:
        print("An error occurred:", e)


#Revers algorithm function
def reverseFunc(driver,browser_config):
    try:
        REVERSE_ARRAY = 'Algorithms_csv_generated_files/TimeComplexity_o(n)/reverse-array'
        if not os.path.exists(REVERSE_ARRAY):
            os.makedirs(REVERSE_ARRAY)
        input_numbers = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "inputArray")))
        read_numbers_and_send_keys("random.txt", input_numbers)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "method")))
        combo_box.click()
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
    
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "r_btn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)

        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_webassembly.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "r_btn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(REVERSE_ARRAY, f'{browser_config["browserName"]}_reverseArray.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)
        time.sleep(1)

    except Exception as e:
        print("An error occurred:", e)


#Threshold image processing function
def thresholdFunc(driver, browser_config):
    try:
        THRESHOLD = 'Algorithms_csv_generated_files/TimeComplexity_o(n)/threshold'
        if not os.path.exists(THRESHOLD):
            os.makedirs(THRESHOLD)
        time.sleep(1)
        file_input = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'thresholdImageInput')))
        file_path = os.path.abspath("images/coverimage2.jpg")
        file_input.send_keys(file_path)
        time.sleep(1)
        thr_combo = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'implementationSelect')))
        thr_combo.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//option[text()='WebAssembly']")))
        option_webassembly.click()
        webassembly_times_thre = []
        for _ in range(100):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "processButton")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeLabel")))
            time.sleep(1)
            webassembly_times_thre.append(time_taken.text)
        thr_combo.click()
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//option[text()='JavaScript']")))
        option_javascript.click()
        javascript_times_thre = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "processButton")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeLabel")))
            time.sleep(1)
            javascript_times_thre.append(time_taken.text)
        time.sleep(1)
        file_path = os.path.join(THRESHOLD, f'{browser_config["browserName"]}_threshold.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times_thre, javascript_times_thre)

    except Exception as e:
        print("An error occurred:", str(e))

#Threshold image processing function
def factorialdFunc(driver, browser_config):
    try:
        FACTORIAL = 'Algorithms_csv_generated_files/TimeComplexity_O(n!)/factorial'
        if not os.path.exists(FACTORIAL):
            os.makedirs(FACTORIAL)
        time.sleep(1)
        thr_combo = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'implementationSelect')))
        thr_combo.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
        webassembly_times_thre = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "fact")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            webassembly_times_thre.append(time_taken.text)
        thr_combo.click()
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_javascript.click()
        javascript_times_thre = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "fact")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            javascript_times_thre.append(time_taken.text)
        time.sleep(1)
        file_path = os.path.join(FACTORIAL, f'{browser_config["browserName"]}_factorialcon.csv')
        time.sleep(1)
        write_csv_file(file_path, driver, browser_config, webassembly_times_thre, javascript_times_thre)

    except Exception as e:
        print("An error occurred:", str(e))



#Threshold image processing function
def permuFunc(driver, browser_config):
    try:
        PERMUTATION = 'Algorithms_csv_generated_files/TimeComplexity_O(n!)/permutation'
        if not os.path.exists(PERMUTATION):
            os.makedirs(PERMUTATION)
        time.sleep(1)
        thr_combo = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'implementationSelect')))
        thr_combo.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
        webassembly_times_thre = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "permutation")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeTaken")))
            time.sleep(1)
            webassembly_times_thre.append(time_taken.text)
     
        thr_combo.click()
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_javascript.click()
        javascript_times_thre = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "permutation")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeTaken")))
            time.sleep(1)
            javascript_times_thre.append(time_taken.text)
        
        time.sleep(2)
        file_path = os.path.join(PERMUTATION, f'{browser_config["browserName"]}_contpermutation.csv')
        write_csv_file(file_path, driver, browser_config, webassembly_times_thre, javascript_times_thre)

    except Exception as e:
        print("An error occurred:", str(e))



def bubleFunc(driver, browser_config):
    try:
        BUBBLE_FOLDER = 'Algorithms_csv_generated_files/TimeComplexity_O(n^2)/bubble'
        if not os.path.exists(BUBBLE_FOLDER):
            os.makedirs(BUBBLE_FOLDER)
        input_numbers = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "inputNumbers")))
        read_numbers_and_send_keys("random.txt", input_numbers)
        time.sleep(1)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "sortingMethod")))
        combo_box.click()
        option_webassembly = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//option[text()='WebAssembly']")))
        option_webassembly.click()
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "buble_btn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        
        combo_box.click()
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//option[text()='JavaScript']")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "buble_btn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)
        
        time.sleep(2)
        file_path = os.path.join(BUBBLE_FOLDER, f'{browser_config["browserName"]}_bubble_sort.csv')
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)
        time.sleep(1)
    
    except Exception as e:
        print("An error occurred:", e)





def selectionFunc(driver, browser_config):
    try:
        SEL_SORT = 'Algorithms_csv_generated_files/TimeComplexity_O(n^2)/selectionsort'
        if not os.path.exists(SEL_SORT):
            os.makedirs(SEL_SORT)
        input_numbers = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "inputArray")))
        read_numbers_and_send_keys("random.txt", input_numbers)
        time.sleep(1)
        combo_box = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "sortingMethod")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "WebAssembly")))
        option_webassembly.click()
        time.sleep(1)
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "sortButton")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "JavaScript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "sortButton")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(SEL_SORT, f'{browser_config["browserName"]}_selectionsort.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)


    except Exception as e:
        print("An error occurred:", e)



def cubpolyFunc(driver, browser_config):
    try:
        CUBPOLY = 'Algorithms_csv_generated_files/TimeComplexity_O(n^3)/cubicpoly'
        if not os.path.exists(CUBPOLY):
            os.makedirs(CUBPOLY)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "selection")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "cubpoly")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "cubpoly")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(CUBPOLY, f'{browser_config["browserName"]}_cubicpolynomial.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)

    except Exception as e:
        print("An error occurred:", e)




def matrixMul(driver, browser_config):
    try:
        MATRIXMUL = 'Algorithms_csv_generated_files/TimeComplexity_O(n^3)/matrixmul'
        if not os.path.exists(MATRIXMUL):
            os.makedirs(MATRIXMUL)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "methodSelect")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
    
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "matrixmul")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "matrixmul")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(MATRIXMUL, f'{browser_config["browserName"]}_matrixmul.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)

    except Exception as e:
        print("An error occurred:", e)


def nesloopmulFunc(driver, browser_config):
    try:
        NESLOOPMUL = 'Algorithms_csv_generated_files/TimeComplexity_O(n^4)/nesloopmul'
        if not os.path.exists(NESLOOPMUL):
            os.makedirs(NESLOOPMUL)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "selection")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
    
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "nesloobtn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "nesloobtn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(NESLOOPMUL, f'{browser_config["browserName"]}_nestloopmul.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)

    except Exception as e:
        print("An error occurred:", e)


def nesloopsumFunc(driver, browser_config):
    try:
        NESLOOPSUM = 'Algorithms_csv_generated_files/TimeComplexity_O(n^4)/nesloosum'
        if not os.path.exists(NESLOOPSUM):
            os.makedirs(NESLOOPSUM)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "implementation")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
    
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "nesloopsumbtn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "nesloopsumbtn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(NESLOOPSUM, f'{browser_config["browserName"]}_nestloopsum.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)

    except Exception as e:
        print("An error occurred:", e)




def binaryFunc(driver, browser_config):
    try:
        BINARYSEARCH = 'Algorithms_csv_generated_files/TimeComplexity_O(log n)/binarysearch'
        if not os.path.exists(BINARYSEARCH):
            os.makedirs(BINARYSEARCH)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "method")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
    
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "binarysearchbtn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "binarysearchbtn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(BINARYSEARCH, f'{browser_config["browserName"]}_binarysearch.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)

    except Exception as e:
        print("An error occurred:", e)





def binaryrotatedFunc(driver, browser_config):
    try:
        BINARYSEARCHROTAT = 'Algorithms_csv_generated_files/TimeComplexity_O(log n)/binarysearchrotated'
        if not os.path.exists(BINARYSEARCHROTAT):
            os.makedirs(BINARYSEARCHROTAT)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "method")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
        time.sleep(1)
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "binrotatbtn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "binrotatbtn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(BINARYSEARCHROTAT, f'{browser_config["browserName"]}_binarysearchrotated.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)

    except Exception as e:
        print("An error occurred:", e)


def imageGenerationFunc(driver, browser_config):
    try:
        IMG_GEN_FOLDER = 'Algorithms_csv_generated_files/TimeComplexity_O(n log n)/image-generation'
        if not os.path.exists(IMG_GEN_FOLDER):
            os.makedirs(IMG_GEN_FOLDER)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "implementationSelect")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
        time.sleep(1)
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "sortButton")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "sortButton")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(IMG_GEN_FOLDER, f'{browser_config["browserName"]}_image_generation_sort.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)

    except Exception as e:
        print("An error occurred:", e)




#Quick sortalgorithm automation
def quickSortFunc(driver, browser_config):
    try:
        QUICK_SORT = 'Algorithms_csv_generated_files/TimeComplexity_O(n log n)/quick_sort'
        if not os.path.exists(QUICK_SORT):
            os.makedirs(QUICK_SORT)
        input_numbers = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "inputArray")))
        read_numbers_and_send_keys("random.txt", input_numbers)
        time.sleep(1)
        combo_box = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "method")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
        time.sleep(1)
        webassembly_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "quick_btn")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(100):
            button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "quick_btn")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timetaken")))
            time.sleep(1)
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(QUICK_SORT, f'{browser_config["browserName"]}_quicksort.csv')
        time.sleep(2)
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)

    except Exception as e:
        print("An error occurred:", e)
