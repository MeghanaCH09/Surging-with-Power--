def power(num):
    if num<=0:
        return False
    return (num&(num-1))==0

n=int(input("Enter a number: "))
if power(n):
    print("Yes, it is a power of 2")
else: 
    print("Not a power of 2")