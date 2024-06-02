import pandas as pd

file_path = 'recalls_and_times_bit_sampling.csv'
data = pd.read_csv(file_path)

p = []
x = []

for params in data['Parameters']:
    parts = params.split(',')
    p.append(int(parts[0]))
    x.append(int(parts[1]))

p_series = pd.Series(p)
x_series = pd.Series(x)

mean_p = p_series.mean()
median_p = p_series.median()
std_p = p_series.std()

mean_x = x_series.mean()
median_x = x_series.median()
std_x = x_series.std()

print("Mean of p:", mean_p)
print("Median of p:", median_p)
print("Standard Deviation of p:", std_p)

print("Mean of x:", mean_x)
print("Median of x:", median_x)
print("Standard Deviation of x:", std_x)
