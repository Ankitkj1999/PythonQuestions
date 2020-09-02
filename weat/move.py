"""import shutil

shutil.move('cr/','other/')"""
"""x=4
if not x==3:
 print('true')"""

"""import glob

if not glob.glob!=('/cf'):
    print ('condition satisfied')
else:
    print('not found')"""

import os
import fnmatch

for filename in os.listdir('.'):
      if fnmatch.fnmatch(filename, '.py '):
                   print(filename)