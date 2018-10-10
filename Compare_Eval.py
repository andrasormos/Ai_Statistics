import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pylab as pylab
from scipy import stats
import os.path

#rewardSum,profit,guessedRightCnt,guessedWrongCnt,guessSkipCnt,guessCnt
# - sum up the last 100 games and calculate the success
# - a period changer button would be cool
# - include a epsilon into graph
epsLog = pd.read_csv("/home/andras/PycharmProjects/TradingGame/epsLog.csv")
eps = epsLog.eps
frame = epsLog.frame

t_period = 100
e_period = 100
eps_period = 10

# 18 - 2048   0.00001
# 20 - 512    0.00025
# 21 - 1024   0.00025
# 22 - 2048   0.00025
# 23 - 1024

log_A = "21"
log_B = "24"
log_C = "27"


def reduceCnt(eps, eps_period):
    epsList = []
    cnt = 0
    temp = 0
    for i in range(len(eps)):
        cnt += 1
        temp += eps[i]

        if cnt == eps_period:
            epsList.append(temp*9)
            cnt = 0
            temp = 0

    return epsList

def loadLog(log_nr):
    tA_log = pd.read_csv("/home/andras/PycharmProjects/TradingGame/logs/trainLog_0" + log_nr + ".csv", sep=",", index_col=0)
    eA_log = pd.read_csv("/home/andras/PycharmProjects/TradingGame/logs/evalLog_0" + log_nr + ".csv", sep=",", index_col=0)
    return tA_log, eA_log

def guessCorrectness(log, period):
    def unpackLog(log):
        rewardSum = log.rewardSum
        profit = log.profit
        guessedRightCnt = log.guessedRightCnt
        guessedWrongCnt = log.guessedWrongCnt
        guessSkipCnt = log.guessSkipCnt
        guessCnt = log.guessCnt
        guessUpCnt = log.guessUpCnt
        guessDownCnt = log.guessDownCnt
        print("Log Count:", len(profit))
        print("Log Period:", period)
        return guessedRightCnt, guessUpCnt, guessDownCnt, guessSkipCnt, rewardSum, guessCnt, profit

    guessedRightCnt, guessUpCnt, guessDownCnt, guessSkipCnt, rewardSum, guessCnt, profit = unpackLog(log)

    profitList = []
    correctnessList = []
    upList = []
    downList = []
    skiplist = []
    scoreList = []
    cnt = 0

    profitSum = 0
    upSum = 0
    downSum = 0
    skipSum = 0
    scoreSum = 0
    rightSum = 0

    for i in range(len(guessCnt)):
        cnt += 1
        profitSum += profit[i]
        upSum += guessUpCnt[i]
        downSum += guessDownCnt[i]
        skipSum += guessSkipCnt[i]
        scoreSum += rewardSum[i]
        rightSum += guessedRightCnt[i]

        if cnt == period:
            if (upSum + downSum) != 0:
                correctness = ( rightSum / (downSum + upSum ) ) * 100
                correctnessList.append(correctness)
            profitList.append(profitSum/period)
            upList.append(upSum/period)
            downList.append(downSum/period)
            skiplist.append(skipSum/period)
            scoreList.append(scoreSum/period)
            profitSum = 0
            upSum = 0
            downSum = 0
            skipSum = 0
            scoreSum = 0
            rightSum = 0
            cnt = 0
    return correctnessList, upList, downList, skiplist, scoreList, profitList




tA_log, eA_log = loadLog(log_A)
tB_log, eB_log = loadLog(log_B)
tC_log, eC_log = loadLog(log_C)

print("t" + log_A)
tA_correctnessList, tA_upList, tA_downList, tA_skiplist, tA_scoreList, tA_profitList = guessCorrectness(tA_log, t_period)
eA_correctnessList, eA_upList, eA_downList, eA_skiplist, eA_scoreList, eA_profitList = guessCorrectness(eA_log, e_period)

print("t" + log_B)
tB_correctnessList, tB_upList, tB_downList, tB_skiplist, tB_scoreList, tB_profitList = guessCorrectness(tB_log, t_period)
eB_correctnessList, eB_upList, eB_downList, eB_skiplist, eB_scoreList, eB_profitList = guessCorrectness(eB_log, e_period)

print("t" + log_C)
tC_correctnessList, tC_upList, tC_downList, tC_skiplist, tC_scoreList, tC_profitList = guessCorrectness(tC_log, t_period)
eC_correctnessList, eC_upList, eC_downList, eC_skiplist, eC_scoreList, eC_profitList = guessCorrectness(eC_log, e_period)


latest = eA_correctnessList[-10:]
print("Correct:", np.mean(latest))
epsred = reduceCnt(eps, eps_period)



# imageName = "run_" + log_nr + "_buy & skip & ETH & t512 & lr0.00025"
imageName = "compare_run_" + log_A + " + run_" + log_B + " + run_" + log_C
fig = plt.figure(figsize=(16, 10))

# TRAINING LOG
# CORRECTNESS  ----------------------------------------------
ax1 = fig.add_subplot(221)
ax1.plot(epsred, "-", color='c', linewidth=1)
ax1.set_ylim([0, 100])
plt.axhline(50, color='black', linewidth=0.5)

ax1.plot(tA_correctnessList, "-", color='darkgreen', linewidth=1, label=log_A)
ax1.plot(tB_correctnessList, "-", color='orange', linewidth=1, label=log_B)
ax1.plot(tC_correctnessList, "-", color='red', linewidth=1, label=log_C)
ax1.legend()


# CHOICES  ----------------------------------------------
ax2 = fig.add_subplot(222)

ax2.plot(tA_upList, "-", color='g', linewidth=1)
#ax2.plot(tA_downList, "-", color='r', linewidth=1)
ax2.plot(tA_skiplist, "-", color='b', linewidth=1)



# EVALUATION LOG
# CORRECTNESS  ----------------------------------------------
ax3 = fig.add_subplot(223)
ax3.set_ylim([35, 65])
plt.axhline(50, color='black', linewidth=0.5)

ax3.plot(eA_correctnessList, "-", color='darkgreen', linewidth=1)
ax3.plot(eB_correctnessList, "-", color='orange', linewidth=1)
ax3.plot(eC_correctnessList, "-", color='red', linewidth=1)

# CHOICES  ----------------------------------------------
ax4 = fig.add_subplot(224)
#ax4.set_xlim([5, 150])
#
# ax4.plot(eA_upList, "-", color='limegreen', linewidth=0.7)
# ax4.plot(eA_skiplist, "-", color='darkgreen', linewidth=0.7)
#
# ax4.plot(eB_upList, "-", color='magenta', linewidth=0.7)
# ax4.plot(eB_skiplist, "-", color='darkmagenta', linewidth=0.7)

ax4.plot(eC_upList, "-", color='red', linewidth=0.7)
ax4.plot(eC_skiplist, "-", color='firebrick', linewidth=0.7)


# # PROFIT  ----------------------------------------------
# ax5 = fig.add_subplot(225)
# ax5.plot(eA_profitList, "-", color='limegreen', linewidth=0.7)
# # ax5.plot(eA_skiplist, "-", color='darkgreen', linewidth=0.7)


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