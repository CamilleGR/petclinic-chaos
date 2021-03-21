import requests
from datetime import datetime
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import argparse



# Arg parser
parser = argparse.ArgumentParser(description='Request an url every seconds to check the status code.')
parser.add_argument('-u','--url',nargs=1, help='url to monitor')
parser.add_argument('-p','--period',nargs=1,default=15, help='repeat period. [default=15s]')
args = parser.parse_args()

# HTTP Session Error handler
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


print('############### START MONITORING :',args.url[0],'###############')
while 1:
    time.sleep(args.period)
    try:
        r = session.get(args.url[0],headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Safari/537.36",
        "Accept-Encoding": "gzip, deflate"
        })

        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("[", dt_string,'] - ',r.status_code,' OK' if r.status_code==200 else ' KO')
    except Exception as e :
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("[", dt_string,'] - Error : Unable to connect')
