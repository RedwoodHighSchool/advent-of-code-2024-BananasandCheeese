import os

def get_data():
    cwd = os.getcwd()
    with open(cwd + '/input.txt', 'r') as file:
        data = file.readlines()
        column1 = []
        column2 = []
        for line in data:
            values = line.strip().split() 
            if len(values) == 2:  
                column1.append(int(values[0]))  
                column2.append(int(values[1]))  
    return column1, column2

def part2():
    column1, column2 = get_data()
    b = 0
    for i in column1:
        sim_score = column2.count(i)
        b += i*sim_score

    return b 

print(part2())