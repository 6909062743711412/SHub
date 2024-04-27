import requests
import numpy as np
def calculate_sum1(data, l, r):
    return sum(data[l:r])
def calculate_sum2(data, l, r):
    even_sum = sum(data[i] for i in range(l, r, 2))
    odd_sum = sum(data[i] for i in range(l+1, r, 2))
    return even_sum - odd_sum
def fetchInputData(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching input data:", e)
        return None
def process_queries(data, queries):
    results = []
    for query in queries:
        queryType = query["type"]
        range_l, range_r = query["range"]
        if queryType == "1":
            result = calculate_sum1(data, range_l, range_r)
        elif queryType == "2":
            result = calculate_sum2(data, range_l, range_r)
        results.append(result)
    return results

def send_output_data(url, token, results):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(url, json=results, headers=headers)
        response.raise_for_status()
        print("Output data sent successfully.")
    except requests.exceptions.RequestException as e:
        print("Error sending output data:", e)


# ===================
input_url = "https://share.shub.edu.vn/api/intern-test/input"
output_url = "https://share.shub.edu.vn/api/intern-test/output"

# Take input data
inputData = fetchInputData(input_url)

if inputData is not None:
    token = inputData.get("token")
    data = inputData.get("data")
    queries = inputData.get("query")

    results = process_queries(data, queries)
    print(results)
    send_output_data(output_url, token, results)
