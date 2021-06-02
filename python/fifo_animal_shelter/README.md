# Challenge Summary
The challenge is to create a class AnimalShelter with methods enqueue and dequeue. The animal shelter operates on a first in first out basis.

## Whiteboard Process
* [Whiteboard](animal-shelter.jpg)

## Approach & Efficiency
I decided to use two queues to handle the enqueueing of the animal shelter queue. There is one queue for cats, and one queue for dogs. All you have to do is see if the thing being enqueued or dequeued is a cat or a dog, and then you just call the same specified method for the cats queue or the dogs queue depending on which type of animal youre looking for. This solution is O(N), because as the number of things you want to enqueue or dequeue increases, the number of steps increases linearly with the size of the input. The steps to enqueue or dequeue one thing is O(1) time.
