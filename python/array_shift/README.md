# Array Shift
* This challenge is to take an array and a number as input, and output an array with the given number inserted into the middle of the given array.
## Whiteboard Process
* [Whiteboard](class2_diagram.md)
### Approach and Efficiency
* For this task i though it would be easiest to split the given array into two equal halves, append the given value to the left half, and then return the concatenated arrays. The time efficiency of this function is O(1), because all of the operations in the function will always run once (if the proper conditions are met), and all of the language functions used are also O(1). The Space complexity for this approach is O(N), because the memory needed to store the two halves and returned modified array is directly proportional to the size of the given array.