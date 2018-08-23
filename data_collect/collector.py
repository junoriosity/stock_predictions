from yahoo_historical import Fetcher
import csv
import datetime
import os.path

fetch_list = ["^GSPC","^RUA","^RUT","IJR"]
store_file_list = ["SP500","RUSSELL3000","RUSSELL2000","SP-SMALL-CAP"]

f = open("/Users/ahsentob/stock_predictions/own_prediction/data_collect/complete_stock_data.txt",'r')
message = [line.rstrip('\n') for line in f]

fetch_list.extend(message)
store_file_list.extend(message)


now = datetime.datetime.now()
#time_list = [now.year-10,now.month,now.day]
time_list = [2005,1,1]

for i in range(len(fetch_list)):
    store_path = '/Users/ahsentob/stock_predictions/own_prediction/data_collect/historical_data/'+store_file_list[i]+'.csv'
    if os.path.exists(store_path):
        continue
    if i % 1 == 0:
        print(i)
        print(fetch_list[i])
    try:
        data = Fetcher(fetch_list[i], time_list)
        hist = data.getHistorical()
        hist.to_csv(store_path)
    except:
        print("Could not get data for "+fetch_list[i])
