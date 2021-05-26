# Challenge Summary
* The goal of this challenge is to be able to insert a value at any point in the linked list, using methods called *append*, *insert_before*, and *insert_after*. *Append* adds a new node to the end of the linked list, *insert_before* adds a new node before a node containing the specified value, and *insert_after* adds a new node after a node containing the specified value.

## Whiteboard Process
* [Whiteboard](ll_insert_methods.png)
<iframe width="768" height="432" src="https://miro.com/app/live-embed/o9J_lCDzbPA=/?moveToViewport=-1187,417,1957,1210" frameBorder="0" scrolling="no" allowFullScreen></iframe>

## Approach and Efficiency
* The approach I used for this challenge was to use variations of the search method that had already been defined. We look for the specified value, and once we find it we apply a particular action. The time complexity for all of these methods is O(N) because they all require a while loop, and worst case is that every method will have to search until the very end of the linked list to find the specified value. The space complexity is O(1) because once the item is found, only the specified new value needs to be added to memory.

## Solution
* To run this solution, you just need to call the desired method and pass in the search value and the new value in that order. The only exception is append, which will just take the new value and put it at the end of the linked list.
