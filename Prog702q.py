from Cl702q import *

def main():
  try:
    vehicles = []
    nums = []
    names = []
    tire = []
    others = []
    with open("Langdat/prog702q.txt", 'r') as f:
      for line in f:
        num = int(line.strip())
        name = line.strip()
        tires = int(line.strip())
        if num == 1:
          value = int(line.strip())
          v = Car(name, tires, value)
          vehicles.append(v)
        elif num == 2:
          miles = int(line.strip())
          value = int(50000 - miles * 0.25)
          v = Truck(name, tires, value, miles)
          vehicles.append(v)
        elif num == 3:
          city = line
          v = Bus(name, tires, 50000, city)
          vehicles.append(v)
        num = int(f.readline())

    total = len(vehicles)
    totalValue = 0
    carValue = 0
    large = ""
    leastTruck = ""
    leastValue = 1000000
    carTire = 0
    truckTire = 0
    busTire = 0
    for v in vehicles:
      totalValue += v.getValue()
      if isinstance(v, Car):
        carTire += v.getTires()
        carValue += v.getValue()
      if isinstance(v, Truck):
        truckTire += v.getTires()
        if v.getValue < leastValue:
          leastValue = v.getValue()
          leastTruck = v.getName()
      if isinstance(v, Bus):
        busTire += v.getTires()
        if len(v.getCity()) > len(large):
          large = v.getCity()

    print("Total number of vehicles is ", total)
    print("Total amount that the cars are worth is ", carValue)
    print("Total amount that the vehicles are worth is ", totalValue)
    print("The longest city name for buses is ", large)
    print("The truck that has the least value is ", leastTruck)
    print("Total number of tires of cars is ", carTire)
    print("Total number of tires of trucks is ", truckTire)
    print("Total number of tires of buses is ", busTire)

  except Exception as e:
    print("Error: ", e)

if __name__ == "__main__":
  main()