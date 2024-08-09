Q: program to find if given number is prime or not?
    a=int(input())
    
    for i in range(2,a):
        if a%i==0:
            print(f"{a} is a not prime number")
            break
    else:
        print(f"{a} is a prime number")

output:  
         10
         10 is a not prime number
