from random import randint,uniform

f = open('timestamp.txt','w')

start_ts = 962668800
last_ts = 962668800
minute_count = 1

while minute_count <= 10:
    delay = round(uniform(0,155),1)
    print(start_ts,delay)
    f.write('{0} {1}\n'.format(start_ts,delay))
    last_ts = start_ts
    seconds = start_ts % 60
    if seconds == 0:
        minute_count += 1
        start_ts += randint(1,60)
    else:
        remaining = 60 - seconds
        start_ts += randint(-1 * (seconds-1),remaining)
    


        
        


        



        
    
    