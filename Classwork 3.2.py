p = int(input("Enter loan amount: "))
R = int(input("Enter the rate of interest: "))
n = int(input("Enter the duration of loan: "))

r=R/(12*100)
x = p*r*((1+r)**n)/((1+r)**n-1)
print("Your monthly payment should be: ",x)

for i in range (1,n):
    b = p-x
    print("Balance is", b)
    p = b
