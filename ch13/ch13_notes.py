import math
import http.server
import webbrowser
import ipaddress
import requests

r = requests

def browse(n):
    web = webbrowser.open(n, new=1)
    print('opening page...')
    return web

n = input('Enter URL: ')
browse(n)

print('Did it work?')
