import myArrays

arr = [7, 3, 8, 5, 2]

print("Numbers:", ", ".join(map(str, arr)))

print("Second largest number:", myArrays.second_largest(arr))

print("Median:", myArrays.median(arr))

print("Smallest and largest number:", ", ".join(map(str, myArrays.min_max(arr))))

print("Numbers as a string:", myArrays.numbers_as_string(arr))
