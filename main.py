import urllib.request
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;92m"
RESET = "\033[0;0m"
BOLD = "\033[1;33m"
REVERSE = "\033[;7m"

site = 'https://www.google.com/' #URL to Site
try:
    web = urllib.request.urlopen(site)
except urllib.request.URLError:
    print(CYAN + 'STATUS - ' + RED + '404')
else:
    print(CYAN + 'STATUS - ' + GREEN + '200')
print(GREEN + '='*30)
print(RESET + 'GitHub: ' + GREEN + 'gitErmesonAlves')
print(RESET + 'Instagram: ' + GREEN + '_ermesonalves_')
print(RESET + 'Linkedin: ' + GREEN + 'ermesonalves')
print(GREEN + '='*30)
