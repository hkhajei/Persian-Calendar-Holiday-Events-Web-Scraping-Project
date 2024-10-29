import requests
import pandas as pd

# URL of the API endpoint
api_url = "https://api.time.ir/v1/event/fa/events/calendar"


# Headers for the request
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Origin': 'https://new.time.ir',
    'Referer': 'https://new.time.ir/',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Api-Key': 'ZAVdqwuySASubByCed5KYuYMzb9uB2f7'
}

months=range(1,13)
years=range(1395,1404)
df=pd.DataFrame()
for year in years:
    for month in months:
        params = {
            'year': year,
            'month': month,
            'day': 0,
            'base1': 0,
            'base2': 1,
            'base3': 2
        }
        # Sending the GET request with headers
        response = requests.get(api_url, params=params, headers=headers)

        # Checking if the request was successful (status code 200)
        if response.status_code == 200:
            # Printing the response content (JSON data in this case)
            response_data=response.json()
            print(response_data)
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
        # Extracting the 'event_list' from the response data
        event_list = response_data['data']['event_list']

        # Creating a DataFrame from the 'event_list'
        new_df = pd.DataFrame(event_list)
        df=pd.concat([df,new_df],axis=0)
        # Display the DataFrame
        print(new_df)
df.to_csv('Holidays.csv',encoding='utf-8-sig',index=False)