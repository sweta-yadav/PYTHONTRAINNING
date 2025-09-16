# This function prints all prime factors of a given number using recursion.
def prime_factors(n, i):
    if(n==1):
        return
    while(n % i != 0):
        i += 1
   
    print(i, end=" ")
    prime_factors(n // i, i)
    

number = int(input("Enter a number: "))
i=2
prime_factors(number, i)
