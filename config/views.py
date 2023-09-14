from django.shortcuts import render
import ftplib
import serial
import time
import datetime
import pandas as pd
import os
import urllib.request
import threading


def main(request):
    return render(request, "main.html")


def burger_list(request):
    return render(request, "burger_list.html")


def index(request):
    py_serial = serial.Serial('COM4', 9600)
    stop_flag = False
    global response3

    while not stop_flag:
        if py_serial.readable():
            response = py_serial.readline()
            response2 = response[:len(response) - 1].decode()
            response3 = int(response2)
            name = response3
            return render(request, 'hihi.html', {'name': name})


# def index1(request):
#     ser2 = serial.Serial('COM4', 9600, timeout=1)
#     stop_flag = False
#     global response3
#
#     while not stop_flag:
#         if ser2.readable():
#             response = ser2.readline()
#             response2 = response[:len(response) - 1].decode()
#             response3 = int(response2)
#             line = response3
#             # name = response3
#
#         time_array = []
#         data_array = []
#
#         i = 0
#
#         while True:
#
#             print('number :', i)
#             previous_date = datetime.date.today()
#
#             current_time = datetime.datetime.now()
#             # line = ser2.readline().decode()
#
#             data = str(line)
#
#             try:
#                 data = float(data)
#                 data_array.append(data)
#                 time_array.append(str(current_time))
#                 print(data)
#                 print(current_time)
#                 render(request, 'hihi.html', {'name': data})
#
#                 time.sleep(300)
#             except ValueError:
#                 time.sleep(2)
#             except TypeError:
#                 time.sleep(2)
#             except SyntaxError:
#                 time.sleep(2)
#
#             current_date = datetime.date.today()
#             if previous_date != current_date:
#                 df = pd.DataFrame(time_array, columns=['time'])
#                 df['Data'] = data_array
#                 file_name = f"data_atlas_{previous_date}.csv"
#                 df.to_csv('./' + file_name, index=False)
#
#                 time_array.clear()
#                 data_array.clear()
#
#                 time.sleep(2)
#                 ftp = ftplib.FTP(host='172.18.99.188')
#                 ftp.set_pasv(False)
#                 ftp.login(user='JMK', passwd='wjdals123!')
#                 ftp.cwd('All_user/JMK/aqua_farm')
#                 ftp.storlines('STOR ' + file_name, open(file_name, 'rb'))
#                 # ftp_connect(filename=file_name)
#                 previous_date = current_date
#                 time.sleep(2)
#                 os.remove('./' + file_name)
#                 i = 0
#             i = i + 1
