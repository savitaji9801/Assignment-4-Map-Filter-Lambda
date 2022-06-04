
# Write a Python program to square the elements of a list using map() function.

num_list = [4,5,2,9]
def square(lst):
    return lst**2
    
data = list(map(square,num_list))
print(data)