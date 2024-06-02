import csv
import matplotlib.pyplot as plt

def read_csv(file_path):
    recalls = []
    recalls_per_second = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            recalls.append(float(row["Recall (%)"]))
            recalls_per_second.append(float(row["Recalls per Second"]))
    return recalls, recalls_per_second

csv_file_1 = 'best_recalls_per_second_bit_sampling.csv'
csv_file_2 = 'best_recalls_per_second.csv'

recalls_1, recalls_per_second_1 = read_csv(csv_file_1)
recalls_2, recalls_per_second_2 = read_csv(csv_file_2)

plt.figure(figsize=(10, 6))
plt.scatter(recalls_1, recalls_per_second_1, c='blue', label='Bit Sampling')
plt.plot(recalls_1, recalls_per_second_1, c='blue', label='Bit Sampling')
plt.scatter(recalls_2, recalls_per_second_2, c='red', label='LSVF')
plt.plot(recalls_2, recalls_per_second_2, c='red', label='LSVF')
plt.title('Recall vs Queries per Second')
plt.xlabel('Recall (%)')
plt.ylabel('Queries per Second')
plt.grid(True)
plt.legend()
plt.show()