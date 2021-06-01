# Challenge Summary
This challege, queues with stacks, is to impliment a queue with methods enqueue and dequeue, using stacks, with methods push, pop, and peek.

## Whiteboard Process
* [Whiteboard](queues_with_stacks.jpg)

## Approach & Efficiency
I  decided to make the front and tail of the queue be stacks. The top of the front is the front node in the queue, and the top of the tail is the last node in the queue. When enqueueing, in order to keep everything in order, you need to check the state of both queues. When one is empty, then an action is taken. Kind of like a slinky. This solution is O(N) time complexity, and O(N) space complexity.

## Solution
* Link to the code is [Here](queue_with_stacks.py)