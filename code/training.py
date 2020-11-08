import Multi
import csv
import numpy as np


def readcsv():
    # inputs = []
    # outputs = []
    with open('data_clean.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            #print(line_count)
            if line_count == 1:
                
                inputs = [[int(row[0]),int(row[1])]]
                outputs = [[int(row[2])]]
            elif line_count >1:
                inputs.append([int(row[0]),int(row[1])])
                outputs.append([int(row[2])])
            if line_count ==30:
                break
            line_count+= 1
    return inputs , outputs



ins,outs = readcsv()
#print(ins,outs)
inputs = np.array(ins)
outputs = np.array(outs)
print(inputs,outputs)

n = Multi.NN(inputs)

print(n.think(inputs))
n.train(inputs, outputs,1000)
print(n.think(inputs))