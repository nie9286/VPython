import os


file = open('CSVTest.csv','r')

lines = file.readlines()


verticesDic={}
faces = []

length = len(lines)
i = 1

while i < length:
    line0 = lines[i]
    line1 = lines[i+1]
    line2 = lines[i+2]

    tokens0 = line0.split(',')
    tokens1 = line1.split(',')
    tokens2 = line2.split(',')

    faces.append([int(tokens0[1]),int(tokens1[1]),int(tokens2[1])])
    verticesDic[tokens0[1]]=[float(tokens0[2]),float(tokens0[3]),float(tokens0[4])]
    verticesDic[tokens1[1]]=[float(tokens1[2]),float(tokens1[3]),float(tokens1[4])]
    verticesDic[tokens2[1]]=[float(tokens2[2]),float(tokens2[3]),float(tokens2[4])]
    i+=3
    

vertices=list(verticesDic.values())

print(vertices)


