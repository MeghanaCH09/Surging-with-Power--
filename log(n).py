def power(m,n):
    result=1
    while n>0:
        if(n%2==0):
            m=m*m
            n>>=1
        else:
            result=result * m
            n=n-1
    return result

m=int(input("Enter a value to represent m: "))
n=int(input("Enter a value to represent n: "))
print("The total of", m ,"and", n ,"is: ", power(m,n))