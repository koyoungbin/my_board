import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import plotly
from plotly.graph_objs import Scatter, Layout

import ftplib

ftp = ftplib.FTP()
ftp.connect('172.18.99.188', 21)
ftp.set_pasv(False)

ftp.login(user='YoungbinKo', passwd='wlfmd123!')
ftp.cwd('All_user/JMK/aqua_farm')  # 여기가 받을 장소

with open(file=r'C:/Users/KoYoungBin/Desktop/test2file/myname4.csv',
          mode='wb') as rf:  # storline은 업로드고 이것은 다운로드다 나스의 myname을
    ftp.retrbinary('RETR data_atlas_2023-09-03.csv', rf.write)  # testfile 에 myname4라는 이름으로 다운로드하는것이다

first_data = pd.read_csv('C:/Users/KoYoungBin/Desktop/test2file/myname4.csv')

time_data = first_data[['time']]

temperature_data = first_data[['temperature']]
DO_data = first_data[['DO']]
EC_data = first_data[['EC']]

# np.savetxt('hh.txt', temperature_data)
#
# print(open("hh.txt").read())

# with open("data.pickle","wb") as fw:
#     pickle.dump(temperature_data, fw)
# print(temperature_data)


temperature_data.DataFrame.filter(items=['temperature_data'])