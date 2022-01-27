import math

def ans(a,b,c):
    root = (b*b)-(4*(a*c))
    roots = math.sqrt(abs(root))
    if roots<0:
        print("error 404")
    elif roots==0:
        print("only one root : ",-b/(2*a))
    else:
        print("Two roots : ",(-b+root)/(2*a)," and ",(-b+root)/(2*a))
    
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))

if(a==0):
    print("error 404")
else:
    ans(a,b,c)    