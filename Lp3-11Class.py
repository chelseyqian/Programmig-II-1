class ClLp311:
  def __init__(self, ds, co, db, te):
    self.design = ds
    self.coding = co
    self.debug = db
    self.test = te
    self.total = 0
    self.percents = [0] * 4

  def _percent(self, number):
    return round((number / self.total) * 100, 2)

  def calculate(self):
    self.total = self.design + self.coding + self.debug + self.test
    self.percents[0] = self._percent(self.design)
    self.percents[1] = self._percent(self.coding)
    self.percents[2] = self._percent(self.debug)
    self.percents[3] = self._percent(self.test)

  def display(self):
    print("Task\t\tTime")
    print(f"Designing\t\t{self.percents[0]}%")
    print(f"Coding\t\t{self.percents[1]}%")
    print(f"Debugging\t\t{self.percents[2]}%")
    print(f"Testing\t\t{self.percents[3]}%")

def main():
  print("Enter the time spent on each task: ")
  design = float(input("Enter the time for designing: "))
  coding = float(input("Enter the time for coding: "))
  debug = float(input("Enter the time for debugging: "))
  test = float(input("Enter the time for testing: "))
  total = ClLp311(design, coding, debug, test)
  total.calculate()
  total.display()

if __name__ == "__main__":
  main()