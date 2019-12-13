import requests, time

while(1):
    r = requests.get("http://127.0.0.1:5000/show")
    print(r)
    time.sleep(2)