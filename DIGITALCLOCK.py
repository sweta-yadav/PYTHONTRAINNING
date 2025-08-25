# import time
# import os

# def digital_clock():
#     h = 3
#     m = 28
#     s = 0
    
#     while True:
        
#         print(f"\n\n\t\t {h:02d}:{m:02d}:{s:02d}")
        
#         time.sleep(1)   
#         os.system("cls")  
        
        
#         s += 1
#         if s == 60:
#             m += 1
#             s = 0
#         if m == 60:
#             h += 1
#             m = 0
#         if h == 12:
#             h = 0


# digital_clock()




#METHOD 2

import time
import sys

h = 12   
m = 20   
s = 0    

while True:
    
    sys.stdout.write(f"\r{h:02d}:{m:02d}:{s:02d}")
    sys.stdout.flush()

    time.sleep(1)  
    s += 1

    if s == 60:   
        s = 0
        m += 1

    if m == 60:   
        m = 0
        h += 1

    if h == 24:   
        h = 0