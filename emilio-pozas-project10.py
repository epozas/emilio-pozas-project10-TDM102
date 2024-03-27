import pandas as pd
pd.set_option('display.max_column',None)
cols = [
    'DepDelay', 'ArrDelay', 'Distance',
    'CarrierDelay', 'WeatherDelay',
    'DepTime', 'ArrTime', 'Diverted', 'AirTime'
]

col_types = {
    'DepDelay': 'float64',
    'ArrDelay': 'float64',
    'Distance': 'float64',
    'CarrierDelay': 'float64',
    'WeatherDelay': 'float64',
    'DepTime': 'float64',
    'ArrTime': 'float64',
    'Diverted': 'int64',
    'AirTime': 'float64'
}
myDF = pd.read_csv("/anvil/projects/tdm/data/flights/2014.csv",usecols=cols, dtype=col_types)
myDF.head()

import numpy as np
mydelays = myDF['DepDelay'].to_numpy()
print('the shape of numpy array is: ', mydelays.shape, ' and the shape is:',mydelays.dtype)
mydelays_clean = np.nan_to_num(mydelays)
print("The average Departure Delay before adding 15 is: ", np.mean(mydelays_clean))
print("The average Departure Delay after adding 15 is: ", np.mean(mydelays_clean + 15))

myarrivaldelays = myDF['ArrDelay'].to_numpy()
myarrivaldelays_clean = np.nan_to_num(myarrivaldelays)
print("Max Arrival Delay: ", np.max(myarrivaldelays_clean), " minutes")
print("Min Arrival Delay: ", np.min(myarrivaldelays_clean), " minutes")

import time
start_time = time.time()

delayed_flights = myDF[(myDF['DepDelay'] > 60) | (myDF['ArrDelay'] > 60)]
my_avg_distance = delayed_flights['Distance'].mean()
print(f"The average flight distance for the delayed flights is {my_avg_distance}.")

end_time = time.time()
print(f"Used time is {end_time - start_time}")

start_time = time.time()

depdelay_array = myDF["DepDelay"].to_numpy()
arrdelay_array = myDF["ArrDelay"].to_numpy()
distance_array = myDF["Distance"].to_numpy()

filtered_distance = distance_array[(depdelay_array > 60) | (arrdelay_array > 60)]
avg_distance = np.mean(filtered_distance)
print(f"The average flight distance for the delayed flights is {avg_distance}.")

end_time = time.time()
print(f"Used time is {end_time - start_time}")