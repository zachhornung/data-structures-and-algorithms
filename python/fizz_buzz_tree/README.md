# Challenge Summary
This challenge is to take in a kary tree, convert any values divisible by 3 to 'fizz', 5 to 'buzz', 15 to 'fizzbuzz', and return a copy of the tree with the modified values.

## Whiteboard Process
* [Whiteboard](fizz_buzz_tree.jpg)

## Approach & Efficiency
we used arrays for children, and this approach ends up with O(n) time efficiency because you must necessarily visit all of the nodes in the tree. The space complexity is O(n) as well because there will be a copy of the tree made. there are no recursive calls so the callstack wont take up more space than O(n).

