# Binary Search of Sorted Array
* The challenge is to write a function that takes in a sorted array and a value to search for.
* [Whiteboard](class3_diagram.png)
* I decided to define a lower bound and an upper bound, and then define the midpoint based on the value of the lower and upper bound. Each bound gets moved depending on if the search value is greater than or less than the search value. The time complexity of this algorithm is O(log N) because as the imput size doubles, the number of steps increase by 1. The space complexity I believe is O(N), because as the input size increases the memory space required scales in direct proportion to it.
