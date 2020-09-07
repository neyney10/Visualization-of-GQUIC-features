import numpy as np
import pandas as pd
import random



class ColorByIP():
    '''
    A coloring method by IP address, color each IP with the given network address prefix
    with another color.
    '''
    def __init__(self, networkAddressPrefix):
        ''' [Constructor]
        Arguments: networkAddressPrefix: string, example: "192.172.50."
        '''
        self.networkAddressPrefix = networkAddressPrefix
    
    def color(self, packets):
        '''
        Get colors for respective packets, matching them by index.
        Input: packets: Pandas.DataFrame or equivalent, with columns of 'Source','Destination'.
        Output: tuple (packetColors, amountOfColors), i.e. packetColors[5] matches packet at packets[5].
        '''
        uniques = packets['Source'].unique()

        uniquef = [] # unique filtered addresses by self.networkAddressPrefix string value.
        for s in uniques:
            if self.networkAddressPrefix in s:
                uniquef.append(s)

        packetColors = packets.apply(by_ip,axis=1,args=([uniquef]))

        return ( packetColors, len(uniquef) )

def by_ip(row, uniquef):
    if row['Source'] in uniquef:
        index = uniquef.index(row['Source'])
        return index
    elif row['Destination'] in uniquef:
        index = uniquef.index(row['Destination'])
        return index
    else:
        return -1



class ColorByTime():
    '''
    A coloring method by array of time intervals, color each time interval
    with another color.
    '''
    def __init__(self, timeIntervals):
        ''' [Constructor]
        Arguments: timeIntervals: float[], example: [30,50,60] for intervals [0-30),[30-50),[50-60),[60-max]
        '''
        self.timeIntervals = timeIntervals
    
    def color(self, packets):
        '''
        Get colors for respective packets, matching them by index.
        Input: packets: Pandas.DataFrame or equivalent, with column of 'Time'.
        Output: tuple (packetColors, amountOfColors), i.e. packetColors[5] matches packet at packets[5].
        '''
        packetColors = np.zeros(len(packets))
        packetsTimeColumn = packets['Time']
        maxTime = np.max(packetsTimeColumn) +1
        modifiedTimeIntervals = [0] + self.timeIntervals + [maxTime]

        for i in range(len(modifiedTimeIntervals)-1):
            packetColors[(packetsTimeColumn >= modifiedTimeIntervals[i]) & 
                        (packetsTimeColumn < modifiedTimeIntervals[i+1])] = i
        
        return (packetColors, len(modifiedTimeIntervals)-1)

class ColorByDefault():
    '''
    A default coloring method, set the same color for all indices.
    '''
    def __init__(self):
        pass
    
    def color(self, packets):
        '''
        Get colors for respective packets, matching them by index.
        Input: packets: Pandas.DataFrame or equivalent, with column of 'Time'.
        Output: tuple (packetColors, amountOfColors), i.e. packetColors[5] matches packet at packets[5].
        '''
        packetColors = np.zeros(len(packets))

        return (packetColors, 1)




def random_color_string():
        return "rgba(" + str(random.randint(0, 255)) +","+ str(random.randint(0, 255)) + "," + str(random.randint(0, 255)) +")"

