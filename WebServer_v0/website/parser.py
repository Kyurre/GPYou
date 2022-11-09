import pandas as pd

path = 'csv/gpu.csv'
results_path = 'csv/results.csv'

# creates a results.csv that is cleaner and does not contain headers. It is ready to scrape.
df = pd.read_csv(path)
# df.to_csv(results_path, sep='\t', header=None, mode='a')


manufaturer_names = ['nvidia', 'asus', 'msi', 'evga', 'maxsun', 'amd']
memory_size = ['24gb', '16gb', '12gb', '11gb', '10gb', '8gb', '6gb', '4gb']
model_name = ['1030']

manufaturer = []
memory = []
model = []


temp = df['Description'][0].split()
for i, j in enumerate(temp):
    # print(j.lower())
    if j.lower() in manufaturer_names:
        manufaturer.append(j)
    if j.lower() in memory_size:
        memory.append(j)

print(manufaturer)
print(memory)

# for line_count, _ in enumerate(df):
# print(df['Description'][line_count].split())


# reads results.csv into a list of split keys
# with open(results_path) as fp:
#line = fp.readlines()
# print(line)

# Split will make it into a tuple
# print(line[0].split())

# Reads and prints tuples in line
# for data in line:
#    print(data.split())
