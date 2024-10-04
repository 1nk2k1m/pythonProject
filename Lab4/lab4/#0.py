n= int(input("Please enter the first number: "))
m= int(input("Please enter the second number: "))
p= input("Please choose the operation:  " )
result=0
if p== "+" :
    result= n + m
elif p== "-":
    result= n-m
elif p== "*":
    result= n*m
elif p== "/":
    result= n/m
print (n,p,m,"=", result)