import datetime
from math import ceil, floor


def percentile(percentile, number_of_elements):
  return (percentile / 100) * number_of_elements

'''Rounds all numbers to whole, whole or whole and a half numbers'''`
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

def percentile_of_dict(counters:dict, minute_timestamp):

  iso8601 = datetime.datetime.fromtimestamp(minute_timestamp).isoformat()
  # create a list of only the values greater than 0 (possibly more effecient, maybe not)
  active_counters = [(x, counters[x]) for x in counters if counters[x] > 0 ]
  active_counters.sort(key=lambda tup: tup[1])
  percentile_index = percentile(90,count)
  fraction = percentile_index % 1
  bracket = 0
  # aggregate each amount of requests per response time until the number is within the percentile calculated on the total amount of requests
  for counter in active_counters:
    bracket += counter[1]
    if bracket >= percentile_index:
      print(iso8601+'Z',(counter[0] * 5) / 10)
      break

def initialize_counter():
  requests_count = dict()
  # 300 * 5 = 1500 meaning each 5 representimestamp .5 miliseconds
  for i in range(0,301,1):
    requests_count[i] = 0
  return requests_count

if __name__ == '__main__':

  previous_timestamp = None #the previous timestamp stored, to compare difference in seconds
  minute_timestamp = None # the first timestamp on the minute for every group of resultimestamp
  count = 0 # how many requestimestamp in the log file total

  input_found = True # Terminates the program when input is not recieved

  while input_found:
      try:
          raw = input()
      except EOFError:
          input_found = False
      if raw == '':
          input_found = False

      if input_found:
        split_request = raw.split(' ')
        raw_timestamp = split_request[0] #timestamp
        raw_request_processing_time = split_request[1] #request processing time
        
        try:
          timestamp = float(raw_timestamp)
          request_processing_time = float(raw_request_processing_time)
        except:
          continue

        if request_processing_time < 0 or request_processing_time > 150:
          continue

        if minute_timestamp is None: # no minute found yet
          if timestamp % 60 == 0: # beginning of minute found
            print("setting minute timestamp for first time",timestamp)
            minute_timestamp = timestamp
        else:
          # minute found and previously set
          if minute_timestamp != timestamp and timestamp % 60 == 0:
            #calculate percentile and output
            percentile_of_dict(counters,minute_timestamp)
            minute_timestamp = timestamp
            #reset counters for next minute
            for c in counters:
              counters[c] = 0
            count = 0
        #first timestamp inputted
        if previous_timestamp is None:
          previous_timestamp = timestamp
        else:
          #discard requestimestamp not related to the minute being evaluated
          if timestamp - previous_timestamp > 60:
            continue 
        rounded_request_processing_time = half_round(request_processing_time)
        # calculate the index between 1 and 300
        request_processing_time_index = (rounded_request_processing_time * 10) / 5
        counters[request_processing_time_index] += 1
        count += 1
        previous_timestamp = timestamp
      elif count > 0:
        percentile_of_dict(counters,minute_timestamp)
        exit()
            
