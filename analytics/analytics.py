from collections import Counter
import matplotlib.pyplot as plt


def histogram_of_frequent_vulnerabilities(vulnerability_counts, title):
    # Data for the histogram
    error_numbers = list(vulnerability_counts.keys())
    counts = list(vulnerability_counts.values())

    # Creating the histogram
    plt.figure(figsize=(10, 6))
    plt.bar(error_numbers, counts, color='blue')

    plt.xlabel('Error Number')
    plt.ylabel('Number of Files with Error')
    plt.title(title)
    plt.xticks(error_numbers)  # Ensure each error number is labeled

    plt.show()


def most_frequent_vulnerabilities_in_files(vulnerability_counts, title):
    sorted_vulnerability_counts = {k: v for k, v in sorted(vulnerability_counts.items(), key=lambda item: int(item[0]))}
    print("vulnerability_counts",sorted_vulnerability_counts)
    histogram_of_frequent_vulnerabilities(sorted_vulnerability_counts, title)

