import pandas as pd
import os

# takes path to a csv
path = 'WebServer_v0/website/csv/gpu.csv'

# Master records to append to
manufaturer = []
memory = []
model = []
gpu_suffix = []
price = []
URL = []


def AmazonParser(path):
    # results_path = 'WebServer_v0/website/csv/results.csv'

    # Get current working directory
    #cwd = os.getcwd()
    #files = os.listdir(cwd)
    #print(f"Files in {cwd}: {files}")

    # creates a results.csv that is cleaner and does not contain headers. It is ready to scrape.
    df = pd.read_csv(path)
    # df.to_csv(results_path, sep='\t', header=None, mode='a')

    # List of details to compare to
    manufaturer_names = ['nvidia', 'asus',
                         'msi', 'evga', 'maxsun', 'amd', 'zotac']
    memory_size = ['24gb', '16gb', '12gb', '11gb', '10gb', '8gb', '6gb', '4gb']
    model_name = ['1030', '1050', '1650', '1660', '1080', '1070',
                  '2060', '2070', '2080', '3060', '3070', '3080']
    gpu_model_suffix = ['ti', 'super']

    for len_count, _ in enumerate(df['Description']):

        temp_manufaturer = []
        temp_memory = []
        temp_model = []
        temp_suffix = []

        temp = df['Description'][len_count].split()
        # print(df['Description'][line_count].split())
        for i, j in enumerate(temp):
            # print(j.lower())
            if j.lower() in manufaturer_names:
                temp_manufaturer.append(j)
            if j.lower() in memory_size:
                temp_memory.append(j)
            if j.lower() in model_name:
                temp_model.append(j)
            if j.lower() in gpu_model_suffix:
                temp_suffix.append(j)

        try:
            manufaturer.append(temp_manufaturer[0])
        except:
            manufaturer.append('')

        try:
            memory.append(temp_memory[0])
        except:
            memory.append('')

        try:
            model.append(temp_model[0])
        except:
            model.append('')

        try:
            gpu_suffix.append(temp_suffix[0])
        except:
            gpu_suffix.append('')

    # Print master record
    # print(len(manufaturer))
    # print(len(memory))
    # print(len(model))
    # print(len(gpu_suffix))


def getPrice():
    df = pd.read_csv(path)
    for len_count, cost in enumerate(df['Price']):
        temp_price = []
        temp_price.append(cost)
        try:
            price.append(temp_price[0])
        except:
            price.append('')

    # print(len(price))


def getURL():
    df = pd.read_csv(path)
    for len_count, link in enumerate(df['Url']):
        temp_URL = []
        temp_URL.append(link)

        try:
            URL.append(temp_URL[0])
        except:
            URL.append('')

    # print(URL)
    # print(len(URL))


def createAmazonTuple():
    AmazonParser(path)
    getPrice()
    getURL()
    records = []
    store = 'Amazon'
    for i in range(0, len(manufaturer)):
        result = (store, model[i] + gpu_suffix[i],
                  manufaturer[i], memory[i], price[i], URL[i])
        records.append(result)

    # print(records)
    return records

# Use this to run the parser.py locally to test that it prints a tuple
# createAmazonTuple()
