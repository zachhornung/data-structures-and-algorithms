import pytest
from stacks_and_queues.queue_with_stacks import Node, Pseudo_queue, Stack

def test_imports():
  assert Node and Pseudo_queue and Stack
  
# stack_1 = Stack()
# stack_2 = Stack()
# pqueue = Pseudo_queue(stack_2, stack_1)
# print(pqueue.dequeue())
# print(pqueue.enqueue('potatoes'))
# print(pqueue.enqueue('peanuts'))
# print(pqueue.enqueue('tea'))
# print(pqueue.dequeue())
# print(pqueue.front.top)
# print(pqueue.tail.top.value)
# pqueue.enqueue('goats')
# print(pqueue.front.top.value)
# print(pqueue.tail.top.value)

def test_empty_dequeue():
  pqueue = Pseudo_queue(Stack(), Stack())
  assert pqueue.dequeue() == 'this queue is empty'
  
def test_enqueue():
  pqueue = Pseudo_queue(Stack(), Stack())
  pqueue.enqueue('baby goats')
  assert pqueue.front.top.value == 'baby goats'
  
def test_multiple_enqueue():
  pqueue = Pseudo_queue(Stack(), Stack())
  pqueue.enqueue('baby goats')
  pqueue.enqueue('hens')
  pqueue.enqueue('roosters')
  assert (pqueue.tail.top.value == 'roosters') and (pqueue.front.top.value == 'baby goats')
  
def test_enqueue_and_dequeue():
  pqueue = Pseudo_queue(Stack(), Stack())
  pqueue.enqueue('baby goats')
  pqueue.enqueue('hens')
  pqueue.enqueue('roosters')
  pqueue.dequeue()
  pqueue.enqueue('cats')
  assert (pqueue.front.top.value == 'hens') and (pqueue.tail.top.value == 'cats')