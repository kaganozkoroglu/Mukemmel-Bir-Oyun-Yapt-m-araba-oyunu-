import subprocess
import time

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
video_url = "https://www.youtube.com/shorts/6L2ezLr4cco?feature=share"

adet = 15
bekleme = 1

for i in range(adet):
    subprocess.Popen([chrome_path, "--new-window", video_url])
    time.sleep(bekleme)

print("Bitti ya")    