Q: Greatest number among three numbers

  a = int(input("Enter first number: ")) 
  b = int(input("Enter second number: "))
  c = int(input("Enter third number: "))
  
  if (a > b and a > c):
      print(f"a is the greatest number")
  elif (b > a and b > c):
      print(f"b is the greatest number")
  else:
      print(f"c is the greatest number")

output:

  Enter first number: 1      
  Enter second number: 2
  Enter third number: 5
  c is the greatest number
