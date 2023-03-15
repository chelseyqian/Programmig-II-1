from Cl702q import *

def main():
  try:
    vehicles = []
    with open("Langdat/prog702q.txt", 'r') as f:
      for line in f:
        vehicles.append(line)
      for i in range(0, len(vehicles), 4):
        num = vehicles[i]
        name = vehicles[i+1]
        tires = vehicles[i+2]
        if num == 1:
          value = vehicles[i+3]
          v = Car(name, tires, value)
          vehicles.append(v)
        elif num == 2:
          miles = vehicles[i+3]
          value = int(50000 - miles * 0.25)
          v = Truck(name, tires, value, miles)
          vehicles.append(v)
        elif num == 3:
          city = vehicles[i+3]
          v = Bus(name, tires, 50000, city)
          vehicles.append(v)
        

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
      totalValue += v.value
      if isinstance(v, Car):
        carTire += v.tires
        carValue += v.value
      if isinstance(v, Truck):
        truckTire += v.tires
        if v.getValue < leastValue:
          leastValue = v.value
          leastTruck = v.name
      if isinstance(v, Bus):
        busTire += v.tires
        if len(v.city) > len(large):
          large = v.city

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