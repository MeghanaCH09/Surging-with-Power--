def power(num):
    count=0
    if num>0 &(~num&(num-1)) ==0:
        while(num>1):
            num>>=1
            count+=1
        if(count%2==0):
            return True
        else: 
            return False

n=int(input("Enter a number: "))
if power(n):
    print(f"Yes, {n} it is a power of 4")
else: 
    print(f"No, {n} Not a power of 4")