#Merge Sort using python

#Conseptually merge sort works as Follows:
# Divide the unsorted list into a sublist.each containing one element (a list of one element is consider sorted ) 
#Repeatedly merge sub lists to produse new sorted sublist until their is only one list remaining. Thi will be the sorted list

#  Best = Average = Worst = O(nlog(n))
"""
Merge sort is an algorithm that follows the Divide and Conquers paradigm. It continuously divides the array into two equal halves. 
Later it starts sorting the lists having a single element each and continuously merges the sorted lists to form the complete sorted list.

"""
def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0: # Loop runs until the lrft and right becomes 0 
        
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])

        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b 
    else:
        c += a
    return c
    
def merge_sort(arr):
    if (len(arr)== 0) or (len(arr)==1):
        return arr

    mid = len(arr)//2
    a = merge_sort(arr[:mid]) # Right side 
    b = merge_sort(arr[mid:]) # Left Side
    return merge(a,b)


if __name__ == "__main__":
    arr = [3, 4, 2, 8, 6, 5, 7, 1, 9]
    print("Sorted List",merge_sort(arr))
