import random as ra
array1_length = int(input("Please input count of bushes: "))
count_of_bushes = [ra.randrange(1,10) for _ in range(array1_length)]
bushes_length = len(count_of_bushes)
sum_of_results = [sum(count_of_bushes[i-1:i+2]) for i in range(1,bushes_length-1)]
print(count_of_bushes)
print(f"The max beries which was collected for one go: {max(sum_of_results)}")

