
from connections import get_access_token
import json
import pandas as pd
import requests
import schedule
import time
type,token=get_access_token()
bearer=f'{type} {token}' 
variable_folder='RetailStores'
# variable_folder='RetailPosBatches2'
url=f"https://amtrakdev106c5dd72b7ca8401cdevaos.axcloud.dynamics.com/data/{variable_folder}/"
response=requests.get(url,headers={'Authorization': bearer})
response_dict = response.json()
with open("response.json") as f:
    json_data=json.load(f)
# data=json.dumps(response_dict, indent=4, sort_keys=True)
# with open("sample.json","w") as outfile:
#     outfile.write(data)


# while True:
#     schedule.run_pending()
#     time.sleep(1)