import pandas as pd

file_path = 'recalls_and_times.csv'
df = pd.read_csv(file_path)

best_recalls = df.loc[df.groupby('Recall (%)')['Recalls per Second'].idxmax()]

output_file_path = 'best_recalls_per_second.csv'
best_recalls.to_csv(output_file_path, index=False)

file_path = 'recalls_and_times_bit_sampling.csv'
df = pd.read_csv(file_path)

best_recalls = df.loc[df.groupby('Recall (%)')['Recalls per Second'].idxmax()]

output_file_path = 'best_recalls_per_second_bit_sampling.csv'
best_recalls.to_csv(output_file_path, index=False)
