b = int(input("Enter the base number whose power you want to find: "))
p = int(input("\nEnter the power number which will exponentiate the base number: "))
c=1

for i in range(1, p+1):
    c = c*b

print("\nAfter exponentiation =", c)