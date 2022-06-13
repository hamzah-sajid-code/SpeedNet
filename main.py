import matplotlib.pyplot as plt
import time
from speedtest import Speedtest
list_download_speed = []
list_upload_speed = []
for i in range(5):
    speedtest = Speedtest()
    download_speed = speedtest.download() / 1000000
    upload_speed = speedtest.upload() / 1000000
    list_download_speed.append(download_speed)
    list_upload_speed.append(upload_speed)
    time.sleep(60)
    print(list_download_speed)
    print(list_upload_speed)
x = [1, 2, 3, 4, 5]
plt.plot(x, list_download_speed, label="Download Speed")
plt.plot(x, list_upload_speed, label="Upload Speed")
plt.title("Speed")
plt.xlabel("Time")
plt.ylabel("Speed")
plt.legend()
plt.show()
