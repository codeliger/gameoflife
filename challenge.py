import datetime
from math import ceil, floor

'''convert unix timestamp to iso time'''
def ts_to_iso(ts):
    return datetime.datetime.fromtimestamp(ts).isoformat()


''' calulates a percentile according to wikipedia'''
def percentile(percentile, number_of_elements):
    return (percentile / 100) * number_of_elements

'''Rounds everything to a whole number or a whole number plus .5'''
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
    # print('Rounding',n,rounded)
    return rounded

''' applies a percentile to a dictionary of values
 and iterates until the percentiles bracket is found '''
def percentile_of_dict(counters: dict, count: int):
    active_counters = [(x, counters[x]) for x in counters if counters[x] > 0]
    tmp_count = 0
    for ind,counter in enumerate(active_counters):
        tmp_count ++ counter[1]
        # print(counter[0],'has',tmp_count)
    percentile_index = percentile(90, count)
    # print('calculated percentile:',percentile_index)
    bracket = 0
    # aggregate each amount of requests per response time until the number is
    # in the percentile calculated on the total amount of requests
    for idx,counter in enumerate(active_counters):
        bracket += counter[1]
        # print(idx,'index',counter[0],'is for',(counter[0]*5)/10,'searching with',percentile_index,'in',bracket)
        if bracket >= percentile_index:
            # print('found bracket',bracket,percentile_index)
            return (counter[0] * 5) / 10
    raise ValueError('The percentile category could not be found in the dictionary.')

''' creates a dict with 300 values representing
 0 to 150 with .5 increments in between '''
def initialize_counter():
    requests_count = dict()
    for i in range(0, 301, 1):
        requests_count[i] = 0
    return requests_count

''' Converts a line from a log file into a
timestamp and request processing time'''
def process_request(raw_request: str)->tuple:
    split_request = raw_request.split(' ')
    raw_ts = split_request[0]
    raw_rpt = split_request[1]
    return float(raw_ts), float(raw_rpt)

''' Forms a string that contains the minute timestamp
 and 90th percentile of response processing time '''
def get_timestamp_percentile(requests_count, count, minute_ts):
    percentile = percentile_of_dict(requests_count, count)
    iso = ts_to_iso(minute_ts)
    return '{0}Z {1}'.format(iso, percentile)

''' Takes lines of user input and processes request processing time'''
def process_request_log():
    requests_count = initialize_counter()
    # the previous ts stored, to compare difference in seconds
    previous_ts = None
    # the first ts on the minute for every group of results
    minute_ts = None
    # how many requests in the log file total
    count = 0
    # Terminates the program when input is not recieved
    input_found = True

    request_outputs = []

    while input_found:
        try:
            raw = input()
        except EOFError:
            input_found = False

        if raw == '':
            input_found = False

        try:
            ts, rpt = process_request(raw)
        except:
            input_found = False

        if input_found:
            if rpt < 0 or rpt > 150:
                # print('discarding response time of',rpt)
                continue

            if minute_ts is None:  # no minute found yet
                if ts % 60 == 0:  # beginning of minute found
                    minute_ts = ts
                    # print('starting first minute')
            else:
                # minute found and previously set
                if minute_ts != ts and ts % 60 == 0:
                    # print('ending minute')
                    # calculate percentile and output
                    request_outputs.append(get_timestamp_percentile(requests_count, count, minute_ts))
                    minute_ts = ts # set new minute 
                    # reset counters for next minute
                    for c in requests_count:
                        requests_count[c] = 0
                    count = 0
            # first ts inputted
            if previous_ts is None:
                # print('setting previous_ts')
                previous_ts = ts
            elif abs(ts - previous_ts) > 60: # discard requests not related to the minute being evaluated
                # print('discarding',ts,previous_ts,ts-previous_ts)
                continue
            rounded_rpt = half_round(rpt)
            # calculate the index between 1 and 300
            rpt_index = (rounded_rpt * 10) / 5
            # print('incrementing',rounded_rpt,rpt_index)
            requests_count[rpt_index] += 1
            count += 1
            previous_ts = ts
            # print(count)
        elif count > 0:
            # print('no input but count',count)
            request_outputs.append(get_timestamp_percentile(requests_count, count, minute_ts))
    return request_outputs

if __name__ == '__main__':
    requests = process_request_log()
    for request in requests:
        print(request)
