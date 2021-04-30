"""
* Selection Sort is a sorting algorithm . This divides the input list into two parts 
#In the selection sort algorithm, an array is sorted by recursively finding the minimum element from the unsorted part and inserting it at the beginning.
#Two subarrays are formed during the execution of Selection sort on a given array.

> The subarray, which is already sorted
> The subarray, which is unsorted.

#Best O(n^2); Average O(n^2); Worst O(n^2)
"""
def selection_sort(List):
    for i in range(len(List)): 
        minimum = i
        for j in range(i + 1, len(List)): #Compare i and i + 1
            if (List[j] < List[minimum]):
                minimum = j
                
        List[i], List[minimum] = List[minimum],List[i] #swap

    return List



if __name__ == "__main__":
    # List = list(map(int,input().split())) <-- for user input 
    List = [3, 4, 2, 6, 5, 7, 1, 9]
    print("Sorting List", selection_sort(List))

