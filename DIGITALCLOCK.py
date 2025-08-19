import time
import os

def digital_clock():
    h = 3
    m = 28
    s = 0
    
    while True:
        # Print time in HH:MM:SS format
        print(f"\n\n\t\t {h:02d}:{m:02d}:{s:02d}")
        
        time.sleep(1)   # wait for 1 second
        os.system("cls")  # clear screen (Windows). Use "clear" on Linux/Mac.
        
        # Update seconds, minutes, hours
        s += 1
        if s == 60:
            m += 1
            s = 0
        if m == 60:
            h += 1
            m = 0
        if h == 12:
            h = 0

# Run clock
digital_clock()
