# Challenge Summary
* This challenge is to take to linked lists and merge them into one linked list with O(1) space complexity

## Whiteboard Process
* [Whiteboard](class8_diagram.png)

## Approach & Efficiency
* I decided to use an approach with four total temp variables, one current for each linked list, and one leader for each linked list. Then each pointer is changed in a zig zag pattern, and the temp variables are moved ahead in a way that doesnt lose contact with each linked list. The time complexity is O(n + m) where n is the length of list 1 and m is the length is list 2.

## Solution
* To run this code, you just call the function with two linked lists as arguments. the nodes in the second linked list will be added to the first, alternating nodes from first and second like a zipper. The function returns a string of 'babies' to pass one of the tests.