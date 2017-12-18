from math import ceil,floor
import operator,datetime

def percentile(p,n):
  return (p / 100) * (n+1)

# 1 = 1, 1.2 = 1, 1.25 = 1.5, 1.7 = 1.5, 1.75 = 2
def half_round(n):
    fraction = n % 1
    if fraction == 0:
      rounded = n
    elif fraction >= 0.75:
      rounded = ceil(n)
    elif fraction < 0.25:
      rounded = floor(n)
    else:
      rounded = (n - n % 1) + .5
    return rounded

counters = dict()

# 300 * 5 = 1500 meaning each 5 represents .5 miliseconds
for i in range(1,301,1):
  counters[i] = 0

last_ts = 0
minute_ts = 0
count = 0

while True:

    raw_input = input("ts rpt:")

    if raw_input == '':
      break

    split_input = raw_input.split(' ')

    raw_ts = split_input[0] #timestamp
    raw_rpt = split_input[0] #request processing time
    
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
    count += 1

# terminated

if count == 0:
  print('Exiting')
  exit()

try:
  iso8601 = datetime.datetime.fromtimestamp(minute_ts).isoformat()
except Exception as e:
  print('minute_ts:',minute_ts,e)


# create a list of only the values greater than 0 (possibly more effecient, maybe not)
active_counters = [(x,counters[x]) for x in counters if counters[x] > 0 ]
active_counters.sort(key=lambda tup: tup[1])

# count total requests
percentile_index = half_round(percentile(90,count))

# use the natural logic of the ordered list to find which counter bracket the percentile falls into
bracket = 0
for counter in active_counters:
  bracket += counter[1]
  if bracket >= percentile_index:
    print(iso8601,(counter[0] * 5) / 10)
    exit()
    
    



    


      

    






    

