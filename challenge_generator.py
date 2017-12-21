import random, sys
import challenge
tsfile = open('timestamp.txt','w')
start_ts = 962668800

def output(p,r):
    return ('{0} {1}\n'.format(r,challenge.half_round(p)))

temp_ts = None
for x in range (1,11):
    for i in range(1,11):
        p = random.uniform(0,200) # extra room for invalid input
        if i == 10:
            start_ts += 60 - (start_ts % 60)
            print(output(p,start_ts))
            tsfile.write(output(p,start_ts))
        elif temp_ts is not None:
            print(output(p,temp_ts))
            tsfile.write(output(p,temp_ts))
            temp_ts = None
        else:
            print(output(p,start_ts))
            tsfile.write(output(p,start_ts))

        r = random.randint(1,100)
        if r <= 40 and start_ts % 60 > 1:
            # decrement second by 1
            sub =  random.randint(1,(start_ts % 60)-1)
            temp_ts = start_ts - sub
        else:
            # increment second by 1
            start_ts += 1


        


        
        


        



        
    
    