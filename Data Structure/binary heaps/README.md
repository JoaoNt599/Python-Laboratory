# Binary Heaps


## A binary heap is a specialized tree data structure that meets two main properties:


### Binary Order Property: 

    In a binary heap, for each node ii with index ii, the values ​​stored in the descendant nodes (children) of ii are always smaller (or larger, depending on the type of heap) than the value stored in node ii.

### Binary Completeness Property: 

    A binary heap is a complete binary tree, which means that all levels of the tree are filled, except possibly the last level, which is filled from left to right.


## Binary heaps are often used in implementing priority queues, where the root node contains the element of highest (in a maximum heap) or lowest (in a minimum heap) priority.


## There are two main types of binary heaps:

### Maximum Heap (Max Heap): 
    
    Each node is greater than or equal to its children. The element with the highest value is at the root.

### Minimum Heap (Min Heap): 
    
    Each node is less than or equal to its children. The element with the lowest value is at the root.


## Basic operations supported by binary heaps include:

### Insert: 
    
    Add a new element to the heap.

### Removal: 

    Remove the element of greatest (in a maximum heap) or smallest (in a minimum heap) value, which is in the root.

### Heapify: 

    Ensure that heap ownership is maintained after a change in a node's value.

### Heap Construction: 

    Create a heap from a collection of elements.


## Binary heaps are efficiently implemented using an array. The location of a node relative to its children and parent can be calculated based on the array indices. This compact representation facilitates efficient data manipulation.

