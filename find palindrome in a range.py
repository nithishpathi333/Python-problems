Q: program to find all palindromes in given range

min_a=int(input("enter the min number of the range:"))
max_a=int(input("enter the max number of the range:"))

count=0
for num in range(min_a,max_a+1):
    num_str=str(num) # here we are taking number,as quesion is about range.But to check palimdrome or not 
                     # we must convert the given int to str because it checks only when input is string 
    if num_str==num_str[::-1]:
        count+=1
        
print("palindromes within the range:",count)

Output: 
        enter the min number of the range:1
        enter the max number of the range:100
        palindromes within the range: 18

    


