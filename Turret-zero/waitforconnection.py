import requests
import time
import ipc
import subprocess
import credentials

# Wait for Network
ipc.send(35022, "WaitForNetwork")
while True:
    ip = subprocess.run(['hostname', '-I'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    if len(ip.split('.'))>1:
        print(f"IP adress found: {ip}")
        break
    time.sleep(3)


# Wait for Server
while True:
    try:
        response = requests.get(f"http://www.micromegas.ovh/grootcam/angle.php", auth=(credentials.user, credentials.passwd))
        if response.status_code == 200:
            print(f"Response from server: {response.text}")
            break
        else:
            print(f"HTTP return code: {response.status_code}")
            ipc.send(35022, "ServerError")

    except Exception as e:
        print(e)
        ipc.send(35022, "WaitForNetwork")

    time.sleep(3)

