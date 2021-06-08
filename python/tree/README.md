# Challenge Summary
define a function that returns the max value in a binary tree

## Whiteboard Process
* [Whiteboard](binary_tree_return_max.jpg)

## Approach & Efficiency
I just decided to have a local counter defined in the return max function, and then a walk function defined inside the return max function.
the walk function accesses the counter with the nonlocal keyword, and then updates its value if the current value is greater than it.
then walk calls itself recursively for the left and right node. the base case is if there is no node. 
the return max function then returns the counter.

