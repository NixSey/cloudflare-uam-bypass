import requests
import sys
import os

def main():
    f = open(str(sys.argv[1]),'wb')
    r = requests.get('https://www.proxy-list.download/api/v1/get?type=http')
    f.write(r.content)
    r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
    f.write(r.content)
    r = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
    f.write(r.content)
    r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
    f.write(r.content)
    f.close()
