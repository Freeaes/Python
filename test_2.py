import requests,random


def get_random_proxies(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append(ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': 'http://'+proxy_ip, 'https': 'https://'+proxy_ip}
    return proxies


url="http://httpbin.org/ip"


ip_list=[
"209.43.33.98:8080",
"35.222.171.32:80",
"167.172.248.53:3128",
"168.149.146.164:8080",
"168.149.142.170:8080",
"198.232.160.7:8080",
"45.79.159.216:3128",
"198.71.61.207:80",
"67.63.33.7:80",
"72.35.40.34:8080",
"168.149.146.172:8080",
"199.116.170.156:8080",
"199.116.170.172:8080",
"199.116.170.173:8080",
"199.116.170.164:8080",
"199.116.170.148:8080",
"199.116.170.171:8080",
"199.116.170.140:8080",
"199.116.170.132:8080",
"199.116.170.165:8080",
"62.210.124.248:3128",
"72.35.40.34:8080",
"51.158.68.68:8811",
"51.158.68.133:8811",
"51.158.111.229:8811",
"51.158.108.135:8811",
"51.158.68.26:8811",
"163.172.136.226:8811",
"168.149.156.172:8080",
"51.158.120.84:8811",
"194.167.44.91:80",
"51.158.106.54:8811",
"200.110.172.2:80",
"51.158.98.121:8811",
"51.158.99.51:8811",
"51.158.113.142:8811",
"163.172.152.52:8811",
"45.77.24.239:3128",
"35.200.115.57:8080",
"52.67.227.92:8080",
"163.172.147.94:8811",
"51.158.123.35:8811",
"46.4.35.219:3128",
"200.89.178.193:8080",
"200.89.178.196:8080",
"200.89.178.209:8080",
"181.30.28.12:3128",
"200.89.174.64:3128",
"181.30.28.14:8080",
"181.30.28.201:3128",
"200.89.178.19:8080",
"200.89.174.70:3128",
"181.30.28.13:3128",
"200.89.174.181:3128",
"200.89.178.194:8080",
"80.59.199.213:8080",
"186.64.122.214:8080",
"187.16.4.126:8080",
"116.196.85.150:3128",
"118.70.144.77:3128",
"128.199.252.41:3128",
"168.149.131.172:8080",
"200.89.174.105:80",
"200.89.178.211:8080",
"168.149.131.164:8080",
"209.90.63.108:80",
"198.232.160.7:8080",
"78.92.232.202:8080",
"189.43.68.169:80",
"70.169.70.83:80",
"193.107.105.73:8080",
"78.46.8.204:80",
"18.231.115.201:3402",
"177.125.43.100:8080",
"200.89.178.208:3128",
"47.244.239.147:80",
"113.28.129.60:80",
"163.180.117.236:8080",
"103.99.177.248:3128",
]
num=1
for i in ip_list:
    proxies=get_random_proxies(ip_list)
    print(proxies)
    # r=requests.get(url,proxies)
    # print(str(num)+' : '+proxy_ip+' == '+str(r.status_code))
    num+=1

