from browser_links import *



def read_numbers_and_send_keys(filename, input_element):
    with open(filename, 'r') as file:
        numbers_str = file.read()

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
        writer.writerow([platform.system(), platform.processor(), str(round(psutil.virtual_memory().total / (1024.0 ** 3), 2)) + " GB"])
        writer.writerow(["Wasm_time_taken", "Js_time_taken"])
        for wasm_time, js_time in zip(webassembly_times, javascript_times):
            writer.writerow([wasm_time, js_time])
        time.sleep(1)


def bubleFunc(driver, browser_config):
    try:
        BUBBLE_FOLDER = 'bubble'
        if not os.path.exists(BUBBLE_FOLDER):
            os.makedirs(BUBBLE_FOLDER)
        
        bubble_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "b_sortt")))
        bubble_button.click()
        WebDriverWait(driver, 2).until(EC.url_to_be(BUBBLE_SORT_URL))
        input_numbers = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "inputNumbers")))
        read_numbers_and_send_keys("random.txt", input_numbers)
        time.sleep(1)
        combo_box = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "sortingMethod")))
        combo_box.click()
        option_webassembly = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//option[text()='WebAssembly']")))
        option_webassembly.click()
        webassembly_times = []
        for _ in range(10):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "buble_btn")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            webassembly_times.append(time_taken.text)
        
        combo_box.click()
        option_javascript = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//option[text()='JavaScript']")))
        option_javascript.click()
        javascript_times = []
        for _ in range(10):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "buble_btn")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            javascript_times.append(time_taken.text)
        
        time.sleep(1)
        file_path = os.path.join(BUBBLE_FOLDER, f'{browser_config["browserName"]}_bubble_sort.csv')
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)
        driver.get(MAIN_URL)
        time.sleep(1)
    
    except Exception as e:
        print("An error occurred:", e)


def imageGenerationFunc(driver, browser_config):
    try:
        IMG_GEN_FOLDER = 'image-generation'
        if not os.path.exists(IMG_GEN_FOLDER):
            os.makedirs(IMG_GEN_FOLDER)
        
        driver.get(IMG_GEN_URL)
        combo_box = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "wasm-js")))
        combo_box.click()
        option_webassembly = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//option[text()='Web Assembly']")))
        option_webassembly.click()
        webassembly_times_img = []
        for _ in range(5):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "sort_btn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            webassembly_times_img.append(time_taken.text)
        combo_box.click()
        option_javascript = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//option[text()='javascript']")))
        option_javascript.click()
        javascript_times_img = []
        for _ in range(5):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "sort_btn")))
            button.click()
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            javascript_times_img.append(time_taken.text)
        
        time.sleep(1)
        file_path_img = os.path.join(IMG_GEN_FOLDER, f'{browser_config["browserName"]}_image_generation_sort.csv')
        write_csv_file(file_path_img, driver, browser_config, webassembly_times_img, javascript_times_img)
        
        driver.get(MAIN_URL)
        time.sleep(1)
    
    except Exception as e:
        print("An error occurred:", e)




#Revers algorithm function
def reverseFunc(driver,browser_config):
    try:
        REVERSE_ARRAY = 'reverse-array'
        if not os.path.exists(REVERSE_ARRAY):
            os.makedirs(REVERSE_ARRAY)
    
        reverse_array = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "r_array")))
        reverse_array.click()
        time.sleep(1)
        input_numbers = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "inputArray")))
        read_numbers_and_send_keys("random.txt", input_numbers)
        combo_box = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "method")))
        combo_box.click()
        option_webassembly = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "webassembly")))
        option_webassembly.click()
    
        webassembly_times = []
        for _ in range(10):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "r_btn")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            webassembly_times.append(time_taken.text)

        option_webassembly = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "javascript")))
        option_webassembly.click()
        javascript_times = []
        for _ in range(10):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "r_btn")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(REVERSE_ARRAY, f'{browser_config["browserName"]}_reverseArray.csv')
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)


        driver.get(MAIN_URL)
        time.sleep(1)

    except Exception as e:
        print("An error occurred:", e)





