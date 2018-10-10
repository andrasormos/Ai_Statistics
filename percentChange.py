import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pylab as pylab
from scipy import stats

# you need at least 2000 games to get a good result


log = pd.read_csv("/home/andras/PycharmProjects/TradingGame/logs/percentChange.csv", sep=",", index_col=0)



percentChange = log.percentChange
summedPercent = sum(percentChange)
print("SUM: ", summedPercent)


fig = plt.figure()

# AX 1 -
ax1 = fig.add_subplot(111)
ax1.plot(percentChange, "-", color='g', linewidth=1)
#plt.axhline(0, color='black', linewidth=0.5)
ax1.set_ylim([-10, 10])
plt.title("Guess Success")




fig.suptitle('Percent Change')  # or plt.suptitle('Main title')
#ax1.legend()
fig.tight_layout()


#fileName = "/home/andras/PycharmProjects/TradingGame/lab/img_" + imageName + ".png"
#fig.savefig(fileName)

plt.show()


'''
321
322
323
324
325
326
'''