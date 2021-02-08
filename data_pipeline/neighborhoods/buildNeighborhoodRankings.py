import math 
import statistics

stdArr = []
fakeNums = [989000, 1210000, 874000, 1494000, 1621000, 699000, 2150000, 3100000]
def standardDev():
    mean = statistics.mean(fakeNums)
    std = statistics.pstdev(fakeNums)
    for num in fakeNums:
        var = num - mean 
        times = var / std
        stdArr.append(times)
        stdArr.append("num")
    return stdArr