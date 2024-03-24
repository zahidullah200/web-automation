import os
import csv
import statistics
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt

def generate_report(metric_name, csv_folder, report_title):
    # Define filenames of the CSV files for each browser
    chrome_csv = os.path.join(csv_folder, 'chrome_' + metric_name + '.csv')
    firefox_csv = os.path.join(csv_folder, 'firefox_' + metric_name + '.csv')
    edge_csv = os.path.join(csv_folder, 'MicrosoftEdge_' + metric_name + '.csv')

    # Read data from each CSV file
    chrome_wasm_times, chrome_js_times = read_csv(chrome_csv)
    firefox_wasm_times, firefox_js_times = read_csv(firefox_csv)
    edge_wasm_times, edge_js_times = read_csv(edge_csv)

    # Calculate statistics for each browser and for both Wasm and Js
    chrome_wasm_mean, chrome_wasm_median = calculate_stats(chrome_wasm_times)
    chrome_js_mean, chrome_js_median = calculate_stats(chrome_js_times)

    firefox_wasm_mean, firefox_wasm_median = calculate_stats(firefox_wasm_times)
    firefox_js_mean, firefox_js_median = calculate_stats(firefox_js_times)

    edge_wasm_mean, edge_wasm_median = calculate_stats(edge_wasm_times)
    edge_js_mean, edge_js_median = calculate_stats(edge_js_times)

    # Plotting the graph
    browsers = ['Chrome', 'Firefox', 'Edge']
    wasm_means = [chrome_wasm_mean, firefox_wasm_mean, edge_wasm_mean]
    js_means = [chrome_js_mean, firefox_js_mean, edge_js_mean]

    plt.figure(figsize=(10, 6))
    plt.plot(browsers, wasm_means, marker='o', color='blue', label='Wasm')
    plt.plot(browsers, js_means, marker='o', color='orange', label='Js')
    plt.xlabel('Browsers')
    plt.ylabel('Mean Time (ms)')
    plt.title(f'Comparison of Wasm and Js Performance Across Browsers for {metric_name}')
    plt.legend()
    plt.grid(True)
    
    # Define the path for saving the image
    image_path = os.path.join('reports', f'{metric_name}.png')
    plt.savefig(image_path)  

    # Generate PDF report
    pdf_file = os.path.join('reports', f'{metric_name}.pdf')
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    styles = getSampleStyleSheet()
    report_title = Paragraph(report_title, styles["Title"])
    doc_title = Paragraph("Performance Statistics", styles["Heading1"])

    data = [
        f"<b>Chrome Browser:</b><br/>"
        f"- Wasm Mean: {chrome_wasm_mean:.3f}, Median: {chrome_wasm_median:.3f}<br/>"
        f"- Js Mean: {chrome_js_mean:.3f}, Median: {chrome_js_median:.3f}<br/>",
        f"<b>Firefox Browser:</b><br/>"
        f"- Wasm Mean: {firefox_wasm_mean:.3f}, Median: {firefox_wasm_median:.3f}<br/>"
        f"- Js Mean: {firefox_js_mean:.3f}, Median: {firefox_js_median:.3f}<br/>",
        f"<b>Edge Browser:</b><br/>"
        f"- Wasm Mean: {edge_wasm_mean:.3f}, Median: {edge_wasm_median:.3f}<br/>"
        f"- Js Mean: {edge_js_mean:.3f}, Median: {edge_js_median:.3f}<br/>"
    ]
    report_data = [Paragraph(text, styles["Normal"]) for text in data]
    graph = Image(image_path, width=400, height=300)

    doc.build([report_title, Spacer(1, 20), doc_title, Spacer(1, 10)] + report_data + [Spacer(1, 20), graph])

    print("PDF report generated successfully.")

def read_csv(filename):
    wasm_times = []
    js_times = []
    try:
        with open(filename, 'r', newline='') as csvfile:
            # Skip the first 4 rows
            for _ in range(4):
                next(csvfile)
            
            reader = csv.DictReader(csvfile)
            for row in reader:
                wasm_time_str = row['Wasm_time_taken'].replace(' ms', '')  # Remove ' ms' suffix
                js_time_str = row['Js_time_taken'].replace(' ms', '')      # Remove ' ms' suffix
                wasm_times.append(float(wasm_time_str))
                js_times.append(float(js_time_str))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    
    return wasm_times, js_times

def calculate_stats(times):
    mean = statistics.mean(times)
    median = statistics.median(times)
    return mean, median

