def merge_sort(list):
    if len(list)>1:
        #Finding the middle element of list
        mid=len(list)//2
        #Dividing the list into two halves
        left=list[:mid]
        right=list[mid:]
        #sorting the first and second half
        merge_sort(left)
        merge_sort(right)
        #two iterators for traversing the two halves
        i=0
        j=0
        #iterator for the main list
        k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                list[k]=left[i]
                i+=1
            else:
                list[k]=right[j]
                j+=1
            k+=1
        #For remaining values
        while i<len(left):
            list[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            list[k]=right[j]
            j+=1
            k+=1
        
if __name__ == '__main__':
    list=list(map(int,input("input the elements in list = ").split()))
    print("list before sorting = ",list)
    merge_sort(list)
    print("list after sorting = ",list)

