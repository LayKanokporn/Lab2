#Lab  Exercise.2.2 1630902656 Kanokporn Hudsree
Array_A = [7,5,10,14,3,9,7]
Array_B = [9,10,3,4,2,5,7,1]
print("Array_A = " + str(Array_A))
print("Array_B = " + str(Array_B))
Array_LengthA = len(Array_A)
Array_LengthB = len(Array_B)
print("length of integer array : " + str(Array_LengthA))
print("length of integer array : " + str(Array_LengthB))
Array_A.append(15)
print("Array_A insert = " + str(Array_A))
ValueA = Array_A.count(7)
print("Value(7)A = " + str(ValueA))
ValueB = Array_B.count(7)
print("Value(7)B = " + str(ValueB))
Array_A.append(1)
print("Array_A Append = " + str(Array_A))
Array_B.append(14)
print("Array_B Append = " + str(Array_B))
Array_C = Array_A.copy()
print("Array_C = " + str(Array_C))
Array_B.extend(Array_C)
print("Array_B Merge Array_C= " + str(Array_B))
ValueC = Array_C.count(7)
print("Value(7)C = " + str(ValueC))
Array_C.sort()
print("Array_C sort = " + str(Array_C))
Array_C.remove(7)
print("Array_C remove = " + str(Array_C))
Array_D = Array_C.copy()
print("Array_D = " + str(Array_D))
Array_D.reverse()
print("Array_D reverse = " + str(Array_D))
print("Array_C = " + str(Array_C))
print("Array_D = " + str(Array_D))