def main():
  try:
    with open("Langdat/prog213b.txt", 'r') as f:
      list = []
      for line in f:
        list.append(int(line))

      for x in list:
        if x < 100:
          print("Quantity: ", x)
          print("Price: ", 5.95)
          print("Total cost: ", (x * 5.95))
          print()
        elif x < 200:
          print("Quantity: ", x)
          print("Price: ", 5.75)
          print("Total cost: ", (x * 5.75))
          print()
        elif x < 300:
          print("Quantity: ", x)
          print("Price: ", 5.4)
          print("Total cost: ", (x * 5.4))
          print()
        else:
          print("Quantity: ", x)
          print("Price: ", 5.15)
          print("Total cost: ", (x * 5.15))
          print()

  except Exception as e:
    print("Error: ", e)

if __name__ == "__main__":
  main()