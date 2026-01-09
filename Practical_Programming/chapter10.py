# How to get current working directory
import os
print(os.getcwd())

# use os.chdir('target directory') to change the current working directory

# How to pull data from a website
import urllib.request
url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
# 1. Create a Request object and add a 'User-Agent' header
req = urllib.request.Request(
    url, 
    headers={'User-Agent': 'Mozilla/5.0'}
)
# 2. Open the request instead of the raw URL
with urllib.request.urlopen(req) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        # print(line)

from typing import TextIO
from io import StringIO

# Problem 1
def backup_file():
    original_file = input('Type the full name of the file to backup: ')
    with open(original_file) as file:
        contents = file.read()
        backup_name = original_file + '.bak'
        with open(backup_name, 'w') as output:
            output.write(contents)
    print(f'Sucessfully backed up to {backup_name}')
            
backup_file()

