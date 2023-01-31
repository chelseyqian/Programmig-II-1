n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
gcd = 1

large = n1
if n1 > n2:
  large = n2

while not (n1 % large == 0 and n2 % large == 0):
  large -= 1

gcd = large

print("The GCD is " + str(gcd))