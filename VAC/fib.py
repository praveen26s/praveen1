n=int(input("enter a number"))
sum=0
m=n
while m>0:
    digit=m%10
    sum=(sum*10)+digit
    m//=10
if n ==sum:
    print(n,"is an amstrong number")
else:
    print(n,"is not an amstrong number")