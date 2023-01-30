eggs = int(input("Enter the number of eggs: "))
price = 0.0

if eggs >= 0 and eggs < 4:
  price = 0.5
elif eggs >= 4 and eggs < 6:
  price = 0.45
elif eggs >= 6 and eggs < 11:
  price = 0.4
elif eggs == 11:
  price = 0.35
else:
  price = 0.35 / 12

print("The bill is equal to " + str(eggs * price))