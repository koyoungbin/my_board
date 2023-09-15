from django.shortcuts import render
import serial
import ftplib
import pandas as pd


def main(request):
    return render(request, "main.html")


def Previous_data(request):
    return render(request, "Previous_data.html")


# def index(request):
#     py_serial = serial.Serial('COM4', 9600)
#
#     while not False:
#         if py_serial.readable():
#             response = py_serial.readline()
#             response2 = response[:len(response) - 1].decode()
#             response3 = int(response2)
#             ser_data = response3
#
#             int_data = 150
#
#             return render(request, 'index.html', {'data': ser_data})

def index(request):
    while not False:
        ftp = ftplib.FTP(host='172.18.99.188')
        ftp.set_pasv(False)
        ftp.login(user='JMK', passwd='wjdals123!')
        ftp.cwd('All_user/JMK/aqua_farm')
        # ftp.retrlines('LIST')
        with open(file=r'C:/Users/KoYoungBin/Desktop/test2file/myname4.csv',
                  mode='wb') as rf:  # storline은 업로드고 이것은 다운로드다 나스의 myname을
            ftp.retrbinary('RETR data_atlas_2023-09-03.csv', rf.write)  # testfile 에 myname4라는 이름으로 다운로드하는것이다

        first_data = pd.read_csv('C:/Users/KoYoungBin/Desktop/test2file/myname4.csv')

        time_data = first_data['time'][0]
        temperature_data = first_data['temperature'][0]
        do_data = first_data['DO'][3]
        ec_data = first_data['EC'][0]

        print(do_data)

        return render(request, 'index.html', {'data': do_data})

# def index1(request):
#     ser2 = serial.Serial('COM4', 9600)  # timeout=1 이거 실행 시키면 그래프가 안 나옴
#     stop_flag = False
#
#     while not stop_flag:
#         if ser2.readable():
#             ser2_data = ser2.readline()
#             ser2_data2 = ser2_data[:len(ser2_data) - 1].decode()
#             float_data = float(ser2_data2)  # 시리얼 값이고 이값이 return 문에 들어간다
#
#             time_array = []
#             data_array = []
#
#             i = 0
#             print('number :', i)
#
#             previous_date = datetime.date.today()
#             current_time = datetime.datetime.now()
#             current_date = datetime.date.today()
#
#             try:
#                 data_array.append(float_data)
#                 time_array.append(str(current_time))
#
#                 print(float_data)
#                 print(current_time)
#
#                 # time.sleep(300)  # 이거 실행 시키면 그래프가 안 나옴
#
#             except ValueError:
#                 time.sleep(2)
#
#             except TypeError:
#                 time.sleep(2)
#
#             except SyntaxError:
#                 time.sleep(2)
#
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
#
#                 ftp = ftplib.FTP(host='172.18.99.188')
#                 ftp.set_pasv(False)
#                 ftp.login(user='JMK', passwd='wjdals123!')
#                 ftp.cwd('All_user/JMK/aqua_farm')
#                 ftp.storlines('STOR ' + file_name, open(file_name, 'rb'))
#                 previous_date = current_date
#
#                 time.sleep(2)
#                 os.remove('./' + file_name)
#                 i = 0
#                 i = i + 1
#
#             return render(request, 'index.html', {'data': float_data})
