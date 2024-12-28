import os, sys, random, string, time
try:import requests
except:os.system('pip install requests')
import requests
# Line Function 
def linex():
    print('\033[0m================================================')
# Logo For script 
logo = f"""
\x1b[38;5;46m     ▗▖  ▗▖ ▗▄▖ ▗▄▄▄  ▗▄▄▄▖▗▄▄▖  ▗▄▖▗▖  ▗▖
\x1b[38;5;47m     ▐▛▚▖▐▌▐▌ ▐▌▐▌  █ ▐▌   ▐▌ ▐▌▐▌ ▐▌▝▚▞▘
\x1b[38;5;48m     ▐▌ ▝▜▌▐▌ ▐▌▐▌  █ ▐▛▀▀▘▐▛▀▘ ▐▛▀▜▌ ▐▌
\x1b[38;5;49m     ▐▌  ▐▌▝▚▄▞▘▐▙▄▄▀ ▐▙▄▄▖▐▌   ▐▌ ▐▌ ▐▌\x1b[38;5;46m V/0.2
\033[0m================================================
 \033[1;35m        Developer : Saifur Rahman Siam
         YouTube   : Crypto Hub (@nbprg)
         GitHub    : github.com/nbprg
         Telegram  : @TataCuto
\033[0m================================================"""
proxy_list = open('proxy.txt','r').read().splitlines()
# get Captcha token 
def get_token():
    while True:
         json_data = {
            'username': api_key
         }
         response = requests.get('https://cryptohubnp.pythonanywhere.com/get_captcha',json=json_data).json()
         if response['success']:
              print(f'\r\r\033[0m>>\033[1;32m Captcha token get successful \033[0m')
              return response['token']
         else:time.sleep(0.5)
# clear terminal session & print logo
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls');print(logo)
    else:
        os.system('clear');print(logo)
# get ip using proxy  / not using for speed up
clear_screen()
api_key = input("\033[0m>>\033[1;32m Input Your Api Key : ")
def get_ip(proxy_url):
     proxy = {'http': proxy_url,'https': proxy_url}
     try:
         response = requests.get('http://ip-api.com/json',proxies=proxy)
         return response.json()['query']
     except:
        return None
# get headers set / with `auth_token` or head only
def get_headers(auth_token=None):
     headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://app.nodepay.ai',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
            }
     if auth_token:
            headers['Authorization'] = f'Bearer {auth_token}'
            headers['origin'] = 'chrome-extension://lgmpfmgeabnnlemejacfljbmonaomfmm'
     return headers

# registration account  |  using proxy or not
def reg_accaunt(email, password, username, ref_code, proxy_url=None, captcha_token=None):
   try:
       if proxy_url:
            print(f'\r\r\033[0m>>\033[1;32m Proxy : {proxy_url} \033[0m')
            proxy_url = {'http': proxy_url,'https': proxy_url}
       register_data = {
           'email': email,
           'password': password,
           'username': username,
           'referral_code': ref_code,
           'recaptcha_token': captcha_token
       }
       headers = get_headers()
       url = "https://api.nodepay.ai/api/auth/register"
       response = requests.post(url,headers=headers,json=register_data,proxies=proxy_url,timeout=10)
       response.raise_for_status()
       return response.json()
   except Exception as e:
       print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m');linex();time.sleep(1)
# login account and age authorization token
def login_acccaunts(email, password, captcha_token,proxy_url):
   try:
       json_data = {
           'user': email,
           'password': password,
           'remember_me': True,
           'recaptcha_token': captcha_token
       }
       proxy_url = {'http': proxy_url,'https': proxy_url}
       headers = get_headers()
       url = "https://api.nodepay.ai/api/auth/login"
       response = requests.post(url,headers=headers,json=json_data,proxies=proxy_url,timeout=10)
       response.raise_for_status()
       return response.json()
   except Exception as e:
       print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m');linex();time.sleep(1)
# active account and confirmation 
def active_recent_accaunt(auth_token,proxy_url):
   try:
       json_data={}
       url = "https://api.nodepay.ai/api/auth/active-account"
       headers = get_headers(auth_token)
       proxy_url = {'http': proxy_url,'https': proxy_url}
       response = requests.post(url, headers=headers,json=json_data,proxies=proxy_url,timeout=10)
       response.raise_for_status()
       if not response.json()['msg'] == 'Success':
           response = requests.post(url, headers=headers,json=json_data,proxies=proxy_url,timeout=10)
       if not response.json()['msg'] == 'Success':
           response = requests.post(url, headers=headers,json=json_data,proxies=proxy_url,timeout=10)
       return response.json()
   except Exception as e:
       print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m');linex();time.sleep(1)

# main def for possess full action
def main():
    clear_screen()
    try:reff_limit = int(input('\033[0m>>\033[1;32m Put Your Reff Amount: '))
    except:print('\033[1;32m⚠️ Input Wrong Default Reff Amaunt is 1k ');reff_limit=1000;time.sleep(1)
    ref_code = input("\033[0m>>\033[1;32m Input referral code : ")
    clear_screen();success_crt = 0
    for atm in range(reff_limit):
        try:
            print(f'\r\r\033[0m>>\033[1;32m Possessing  {str(success_crt)}/{str(reff_limit)} complete : {((atm+1) / reff_limit) * 100:.2f}% ')
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = str(''.join(random.choice(characters) for _ in range(12))).lower()
            password = str(''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3)))
            email = f"{username}{str(random.choice(domains))}"
            proxy_url = random.choice(proxy_list)
            captcha_token = get_token()
            response_data = reg_accaunt(email, password, username, ref_code, proxy_url, captcha_token)
            #print(response_data)
            if response_data['msg'] == 'Success':
                print(f'\r\r\033[0m>>\033[1;32m Account Create Successful \033[0m')
                captcha_token = get_token()
                response_data = login_acccaunts(email, password, captcha_token,proxy_url)
                #print(response_data)
                if response_data['msg'] == 'Success':
                    print(f'\r\r\033[0m>>\033[1;32m Account Login Successfuly \033[0m')
                    auth_token = response_data['data']['token']
                    response_data = active_recent_accaunt(auth_token,proxy_url)
                    #print(response_data)
                    if response_data['msg'] == 'Success':
                         print(f'\r\r\033[0m>>\033[1;32m Successfuly Referral Done \033[0m')
                         success_crt+=1
                         open('accaunts.txt','a').write(f"{str(email)}|{str(password)}|{str(auth_token)}\n");time.sleep(1)
                    else:
                        print(f'\r\r\033[1;31m🌲 Referral Error, Not Success \033[0m {response_data["msg"]}');time.sleep(1)
                        linex()
                else:
                    print(f'\r\r\033[1;31m🌲 Account Login Failed \033[0m {response_data["msg"]}');time.sleep(1)
                    linex()
            else:
                print(f'\r\r\033[1;31m🌲 Account Create Failed \033[0m {response_data["msg"]}');time.sleep(1)
                linex()
            linex()
        except Exception as e:
            print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m');linex();time.sleep(1)
    print('\r\r\033[0m>>\033[1;32m Your Referral Completed \033[0m')
    exit()
main()
