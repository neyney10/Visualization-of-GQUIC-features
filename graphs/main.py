from plot_by import plot_by_time, plot_by_ip
import pandas as pd
import sessions as Sessions

# Constants
CSV_FILE = './csv-preprocess/output/record_22_inside.csv'

fields = ['Length' ,'Version',"Reset","Diversification nonce","CID Length","NONCE_DEC","Packet Number Length","Multipath","Reserved","CID","Version value","Packet Number","Tag","MAH_DEC"]
fields2 = ['MAH_DEC']
ip='192.168.50.'

# Main run.
print("Starting... Loading CSV")

packets = pd.read_csv(CSV_FILE,encoding='iso-8859-1') # DEFAULT IS UTF-8.

print("Display plot...")

sessions = Sessions.getSessions(packets)
plot_by_ip(sessions[0,1], fields2, ip)
plot_by_ip(packets, ['Packet Number'], ip)
plot_by_time(packets, ['NONCE_DEC'], [200,400,600])

print("Exiting...")