#insertion sort
def insertion_sort(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while(j>=0 and l[j]>key):
            l[j+1]=l[j]
            j-=1
        l[i]=key
l=list(map(int,input("input elements in list ").split()))
print("array is =",l)
a=insertion_sort(l)
print("sorted array is ",l)
