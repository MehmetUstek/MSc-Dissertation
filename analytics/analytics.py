from collections import Counter
import matplotlib.pyplot as plt

from utils.load_json_based_on_extension_type import load_json_based_on_extension_type


def histogram_of_frequent_vulnerabilities(vulnerability_counts, title,file_extension):
    # Data for the histogram
    error_numbers = list(vulnerability_counts.keys())
    counts = list(vulnerability_counts.values())

    # Creating the histogram
    plt.figure(figsize=(10, 6))
    bars = plt.bar(error_numbers, counts, color='blue')

    plt.xlabel('Error Number')
    plt.ylabel('Number of Files with Error')
    plt.title(title)
    plt.xticks(error_numbers)  # Ensure each error number is labeled

    error_descriptions = load_json_based_on_extension_type(file_extension)
    
    for bar, (error_number, count) in zip(bars, vulnerability_counts.items()):
        plt.text(bar.get_x() + bar.get_width()/2, 10, f'{error_descriptions[error_number]}', 
            va='bottom', ha='center', color='white', rotation=90, fontsize=7)

    plt.show()


def most_frequent_vulnerabilities_in_files(vulnerability_counts, title, file_extension):
    print("vulnerability_counts_düz", vulnerability_counts)
    sorted_vulnerability_counts = {k: v for k, v in sorted(vulnerability_counts.items(), key=lambda item: int(item[0]))}
    print("vulnerability_counts",sorted_vulnerability_counts)
    histogram_of_frequent_vulnerabilities(sorted_vulnerability_counts, title, file_extension)

