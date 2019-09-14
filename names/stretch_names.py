
import time
import sys
sys.path.append('..')
from binary_tree_search import BinarySearchTree

start_time = time.time()
duplicates = []

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_2.sort()

def bin_search(arr, search_val):
    first = 0
    last = len(arr) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if search_val == arr[mid]:
            index = arr[mid]
        else:
            if arr[mid] < search_val:
                first = mid + 1
            else:
                last = mid - 1
    return index

ns = ["aaron", "zach", "debbie"]
# print(bin_search(names_2, 'Zach Irvin'))
# print(bin_search(ns, 'zach'))
for n in names_1:
    return_val = bin_search(names_2, n)
    if return_val != -1:
        duplicates.append(n)


# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

