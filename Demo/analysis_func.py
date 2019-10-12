import pandas as pd
from scipy.stats import pearsonr

life_expectancy = pd.read_csv("Resources/life_expectancy.csv", encoding="ISO-8859-1")[["Country", "2017"]]

#Change column names for clarity
life_expectancy = life_expectancy.rename(columns = {"Country": "Countries", "2017":"Expectancy 2017"})

def analysis(data_path):

    try:
        data = pd.read_csv(data_path)
    except:
        try:
            data = pd.read_csv(data_path, encoding="ISO-8859-1")
        except:
            print("Error: It was not possible to read the CSV file.")
            return

    #Inner join to ensure all the countries are the same in both dataframes
    try:
        joint_data = life_expectancy.merge(data, on="Countries", how="inner")
    except:
        print("Error: It was not possible to merge the data. Please check column names on your data file.")

    try:
        for column in joint_data.columns[2:]:
            
            joint_data[column] = pd.to_numeric(joint_data[column])
    except:
        print("Error: Could not convert dataset columns to float values. Please check for missing values in your data.")
        return
    
    # Just in case there's still missing data
    joint_data = joint_data.dropna()

    # Create empty lists to keep track of values
    coeffs = []
    p_values = []

    # Get all the years we will be using for our analysis
    years = joint_data.columns[2:]

    # Get the coefficients and the p-values
    for year in years:
        coeff, p = pearsonr(joint_data["Expectancy 2017"], joint_data[year])
        coeffs.append(coeff)
        p_values.append(p)

    return coeffs, p_values, len(joint_data)