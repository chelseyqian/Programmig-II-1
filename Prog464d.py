import random
import numpy as np

def printMatrix(mat):
  for row in mat:
    for num in row:
      print(f"{num:3d}", end = "")
    print()

def main():
  mat1 = []
  mat2 = []
  for r in range(5):
    row1 = []
    row2 = []
    for c in range(5):
      rnd1 = random.randint(-50, 99)
      row1.append(rnd1)
      row2.append(0)
    mat1.append(row1)
    mat2.append(row2)
  for i in range(5):
    for j in range(5):
      mat2[j][i] = mat1[i][j]

  print("Original: ")
  printMatrix(mat1)

  print("Transpose: ")
  printMatrix(mat2)

if __name__ == "__main__":
  main()