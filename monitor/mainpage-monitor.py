import requests
from datetime import datetime
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


print('############### START MONITORING ###############')
while 1:
    time.sleep(15)
    try:
        r = session.get("http://192.168.99.101:30000",headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Host":"192.168.99.101:30000"
        })

        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("[", dt_string,'] - ',r.status_code,' OK' if r.status_code==200 else ' KO')
    except Exception as e :
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("[", dt_string,'] - ',e)