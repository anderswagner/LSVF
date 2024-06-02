import pandas as pd

file_path = 'recalls_and_times.csv'
data = pd.read_csv(file_path)

filtered_data = data[data['Recall (%)'] == 100.0]

mean_recalls_per_second = filtered_data['Recalls per Second'].mean()
median_recalls_per_second = filtered_data['Recalls per Second'].median()
std_recalls_per_second = filtered_data['Recalls per Second'].std()

print("Mean of Recalls per Second:", mean_recalls_per_second)
print("Median of Recalls per Second:", median_recalls_per_second)
print("Standard Deviation of Recalls per Second:", std_recalls_per_second)

output_file_path = 'filtered_recalls_100.csv'
filtered_data[['Recalls per Second']].to_csv(output_file_path, index=False)
