def ans(number,n):
    temp = n
    power=0
    while(temp>0):
        temp=int(temp/10)
        power=power+1
    num1=0
    num2=0
    while(n>0):
        num1=int(n%10)
        num2=(num1**power)+num2
        n=int(n/10)
    if num2==number:
        print(number," is a Armstrong number.")
    else:
        print(number," is not a Armstrong number.")


number = int(input("enter a number : "))
n=number
if number>=0:
    ans(number,n)