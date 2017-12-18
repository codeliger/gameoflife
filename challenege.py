from math import ceil,floor
import operator,datetime

def percentile(p,n):
  return p / 100 * (n+1)

def half_round(n):
    fraction = n % 1
    if fraction > 0.5:
      rounded = ceil(n)
    elif fraction < 0.5:
      rounded = floor(n)
    else:
      rounded = n



counters = dict()

# 300 * 5 = 1500 meaning each 5 represents .5 miliseconds
for i in range(1,301,1):
  counters[i] = 0

terminate = False

last_ts = 0
minute_ts = 0

while terminate == False:

    raw_ts = input('Timestamp:')
    
    if raw_ts == '':
      terminate = True
      continue

    raw_rpt = input('Request Processing Time:')

    # stop when empty
    if raw_rpt == '':
      terminate = True
      continue
    
    ts = float(raw_ts)
    rpt = float(raw_rpt)

    if rpt == 0 or rpt > 150:
      continue

    # if its the first request 
    if last_ts == 0:
      # if its not the first request of the timestamps minute keep skipping
      if ts % 60 != 0:
        continue
      minute_ts = ts
      last_ts = ts

    # if request doesnt belong to minute discard it
    if ts - last_ts > 60:
        continue

    rounded_rpt = half_round(rpt)

    # calculate the index between 1 and 300
    rpt_index = (rounded_rpt * 10) / 5

    counters[rpt_index] += 1

# terminated

#calculate percentile
total_requests = sum(counters)
sorted_counters = sorted(counters.items(), key=operator.itemgetter(1))
print(counters)
percentile_index = half_round(percentile(90,total_requests))

iso8601 = datetime.datetime.fromtimestamp(minute_ts).isoformat()
print(iso8601,counters[percentile_index])





    


      

    






    

