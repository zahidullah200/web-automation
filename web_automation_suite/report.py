from web_automation_suite.browsers_links_and_pageURL import *
from web_automation_suite.merge import merge_pdfs

def generate_report(metric_name, csv_folder, report_title):
    browsers = ['chrome', 'firefox', 'MicrosoftEdge']
    times = {browser: read_csv(os.path.join(csv_folder, f'{browser}_{metric_name}.csv')) for browser in browsers}
    stats = {browser: calculate_stats(times[browser]) for browser in browsers}
    
    plot_graph(browsers, stats, metric_name)
    generate_pdf_report(metric_name, report_title, stats)

def read_csv(filename):
    wasm_times, js_times = [], []
    try:
        with open(filename, 'r') as csvfile:
            for _ in range(4):
                next(csvfile)
            reader = csv.DictReader(csvfile)
            for row in reader:
                wasm_times.append(float(row['Wasm_time_taken'].replace(' ms', '')))
                js_times.append(float(row['Js_time_taken'].replace(' ms', '')))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return wasm_times, js_times

def calculate_stats(times):
    wasm_mean = statistics.mean(times[0])
    wasm_median = statistics.median(times[0])
    js_mean = statistics.mean(times[1])
    js_median = statistics.median(times[1])
    return {'wasm_mean': wasm_mean, 'wasm_median': wasm_median, 'js_mean': js_mean, 'js_median': js_median}

def plot_graph(browsers, stats, metric_name):
    wasm_means = [stats[browser]['wasm_mean'] for browser in browsers]
    js_means = [stats[browser]['js_mean'] for browser in browsers]
    
    bar_width = 0.35
    index = range(len(browsers))
    
    plt.figure(figsize=(10, 6))
    plt.bar(index, wasm_means, bar_width, label='Wasm', color='blue')
    plt.bar([i + bar_width for i in index], js_means, bar_width, label='Js', color='orange')
    plt.xlabel('Browsers')
    plt.ylabel('Mean Time (ms)')
    plt.title(f'Comparison of Wasm and Js Performance Across Browsers for {metric_name}')
    plt.xticks([i + bar_width / 2 for i in index], ['Chrome', 'Firefox', 'Edge'])
    plt.legend()
    plt.grid(True)
    
    image_path = os.path.join('reports', f'{metric_name}.png')
    plt.savefig(image_path)
    plt.close()

def generate_pdf_report(metric_name, report_title, stats):
    pdf_file = os.path.join('reports', f'{metric_name}.pdf')
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    styles = getSampleStyleSheet()
    
    content = [Paragraph(report_title, styles["Title"]), Spacer(1, 20), Paragraph("Performance Statistics", styles["Heading1"])]
    
    for browser, browser_stats in stats.items():
        content.append(Paragraph(f"<b>{browser.capitalize()} Browser:</b><br/>"
                                 f"- Wasm Mean: {browser_stats['wasm_mean']:.3f}, Median: {browser_stats['wasm_median']:.3f}<br/>"
                                 f"- Js Mean: {browser_stats['js_mean']:.3f}, Median: {browser_stats['js_median']:.3f}<br/>", 
                                 styles["Normal"]))
        content.append(Spacer(1, 10))
    
    image_path = os.path.join('reports', f'{metric_name}.png')
    content.append(Image(image_path, width=400, height=300))
    
    doc.build(content)
    print(f"PDF report for {metric_name} generated successfully.")

def generate_reports():
    reports_info = {
        'power': ('Power of a number Report in 3 Major Browsers o(1)', 'Algorithms_csv_generated_files/TimeComplexity_o(1)/power'),
        'summation': ('Summation of Numbers Report in 3 Major Browsers o(1)', 'Algorithms_csv_generated_files/TimeComplexity_o(1)/summation'),
        'reverseArray': ('Reverse Array Report in 3 Major Browsers o(n)', 'Algorithms_csv_generated_files/TimeComplexity_o(n)/reverse-array'),
        'threshold': ('Threshold Image Processing Report in 3 Major Browsers o(n)', 'Algorithms_csv_generated_files/TimeComplexity_o(n)/threshold'),
        'factorialcon': ('Factorial of a Number Report in 3 Major Browsers O(n!)', 'Algorithms_csv_generated_files/TimeComplexity_O(n!)/factorial'),
        'contpermutation': ('Continuous Permutation of Numbers Report in 3 Major Browsers O(n!)', 'Algorithms_csv_generated_files/TimeComplexity_O(n!)/permutation'),
        'bubble_sort': ('Bubble Sort of Numbers Report in 3 Major Browsers O(n^2)', 'Algorithms_csv_generated_files/TimeComplexity_O(n^2)/bubble'),
        'selectionsort': ('Selection Sort Report in 3 Major Browsers O(n^2)', 'Algorithms_csv_generated_files/TimeComplexity_O(n^2)/selectionsort'),
        'cubicpolynomial': ('Cubic Polynomial of Number Report in 3 Major Browsers O(n^3)', 'Algorithms_csv_generated_files/TimeComplexity_O(n^3)/cubicpoly'),
        'matrixmul': ('Matrix Multiplication Report in 3 Major Browsers O(n^3)', 'Algorithms_csv_generated_files/TimeComplexity_O(n^3)/matrixmul'),
        'nestloopmul': ('Nested Loop Multiplication Report in 3 Major Browsers O(n^4)', 'Algorithms_csv_generated_files/TimeComplexity_O(n^4)/nesloopmul'),
        'nestloopsum': ('Nested Loop Summation Report in 3 Major Browsers O(n^4)', 'Algorithms_csv_generated_files/TimeComplexity_O(n^4)/nesloosum'),
        'binarysearch': ('Binary Search Report in 3 Major Browsers O(log n)', 'Algorithms_csv_generated_files/TimeComplexity_O(log n)/binarysearch'),
        'binarysearchrotated': ('Binary Search Rotated Report in 3 Major Browsers O(log n)', 'Algorithms_csv_generated_files/TimeComplexity_O(log n)/binarysearchrotated'),
        'image_generation_sort': ('Image Generation and Sort Report in 3 Major Browsers O(n log n)', 'Algorithms_csv_generated_files/TimeComplexity_O(n log n)/image-generation'),
        'quicksort': ('Quick Sort Report in 3 Major Browsers O(n log n)', 'Algorithms_csv_generated_files/TimeComplexity_O(n log n)/quick_sort'),
    }
    
    for metric, (title, csv_folder) in reports_info.items():
        generate_report(metric, csv_folder, title)

    pdf_files = [os.path.join('reports', f'{metric}.pdf') for metric in reports_info.keys()]
    merge_pdfs(pdf_files, 'all_reports_combined.pdf')