#Threshold image processing function
def thresholdFunc(driver, browser_config):
    try:
        THRESHOLD = 'threshold'
        if not os.path.exists(THRESHOLD):
            os.makedirs(THRESHOLD)
        
        time.sleep(1)
        file_input = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'thre_btn')))
        file_input.click()
        file_input = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'thresholdImageInput')))
        file_path = os.path.abspath("images/coverimage2.jpg")
        file_input.send_keys(file_path)
        time.sleep(1)
        thr_combo = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'implementationSelect')))
        thr_combo.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//option[text()='WebAssembly']")))
        option_webassembly.click()
        webassembly_times_thre = []
        for _ in range(5):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "processButton")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeLabel")))
            webassembly_times_thre.append(time_taken.text)
        thr_combo.click()
        option_javascript = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//option[text()='JavaScript']")))
        option_javascript.click()
        javascript_times_thre = []
        for _ in range(5):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "processButton")))
            button.click()
            time.sleep(3)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeLabel")))
            javascript_times_thre.append(time_taken.text)
        time.sleep(1)
        file_path = os.path.join(THRESHOLD, f'{browser_config["browserName"]}_threshold.csv')
        write_csv_file(file_path, driver, browser_config, webassembly_times_thre, javascript_times_thre)

        
        driver.get(MAIN_URL)
        time.sleep(3)

    except Exception as e:
        print("An error occurred:", str(e))




def fiboFunc(driver, browser_config):
    try:
        FIBO_CAL = 'fibonacci'
        if not os.path.exists(FIBO_CAL):
            os.makedirs(FIBO_CAL)
        
        fibo_btn = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "fibo_btn")))
        time.sleep(1)
        fibo_btn.click()
        time.sleep(1)
        input_numbers = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "inputNumber")))
        input_numbers.send_keys(36)  # Change this value as needed
        time.sleep(1)
        combo_box = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "method")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "WebAssembly")))
        option_webassembly.click()
    
        webassembly_times = []
        for _ in range(10):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "fibo_calc_btn")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "JavaScript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(10):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "fibo_calc_btn")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "time_taken")))
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(FIBO_CAL, f'{browser_config["browserName"]}_fibonacci.csv')
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)


        driver.get(MAIN_URL)
        time.sleep(3)

    except Exception as e:
        print("An error occurred:", e)



#Quick sortalgorithm automation
def quickSort(driver, browser_config):
    try:
        QUICK_SORT = 'quick_sort'
        if not os.path.exists(QUICK_SORT):
            os.makedirs(QUICK_SORT)
        
        fibo_btn = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "quick_btn")))
        time.sleep(1)
        fibo_btn.click()
        time.sleep(1)
        input_numbers = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "inputArray")))
        read_numbers_and_send_keys("random.txt", input_numbers)
        time.sleep(1)
        combo_box = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "method")))
        combo_box.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "WebAssembly")))
        option_webassembly.click()
    
        webassembly_times = []
        for _ in range(10):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "quick_btn")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeLabel")))
            webassembly_times.append(time_taken.text)
        time.sleep(1)
        option_javascript = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "JavaScript")))
        option_javascript.click()
        javascript_times = []
        for _ in range(10):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "quick_btn")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "timeLabel")))
            javascript_times.append(time_taken.text)

        time.sleep(1)
        file_path = os.path.join(QUICK_SORT, f'{browser_config["browserName"]}_quicksort.csv')
        write_csv_file(file_path, driver, browser_config, webassembly_times, javascript_times)


        driver.get(MAIN_URL)
        time.sleep(3)

    except Exception as e:
        print("An error occurred:", e)



#Image convolution algorithm automation
def convolution(driver, browser_config):
    try:
        CONV = 'convolution'
        if not os.path.exists(CONV):
            os.makedirs(CONV)
        
        time.sleep(1)
        file_input = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'con_btn')))
        file_input.click()
        file_input = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'fileInput')))
        file_path = os.path.abspath("images/coverimage2.jpg")
        file_input.send_keys(file_path)
        time.sleep(1)
        thr_combo = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'implementationSelect')))
        thr_combo.click()
        time.sleep(1)
        option_webassembly = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//option[text()='WebAssembly']")))
        option_webassembly.click()
        webassembly_times_thre = []
        for _ in range(5):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "processButton")))
            button.click()
            time.sleep(1)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "performanceLabel")))
            webassembly_times_thre.append(time_taken.text)
        thr_combo.click()
        option_javascript = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//option[text()='JavaScript']")))
        option_javascript.click()
        javascript_times_thre = []
        for _ in range(5):
            button = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "processButton")))
            button.click()
            time.sleep(3)
            time_taken = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "performanceLabel")))
            javascript_times_thre.append(time_taken.text)
        time.sleep(1)
        file_path = os.path.join(CONV, f'{browser_config["browserName"]}_convolution.csv')
        write_csv_file(file_path, driver, browser_config, webassembly_times_thre, javascript_times_thre)

        
        driver.get(MAIN_URL)
        time.sleep(3)

    except Exception as e:
        print("An error occurred:", str(e))

