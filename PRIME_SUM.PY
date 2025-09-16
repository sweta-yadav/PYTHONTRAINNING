for i in range(200,1000):
    if(prime(i) and sod(prime(i)) and alldig(i)):



def prime(i):
    if(i !=1 and i != 0):
        for j in range(2, int(i**0.5) + 1):
            if(i % j == 0):
                return False
        return True

def sod(i):
    if(i != 1 and i != 0):
        s = 0
        while(i > 0):
            s += i % 10
            i //= 10
        return s % 2 == 0

def alldig(i)