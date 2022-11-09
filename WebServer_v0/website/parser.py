import pandas as pd
import os

path = 'WebServer_v0/website/csv/gpu.csv'
results_path = 'WebServer_v0/website/csv/results.csv'


# Get current working directory
#cwd = os.getcwd()
#files = os.listdir(cwd)
#print(f"Files in {cwd}: {files}")

# creates a results.csv that is cleaner and does not contain headers. It is ready to scrape.
df = pd.read_csv(path)
# df.to_csv(results_path, sep='\t', header=None, mode='a')


manufaturer_names = ['nvidia', 'asus',
                     'msi', 'evga', 'maxsun', 'amd', 'zotac']
memory_size = ['24gb', '16gb', '12gb', '11gb', '10gb', '8gb', '6gb', '4gb']
model_name = ['1030', '1050', '1660', '1080', '1070',
              '2060', '2070', '2080', '3060', '3070', '3080']

manufaturer = ['msi', 'nvidia', 'asus']
memory = ['6gb',           '8gb']
model = ['1080', '2070', '3080']


temp = df['Description'][2].split()
print(temp)
for i, j in enumerate(temp):
    print(j.lower())
    if j.lower() in manufaturer_names:
        manufaturer.append(j)
    if j.lower() in memory_size:
        memory.append(j)
    else:
        memory.append('')
    if j.lower() in model_name:
        model.append(j)


print(manufaturer)
print(memory)
print(model)

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
