import os
import pandas as pd

#
# This program requires to launch data from https://archive-beta.ics.uci.edu/ml/datasets/daily+and+sports+activities
# Unzip the data and copy data_selecta.py in a same directory data folder
# Launch 'python data_selecta.py'
#

# Will be auto-saved as a xz compressed pickle file
result_file = 'activities.xz'

try:
    os.remove(result_file)
except FileNotFoundError:
    pass

columns = {0: 'T_xacc',  1: 'T_yacc',  2: 'T_zacc',
           3: 'T_xgyro', 4: 'T_ygyro', 5: 'T_zgyro',
           6: 'T_xmag',  7: 'T_ymag',  8: 'T_zmag',
           9:  'RA_xacc',  10: 'RA_yacc',  11: 'RA_zacc',
           12: 'RA_xgyro', 13: 'RA_ygyro', 14: 'RA_zgyro',
           15: 'RA_xmag',  16: 'RA_ymag',  17: 'RA_zmag',
           18: 'LA_xacc',  19: 'LA_yacc',  20: 'LA_zacc',
           21: 'LA_xgyro', 22: 'LA_ygyro', 23: 'LA_zgyro',
           24: 'LA_xmag',  25: 'LA_ymag',  26: 'LA_zmag',
           27: 'RL_xacc',  28: 'RL_yacc',  29: 'RL_zacc',
           30: 'RL_xgyro', 31: 'RL_ygyro', 32: 'RL_zgyro',
           33: 'RL_xmag',  34: 'RL_ymag',  35: 'RL_zmag',
           36: 'LL_xacc',  37: 'LL_yacc',  38: 'LL_zacc',
           39: 'LL_xgyro', 40: 'LL_ygyro', 41: 'LL_zgyro',
           42: 'LL_xmag',  43: 'LL_ymag',  44: 'LL_zmag',}

df_list = []
activity_path = 'data'
for activity in sorted(os.listdir(activity_path)):
    people_path = os.path.join(activity_path, activity)
    for individual in sorted(os.listdir(people_path)):
        set_path = os.path.join(people_path, individual)
        for datafile in sorted(os.listdir(set_path)):
            df = pd.read_csv(os.path.join(set_path, datafile), header=None)
            df['activity']=activity
            df['individual']=individual
            df['set']=os.path.splitext(datafile)[0]
            print(os.path.join(set_path, datafile))
            # append the dataframe in a csv file
            df = df.rename(columns=columns)
            df_list.append(df)
            

df = pd.concat(df_list)
df = df.reset_index(drop=True)
df.to_pickle(result_file)