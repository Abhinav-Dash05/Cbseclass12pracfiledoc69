no = int(input('Enter any number to check: '))
noo = no
sum = 0
while(no>0):
    ans = no%10
    sum = sum+ (ans*ans*ans)
    no = int(no % 10)
if sum == noo:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")