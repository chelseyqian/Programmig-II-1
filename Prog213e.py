def main():
  try:
    list = []
    with open("Langdat/prog213e.dat", 'r') as f:
      for line in f:
        list.append(int(line))
      
      count1 = 0
      count2 = 0
      count3 = 0
      count4 = 0
      count5 = 0
      for x in range(1, list[0]+1):
        if list[x] < 20:
          count1 += 1
        elif list[x] < 40:
          count2 += 1
        elif list[x] < 60:
          count3 += 1
        elif list[x] < 80:
          count4 += 1
        else:
          count5 += 1

      print("Age Group\tDistribution\tPercentage")
      print(f"<20\t{count1}\t{count1/list[0]}")
      print(f"20-39\t{count2}\t{count2/list[0]}")
      print(f"40-59\t{count3}\t{count3/list[0]}")
      print(f"60-79\t{count4}\t{count4/list[0]}")
      print(f">79\t{count5}\t{count5/list[0]}")

  except Exception as e:
    print("Error: ", e)

if __name__ == "__main__":
  main()