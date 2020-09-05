from plot import scatter_plot_plottly,scatter_plot_by_session
from color_packets import setColorForPackets,setColorsByTime
import pandas as pd
import sessions as Sessions

# Constants
# CSV_FILE = './data/modified_csv/record_23_inside-mah.csv'
CSV_FILE = './csv-preprocess/output/record_22_inside.csv'
# Main run.
print("Starting... Loading CSV")

packets = pd.read_csv(CSV_FILE,encoding='iso-8859-1') # DEFAULT IS UTF-8.

print("Display plot...")

fields = ['Length' ,'Version',"Reset","Diversification nonce","CID Length","NONCE_DEC","Packet Number Length","Multipath","Reserved","CID","Version value","Packet Number","Tag","MAH_DEC"]
fields2 = ['MAH_DEC']
colorsArr=['rgb(0,0,255)','rgb(255,0,0)', 'rgb(0,255,0)','rgb(92, 138, 102)','rgb(0,0,0)','rgb(255, 253, 0)']
ip='192.168.50.'

'''
def plot_all_fields(packets,fields,time):
    for field in fields:
        scatter_plot_plottly2(packets,'Time',field,time, ['rgb(0,0,255)','rgb(255,0,0)', 'rgb(0,255,0)'])

plot_all_fields(packets,fields,[300,3000])
'''
def plot_all_by_time(packets, fields,colorValues,times):
    # need to check if the size fits
    colors,colorVals = setColorsByTime(packets,times,colorValues )

    for field in fields:
        scatter_plot_plottly(packets,'Time',field,colors,colorVals)


def plot_all_by_ip(packets, fields,colorValues,ip):
    packets, numOfColors = setColorForPackets(packets, ip)
    print(packets)
    colorVals = colorValues[:numOfColors]
    colors = packets['Colors']

    for field in fields:
        scatter_plot_plottly(packets, 'Time', field, colors, colorVals)

def plot_by_sessions(packets,fields,colorValues):
    sessions = Sessions.getSessions(packets)

    for field in fields:
        scatter_plot_by_session(sessions[0], 'Time', field)




plot_by_sessions(packets,fields,colorsArr)
# plot_all_by_ip(packets,fields,colorsArr,ip)


print("Exiting...")