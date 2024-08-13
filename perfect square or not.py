Q: check wheather given number is Perfect square or not?

    a=int(input())
    count=0
    for i in range(1,a+1):
        if a==i*i:
            count+=1
    if count==1:
        print("yes")
    else:
        print("no")

output: 
      49
      yes
      50
      no
