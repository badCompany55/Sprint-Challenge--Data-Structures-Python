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

bst_1 = BinarySearchTree(names_1[0])
bst_2 = BinarySearchTree(names_2[0])

for n in names_1:
    if n != names_1[0]:
        bst_1.insert(n)

for n in names_2:
    if n != names_2[0]:
        bst_2.insert(n)

def callback(val):
    the_return = bst_2.contains(val)
    if the_return != False:
        duplicates.append(the_return)

cb = callback
bst_1.for_each(cb)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# runtime Complex is O(n^2)
# One for loop with another nested for loop


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

