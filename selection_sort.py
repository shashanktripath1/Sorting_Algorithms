#selection sort
import sys
l=list(map(int,input("Enter the numebr of elements").split()))
def selection_sort(l):
    for i in range(len(l)):
        min_index=i
        for j in range(i+1,len(l)):
            if l[min_index]>l[j]:
                min_index=j
        l[i],l[min_index]=l[min_index],l[i]
print("the list before sorting is = ",l)
selection_sort(l)
print("the list after sorting is = ",l)
