import os
import pandas as pd
import numpy as np

#
# This program requires to load data from https://archive.ics.uci.edu/ml/datasets/daily+and+sports+activities
# Unzip the data and copy data_selecta.py in a same directory data folder
# Launch 'python data_selecta.py'
# Generated with Python 3.8 / Pandas 1.1.0
#

# Will be auto-saved as a xz compressed pickle file
result_file = 'activities.csv.xz'

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
df.to_csv(result_file)

# Select personn 1 and Left Leg Magnetometer
p1_left_leg = df[df['individual'] == 'p1'][['LL_xmag', 'LL_ymag', 'LL_zmag', 'activity']]

# Filter cross_training, jumping, stepper and walking
p1_left_leg_filter = (p1_left_leg['activity'] == 'a14') | (p1_left_leg['activity'] == 'a18') | (p1_left_leg['activity'] == 'a13') | (p1_left_leg['activity'] == 'a09')
p1_left_leg = p1_left_leg[p1_left_leg_filter]

# More verbose activity - bigger files, but ok
p1_left_leg['activity'] = p1_left_leg['activity'].replace(['a09', 'a13', 'a18', 'a14'],
                                                          ['walking', 'stepper', 'jumping', 'cross_training'])

records = p1_left_leg.to_records(index=False)
p1_left_leg_np = np.array(records, dtype = [('LL_xmag', '<f4'), ('LL_ymag', '<f4'), ('LL_zmag', '<f4'),
                                            ('activity', '<U15')]) # Force activity as a string of length 15 (or less)

# Save as a numpy array
with open('activities_p1_left_leg.npy', 'wb') as f:
    np.save(f, p1_left_leg_np)

# Save as a csv
p1_left_leg.to_csv('activities_p1_left_leg.csv', header=None)