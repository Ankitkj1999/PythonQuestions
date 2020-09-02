"""
import glob

if glob.glob!=('/Python*'):
    print ('condition satisfied')
else:
    print('not found')
"""

import os
import shutil

if not os.path.exists("other"):
    os.makedirs("other")
    print("created other directory")

source='/Weat/other/'

files = os.listdir()

for file in files:
    if file.startswith("x"):
        for eachFile in os.listdir(file):
            filePath = os.path.join(file, eachFile)
            shutil.move(filePath, source)