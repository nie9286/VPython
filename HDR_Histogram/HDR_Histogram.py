from functools import total_ordering
from matplotlib import pyplot as plt
import imageio


path = "T_IBL_HDR.HDR"
img = imageio.imread(path, format='HDR-FI')

maxPlotValue = 5
step = 0.1

rvalues = []
for row in img:
    for pixel in row:
        rvalues.append(pixel[0])

rvalues.sort()
rvalues.reverse()
total = len(rvalues)
print(rvalues[0])

valueTypes={}
for value in rvalues:
    value100 = min(value,maxPlotValue) * (1/step)
    valueint = int(value100)
    valuefloat = float(valueint) * step
    if valuefloat in valueTypes:
        valueTypes[valuefloat] = valueTypes[valuefloat]+ 1
    else:
        valueTypes[valuefloat] = 1

keys = valueTypes.keys()
values = valueTypes.values()
percents = []

for value in values:
    percent = value / float(total)
    percents.append(percent)

fig, ax = plt.subplots(1)
ax.set_xlabel('Intensity $\Delta_i$')
ax.set_ylabel('Percent')
ax.set_title(path)
plt.plot(keys,percents)
plt.show()



