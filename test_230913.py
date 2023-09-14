import serial
import time
import datetime
import pandas as pd
import ftplib
import os
import urllib.request  # URL( 대부분의 HTTP) 을 여는데 도움을 줌
import threading  # 파이썬은 하나의 스레드만 가능한데 이것을 하면 2가지이상의 일을 거의 동시에 수행 가능해짐
from config.views import index1

ser2 = serial.Serial('COM4', 9600, timeout=1)  # 시리얼 포트 설정 for atlas science

# def ftp_connect(filename):
#     ftp.cwd('All_user/JMK/aqua_farm')
#     ftp.storlines('STOR ' + filename, open(filename, 'rb'))
def main_loop():
    time_array = []
    data_array = []

    i = 0

    while True:

        print('number :', i)
        previous_date = datetime.date.today()

        current_time = datetime.datetime.now()
        line = ser2.readline().decode()

        data = str(line)

        try:
            data = float(data)
            data_array.append(data)
            time_array.append(str(current_time))
            print(data)
            index1(data=data)
            print(current_time)
            # URl = 'https://api.thingspeak.com/update?api_key='  # thingspeak 의 웹사이트를 말함
            # KEY = 'GLCXDNCAD19NG68H'  # 영빈이의 계정에 등록된 Write API Key 의 값을 말한다
            # HEADER = '&field1={}&field2={}&field3={}'.format(temperature_data, DO_data, EC_data)
            # NEW_URL = URl + KEY + HEADER
            # print(NEW_URL)
            # NEW_data = urllib.request.urlopen(NEW_URL)
            # print(NEW_data)  # 기존 대쉬보드에 새로운 데이터를 집어넣는 방식으로 보인다 만약 위의 4개의 코딩을 지우고 실행시키면 오류는 안 나오나 값이 대쉬보드 상에 업데이트가 안된다

            time.sleep(300)
        except ValueError:
            time.sleep(2)
        except TypeError:
            time.sleep(2)
        except SyntaxError:
            time.sleep(2)

        current_date = datetime.date.today()
        if previous_date != current_date:
            df = pd.DataFrame(time_array, columns=['time'])
            df['Data'] = data_array
            file_name = f"data_atlas_{previous_date}.csv"
            df.to_csv('./' + file_name, index=False)

            time_array.clear()
            data_array.clear()

            time.sleep(2)
            ftp = ftplib.FTP(host='172.18.99.188')
            ftp.set_pasv(False)
            ftp.login(user='JMK', passwd='wjdals123!')
            ftp.cwd('All_user/JMK/aqua_farm')
            ftp.storlines('STOR ' + file_name, open(file_name, 'rb'))
            # ftp_connect(filename=file_name)
            previous_date = current_date
            time.sleep(2)
            os.remove('./' + file_name)
            i = 0
        i = i + 1


if __name__ == "__main__":
    main_loop()