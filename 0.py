import random as ra
array1_length = int(input("Please input first array size: "))
array2_length = int(input("Please input second array size: "))

first_array = set([ra.randrange(1,10) for _ in range(array1_length)])
second_array = set([ra.randrange(1,10) for _ in range(array2_length)]) 

intersection_of_sets = sorted(first_array.intersection(second_array))

print(f"Intersection of arrays#1 {first_array} and #2 {second_array}:{intersection_of_sets}")