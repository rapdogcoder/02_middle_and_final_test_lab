from functools import reduce
from math import sqrt
import sys
def read_data(filename):
    data = []
    with open(filename) as f:
        data = [list(map(lambda x: x.strip().strip('\n'),i.split(','))) for i in f.readlines() if i.split(',')[0].isdigit()]
    return data
def add_weighted_average(data, weight):
    for i, row in enumerate(data):
        if row[0].isdigit():
            row = list(map(int,row))
            value = ((row[0]*weight[0])+(row[1]*weight[1]))/len(row)
            row.append(value)
            data[i] = row   # TODO
    return data

def analyze_data(data):
    mean = reduce(lambda acc, cur: acc+cur,data)/len(data)     # TODO
    var = sqrt(reduce(lambda acc,cur:acc+cur**2,data)/len(data)-mean)             # TODO
    median = sorted(data)[len(data)//2]     # TODO
    return mean, var, median, min(data), max(data)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        data = add_weighted_average(data, [40/125, 60/100])
        sys.stdout = open('stdout.md','w')
        if len(data[0]) == 3:      # Check 'data' is valid
            print('### Individual Score')
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
            print()

            print('### Examination Analysis')
            col_n = len(data[0])
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [ [row[c] for row in data] for c in range(col_n) ]
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')
        sys.stdout.close()