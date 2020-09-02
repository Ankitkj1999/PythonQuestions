print("**QUESTION NO. 1 SOLUTION**")
print("submitted by Abhinav Kumar Singh")
from itertools import permutations 

import string 

  

s = "jhon"

a = string.ascii_letters 

p = permutations(s) 

  
#  dictionary 

d = [] 

for i in list(p): 

  

    # Print only if not in dictionary 

    if (i not in d): 

        d.append(i) 

        print(''.join(i))