def sumn(n):
  if n == 3:
    return 3
  return n + sumn(n - 3)

def main():
  num = int(input("Enter a number: "))
  while num != 0:
    sum = sumn(num)
    print("Sum is ", sum)
    num = int(input("Enter a number: "))

if __name__ == "__main__":
  main()