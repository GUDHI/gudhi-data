import os
import pandas as pd

#
# This program requires to launch data from https://archive-beta.ics.uci.edu/ml/datasets/daily+and+sports+activities
# Unzip the data and copy data_selecta.py in the data folder
# Launch 'python data_selecta.py'
#
# One can modify activities or people values for more data.
# usecols=[42,43,44] will select left leg magnetometer x, y and z values
#

activities=['a09',  # walking
            'a13',  # stepper
            'a14',  # cross training
            'a18',] # jumping

people = ['p1',]

df_list = []
for activity in activities:
    for individual in people:
        path = os.path.join(activity, individual)
        for datafile in sorted(os.listdir(path)):
            # Load left leg magnetometer (x,y,z) and reanme columns
            df = pd.read_csv(os.path.join(path, datafile), header=None, usecols=[42,43,44]).rename(columns={42: "LL_xmag", 43: "LL_ymag", 44: "LL_zmag"})
            df['activity']=activity
            df['individual']=individual
            df['set']=os.path.splitext(datafile)[0]
            print(os.path.join(path, datafile))
            df_list.append(df)

df = pd.concat(df_list)
df.to_csv('left_leg_magnetometer.csv', index=False)
