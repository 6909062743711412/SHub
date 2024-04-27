import requests
import pandas as pd
from io import BytesIO
def fetchExcelData(url):     # Fetch Data from URL
    try:
        response = requests.get(url)
        response.raise_for_status()   # Raise error for bad responses
        return response.content
    except requests.exceptions.RequestException as e:   # Error API
        print("Error fetch data:", e)
        return None

def filterData(dataframe, feature, threshold):
    try:
        filtered_df = dataframe[dataframe[feature] > threshold]  # All raws of Sales column have the value > threshold
        return filtered_df
    except Exception as e:
        print("Error filtering data:", e)
        return None

def saveFilteredData(filtered_df, output_file):
    try:
        filtered_df.to_excel(output_file, index=False)
        print("Filtered data saved successfully.")
    except Exception as e:
        print("Error saving filtered data:", e)


# ===============================================================
excelUrl = "https://go.microsoft.com/fwlink/?LinkID=521962"
excelData = fetchExcelData(excelUrl)
feature = ' Sales'
threshold = 50000

if excelData is not None:
    print("Excel data taken successfully.")
    dataframe = pd.read_excel(BytesIO(excelData))
    # print(dataframe)     # Print all data
    if dataframe is not None:
        filtered_df = filterData(dataframe, feature, threshold)
        if filtered_df is not None:     # Checked filtered_data successfully
            #  Save the filtered data
            output_file = "filtered_data.xlsx"
            saveFilteredData(filtered_df, output_file)
else:
    print("Failed to taken Excel data. Exiting.")

