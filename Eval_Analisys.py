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



log_nr = "27"

#imageName = "run_" + log_nr + "_random actions"
#imageName = "run_" + log_nr + "_buy & skip actions"
#imageName = "run_" + log_nr + "_buy & skip actions ETH added"
imageName = "run_" + log_nr

t_period = 100
e_period = 100
eps_period = 10

t_file = os.path.exists("/home/andras/PycharmProjects/TradingGame/logs/trainLog_0" + log_nr + ".csv")
e_file = os.path.exists("/home/andras/PycharmProjects/TradingGame/logs/evalLog_0" + log_nr + ".csv")


# random: 50.0125195
epsLog = pd.read_csv("/home/andras/PycharmProjects/TradingGame/epsLog.csv")
eps = epsLog.eps
frame = epsLog.frame
#print(frame)

# FIND SAVE FILE
OldMin = 0
OldMax = 10000
NewMin = 0
NewMax = 443525
OldValue = 4000

NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
print("NewValue", NewValue)

# 443525

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.plot(frame,eps, "-", color='g', linewidth=1)
# ax1.set_ylim([0, 1.2])
# #plt.axhline(50, color='black', linewidth=0.5)



if t_file == True:
    t_log = pd.read_csv("/home/andras/PycharmProjects/TradingGame/logs/trainLog_0" + log_nr + ".csv", sep=",", index_col=0)
    t_profit = t_log.profit
    t_rewardSum = t_log.rewardSum
    t_profit = t_log.profit
    t_guessedRightCnt = t_log.guessedRightCnt
    t_guessedWrongCnt = t_log.guessedWrongCnt
    t_guessSkipCnt = t_log.guessSkipCnt
    t_guessCnt = t_log.guessCnt
    t_guessUpCnt = t_log.guessUpCnt
    t_guessDownCnt = t_log.guessDownCnt

    print("eval len", len(t_rewardSum))

    print("t_Log Count:", len(t_profit))
    print("t_Log Period:", t_period)

if e_file == True:
    e_log = pd.read_csv("/home/andras/PycharmProjects/TradingGame/logs/evalLog_0" + log_nr + ".csv", sep=",", index_col=0)
    e_profit = e_log.profit
    e_rewardSum = e_log.rewardSum
    e_profit = e_log.profit
    e_guessedRightCnt = e_log.guessedRightCnt
    e_guessedWrongCnt = e_log.guessedWrongCnt
    e_guessSkipCnt = e_log.guessSkipCnt
    e_guessCnt = e_log.guessCnt
    e_guessUpCnt = e_log.guessUpCnt
    e_guessDownCnt = e_log.guessDownCnt
    print("e_Log Count:", len(e_profit))
    print("e_Log Period:", e_period)




def guessCorrectness(guessedRightCnt, guessUpCnt, guessDownCnt, guessSkipCnt, rewardSum, guessCnt, profit, period):
    correctnessList = []
    upList = []
    downList = []
    skiplist = []
    scoreList = []
    cnt = 0

    upSum = 0
    downSum = 0
    skipSum = 0
    scoreSum = 0
    rightSum = 0

    for i in range(len(guessCnt)):
        cnt += 1
        upSum += guessUpCnt[i]
        downSum += guessDownCnt[i]
        skipSum += guessSkipCnt[i]
        scoreSum += rewardSum[i]
        rightSum += guessedRightCnt[i]

        if cnt == period:
            if (upSum + downSum) != 0:
                correctness = ( rightSum / (downSum + upSum ) ) * 100
                correctnessList.append(correctness)
            upList.append(upSum/period)
            downList.append(downSum/period)
            skiplist.append(skipSum/period)
            scoreList.append(scoreSum/period)
            upSum = 0
            downSum = 0
            skipSum = 0
            scoreSum = 0
            rightSum = 0
            cnt = 0

    return correctnessList, upList, downList, skiplist, scoreList

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

fig = plt.figure(figsize=(12, 10))

if t_file == True:
    epsred = reduceCnt(eps, eps_period)
    t_correctnessList, t_upList, t_downList, t_skiplist, t_scoreList = guessCorrectness(t_guessedRightCnt, t_guessUpCnt, t_guessDownCnt, t_guessSkipCnt, t_rewardSum, t_guessCnt, t_profit, t_period)

    # AX 1 -
    ax1 = fig.add_subplot(221)
    ax1.plot(epsred, "-", color='c', linewidth=1)
    ax1.plot(t_correctnessList, "-", color='g', linewidth=1)
    ax1.set_ylim([0, 100])
    plt.axhline(50, color='black', linewidth=0.5)
    #plt.title("Train Success Percentage")


    # AX 2 -
    ax2 = fig.add_subplot(222)
    ax2.plot(t_upList, "-", color='g', linewidth=1)
    #ax2.plot(t_downList, "-", color='r', linewidth=1)
    ax2.plot(t_skiplist, "-", color='b', linewidth=1)
    #ax2.set_ylim([-50, 50])
    #ax2.set_xlim([0, Epoch])
    #plt.axhline(0, color='black', linewidth=0.5)
    #plt.title("Train Guess Occurences")

if e_file == True:
    e_correctnessList, e_upList, e_downList, e_skiplist, e_scoreList = guessCorrectness(e_guessedRightCnt, e_guessUpCnt, e_guessDownCnt, e_guessSkipCnt, e_rewardSum, e_guessCnt, e_profit,e_period)

    # fig = plt.figure()
    # ax1 = fig.add_subplot(111)
    # ax1.plot(e_profit, "-", color='g', linewidth=1)

    latest = e_correctnessList[-10:]
    print("Correct:", np.mean(latest))

    # AX 3 -
    ax3 = fig.add_subplot(223)
    ax3.plot(e_correctnessList, "-", color='g', linewidth=1)
    ax3.set_ylim([35, 65])
    plt.axhline(50, color='black', linewidth=0.5)
    #plt.title("Eval Success Percentage")

    # AX 4 -
    ax4 = fig.add_subplot(224)
    ax4.plot(e_upList, "-", color='g', linewidth=1)
    #ax4.plot(e_downList, "-", color='r', linewidth=1)
    ax4.plot(e_skiplist, "-", color='b', linewidth=1)
    #ax4.set_ylim([-70, 70])
    #ax4.set_xlim([0, Epoch])
    #plt.axhline(0, color='black', linewidth=0.5)
    #plt.title("Eval Guess Occurences")


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