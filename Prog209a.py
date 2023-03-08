def main():
  try:
    with open("Langdat/prog215a.dat", 'r') as f:
      list = []
      for line in f:
        list.append(int(line))

      less = 0
      greater = 0
      total = len(list)

      for x in list:
        if x < 500:
          less += 1
        else:
          greater += 1

      print("The number of numbers less than 500 is ", less)
      print("The number of numbers greater than or equal to 500 is ", greater)
      print("The total number of numbers is ", total)

  except Exception as e:
    print("Error", e)

if __name__ == "__main__":
  main()