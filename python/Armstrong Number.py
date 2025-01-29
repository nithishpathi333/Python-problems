Q: check if given number is Armstrong number or not?

    arms_number=int(input())
    digits=str(arms_number)
    length=len(digits)
    sum_arms_number=sum(int(digit)**length for digit in digits)
    if arms_number==sum_arms_number:
        print("yes")
    else:
        print("no")

output: 
    153
    yes
