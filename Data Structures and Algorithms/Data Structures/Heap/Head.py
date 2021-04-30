"""
It’s a complete tree (All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array.
A Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to Min Heap.


Properties of Heap:
The root is the second item in the array. We skip the index zero cell of the array for the convenience of implementation. Consider k-th element of the array, the
its left child is located at 2*k index
its right child is located at 2*k+1. index
its parent is located at k/2 index


Applications
Applications of Heaps:
1) Heap Sort: Heap Sort uses Binary Heap to sort an array in O(nLogn) time.

2) Priority Queue: Priority queues can be efficiently implemented using Binary Heap because it supports insert(), delete() and extractmax(), decreaseKey() operations in O(logn) time. Binomoial Heap and Fibonacci Heap are variations of Binary Heap. These variations perform union also efficiently.

3) Graph Algorithms: The priority queues are especially used in Graph Algorithms like Dijkstra’s Shortest Path and Prim’s Minimum Spanning Tree.

4) Many problems can be efficiently solved using Heaps. See following for example.

K’th Largest Element in an array
Sort an almost sorted array
Merge K Sorted Arrays


So why is Binary Heap Preferred for Priority Queue?¶
Since Binary Heap is implemented using arrays, there is always better locality of reference and operations are more cache friendly.
Although operations are of same time complexity, constants in Binary Search Tree are higher.
We can build a Binary Heap in O(n) time. Self Balancing BSTs require O(nLogn) time to construct.
Binary Heap doesn’t require extra space for pointers.
Binary Heap is easier to implement.
There are variations of Binary Heap like Fibonacci Heap that can support insert and decrease-key in ?(1) time

"""

class BinaryHeap(object):
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0

    # for shifting the node up
    def shiftUp(self, index):
        while (index // 2) > 0:
            if self.heap[index] < self.heap[index // 2]:     # (currentSize // 2) is the parent 
                temp = self.heap[index // 2]
                self.heap[index // 2] = self.heap[index]
                self.heap[index] = temp
            index = index // 2

    # to insert a node in the heap
    def insert(self, key):
        self.heap.append(key)
        self.currentSize += 1
        self.shiftUp(self.currentSize)

    # for shifting down a node
    def shiftDown(self, index):
        while(index * 2) <= self.currentSize:
            minimumChild = self.minChild(index)
            if self.heap[index] > self.heap[minimumChild]:
                temp = self.heap[index]
                self.heap[index] = self.heap[minimumChild]
                self.heap[minimumChild] = temp
            index = minimumChild
        
    # for finding the child with minimum value
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
        
    # for deleting a node from the heap and maintaining the heap property
    def delete(self):
        deletedNode = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.currentSize -= 1
        self.heap.pop()
        self.shiftDown(1)
        return deletedNode
    
    # for building heap
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.shiftDown(i)
            i = i - 1
                
bh = BinaryHeap()
bh.buildHeap([9,5,6,2,3])

print('Deleted:',bh.delete())
print('Deleted:',bh.delete())
print('Deleted:',bh.delete())
bh.insert(3)
print('Deleted:',bh.delete())

#OUTPUT:-
# Deleted: 2
# Deleted: 3
# Deleted: 5
# Deleted: 3
