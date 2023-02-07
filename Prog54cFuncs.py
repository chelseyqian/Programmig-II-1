def calcArea(r):
  return 3.14159 * r * r

def calcCir(r):
  return 2 * 3.14159 * r

def areaCir(r):
  area = calcArea(r)
  cir = calcCir(r)
  return area, cir

def main():
  radius = int(input("Enter radius: "))
  a, c = areaCir(radius)
  print(f"Area: {a}\nCircumference: {c}")

if __name__ == "__main__":
  main()