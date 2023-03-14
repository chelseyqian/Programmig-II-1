class Vehicle:
  def __init__(self, name, tires, value):
    self._name = name
    self._tires = tires
    self._value = value

  def getName(self):
    return self._name

  def getTires(self):
    return self._tires

  def getValue(self):
    return self._value


class Car(Vehicle):
  def __init__(self, name, tires, value):
    super().__init__(name, tires, value)


class Truck(Vehicle):
  def __init__(self, name, tires, value, miles):
    super().__init__(name, tires, value)
    self.miles = miles


class Bus(Vehicle):
  def __init__(self, name, tires, value, city):
    super().__init__(name, tires, value)
    self.city = city

  def getCity(self):
    return self.city