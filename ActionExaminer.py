import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pylab as pylab
from scipy import stats
import os.path


log_nr = "35"
imageName = "run_" + log_nr
t_period = 100
e_period = 50
eps_period = 1


a_log = pd.read_csv("/home/andras/PycharmProjects/TradingGame/logs/actionLog_0" + log_nr + ".csv", sep=",", index_col=0)
print(a_log)

a_price = a_log.BTCPrice
a_bought = a_log.bought
a_sold = a_log.sold

priceMax = np.amax(a_price)
priceMin = np.amin(a_price)
print(priceMin, priceMax)

fig = plt.figure(figsize=(12, 10))


#e_correctnessList, e_upList, e_downList, e_skiplist, e_scoreList = guessCorrectness(e_guessedRightCnt, e_guessUpCnt, e_guessDownCnt, e_guessSkipCnt, e_rewardSum, e_guessCnt, e_profit,e_period)
#latest = e_correctnessList[-10:]
#print("Correct:", np.mean(latest))

# AX 1
ax1 = fig.add_subplot(211)
ax1.plot(a_price, "-", color='b', linewidth=1)
ax1.plot(a_bought, "*", color='g', linewidth=1)
ax1.plot(a_sold, "*", color='r', linewidth=1)
ax1.set_ylim([priceMin, priceMax])
#plt.axhline(0, color='black', linewidth=0.5)
#plt.title("Eval Success Percentage")

# # AX 3 -
# ax3 = fig.add_subplot(223)
# ax3.plot(e_correctnessList, "-", color='g', linewidth=1)
# ax3.set_ylim([35, 65])
# plt.axhline(50, color='black', linewidth=0.5)
# #plt.title("Eval Success Percentage")

# # AX 4 -
# ax4 = fig.add_subplot(224)
# ax4.plot(e_upList, "-", color='g', linewidth=1)
# #ax4.plot(e_downList, "-", color='r', linewidth=1)
# ax4.plot(e_skiplist, "-", color='b', linewidth=1)
# #ax4.set_ylim([-70, 70])
# #ax4.set_xlim([0, Epoch])
# #plt.axhline(0, color='black', linewidth=0.5)
# #plt.title("Eval Guess Occurences")


fig.suptitle(imageName)  # or plt.suptitle('Main title')
#ax1.legend()
#fig.tight_layout(rect=[0, 0.03, 1, 0.95])

fileName = "/home/andras/PycharmProjects/TradingGame/lab/img_" + imageName + ".png"
fig.savefig(fileName)

plt.show()


'''
321
322
323
324
325
326
'''