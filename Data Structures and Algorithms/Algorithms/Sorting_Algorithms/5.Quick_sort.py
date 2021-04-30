# Quick Sort using Python

#  Best = Average = O(nlog(n)); Worst = O(n^2)

#Quick sort is divide-and-conquer algorithm. it works by a selecting a pivot element from an array and partitionong the other elements into two sub-array.
# according to wheather their are less that or greaterthan the pivot. the sub-arrays are then sorted recursively. 




# divide function
def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high] # pivot element
   for j in range(low , high):
      # If current element is smaller
      if arr[j] <= pivot:
         # increment
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )
# sort
def quickSort(arr,low,high):
   if low < high:
      # index
      pi = partition(arr,low,high)
      # sort the partitions
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)

if __name__ == "__main__":
    arr = [2,5,3,8,6,5,4,7]
    quickSort(arr,0,len(arr)-1)
    print ("Sorted array is:")
    for i in range(len(arr)):
     print (arr[i],end=" ")