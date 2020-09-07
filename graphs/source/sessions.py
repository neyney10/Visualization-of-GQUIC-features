import numpy as np

def getSessions(packets) -> np.ndarray:
    '''
    Input: packets, type: Dataframe with columns of Source, Destination, Source Port, Destination Port.
    Output: 2-Diemnsional ndarray (matrix) with columns of 'name'(0) as string and 'group'(1) as Dataframe of packets related to the session.

    Example: packets is a dataframe object with respected columns of Source, Destination... etc.
        sessions = getSessions(packets)
        print(sessions[:,0]) # Will print all session-ids by the format of ip.src-ip.dst-src.port
        print(sessions[0])   # Will print a session (two elements), the first is the session-id and second is the packets as dataframe.
        print(sessions[0,0]) # Will print only the session-id
        print(sessions[0,1]) # Will print only the packets as dataframe.

    '''
    sessions = packets.groupby(lambda x: _get_session(packets, x))
    sessions_list = []
    for name, group in sessions:
        sessions_list.append([name,group])

    return np.array(sessions)


def getFlows(session):
    '''
    Input: a session (an element from one created by the getSessions function or equivalent format) with first index of 'name'(0) as string and second index 'group'(1) as Dataframe
    Output: 2-element tuple, first for outgoing from source and second for incoming, where the ingoing is determined by the first packet captured -> assuming that it is the one who initiates the session.
            each one is a dataframe object containing packets. 

    Example: packets is a dataframe object with respected columns of Source, Destination... etc.
        sessions = getSessions(packets)
        (outFLow, inFlow) = getFlows(sessions[0])
    '''
    sessionPackets = session[1]
    addresses = sessionPackets['Source'].unique()
    
    outgoingPackets = sessionPackets[sessionPackets['Source'] == addresses[0]]
    incomingPackets = sessionPackets[sessionPackets['Source'] == addresses[1]]

    return (outgoingPackets, incomingPackets)


def _get_session(x,ind):
    if not x['Destination Port'][ind] or len(str(x['Destination Port'][ind])) <=2:
        return 'unidentified session'
    if 443 == x['Destination Port'][ind]:
        return str(x['Source'][ind]) +'-'+ str(x['Destination'][ind]) +'-'+ str(x['Source Port'][ind])
    else:
        return str(x['Destination'][ind]) +'-'+ str(x['Source'][ind]) +'-'+ str(x['Destination Port'][ind])


