def partition(list,low,high):
    #choosing last element as pivot
    pivot=list[high]
    #pointer for greater element
    i=low-1
    #traverse through all element
    #compare each element with pivot
    for j in range(low,high):
        if list[j]<=pivot:
            #if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            (list[i], list[j]) = (list[j], list[i])
    list[i+1],list[high]=list[high],list[i+1]
        # return the position from where partition is done
    return i+1
def quick_sort(list,low,high):
    if low<high:
        p=partition(list,low,high)
        #recursive call on the left of pivot
        quick_sort(list,low,p-1)
        #recursive call on the right of pivot
        quick_sort(list,p+1,high)    
if __name__=='__main__':
    list=list(map(int,input("input the elements in list = ").split()))
    print("list before sorting = ",list)
    n=len(list)
    quick_sort(list,0,n-1)
    print("list after sorting = ",list)
