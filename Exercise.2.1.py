#Lab  Exercise.2.1 1630902656 Kanokporn Hudsree
Array_A = [5,7,9,11,13]
sum=0



print("Array_A = " + str(Array_A))
Array_Length = len(Array_A)



print("length of integer array : " + str(Array_Length))
for i in range(0, len(Array_A)):  
   sum = sum + Array_A[i];  
   
print("Sum of all the elements of an array: " + str(sum))