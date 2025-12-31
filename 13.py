n = int(input("Enter any number: "))
sumo = 0
for i in range(1,n):
    if (n%i == 0):
        sumo = sumo + i
if(sumo == n):
    print('The number is a perfect number! ')
else:
    print('The number is not a perfect number! ')