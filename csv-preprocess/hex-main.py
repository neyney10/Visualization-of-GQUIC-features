from hex2 import modifyCSV
import os

CSV_DIR  = './hex2dec-script/input/'
CSV_OUT  = './hex2dec-script/output/'

directory = os.fsencode(CSV_DIR)
out_directory = os.fsencode(CSV_OUT)
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".csv"): 
            filepath = str(CSV_DIR) + filename
            outpath = str(CSV_OUT) + filename
            print("[...Modifying file: "+ filepath + "]")
            modifyCSV(filepath, outpath)
    else:
        continue



