num = int(input("Enter a number between 1 to 20: "))
secret = 6

print("Computer's number: " + str(secret))
print("Player's number: " + str(num))

if num == secret:
  print("You won")
else:
  print("Better luck next time")
  