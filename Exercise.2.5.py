#Lab  Exercise.2.5 1630902656 Kanokporn Hudsree
arr = [],[],[],[],[],[]
matrix = list(arr)

matrix.append([])
matrix[4].append("value 4")
matrix[4].append("Pen")
matrix[4].append(10)
matrix[4].append("In stock")
matrix[5].append("value 5")
matrix[5].append("Colour pencil")
matrix[5].append(5)
matrix[5].append("In stock")
matrix[6].append("value 6")
matrix[6].append("A4 Paper")
matrix[6].append(0)
matrix[6].append("Out of stock")


for i in range(0,len(matrix)):
  if matrix[i][1] == "Ruler":
    matrix [i][2] = matrix [i][2] - 1
  if matrix[i][1] == "Pencil":
    matrix [i][2] = matrix [i][2] - 1
  if matrix[i][1] == "Pen":
    matrix [i][2] = matrix [i][2] - 2
  if matrix[i][1] == "Colour pencil":
    matrix [i][2] = matrix [i][2] - 1
  if matrix[i][2] == 0:
    matrix [i][3] = "Out of stock"
print(matrix)


