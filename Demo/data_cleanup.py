import pandas as pd
import numpy as np
import csv

bmi_data_path = "Resources/bmi_data.csv"
data_array = np.array([])
countries = []

with open(bmi_data_path) as data_file:
    csv_reader = csv.reader(data_file, delimiter=',')

    # Skip headers
    next(csv_reader)
    next(csv_reader)
    next(csv_reader)
    next(csv_reader)

    for line in csv_reader:
        stop = len(line)
        both_ind = range(1, stop, 3)

        try:
            both_data = [float(line[x].split(" ")[0]) for x in both_ind][::-1] #Reverse list because Data starts in 2016 and goes backwards
            if data_array.shape[0] == 0:
                 data_array = np.append(data_array, both_data)
            else:
                data_array = np.vstack((data_array, both_data))
            
            countries.append(line[0])

        except:
            continue

bmi_dataframe = pd.DataFrame(data_array, columns = range(1975,2017))

bmi_dataframe["Countries"] = countries

# Change order of columns so that "Countries" is first
cols = bmi_dataframe.columns.tolist()
cols = cols[-1:] + cols[:-1]
bmi_dataframe = bmi_dataframe[cols]

bmi_dataframe.to_csv("Resources/bmi_data_clean.csv", index = False)