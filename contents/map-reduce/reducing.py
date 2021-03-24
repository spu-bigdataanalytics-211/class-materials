import json
import itertools

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))

sums = {}
sorted_map_file = 'pg2701.txt.map.sorted'
reduced_map_file = 'pg2701.txt.map.reduced'

previous = None
M = [None, 0]

def checkmax(key, sum):
    global m, M
    if M[1] < sum:
        M[1] = sum
        M[0] = key

try:
    in_file = open(sorted_map_file, 'r')
    for line in in_file:
        key, value = line.split('\t')
        
        if key != previous:
            if previous is not None:
                checkmax(previous, sum)
            previous = key
            sum = 0
            
        sum += int(value)
        
    checkmax(previous, sum)
    in_file.close()
except IOError:
    print("error performing file operation")
    
print("max: %s = %d" % (M[0], M[1]))
with open(reduced_map_file, 'w+') as stream:
    json.dump(take(10, sums.items()), stream, sort_keys=True)