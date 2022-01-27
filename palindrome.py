def ans(number):
    num1=number
    num2=0
    while num1>0 :
        num2 = int(num2*10)+(num1%10)
        num1 = int(num1/10)

    if num2 == number:
        print(number ," is a pal")
    else:
        print(number ," is not a ")       

number = int(input("Enter a number : "))
if number>0:
    ans(number)