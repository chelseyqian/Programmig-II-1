class Calculate:
  def __init__(self, n1, n2, n3, n4):
    self.n1 = n1
    self.n2 = n2
    self.n3 = n3
    self.n4 = n4
    self.sum = 0
    self.ave = 0

  def cal(self):
    self.sum = self.n1 + self.n2 + self.n3 + self.n4
    self.ave = self.sum / 4

  def getSum(self):
    return self.sum

  def getAve(self):
    return self.ave

def main():
  n1 = int(input("Enter the first number: "))
  n2=int(input("Enter the second number: "))
  n3=int(input("Enter the third number: "))
  n4=int(input("Enter the fourth number: "))
  calculate = Calculate(n1, n2, n3, n4)
  calculate.cal()
  print("Sum is ", calculate.getSum())
  print("Average is ", calculate.getAve())

if __name__ == "__main__":
  main()