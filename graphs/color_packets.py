import numpy as np
import pandas as pd
import random

def setColorForPackets(packets, networkAddress):
    uniques = packets['Source'].unique()

    uniquef = []
    countClasses = 0
    for s in uniques:
        if networkAddress in s:
            uniquef.append(s)
            countClasses+=1

    packets['Colors'] = packets.apply(by_ip,axis=1,args=([uniquef]))

    return (packets, countClasses)


def by_ip(row, uniquef):
    if row['Source'] in uniquef:
        index = uniquef.index(row['Source'])
        return index
    elif row['Destination'] in uniquef:
        index = uniquef.index(row['Destination'])
        return index
    else:
        return -1


def random_color_string():
        return "rgba(" + str(random.randint(0, 255)) +","+ str(random.randint(0, 255)) + "," + str(random.randint(0, 255)) +")"


def setColorsByTime(packets,time,timeColors):
    colors = np.zeros(len(packets))
    packetsMatrix = packets.to_numpy()
    colorValues = [[0, timeColors[0]]]
    for i in range(len(time)):
        colors[packetsMatrix[:, 1] >= time[i]] = (i + 1)
        colorValues.append([(i + 1) / len(time), timeColors[(i + 1)]])

    return colors,colorValues