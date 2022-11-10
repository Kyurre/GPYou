import pandas as pd
import os

def AmazonParser():
    path = 'WebServer_v0/website/csv/gpu.csv'
    results_path = 'WebServer_v0/website/csv/results.csv'


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
    model_name = ['1030', '1050', '1660', '1080', '1070',
                  '2060', '2070', '2080', '3060', '3070', '3080']


    # Master records to append to
    manufaturer = []
    memory = []
    model = []

    '''
    temp_manufaturer = []
    temp_memory = []
    temp_model = []

    # Use the colum name description and split text into list
    temp = df['Description'][3].split()
    print(temp)
    for i, j in enumerate(temp):
        # print(j.lower())
        if j.lower() in manufaturer_names:
            temp_manufaturer.append(j)
        if j.lower() in memory_size:
            temp_memory.append(j)
        if j.lower() in model_name:
            temp_model.append(j)

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
    '''

    for len_count, _ in enumerate(df['Description']):

        temp_manufaturer = []
        temp_memory = []
        temp_model = []

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


    # Print master record
    print(len(manufaturer))
    print(len(memory))
    print(len(model))

    
    # reads results.csv into a list of split keys
    # with open(results_path) as fp:
    #line = fp.readlines()
    # print(line)

    # Split will make it into a tuple
    # print(line[0].split())

    # Reads and prints tuples in line
    # for data in line:
    #    print(data.split())
