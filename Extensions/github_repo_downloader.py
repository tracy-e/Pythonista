# -*- coding: utf-8 -*-
"""
Created by TracyYih 2017-4-6.
"""

import appex
import os
import urllib.request
import zipfile
import random
import re
import clipboard

download_dir = '../../Github/'

if appex.is_running_extension():
	url = appex.get_url()
else:
	url = clipboard.get()

m = re.match((r'^http(s?)://([\w-]*\.)?github\.com/(?P<user>[\w-]+)/(?P<repo>[\.\w-]*)'
                 '((/tree|/blob)/(?P<branch>[\w-]*))?'), url)
if m is not None:
	user = m.groupdict()['user']
	repo = m.groupdict()['repo']
else:
	user = input('Please enter the name of the user > ')
	repo = input('Please enter the name of the repo > ')

url_format = 'https://github.com/{user}/{repo}/archive/master.zip'
url = url_format.format(user=user, repo=repo)

print(url)

downloadname = download_dir + str(random.randint(0x000000, 0xFFFFFF)) + "_master.zip"

print("Downloading...")
urllib.request.urlretrieve(url, downloadname)

print("Extracting...")
zipped = zipfile.ZipFile(downloadname, 'r')
zipped.extractall(download_dir)
zipped.close()

print("Cleaning up...")
os.remove(downloadname)
print('Done')
