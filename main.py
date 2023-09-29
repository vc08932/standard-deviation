import statistics
import math

def sd_p(item):
    mean = statistics.mean(item)
    sum = 0
    for i in range(len(item)):
        sum += (item[i] - mean)**2
    
    return math.sqrt(sum/len(item))

def sc(x,item):
    sd = sd_p(item)
    mean = statistics.mean(item)
    return (x-mean)/sd