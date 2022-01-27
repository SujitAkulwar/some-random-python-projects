def ans(number,n):
    if n==1:
        print("factorial of ",n," is ",number) 
    elif n>1:
        n = n-1
        number = number * n
        ans(number,n)
       

number = int(input("Enter a number : "))
n = number
if number>0:
    ans(number,n)
else:
    print("ERROR 404")
    print("Please enter a positive number") 
