import pandas as pd
import numpy as np

def modifyCSV(CSV_FILE, CSV_OUT):
    print("Reading CSV...")
    packets = pd.read_csv(CSV_FILE,encoding='iso-8859-1') # DEFAULT IS UTF-8.

    # modify header names
    print("Changing header names...")
    packets.rename(columns={'Version.1': 'Version value', 'Diversification nonce.1': 'Diversification nonce value'}, inplace=True)

    def hex2dec(mah):
        mah = str(mah)

        if len(mah) < 4:
            return ''
        
        return int(mah,16)

    print("Transforming hex2dec of MAH...")
    MAH = packets['Message Authentication Hash']
    MAH_DEC = MAH.transform(hex2dec)

    print("Transforming hex2dec of nonce...")
    NONCE = packets['Diversification nonce value']
    NONCE_DEC = NONCE.transform(hex2dec)
    print("Shrinking NONCE values to fit range...")
    a = np.array(NONCE_DEC)
    a[a == ''] = 0
    a = a / pow(10,70)
    a[a == 0] = np.nan
    
    print("Adding transformation results to the dataframe...")
    packets['MAH_DEC']   = MAH_DEC
    packets['NONCE_DEC'] = a

    print("Saving to CSV...")
    packets.to_csv(CSV_OUT)

    print("Finish...")
