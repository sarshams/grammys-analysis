# get billboard data for range: 9/1/19 - 8/31/20

#import statements
import billboard as bb
import pandas as pd


def createDates():
    dateList = pd.date_range('2019-09-01', '2020-08-31').tolist()
    return [d.strftime('%Y-%m-%d') for d in dateList]

validDates = []
invalidDates = []
length = len(createDates())
count = 0

#first check if we have data for each date
for d in createDates():
    if len(bb.ChartData('hot-100', date=d)) > 0:        
        validDates.append(d)
    else:
        invalidDates.append(d)
    count += 1
    print(str(count) + "/" + str(length) + " done")
        

# chart = bb.ChartData('hot-100')
# print(chart.date)
# # for e in chart.entries:
# #     print(e.title)