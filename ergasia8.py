import urllib.request
import json
from time import sleep
def get_coin_data(coin):
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR&e=CCCAGG"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    d=json.loads(html)
    return d[coin]["EUR"]
f=open('wallet.txt','r')
x=f.read()
f.close()
y=json.loads(x)
z=list(y.keys())

for i in z:
    print(get_coin_data(i)*y[i])
    sleep(5)
