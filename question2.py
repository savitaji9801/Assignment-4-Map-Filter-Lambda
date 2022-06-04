
# Write a Python program to triple all numbers of a given list of integers. Use Python map.

nums = [1,2,3,4,5,6,7]
result = list(map(lambda x: x*3, nums))
print(result)