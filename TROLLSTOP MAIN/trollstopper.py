#By Grant Baumstark
#GrantBaum on Github

#Importing needed librarys.

import requests
import time

#Title of the aplication will be displayed in the terminal.

print('''
████████╗██████╗░░█████╗░██╗░░░░░██╗░░░░░░██████╗████████╗░█████╗░██████╗░██████╗░███████╗██████╗░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
░░░██║░░░██████╔╝██║░░██║██║░░░░░██║░░░░░╚█████╗░░░░██║░░░██║░░██║██████╔╝██████╔╝█████╗░░██████╔╝
░░░██║░░░██╔══██╗██║░░██║██║░░░░░██║░░░░░░╚═══██╗░░░██║░░░██║░░██║██╔═══╝░██╔═══╝░██╔══╝░░██╔══██╗
░░░██║░░░██║░░██║╚█████╔╝███████╗███████╗██████╔╝░░░██║░░░╚█████╔╝██║░░░░░██║░░░░░███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝''')
time.sleep(2)
print('Stops you from clicking a troll link ever again!')
time.sleep(2)
url = input('URL TO CHECK: ')

#Makes the code look cooler.

time.sleep(2)
print('ANALYZING...')
time.sleep(1)
print('ANALYZING...')
time.sleep(1)
print('ANALYZING...')
time.sleep(1)
print('ANALYZING...')
time.sleep(1)
print('ANALYZING...')
time.sleep(2)
headers = {'User-Agent': '<yourUserAgent>'}

#The python script looks for certain words that are included in the actual video and not just the link.
#Keywords (that tell the computer when it is a troll) go here.

keywords = ['Rick','Astley','Rick Astley - Never Gonna Give You Up (Video)',
'Official Rick Astley','Never gonna give you up','Never gonna let you down',
'Never gonna run around and desert you','Never gonna make you cry','Never gonna say goodbye',
'Never gonna tell a lie and hurt you','Stick Bugged','Get Stick Bugged Lol',
'You know the rules and so do I','Get trolled','Trolled','Youve been trolled','Rickroll',
'Sussy','Baka','Sussy Baka','Among us','Amogus','Chungus','Coconut malled','Jebated']

#Looks for the URL and searches for keywords.

response = requests.get(url, headers=headers)

#Finds results based on what words are in the video and description.

def checker(resp):

    found_keywords = 0
    for el in keywords:
        if el.lower() in str(resp.content).lower():
            print(f"DONT CLICK. IT IS A TROLL LINK. KEYWORDS FOUND: ")
            break
    for el in keywords:
        if el.lower() in str(resp.content).lower():
            print(f'-{el}')
            found_keywords = found_keywords+1

    if found_keywords == 0:
        print(f"Not a troll! Link is safe to click.")

#Prints results.

checker(response)