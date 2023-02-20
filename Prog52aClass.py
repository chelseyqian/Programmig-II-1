class Shape:
  # Constructor: set up class data
  def __init__(self, length, width):
    # self: give access to the class
    self.length = length
    self.width = width
    self._area = 0;
    self.perim = 0;
    # 变量前面加下划线，就变成了private，只能在此class里使用

  # Setter/Mutator
  def calculate(self):
    self._area = self.length * self.width
    self.perim = self.length * 2 + self.width * 2

  # Accessor/Getters
  def getArea(self):
    return self._area

  def getPerimeter(self):
    return self.perim

def main():
  len = int(input("Enter length: "))
  wid = int(input("Enter width: "))
  shape = Shape(len, wid)
  shape.calculate()
  print("Area: ", shape.getArea())
  print("Perimeter: ", shape.getPerimeter())

if __name__ == "__main__":
  main()