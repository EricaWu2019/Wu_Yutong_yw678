import pandas, numpy

### Train Data Wrangling ###
# Open raw Train data
csvPath = '/Users/Meinertsen/PycharmProjects/Taxi/'
dtrain = pandas.DataFrame(pandas.read_csv(csvPath +"train.csv"))
# Prepare Train data
dtrain["pickup_datetime"] = pandas.to_datetime(dtrain["pickup_datetime"])
dtrain["dropoff_datetime"] = pandas.to_datetime(dtrain["dropoff_datetime"])
dtrain["Month"]=pandas.to_datetime(dtrain["pickup_datetime"]).dt.month
dtrain["Week"]=pandas.to_datetime(dtrain["pickup_datetime"]).dt.week
dtrain["Weekday"]=pandas.to_datetime(dtrain["pickup_datetime"]).dt.weekday_name
dtrain["Hour"]=pandas.to_datetime(dtrain["pickup_datetime"]).dt.hour
# Save wrangled Train data
dtrain.to_csv(csvPath + "dtrain.csv") # Save to csv

### Test Data Wrangling ###
# Open raw Test data
csvPath = '/Users/Meinertsen/PycharmProjects/Taxi/'
dtest = pandas.DataFrame(pandas.read_csv(csvPath +"test.csv"))
# Prepare Train data
dtest["pickup_datetime"] = pandas.to_datetime(dtrain["pickup_datetime"])
#dtrain["dropoff_datetime"] = pandas.to_datetime(dtrain["dropoff_datetime"])
dtest["Month"]=pandas.to_datetime(dtest["pickup_datetime"]).dt.month
dtest["Week"]=pandas.to_datetime(dtest["pickup_datetime"]).dt.week
dtest["Weekday"]=pandas.to_datetime(dtest["pickup_datetime"]).dt.weekday_name
dtest["Hour"]=pandas.to_datetime(dtest["pickup_datetime"]).dt.hour
# Save wrangled Test data
dtest.to_csv(csvPath + "dtest.csv") # Save to csv

### Weather Data Wrangling ###
# Open raw Weather data
csvPath = '/Users/Meinertsen/PycharmProjects/Weather/'
dweath = pandas.DataFrame(pandas.read_csv(csvPath + "2016Weather" + ".csv"))
# Prepare Weather data
dweath['Datetime'] = pandas.to_datetime(dweath["Datetime"])
dweath=dweath.rename(columns={'Datetime': 'pickup_datetime'}) # Renames Datetime column to pickup_datetime
dweath = dweath.replace(-999.0, numpy.nan)
dweath = dweath.replace(-9999.0, numpy.nan)
dweath = dweath.drop_duplicates(subset='pickup_datetime', keep='last')
dweath.sort_values(by='pickup_datetime', inplace=True)
# Save wrangled Weather data
csvPath = '/Users/Meinertsen/PycharmProjects/Taxi/'
pandas.DataFrame(dweath).to_csv(csvPath + "Weather" + ".csv", header=True, index=False, encoding='utf-8') # Save to csv

# Sort data before merge
dtrain.sort_values(by='pickup_datetime', inplace=True)
dtest.sort_values(by='pickup_datetime', inplace=True)
dweath.sort_values(by='pickup_datetime', inplace=True)
dmerge=pandas.merge_asof(dtrain,dweath, on="pickup_datetime", tolerance=pandas.Timedelta('31m'))
tmerge=pandas.merge_asof(dtest,dweath, on="pickup_datetime", tolerance=pandas.Timedelta('31m'))


# Save merged data
csvPath = '/Users/Meinertsen/PycharmProjects/Taxi/'
dmerge.to_csv(csvPath + "dmerge" + ".csv", header=True, index=False, encoding='utf-8')
tmerge.to_csv(csvPath + "tmerge" + ".csv", header=True, index=False, encoding='utf-8')
