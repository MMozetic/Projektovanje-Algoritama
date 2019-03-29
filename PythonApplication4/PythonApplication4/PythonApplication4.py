import random
import time
from module1 import insertion_sort
from module2 import bubble_sort
from module3 import linear_search
from module5 import binary_search

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100, 10)

#print(l)
#a = input()
#index = linear_search(l,int(a))
#print("Indeks elementa je: ")
#print(index)

print(l)
a = input()
insertion_sort(l)
index = binary_search(l,0,len(l)-1,int(a))
print("Indeks elementa je: ")
print(index)

#start_time = time.clock()
#print(l)
#insertion_sort(l)
#print(l)
#end_time = time.clock() - start_time
#print("Insertion Sort Duration: ", end_time)

#start_time = time.clock()
#print(l)
#bubble_sort(l)
#print(l)
#end_time = time.clock() - start_time
#print("   Bubble Sort Duration: ", end_time)